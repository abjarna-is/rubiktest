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

   \begin{document} 

   \begin{figure}[ht]
      \centering
      \pgfmathsetmacro{\BarOffset}{0.15}

      \pgfplotsset{
      % define a new style to use on both axis environments
      MyAxis/.style={
               ybar,
               scale only axis,
               width=12cm,
               height=8cm,
               ymin=0,
               xmin=-0.5,
               xmax=7.5, % you need to increase this if you add more data
               area legend,
               bar width=10pt
         }
      }

      \pgfplotstableread{
         %Returns         %Sharpe
      0 6.4              0.232      
      1 4.5              0.279      
      2 12.8             0.397      
      3 4.4              0.279   
      4 13.6             0.462
      5 6.5              0.221
      6 11.1             0.337
      7 9.4              0.377

      }\dataset

      \begin{tikzpicture}
      \begin{axis}[
         title= \Large{Average annual returns and Sharpe ratios for value and growth portfolios},
         ylabel={Average annual return (\%)},
         ymax=16,
         ymajorgrids=true,
         xtick={0,...,7},
         xtick pos=left,
         ytick pos=left,
         xticklabels = {
            Value,
            Growth,
            Value,
            Growth,
            Value,
            Growth,
            Value,
            Growth
         },
         yticklabel style={xshift=-0.5ex},
         tickwidth=5pt,
         extra x ticks={-0.5,1.5,...,3.5,5.5,7.5},
         extra x tick labels={},
         extra x tick style={tickwidth=1.2cm},
         minor x tick style = {opacity=0},
         MyAxis\begin{tikzpicture}
      \node[draw, rectangle] (a) {Rectangle};
      \node[draw, circle, blue, below of=a] (b) {Circle};
      \draw[->, thick, red] (a) -- (b);
   \end{tikzpicture}
      ]
      \addplot[draw=black,fill=black!20] table[x expr=\coordindex-\BarOffset,y index=1] \dataset; %Return
      \label{returnplot}
      \end{axis}

      \begin{axis}[
         name=ax2,
         ymax=0.5,
         MyAxis,
         ylabel=Average Sharpe ratio,
         ytick pos=right,
         yticklabel style={xshift=0.5ex},
         clip=false,
         xtick={0.5,2.5,4.5,6.5},
         xticklabels={P/E ratio, P/B ratio, P/C ratio, P/S ratio},
         xticklabel style={yshift=-5mm},
         tickwidth=5pt,
         xtick style={draw=none}
      ]
      \addplot[draw=black,fill=black!40] table[x expr=\coordindex+\BarOffset,y index=2] \dataset; %Sharpe ratio
      \label{ratioplot}

      \end{axis}

      % legend
      \node [below=1.3cm] at (ax2.south) {\ref{returnplot} Return \quad \ref{ratioplot} Sharpe ratio};
      \end{tikzpicture}

      \captionsetup{labelfont=bf, format=plain, labelformat=default}
      \caption{Average annual returns and Sharpe ratios for value and growth portfolios in the period 1992-2017, portfolios were created using different financial ratios.}
      \label{fig:overview}
      \end{figure}
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
