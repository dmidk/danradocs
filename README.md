[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17294180.svg)](https://doi.org/10.5281/zenodo.17294180)
[![Preprint](https://img.shields.io/badge/preprint-darkred?logo=arxiv)](https://doi.org/10.48550/arXiv.2510.04681)
[![Documentation](https://img.shields.io/badge/docs-jupyter_book-blue?logo=jupyter)](https://dmidk.github.io/danradocs/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

# danra-book

This is the jupyter book for the DANRA (Danish Reanalysis) project and dataset.

## Overview

This Jupyter book serves as an interactive guide and documentation for the DANRA dataset.

## Getting Started

To get started with the DANRA book, either visit the documentation at https://dmidk.github.io/danradocs/ or clone the repository and install the required dependencies to run the notebooks locally.
We recommend using [uv](https://docs.astral.sh/uv/) to create a virtual environment and install the dependencies.

```bash
git clone git@github.com:dmidk/danradocs.git
cd danradocs
uv sync
```

To build the book locally, run

```bash
uv run jupyter-book build danra-book/
```

and open `danra-book/_build/html/index.html` in a browser.

Navigate to the `danra-book/notebooks` directory and start explore and/or create new notebooks.
To add a new notebook, to the jupyter book, you can add the notebook to the `danra-book/notebooks` directory and add the path to the notebook in the `_toc.yml` file.

## Releasing

The documentation is published for each version of the DANRA dataset, at `https://dmidk.github.io/danradocs/<data version>/`, e.g. https://dmidk.github.io/danradocs/v0.6.1/.
https://dmidk.github.io/danradocs/ redirects to the most recent release, and so do URLs that no longer exist.

To publish a release:

1. Set `data_version` in `danra-book/_config.yml` to the version of the dataset the docs describe.
2. Push a tag, e.g. `git tag v0.3.0 && git push upstream v0.3.0`. CI builds the book, publishes it to the folder for `data_version` and points https://dmidk.github.io/danradocs/ to it. Publishing the same data version again replaces that folder.

A tag containing `rc` (e.g. `v0.3.0rc1`) is published to the folder for `data_version` as well, but the site root is not changed. Use this to share docs for a dataset version that is not public yet.
