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

   % A simple cycle
   % Author : Jerome Tremblay
   \documentclass{article}
   \usepackage{tikz}
   \begin{document}
   \begin{tikzpicture}

   \def \n {5}
   \def \radius {3cm}
   \def \margin {8} % margin in angles, depends on the radius

   \foreach \s in {1,...,\n}
   {
   \node[draw, circle] at ({360/\n * (\s - 1)}:\radius) {$\s$};
   \draw[->, >=latex] ({360/\n * (\s - 1)+\margin}:\radius) 
      arc ({360/\n * (\s - 1)+\margin}:{360/\n * (\s)-\margin}:\radius);
   }
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
