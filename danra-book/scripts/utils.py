import pickle
import tempfile
from pathlib import Path

import scipy.spatial
from loguru import logger

LOOKUP_INFO = {}


def sel_nearest_to_latlon_pt(ds, pt, wrap_lon=True):
    """
    For a gridded Harmonie dataset (ds), find the nearest grid point to a given
    lat/lon point (pt) and return a selection of the dataset with only
    that grid point.

    NOTE: this function internally uses a KDTree for fast nearest neighbour
    lookup, this tree is cached based on the suite_name of the dataset. The
    distance is computed as Euclidean distance in the lat/lon space and so is
    not the actual distance on the earth's surface.

    Parameters
    ----------
    ds : xarray.Dataset
        Harmonie dataset
    pt : dict
        Dictionary with keys "lat" and "lon" specifying the lat/lon point to
        find the nearest grid point to.
    wrap_lon : bool, optional
        Whether to wrap the longitude values to the domain bounds (default: True)
    """
    identifier = ds.attrs.get("suite_name")
    if identifier is None:
        raise ValueError("dataset must have a suite_name attribute")

    if not isinstance(pt, dict):
        raise TypeError("pt_latlon must be a dict with keys 'lat' and 'lon'")

    lon, lat = pt["lon"], pt["lat"]

    @cache_to_pickle(identifier)
    def build_tree():
        logger.info(
            f"Building nearest-point to lat/lon lookup tree for {identifier}"
        )
        values = list(zip(ds.lon.values.flatten(), ds.lat.values.flatten()))
        tree_kdtree = scipy.spatial.cKDTree(values)
        latlon_bounds = dict(
            lat=(ds.lat.min().values, ds.lat.max().values),
            lon=(ds.lon.min().values, ds.lon.max().values),
        )
        return dict(tree=tree_kdtree, latlon_bounds=latlon_bounds)

    if identifier in LOOKUP_INFO:
        lookup_info = LOOKUP_INFO[identifier]
    else:
        lookup_info = build_tree()
        LOOKUP_INFO[identifier] = lookup_info

    lookup_tree = lookup_info["tree"]
    latlon_bounds = lookup_info["latlon_bounds"]

    if wrap_lon:
        lon_wrapped, applied_lon_offset = _wrap_lon(lon, latlon_bounds["lon"])
    else:
        # check that the longitude is within the bounds
        if lon < latlon_bounds["lon"][0] or lon > latlon_bounds["lon"][1]:
            raise ValueError(
                f"Longitude value ({lon}) is not within the domain bounds ({latlon_bounds['lon']})"
            )

    # check that the latitude is within the bounds
    if lat < latlon_bounds["lat"][0] or lat > latlon_bounds["lat"][1]:
        raise ValueError(
            f"Latitude value ({lat}) is not within the domain bounds ({latlon_bounds['lat']})"
        )

    _, idx_nearest = lookup_tree.query((lon_wrapped, lat))
    nx, ny = ds.lon.shape
    i, j = idx_nearest % ny, idx_nearest // ny

    ds_point = ds.isel(x=i, y=j)

    if wrap_lon:
        ds_point["lon"] = ds_point["lon"] - applied_lon_offset

    return ds_point


def cache_to_pickle(identifier):
    """
    This function can be used as a decorator to cache the return value of a
    function to a pickle file. The function must return a pickleable object.
    """

    def decorator(func):
        fp_pickle = Path(tempfile.gettempdir()) / f"{identifier}.pkl"

        def wrapper(*args, **kwargs):
            if fp_pickle.exists():
                with open(fp_pickle, "rb") as f:
                    return pickle.load(f)
            else:
                result = func(*args, **kwargs)
                fp_pickle.parent.mkdir(parents=True, exist_ok=True)
                with open(fp_pickle, "wb") as f:
                    pickle.dump(result, f)
                return result

        return wrapper

    return decorator


def _wrap_lon(lon, lon_bounds):
    """
    Attempt to wrap longitude values to the given bounds.

    Parameters
    ----------
    lon : float
        Longitude value to wrap
    lon_bounds : tuple
        Tuple of (min, max) longitude values
    """
    applied_rotation = 0.0
    exception_text = (
        f"The provided longitude value ({lon}) cannot be placed within the "
        f"bounds ({lon_bounds}), even after applying a 360deg wrapping."
    )
    while lon < lon_bounds[0] or lon > lon_bounds[1]:
        if lon < lon_bounds[0]:
            if applied_rotation < 0:
                raise ValueError(exception_text)
            lon += 360
            applied_rotation += 360
        elif lon > lon_bounds[1]:
            lon -= 360
            if applied_rotation > 0:
                raise ValueError(exception_text)
            applied_rotation -= 360

    return lon, applied_rotation
