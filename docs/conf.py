import doctest
import os
import sys
from typing import Any, Dict, List, Optional

import sphinx_book_theme
from docutils.nodes import document
from sphinx.application import Sphinx

import scipp_uncertainty

sys.path.insert(0, os.path.abspath("."))

from version import VersionInfo  # noqa: E402

sys.path.insert(0, os.path.abspath('.'))

# General information about the project.
project = "scippuncertainty"
copyright = "2023 Scipp contributors"
author = "Scipp contributors"

version_info = VersionInfo(repo=project)
long_version = scipp_uncertainty.__version__
outdated = not version_info.is_latest(long_version)


def make_text_icon(text: str) -> str:
    # Inject some text into the icon of a launch button.
    # This may need to be updated in future releases of sphinx-book-theme.
    return ('"></i>'
            f'<span class="btn__text-container">{text}</span>'
            '<i class="fa fa-caret-down')


def add_button_group(context: Dict[str, Any], buttons: List[Dict[str, str]], *,
                     name: str, label: str) -> None:
    context["header_buttons"].append({
        "type": "group",
        "buttons": buttons,
        "icon": make_text_icon(name),
        "label": label,
        "tooltip": name,
    })


def add_related_project_buttons(context: Dict[str, Any]) -> None:
    base = "https://scipp.github.io"
    buttons = [
        {
            "type": "link",
            "text": "scipp",
            "url": f"{base}"
        },
        {
            "type": "link",
            "text": "plopp",
            "url": f"{base}/plopp"
        },
        {
            "type": "link",
            "text": "scippnexus",
            "url": f"{base}/scippnexus"
        },
        {
            "type": "link",
            "text": "scippneutron",
            "url": f"{base}/scippneutron"
        },
        {
            "type": "link",
            "text": "ess",
            "url": f"{base}/ess"
        },
    ]
    add_button_group(context,
                     buttons,
                     name="Related projects",
                     label="related-projects")


def add_version_buttons(context: Dict[str, Any]) -> None:
    base = "https://scipp.github.io/scippuncertainty"
    releases = version_info.minor_releases(first='0.0')
    if outdated:
        current = f"{long_version} (outdated)"
        latest = "latest"
        entries = ['.'.join(long_version.split('.')[:2])]
    elif not releases:
        current = "unknown"
        latest = "unknown"
        entries = []
    else:
        current = f"{long_version} (latest)"
        latest = f"{releases[0]} (latest)"
        entries = releases[1:]
    lines = [{"type": "link", "text": latest, "url": f"{base}"}]
    for r in entries:
        lines.append({
            "type": "link",
            "text": f"{r}",
            "url": f"{base}/release/{r}"
        })
    add_button_group(context, lines, name=current, label="versions")


def add_buttons(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Optional[document],
) -> None:
    add_related_project_buttons(context)
    add_version_buttons(context)


sphinx_book_theme.add_launch_buttons = add_buttons

html_show_sourcelink = True

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.bibtex",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "nbsphinx",
]

intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
    "python": ("https://docs.python.org/3", None),
    "scipp": ("https://scipp.github.io/", None),
}

# autodocs includes everything, even irrelevant API internals. autosummary
# looks more suitable in the long run when the API grows.
# For a nice example see how xarray handles its API documentation.
autosummary_generate = True

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = False
napoleon_preprocess_types = True
typehints_defaults = "comma"
typehints_use_rtype = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"
html_sourcelink_suffix = ""  # Avoid .ipynb.txt extensions in sources

# The master toctree document.
master_doc = "index"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = scipp_uncertainty.__version__
# The full version, including alpha/beta/rc tags.
release = scipp_uncertainty.__version__

warning_is_error = True

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": f"https://github.com/scipp/{project}",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "show_toc_level": 2,  # Show subheadings in secondary sidebar
}

html_title = "ScippUncertainty"
html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "scippuncertaintydoc"

# -- Options for doctest --------------------------------------------------

# sc.plot returns a Figure object and doctest compares that against the
# output written in the docstring. But we only want to show an image of the
# figure, not its `repr`.
# In addition, there is no need to make plots in doctest as the documentation
# build already tests if those plots can be made.
# So we simply disable plots in doctests.
doctest_global_setup = """
"""

doctest_default_flags = (
    doctest.ELLIPSIS
    | doctest.IGNORE_EXCEPTION_DETAIL
    | doctest.DONT_ACCEPT_TRUE_FOR_1
    | doctest.NORMALIZE_WHITESPACE
)

# -- Options for linkcheck ------------------------------------------------

linkcheck_ignore = [
    # Specific lines in GitHub blobs cannot be found by linkcheck.
    r"https?://github\.com/.*?/blob/[a-f0-9]+/.+?#",
]

# -- Options for bibtex ---------------------------------------------------
bibtex_bibfiles = ["bibliography.bib"]
bibtex_reference_style = "label"
