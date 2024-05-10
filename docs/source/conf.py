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
tikz_proc_suite = 'GhostScript'
tikz_transparent = True
tikz_latex_preamble = r'''
\usepackage{tikz}
\usepackage[english]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[a4paper,top=3cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{pgfplots}
\usepackage{pgfplotstable}
\usepackage{caption}

\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows,patterns,plotmarks,calc,3d,matrix,positioning,arrows.meta,shapes.geometric}
'''
tikz_output_format = 'png'




templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']



