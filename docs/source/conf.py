# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rubiktest-projectname'
copyright = '2024, rubiktest-authorname'
author = 'rubiktest-authorname'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_togglebutton',
    'sphinxcontrib.tikz',
]

# Configuration for sphinxcontrib-tikz
tikz_proc_suite = 'pdf2svg'
tikz_latex_preamble = r"""
\usepackage{pgfplots}
\pgfplotsset{compat=newest}
"""
tikz_output_format = 'svg'
tikz_tikzlibraries = 'pgfplots.groupplots'
tikz_externalize = True
tikz_latex_args = [r"-shell-escape"]




templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']



