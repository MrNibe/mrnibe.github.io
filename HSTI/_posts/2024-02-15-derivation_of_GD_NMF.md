---
layout: single
classes: wide
title:  "Derivation of update rules for gradient decent for non-negative matrix factorization"
date:   2024-02-15
---

The cost function

$$
\begin{align} \label{eq:arg_min}
  \arg \min_{\mathbf{W,H}} ||\mathbf{X} - \mathbf{WH}||_F^2 + ||\mathbf{MW}||_F^2 \qquad \textrm{s.t.} \quad \mathbf{W,H} \geq 0
\end{align} 
$$

For the gradient decent algorithm we need to define a cost function, $f(\mathbf{W,H})$ which we in this case want to minimize:

$$
\begin{align} \label{eq:cost_f}
 f(\mathbf{W,H}) = ||\mathbf{X} - \mathbf{WH}||_F^2 + ||\mathbf{MW}||_F^2
\end{align} 
$$

To find the minimum we are going to take a step in the opposite direction of the gradient. This will make us get closer to the minimum value of the function (provided the step size is not too large as to overshoot). If we combine all the independent parameters which we are trying to fit (in this case $\mathbf{W}$ and $\mathbf{H}$) into a single parameter vector, $\mathbf{θ}$, we then have the update scheme:

$$
\begin{align} \label{eq:f_update}
 \mathbf{θ}_{l+1} = \mathbf{θ}_{l} - \alpha \nabla f(\mathbf{θ}_{l})
\end{align} 
$$

Here, $l$ denotes the iteration of this iterative update scheme and $\alpha$ is the step length. Usually, $\alpha$ is just a constant step length, but it can also change during the decent. In that case it would be denoted $\alpha_l$. Similarly, the step size can also be specific for each parameter. In that case Eq. (\ref{eq:f_update}) becomes: 

$$
\begin{align} \label{eq:f_update_elementwise}
 \mathbf{θ}_{l+1} = \mathbf{θ}_{l} - \mathbf{α} \circ \nabla f(\mathbf{θ}_{l})
\end{align} 
$$
where $\circ$ denotes element wise multiplication. 

Now, the gradient $\nabla f(\mathbf{W,H})$ is derived. We must find the gradient both with respect to $\mathbf{W}$ and $\mathbf{H}$ as we want to minimize them both. Firstly, we start by deriving $\nabla_\mathbf{W} f(\mathbf{W,H})$

## Gradient with respect to W

We can find the derivatives of the terms in $f(\mathbf{W,H})$ individually and combine them in the end. We start by:

$$
\begin{align} \label{eq:F2_trace}
 ||\mathbf{X} - \mathbf{WH}||_F^2 = \textrm{tr}[(\mathbf{X-WH})^T (\mathbf{X-WH})] =\textrm{tr}[\mathbf{X}^T\mathbf{X} - \mathbf{X}^T\mathbf{WH} - \mathbf{H}^T\mathbf{W}^T\mathbf{X} + \mathbf{H}^T\mathbf{W}^T\mathbf{WH}] 
\end{align} 
$$

Properties of the trace:

$$
\begin{align} \label{eq:trace_props}
  \textrm{tr}[\mathbf{A} +\mathbf{B}] &=\textrm{tr}[\mathbf{A}] + \textrm{tr}[\mathbf{B}] \\[1.2em] 
  \textrm{tr}[\mathbf{ABC}] &= \textrm{tr}[\mathbf{CAB}] = \textrm{tr}[\mathbf{BCA}]
\end{align} 
$$

From [The Matrix Cookbook](https://www2.imm.dtu.dk/pubdb/edoc/imm3274.pdf):

$$
\begin{align} \label{eq:M_cook_book}
  \mathbf{\nabla_X} \textrm{tr}[\mathbf{AX}] &= \mathbf{A}^T \\[1.2em] 
  \mathbf{\nabla_X} \textrm{tr}[\mathbf{X}^T\mathbf{A}] &= \mathbf{A}\\[1.2em]
  \mathbf{\nabla_X} \textrm{tr}[\mathbf{X}^T\mathbf{AX}] &= (\mathbf{A} + \mathbf{A}^T)\mathbf{X}\\[1.2em]
  \mathbf{\nabla_X} \textrm{tr}[\mathbf{XA}\mathbf{X}^T] &= \mathbf{X}(\mathbf{A}^T + \mathbf{A})\\[1.2em]
\end{align} 
$$

Firstly, we are only interested in the derivative with respect to $\mathbf{W}$. We quickly see that $\mathbf{\nabla_W X}^T\mathbf{X} = 0$. Then we have: 

$$
\begin{align} \label{eq:W_deriv_1}
  \mathbf{\nabla_W} \textrm{tr}[\mathbf{X}^T\mathbf{WH}] &= \mathbf{\nabla_W} \textrm{tr}[\mathbf{HX}^T\mathbf{W}] = (\mathbf{HX}^T)^T = \mathbf{XH}^T \\[1.2em]
  \mathbf{\nabla_W} \textrm{tr}[\mathbf{H}^T\mathbf{W}^T\mathbf{X}] &= \mathbf{\nabla_W} \textrm{tr}[\mathbf{W}^T\mathbf{XH}^T] = \mathbf{XH}^T \\[1.2em]
  \mathbf{\nabla_W} \textrm{tr}[\mathbf{H}^T\mathbf{W}^T\mathbf{WH}] &= \mathbf{\nabla_W} \textrm{tr}[\mathbf{WHH}^T\mathbf{W}^T] = \mathbf{W}((\mathbf{HH}^T)^T + (\mathbf{HH}^T)) =  2\mathbf{W}\mathbf{HH}^T\\[1.2em]
\end{align} 
$$

Combining this yields:

$$
\begin{align} \label{eq:W_deriv_F2}
  \mathbf{\nabla_W} ||\mathbf{X} - \mathbf{WH}||_F^2 = 2\mathbf{W}\mathbf{HH}^T - 2\mathbf{XH}^T
\end{align} 
$$

Next up, we have: 

$$
\begin{align} \label{eq:M_trace}
 ||\mathbf{MW}||_F^2 = \textrm{tr}[(\mathbf{MW})^T (\mathbf{MW})] =\textrm{tr}[\mathbf{W}^T\mathbf{M}^T \mathbf{MW}] 
\end{align} 
$$

Similarly to before, the gradient becomes 

$$
\begin{align} \label{eq:gradient_M}
 \nabla_\mathbf{W} \lambda||\mathbf{MW}||_F^2 = \lambda(\mathbf{M}^T\mathbf{M} + (\mathbf{M}^T\mathbf{M})^T)\mathbf{W} = 2\lambda\mathbf{M}^T\mathbf{MW} 
\end{align} 
$$

The final expression of the gradient with respect to $\mathbf{W}$ becomes:

$$
\begin{align} \label{eq:gradient_f_wrt_W}
 \nabla_\mathbf{W} f(\mathbf{W,H}) =  2\mathbf{W}\mathbf{HH}^T - 2\mathbf{XH}^T + 2\lambda\mathbf{M}^T\mathbf{MW} 
\end{align} 
$$

The update step therefore becomes:

$$
\begin{align} 
 \mathbf{W} &\leftarrow  \mathbf{W} -  \alpha\nabla_\mathbf{W} f(\mathbf{W,H}) \\[1.2em]
 \mathbf{W} &\leftarrow  \mathbf{W} -  \alpha(\mathbf{W}\mathbf{HH}^T - \mathbf{XH}^T + \lambda\mathbf{M}^T\mathbf{MW})\label{eq:W_update}
\end{align} 
$$

Here, the 2's are omitted as they can be "absorbed" by the step size.


### Choosing the right step size
We try to solve, $\arg \min f(\mathbf{θ})$ using gradient decent: $\mathbf{θ} = \mathbf{θ} - \alpha \nabla f(\mathbf{θ})$. The step size can bee chosen to be $0 \leq \alpha \leq 2/L$, where $L$ is the Lipschitz constant. It is stated that

$$
\begin{align} \label{eq:lipschitz}
 L \geq \frac{||\nabla f(\mathbf{a}) - \nabla f(\mathbf{b})||_2}{||\mathbf{a} - \mathbf{b}||_2} 
\end{align} 
$$ 

This does indeed look like the mean value theorem stating that

$$
\begin{align} \label{eq:mean_value_theorem}
 \frac{\psi(\mathbf{a}) - \psi(\mathbf{b})}{\mathbf{a} - \mathbf{b}} = \psi'(\mathbf{γ})  
\end{align} 
$$

The left-hand side is the slope of the secant for the function, $\psi$ evaluated points $\mathbf{a}$ and $\mathbf{b}$, while the right-hand side is the slope of the function evaluated at the point $\mathbf{γ}$. That means that the slope of the function between $\mathbf{a}$ and $\mathbf{b}$ at least at one point ($\mathbf{γ}$) is equal to the slope of the line connecting $\psi(\mathbf{a})$ and $\psi(\mathbf{b})$. 

To find the Lipschitz constant, we should therefore differentiate $\nabla_\mathbf{W} f(\mathbf{W,H})$ yet again. Doing so we find that 

$$
\begin{align} \label{eq:f_2nd_deriv}
 \nabla^2_\mathbf{W} f(\mathbf{W,H}) =  2\nabla_\mathbf{W}(\mathbf{WHH}^T - \mathbf{XH}^T + \lambda \mathbf{M}^T\mathbf{MW}) = 2(\mathbf{HH}^T + \lambda\mathbf{M}^T\mathbf{M})
\end{align} 
$$

then Eq. (\ref{eq:lipschitz}) becomes:

$$
\begin{align} \label{eq:lipschitz_expand}
 \frac{||\nabla f(\mathbf{A}) - \nabla f(\mathbf{B})||_2}{||\mathbf{A} - \mathbf{B}||_2} = ||\nabla^2_\mathbf{W} f(\mathbf{W,H})||_2 = 2||\mathbf{HH}^T + \lambda\mathbf{M}^T\mathbf{M}||_2 \leq L  
\end{align} 
$$ 

Taking the square of the expression yields:

$$
\begin{align} \label{eq:lipschitz_squared}
 4||\mathbf{HH}^T + \lambda\mathbf{M}^T\mathbf{M}||_2^2 \leq L^2  
\end{align} 
$$ 

Using $\|\|\mathbf{P} + \mathbf{Q}\|\|_2^2 \leq (\|\|\mathbf{P}\|\|_2 + \|\|\mathbf{Q}\|\|_2))^2$ we arrive (and I get stuck) at

$$
\begin{align} \label{eq:lipschitz_final}
 2||\mathbf{HH}^T + \lambda\mathbf{M}^T\mathbf{M}||_2 \leq 2(||\mathbf{\mathbf{HH}^T}||_2 + ||\mathbf{\lambda\mathbf{M}^T\mathbf{M}}||_2) \leq L^2  
\end{align} 
$$ 


## Gradient with respect to H

In the case of $\mathbf{H}$, there is only one term, where the gradient needs to be calculated: $\mathbf{\nabla_H} \|\|\mathbf{X} - \mathbf{WH}\|\|_F^2$. Here the derivatives of the single terms in Eq. (\ref{eq:F2_trace}) with respect to $\mathbf{H}$ become:

$$
\begin{align} \label{eq:H_deriv_1}
  \mathbf{\nabla_H} \textrm{tr}[\mathbf{X}^T\mathbf{WH}] &= (\mathbf{X}^T\mathbf{W})^T = \mathbf{W}^T\mathbf{X} \\[1.2em]
  \mathbf{\nabla_H} \textrm{tr}[\mathbf{H}^T\mathbf{W}^T\mathbf{X}] &= \mathbf{W}^T\mathbf{X} \\[1.2em]
  \mathbf{\nabla_H} \textrm{tr}[\mathbf{H}^T\mathbf{W}^T\mathbf{WH}] &= (\mathbf{W}^T\mathbf{W}^T + (\mathbf{W}^T\mathbf{W}^T)^T)\mathbf{H} =  2\mathbf{WW}^T\mathbf{H}\\[1.2em]
\end{align} 
$$

Combining this, the gradient becomes:

$$
\begin{align} \label{eq:gradient_H}
 \nabla_\mathbf{H} f(\mathbf{W,H}) =  2\mathbf{WW}^T\mathbf{H} - 2\mathbf{W}^T\mathbf{X} 
\end{align} 
$$

The update step for $\mathbf{H}$ then becomes:

$$
\begin{align} \label{eq:update_H}
  \mathbf{H} &\leftarrow  \mathbf{H} -  \alpha(\mathbf{WW}^T\mathbf{H} - \mathbf{W}^T\mathbf{X})
\end{align} 
$$

As it was proposed by D. Lee and H. Seung in their paper [Algorithms for Non-negative Matrix Factorization](https://proceedings.neurips.cc/paper_files/paper/2000/file/f9d1152547c0bde01830b7e8bd60024c-Paper.pdf), it is possible to pick a step size, which ensures that $\mathbf{H}$ stays positive. Setting $\alpha = \mathbf{H}/\mathbf{WW}^T\mathbf{H}$ we get:

$$
\begin{align} \label{eq:update_H_w_step}
  \mathbf{H} &\leftarrow  \mathbf{H} - \frac{\mathbf{H}}{\mathbf{WW}^T\mathbf{H}} \circ \mathbf{WW}^T\mathbf{H} + \frac{\mathbf{H}}{\mathbf{WW}^T\mathbf{H}} \circ \mathbf{W}^T\mathbf{X} \\[1.2em]
  \mathbf{H} &\leftarrow \mathbf{H} \circ \frac{\mathbf{W}^T\mathbf{X}}{\mathbf{WW}^T\mathbf{H}} 
\end{align} 
$$


