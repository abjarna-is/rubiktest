.. rubiktest-projectname documentation master file, created by
   sphinx-quickstart on Wed May  8 23:02:24 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to rubiktest-projectname's documentation by abjarna!
==============================================================

Smá meira test.

Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`.

.. math:: e^{i\pi} + 1 = 0
   :label: euler

Euler's identity, equation :eq:`euler`, was elected one of the most
beautiful mathematical formulas.

:math:`\underline{x}=[  x_{1}, ...,  x_{n}]^{T}`

.. admonition:: Dæmi og lausn
   :class: tip

   Hér er dæmi og lausn

.. admonition:: Annað dæmi og lausn sem er hægt að opna og loka
   :class: tip dropdown

   Hér er annað dæmi og lausn

.. tikz:: 

\documentclass{article}
\usepackage{tikz}
\usepackage{pgfplots} % This package is required for creating plots

\begin{document}

\begin{tikzpicture}
\begin{axis}[
    ybar, % Style of the plot
    symbolic x coords={A, B, C, D, E}, % X-axis labels
    xtick=data, % Only show ticks for data points
    nodes near coords, % Display the value of each bar
    ymin=0, % Minimum value on the y-axis
    ylabel={Value}, % Label for the y-axis
    xlabel={Category}, % Label for the x-axis
]
% Data to plot
\addplot coordinates {(A,10) (B,15) (C,7) (D,20) (E,8)};
\end{axis}
\end{tikzpicture}

\end{document}


+----------+----------+
| Header 1 | Header 2 |
+==========+==========+
| 1        | one      |
+----------+----------+
| 1,5      | test     |
+----------+----------+
| 2        | two      |
+----------+----------+

.. toctree::
   :maxdepth: 2
   :caption: Contents:




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
