---
layout: single
classes: wide
title:  "Calculating frequency spectrum from interferograms"
date:   2024-01-16
---

This section will be mostly a selection of assorted notes on some of my findings as I have tried to convert from the mirror separation dependent interferograms to the frequency/wavelength dependent incident spectra. There will for this reason not be any real common thread going through the text. 


Firstly, we must setup the model by calculating the total radiation flux both incident on the sensor but also the amount of flux leaving the system:

$$
\begin{align} \label{eq:fpi_flux}
	\mathbf{\Phi} = \mathbf{T_{SFPI}}\circ(\mathbf{t_{samp}}\odot\mathbf{m_{BB}}(T_{BB}) + (\mathbf{1} - \mathbf{t_{samp}})\odot\mathbf{m_{env}}(T_{env})) + \mathbf{R_{SFPI}} \circ \mathbf{m_{sens}}(T_{sens}) 
\end{align} 
$$

Here, $\odot$ and $\circ$ represent element-wise (Hadamard product) and row/element-wise multiplication respectively. By row/element-wise I mean that each row of the matrix is multiplied element-wise by each element in the vector. $\mathbf{T_{SFPI}}$ and $\mathbf{R_{SFPI}}$ are the transmission and reflection matrices of the SFPI calculated using TMM. $\mathbf{t_{samp}}$ is the FTIR transmission spectrum of the sample. Since I do not have the reflectance spectra of the samples, these are estimated simply by $(\mathbf{1} - \mathbf{r_{samp}})$ (assuming the samples are loss-less). $\mathbf{m_{BB}}(T_{BB})$, $\mathbf{m_{env}}(T_{env})$, and $\mathbf{m_{sens}}(T_{sens})$ are the black body spectra of the black body behind the sample, the environmental background emission and the sensor. $T_{BB}$, $T_{env}$, and $T_{sens}$ are the temperatures of the black body, the environment, and the sensor respectively. 

Since the signal measured by the microbolometer is related to the difference in $\mathbf{\Phi}$ and the flux of the sensor itself. 

$$
\begin{align} \label{eq:fpi_signal}
	\mathbf{\Delta\Phi} = \mathbf{\Phi} - \mathbf{m_{sens}}(T_{sens}) 
\end{align} 
$$

Finally, the interferogram is related to the matrix-vector product of $\mathbf{\Delta\Phi}$ and the system response $\mathbf{s}$

$$
\begin{align} \label{eq:sensor_response_Ax=b}
	\mathbf{i} = \mathbf{\Delta\Phi} \mathbf{s} 
\end{align} 
$$

We know $\mathbf{i}$ (because we measured it), we have an estimate of $\mathbf{s}$ (from [here]({% link HSTI/_posts/2023-10-25-Estimating_system_matrix.md %})) and we have a pretty good idea of some parts of $\mathbf{\Delta\Phi}$. The "unknown" part of $\mathbf{\Delta\Phi}$ is the spectrum of the subject:

$$
\begin{align} \label{eq:unknown_part}
	\mathbf{x}=\mathbf{t_{samp}}\odot\mathbf{m_{BB}}(T_{BB}) + (\mathbf{1} - \mathbf{t_{samp}})\odot\mathbf{m_{env}}(T_{env})
\end{align} 
$$

From here it is possible to rewrite and combine Eq. \ref{eq:fpi_signal}, \ref{eq:sensor_response_Ax=b} in order to transform the problem back into $\mathbf{Ax}=\mathbf{b}$. The right-hand-side becomes:

$$
\begin{align} \label{eq:rhs}
	\mathbf{b}=\mathbf{i} - [\mathbf{R_{SFPI}} \circ \mathbf{m_{sens}}(T_{sens}) - \mathbf{m_{sens}}(T_{sens})]\mathbf{s}
\end{align} 
$$

Note here that $\mathbf{m_{sens}}(T_{sens})$ is subtracted from each row in $\mathbf{R_{SFPI}} \circ \mathbf{m_{sens}}(T_{sens})$ before the dotproduct of the entire thing and $\mathbf{s}$ is calculated. $\mathbf{A}$ then becomes:

$$
\begin{align} \label{eq:A}
	\mathbf{A} = \mathbf{T_{SFPI}}\circ\mathbf{s}
\end{align} 
$$

We are then left to find a method of calculating $\mathbf{x}$ from $\mathbf{A}$ and $\mathbf{b}$... and that turns out to be easier said than done...


## Tikhonov regularization
The first attempt is calculating $\mathbf{x}$ directly from the pseudoinverse and tikhonov regularization. We define the regularization matrix $\mathbf{M}$ as

$$
\begin{align} \label{eq:M_reg}
	\mathbf{M} = \begin{bmatrix}
	1 & -1 & 0 & 0 & 0  & \dots \\
	-1 & 2 & -1 & 0 & 0 & \dots\\
	0 & -1 & 2 & -1 & 0 & \dots\\
	\vdots & \ddots & \ddots & \ddots & \ddots & \ddots\\
	\dots & 0 & 0 & -1 & 2 & -1\\
	\dots & 0 & 0 & 0 & -1 & 1\\
	\end{bmatrix}
\end{align} 
$$

We can then solve for $\mathbf{x}$ directly

$$
\begin{align} \label{eq:tikhonov_x}
	\mathbf{x} = (\mathbf{A}^T\mathbf{A} + \gamma \mathbf{M})^{-1}\mathbf{A}^T\mathbf{b}
\end{align} 
$$

Here, $\gamma$ is a regularization parameter controlling the influence of $\mathbf{M}$.


Trying to solve for the dichloromethane spectrum yields the result presented in Fig 1.

<center><img src="/HSTI/images/calculating_frequency_spectrum/dichloromethane_tikhonov.png" alt="Dichloromethane from tikhonov" width="80%" height="80%">
<figcaption><b>Fig 1:</b> Reconstruction of dichloromethane based on measured interferogram and using Tikhonov method.  </figcaption></center>



## Gauss-Seidel

From "Iterative Methods for Sparse Linear Systems" by Yousef Saad. 

This is an iterative row projection method. 

$$
\begin{align} \label{eq:gauss_seidel}
	&1. \quad\textrm{Choose initial }  x\nonumber\\
	&2. \quad\textrm{For }i = 1, 2, ..., n \textrm{ do}: \nonumber\\
	&3. \quad\quad \delta_i = \omega \frac{b_i - \langle \mathbf{x} | \mathbf{A}^T\mathbf{e}_i \rangle}{‖\mathbf{A}^T\mathbf{e}_i‖_2^2} \nonumber\\
	&4. \quad\quad \mathbf{x} = \mathbf{x} + \delta_i \mathbf{A}^T\mathbf{e}_i\nonumber
\end{align} 
$$

Here, $b_i$ represents the $i^\textrm{th}$ element of $\mathbf{b}$ and $\langle\mathbf{a}_1\|\mathbf{a}_2\rangle$ is the inner dot product defined as $\mathbf{a}_1^\dagger\mathbf{a}_2$ with superscript $\dagger$ denoting the conjugate transpose. $\mathbf{e}_i$ is the $i^\textrm{th}$ column of the identity matrix which effectively means that $\mathbf{A}^T\mathbf{e}_i$ simply is the transpose of the $i^\textrm{th}$ row of $\mathbf{A}$. $\omega$ is denoted as a relaxation parameter. 

This method is relatively quick, but as seen in Fig. 2, not really that accurate. I also have not been able to implement Tikhonov regularization in this scheme - I am not quite sure why it does not work.


<center><img src="/HSTI/images/calculating_frequency_spectrum/dichloromethane_Gauss-Seidel.png" alt="Dichloromethane from Gauss-Seidel" width="80%" height="80%">
<figcaption><b>Fig 2:</b> Reconstruction of dichloromethane based on measured interferogram and using Gauss-Seidel method.  </figcaption></center>

## "Fast" Non-Negative Least Squares (FNNLS)

This least squares solver solves the $\mathbf{Ax}=\mathbf{b}$ problem subject to $\mathbf{x} >= 0$. The Tikhonov regularization is implemented the following:

$$
\begin{align} \label{eq:A_tilde}
	\mathbf{\tilde{A}} = \begin{bmatrix}
	\mathbf{A} \\
	\gamma\mathbf{M}
	\end{bmatrix}
\end{align} 
$$

$$
\begin{align} \label{eq:b_tilde}
	\mathbf{\tilde{b}} = \begin{bmatrix}
	\mathbf{b} \\
	\mathbf{0}
	\end{bmatrix}
\end{align} 
$$

The FNNLS implementation in python is then used to solve $\mathbf{\tilde{A}x}=\mathbf{\tilde{b}}$. This however is VERY SLOW - upwards of 20 minutes on the M1 Macbook running full tilt. The result is shown in Fig. 3 

<center><img src="/HSTI/images/calculating_frequency_spectrum/dichloromethane_fnnls.png" alt="Dichloromethane from FNNLS" width="80%" height="80%">
<figcaption><b>Fig 3:</b> Reconstruction of dichloromethane based on measured interferogram and using FNNLS.  </figcaption></center>

## Conjugate gradient (Craig's method)
This one is also from "Iterative Methods for Sparse Linear Systems" by Yousef Saad. Here I have managed to do Tikhonov regularization in a similar way to the FNNLS method.

$$
\begin{align} \label{eq:CGNE}
	1.& \quad\textrm{Choose initial }  x\nonumber\\
	2.& \quad \mathbf{r}_0 = \mathbf{\tilde{b}} - \mathbf{\tilde{A}x}_0 \nonumber\\
	3.& \quad \mathbf{p}_0 = \mathbf{\tilde{A}}^T\mathbf{r}_0 \nonumber\\
	4.& \quad\textrm{For }i = 1, 2, ... \textrm{ until convergence do}: \nonumber\\
	5.& \quad\quad \alpha_i = \langle\mathbf{r}_i | \mathbf{r}_i\rangle/\langle\mathbf{p}_i | \mathbf{p}_i\rangle \nonumber\\
	6.& \quad\quad \mathbf{x}_{i+1} = \mathbf{x}_i + \alpha_i \mathbf{p}_i\nonumber\\
	7.& \quad\quad \mathbf{r}_{i+1} = \mathbf{r}_i - \alpha_i \mathbf{\tilde{A}p}_i\nonumber\\
	8.& \quad\quad \beta_i = \langle\mathbf{r}_{i+1} | \mathbf{r}_{i+1}\rangle/\langle\mathbf{r}_{i} | \mathbf{r}_{i}\rangle \nonumber\\
	9.& \quad\quad \mathbf{p}_{i+1} = \mathbf{\tilde{A}}^T\mathbf{r}_{i+1} + \beta_i \mathbf{p}_i\nonumber\\
	10.&\quad\textrm{End do}\nonumber
\end{align} 
$$

For these calculations I have not set a convergence criterion but rather just an upper limit to the number of iterations. There are therefore two parameters to tweek the solver: The regularization parameter, $\gamma$ and the number of iterations - both of which have quite an impact on the solutions. 

Of course the computation takes longer the more iterations are performed. 1000 iterations take around 15 seconds. Fig. 4 illustrate how the reconstructions are influenced by the number of iterations and Fig. 5 show how the regularization parameter affects the results. 

<center><img src="/HSTI/images/calculating_frequency_spectrum/dichloromethane_CGNE_const_gamma.png" alt="Dichloromethane from CGNE with constant gamma" width="100%" height="100%">
<figcaption><b>Fig 4:</b> Reconstruction of dichloromethane based on measured interferogram and using CG with constant $\gamma=1\times 10^9$.  </figcaption></center>

<center><img src="/HSTI/images/calculating_frequency_spectrum/dichloromethane_CGNE_const_it.png" alt="Dichloromethane from CGNE with constant gamma" width="100%" height="100%">
<figcaption><b>Fig 5:</b> Reconstruction of dichloromethane based on measured interferogram and using CG with constant number of iterations (500).  </figcaption></center>

With the dichloromethane spectrum it might be a little difficult to judge whether the algorithm is doing anything at all since the two features are in either end of the spectrum, and the reconstructions tend towards zero at both ends. I tried using the same method on the methanol spectrum as presented in Fig. 6. Here It is clear to see that the method correctly captures the absorption bands at ≈ 9.5 µm. Still it is not a great fit. 

<center><img src="/HSTI/images/calculating_frequency_spectrum/methanol_CGNE.png" alt="Dichloromethane from CGNE with constant gamma" width="80%" height="80%">
<figcaption><b>Fig 6:</b> Reconstruction of methanol based on measured interferogram and using CG with $\gamma=1\times 10^8$ and $3000$ iterations.  </figcaption></center>


## Something about Krylov spaces?

The Krylov space is a subspace of $\mathbf{A}$ and $\mathbf{b}$:

$$
\begin{align} \label{eq:krylov}
	\mathcal{K}_k = \textrm{span} \{\mathbf{A}^T\mathbf{b}, (\mathbf{A}^T\mathbf{A})\mathbf{A}^T\mathbf{b}, (\mathbf{A}^T\mathbf{A})^2\mathbf{A}^T\mathbf{b} \dots (\mathbf{A}^T\mathbf{A})^{k-1}\mathbf{A}^T\mathbf{b} \}
\end{align} 
$$

This forms a set of $k$ basis vectors which span $\mathcal{K}_k$ and they can even be orthonormal. An algorithm based on the Gram-Schmidt (QR-factorization) can be formulated (from chapter 6 in [Discrete Inverse Problems: Insight and Algorithms](https://epubs.siam.org/doi/book/10.1137/1.9780898718836).   

$$
\begin{align} \label{eq:krylov_routine}
	1.& \quad\textrm{Choose number of components, }  k\nonumber\\
	2.& \quad \mathbf{w}_1 = \mathbf{A}^T\mathbf{b} \nonumber\\
	3.& \quad \mathbf{w}_1 = \mathbf{w}_1 / ‖\mathbf{w}_1‖_2 \nonumber\\
	4.& \quad\textrm{For }i = 2, 3, ... k \textrm{ do}: \nonumber\\
	5.& \quad\quad \mathbf{w}_i = \mathbf{A}^T\mathbf{A}\mathbf{w}_{i-1} \nonumber\\
	6.& \quad\quad \textrm{For }j = 1, ... i-1 \textrm{ do}: \nonumber\\
	7.& \quad\quad\quad \mathbf{w}_i = \mathbf{w}_i - (\mathbf{w}_j^T\mathbf{w}_i)\mathbf{w}_j\nonumber\\
	8.& \quad\quad \mathbf{w}_i = \mathbf{w}_i / ‖\mathbf{w}_i‖_2 \nonumber\\
\end{align} 
$$

Each vector $\mathbf{w}_i$ form the columns of the matrix $\mathbf{W}$. The higher the component, the higher the frequencies are represented in the signal (Fig. 7). 

<center><img src="/HSTI/images/calculating_frequency_spectrum/krylov_vectors.png" alt="Krylov vectors" width="100%" height="100%">
<figcaption><b>Fig 7:</b> The first 6 orthonormal vectors of $\mathcal{K}_k$ for the dichloromethane measurements.  </figcaption></center>


It is then possible to use $\mathbf{W}$ as basis vectors and project $\mathbf{Ax} = \mathbf{b}$ onto them by setting:

$$
\begin{align} \label{eq:krylov_Ax_b}
	&\mathbf{x}^{(k)} = \mathbf{W}_k \mathbf{y}^{(k)} \\
	\Rightarrow & \mathbf{y}^{(k)} = \textrm{argmin}_y ‖\mathbf{AW}_k\mathbf{y} - \mathbf{b}‖_2
\end{align} 
$$

which can then be solved for $\mathbf{y}$ in any way we as we see fit. Firstly, I will solve it naively by simply using:

$$
\begin{align} \label{eq:solve_krylov}
	&\mathbf{A'}_{k} = \mathbf{AW}_k \\
	& \mathbf{y}^{(k)} = (\mathbf{A'}_k^T\mathbf{A'}_k)^{-1}\mathbf{A'}_k^T\mathbf{b}
\end{align} 
$$

Fig 8 illustrates how $k$ influences the solutions. The more components are included in the projection, the more unstable/noisy the solution. 

<center><img src="/HSTI/images/calculating_frequency_spectrum/dichloromethane_krylov_no_tikhonov.png" alt="Krylov solutions" width="100%" height="100%">
<figcaption><b>Fig 8:</b> Influence of $k$ in the solutions. No other regularization is added.  </figcaption></center>


We can then use Tikhonov regularization as usual when solving for $\mathbf{y}^{(k)}$. This has the expected effect off lowering the amount of oscillations as depicted in Fig. 9.

<center><img src="/HSTI/images/calculating_frequency_spectrum/dichloromethane_krylov_w_tikhonov.png" alt="Krylov solutions with tikhonov" width="80%" height="80%">
<figcaption><b>Fig 9:</b> Tikhonov regularization has been applied to one of the solutions from Fig. 8. 25 components are included in the model and $\gamma = 1\times 10^7$.  </figcaption></center>

