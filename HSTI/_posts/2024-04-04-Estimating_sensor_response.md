---
layout: single
classes: wide
title:  "Estimating sensor response"
date:   2024-04-04
---

I have previously had some luck with with using fast nonnegative least squares (FNNLS) to estimate the sensor response based on empirical measurements. For this I need for formulate an $\mathbf{Ax} = \mathbf{b}$ problem for the solver. [It has previously been described how to set up this problem, so I will not go into much detail here]({% link HSTI/_posts/2023-10-25-Estimating_system_matrix.md %})_. Just know that the $\mathbf{A}$ matrix expresses the known (estimated from FTIR) net flux (incident minus emitted), $\mathbf{b}$ is the measured interferogram (without offset - we'll discuss that later), and $\mathbf{x}$ is the sensor response we need to solve for.  

$$
\begin{align} \label{eq:fpi_flux}
	\mathbf{A} = \mathbf{T_{SFPI}}\diamond(\mathbf{t_{samp}}\circ\mathbf{m_{BB}}(T_{BB}) + \mathbf{r_{samp}}\circ\mathbf{m_{env}}(T_{env})) + \mathbf{R_{SFPI}} \diamond \mathbf{m_{sens}}(T_{sens}) - \mathbf{m_{sens}}(T_{sens}) 
\end{align} 
$$

Here, $\mathbf{t_{samp}}$, and $\mathbf{r_{samp}}$ are FTIR measurements of the sample's transmittance and reflectance respectively. $\mathbf{T_{SFPI}}$ and $\mathbf{R_{SFPI}}$ are transmittance and reflectance estimates of the SFPI and $\mathbf{m_{subscript}}(T)$ are black body spectra at the temperature, $T$. The solution needs to be smoothness regularized, and the final system of equations for all measurements therefore becomes

$$
\begin{align} \label{eq:soe}
	\begin{bmatrix}
	\mathbf{A_{acetone}} \\
	\mathbf{A_{ammonia}}\\
	\vdots\\
	\mathbf{A_{toluene}}\\
	\gamma_{reg}\mathbf{M}\\
	\end{bmatrix}
	\mathbf{x}
	=
	\begin{bmatrix}
	\mathbf{b_{acetone}} \\
	\mathbf{b_{ammonia}}\\
	\vdots\\
	\mathbf{b_{toluene}}\\
	\mathbf{0}
	\end{bmatrix}
\end{align} 
$$

where $\gamma_{reg}$ is the regularization parameter, and $\mathbf{M}$ is the smoothness regularization matrix.