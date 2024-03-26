---
layout: single
classes: wide
title:  "Matrix derivatives for future reference"
date:   2024-03-26
---

Derivatives of $\|\|\mathbf{WH} - \mathbf{X}\|\|_F^2 = \|\|\mathbf{X} - \mathbf{WH}\|\|_F^2$ can be expressed as:

$$
\begin{align} \label{eq:deriv1}
 &\nabla_{W}||\mathbf{WH} - \mathbf{X}||_F^2 = 2\mathbf{WHH}^T - 2 \mathbf{XH}^T \\[1.2em]
 &\nabla_{H}||\mathbf{WH} - \mathbf{X}||_F^2 = 2\mathbf{W}^T\mathbf{WH} - 2 \mathbf{W}^T\mathbf{X} \\[1.2em]
 &\nabla_{X}||\mathbf{WH} - \mathbf{X}||_F^2 = 2\mathbf{X} - 2\mathbf{WH}
\end{align} 
$$ 

And derivatives of $\|\|\mathbf{MW}\|\|_F^2$ can be expressed as:

$$
\begin{align} \label{eq:deriv2}
 &\nabla_{W}||\mathbf{MW}||_F^2 = 2\mathbf{M}^T\mathbf{MW} \\[1.2em]
 &\nabla_{H}||\mathbf{MW}||_F^2 = 2\mathbf{MWW}^T
\end{align} 
$$ 