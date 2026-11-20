"""Add or update a version in versions.json, the list shown in the version dropdown.

Usage: update_versions.py <path to versions.json> <data version> <is release candidate: true|false>

A release is marked as preferred (the most recent release); a release candidate
is listed with "(release candidate)" and does not change which version is preferred.
"""

import json
import sys
from pathlib import Path

path, version, is_rc = Path(sys.argv[1]), sys.argv[2], sys.argv[3] == "true"

versions = json.loads(path.read_text()) if path.exists() else []
versions = [v for v in versions if v["version"] != version]

entry = {
    "name": f"{version} (release candidate)" if is_rc else version,
    "version": version,
    "url": f"/danradocs/{version}/",
}
if not is_rc:
    for v in versions:
        v.pop("preferred", None)
    entry["preferred"] = True
versions.append(entry)

versions.sort(
    key=lambda v: tuple(int(x) for x in v["version"].lstrip("v").split(".")),
    reverse=True,
)
path.write_text(json.dumps(versions, indent=2) + "\n")
