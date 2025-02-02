.. rubiktest-projectname documentation master file, created by
   sphinx-quickstart on Wed May  8 23:02:24 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to rubiktest-projectname's documentation by abjarna!
==============================================================

Smá meira dæmi þá æða áfram sýki. asdsdff afasf testing test. 1 + 2 = 9. Hér verður flott síða. lj lkjlkjlkj. asdf adsfasdf.

Since Pythagoras, we know that :math:`1+2=9`.

   asdf asdadsffasdf asdf asdf asdf

asdf

.. code-block:: javascript

  alert('Hello, World!')

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

   .. tikz:: test2.tex -- lkj lkj lkj lkj lkj lkj lkjlkjlkjlkj lkj lkj lkj lk jlkj lkj lk jlkj lkj lkJ LKJ
      :include: _tex/test.tex

test.tex

.. tikz::
   :include: _tex/test.tex

Verðgólf inn í RST

.. tikz:: 
   \begin{tikzpicture}[domain=0:5,scale=1,thick]
   \usetikzlibrary{calc}   %allows coordinate calculations.
   %Define linear parameters for supply and demand
   \def\dint{4.5}          %Y-intercept for DEMAND.
   \def\dslp{-0.5}         %Slope for DEMAND.
   \def\sint{1.2}          %Y-intercept for SUPPLY.
   \def\sslp{0.8}          %Slope for SUPPLY.
   \def\pfc{2.5}           %Price floor or ceiling
   \def\demand{\x,{\dslp*\x+\dint}}
   \def\supply{\x,{\sslp*\x+\sint}}
   % Define coordinates.
      \coordinate (ints) at ({(\sint-\dint)/(\dslp-\sslp)},{(\sint-\dint)/(\dslp-\sslp)*\sslp+\sint});
      \coordinate (ep) at  (0,{(\sint-\dint)/(\dslp-\sslp)*\sslp+\sint});
      \coordinate (eq) at  ({(\sint-\dint)/(\dslp-\sslp)},0);
      \coordinate (dint) at (0,{\dint});
      \coordinate (sint) at (0,{\sint});
      \coordinate (pfq) at  ({(\pfc-\dint)/(\dslp)},0);
      \coordinate (pfp) at  ({(\pfc-\dint)/(\dslp)},{\pfc});
      \coordinate (sfq) at  ({(\pfc-\sint)/(\sslp)},0);
      \coordinate (sfp) at  ({(\pfc-\sint)/(\sslp)},{\pfc});
   % DEMAND
      \draw[thick,color=blue] plot (\demand) node[right] {Eftirspurnin: $P(q) = -\frac{1}{2}q+\frac{9}{2}$};
   % SUPPLY
      \draw[thick,color=purple] plot (\supply) node[right] {Framboð};
   % Draw axes, and dotted equilibrium lines.
      \draw[->] (0,0) -- (6.2,0) node[right] {$Q$};
      \draw[->] (0,0) -- (0,6.2) node[above] {$P$};
      %Price floor and ceiling lines
      \draw[dashed,color=black] plot (\x,{\pfc}) node[right] {$P_c$};
      \draw[dashed] (pfp) -- (pfq) node[below] {$Q_d$};
      \draw[dashed] (sfp) -- (sfq) node[below] {$Q_s$};
   \draw[->,baseline=5] ($(0,{\pfc})+(-1.5,0.7)$) node[label= left:Verðgólf] {} -- ($(0,{\pfc})+(-.1,0.1)$);
   \end{tikzpicture}

test2.tex

.. tikz::
   :include: _tex/test2.tex
   
test3.tex

.. tikz::
   :include: _tex/test3.tex

test4.tex

.. tikz::
   :include: _tex/test4.tex

test_table.tex

.. tikz::
   :include: _tex/test_table.tex

test_table1.tex

.. tikz::
   :include: _tex/test_table1.tex

test_table2.tex

.. tikz::
   :include: _tex/test_table2.tex

test_canvas1.tex - Error and Cost

.. tikz::
   :include: _tex/test_canvas1.tex

test_canvas2.tex

.. tikz::
   :include: _tex/test_canvas2.tex

test_canvas3.tex

.. tikz::
   :include: _tex/test_canvas3.tex

Euler's identity, assfdfdf equation :eq:`euler`, was elected one of the most


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
