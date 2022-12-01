"""Sphinx configuration."""
project = "Computerender"
author = "computerender"
copyright = "2022, computerender"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
