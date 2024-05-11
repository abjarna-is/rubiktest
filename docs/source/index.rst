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

  Setjum :math:`b_y=-6b_x` inn og fáum:

.. math::
   9 = \sqrt{b_x^2+b_y^2}

.. math::
   \begin{aligned}
   9 &= \sqrt{b_x^2+b_y^2}\\
   &=\sqrt{b_x^2+(-6b_x)^2} \\
   &= \sqrt{b_x^2+36b_x^2} \\
   &=\sqrt{37b_x^2} \\
   &=b_x\sqrt{37} \\
   b_x&=\frac{9}{\sqrt{37}} \approx 1.480\\
   b_y&= -6b_x = \frac{-54}{\sqrt{37}} \approx -8.878
   \end{aligned}

Vigur sem er samsíða :math:`\overline{a}=(-1,6)` og hefur lengdina 9 er því

.. math::
   \overline{b}= \begin{pmatrix} \frac{9}{\sqrt{37}} \\  \frac{-54}{\sqrt{37}} \end{pmatrix}

.. admonition:: Dæmi og lausn
   :class: tip

   Hér er dæmi og lausn

.. admonition:: Annað dæmi og lausn sem er hægt að opna og loka
   :class: tip dropdown

   Hér er annað dæmi og lausn

.. admonition:: Dæmi og lausn
   :class: tip

   .. tikz:: lkj lkj lkj lkj lkj lkj lkjlkjlkjlkj lkj lkj lkj lk jlkj lkj lk jlkj lkj lkJ LKJ
      :align: left
      :include: _tex/test.tex

Hér er (reyndar ekki) hægt að vísa í mynd 1.

.. tikz::
   :align: left
   :include: _tex/test.tex

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
