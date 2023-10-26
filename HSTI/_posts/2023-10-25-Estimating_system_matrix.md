---
layout: single
classes: wide
title:  "Chasing the system response matrix"
date:   2023-10-25
---

A reoccurring issue is not knowing the exact response matrix of the hyperspectral camera. This matrix should describe the relationship between the mirror separation of the scanning Fabry-Pérot interferometer (SFPI), the wavelength of the incident light and the output of the camera. Knowing this would aid in reconstructing the wavelength/wavenumber dependent spectra of the incident light, which at the moment are obscured and hidden in the interferograms. 

I therefore set out to find this response matrix and will in the following document my attempts and findings.

## We need data... this is how we get it

All of the experiments are going to be transmission measurements, since this gives the most well defined reference spectra. A black body radiator set to a given temperature gives a well defined emission spectrum given by the spectral exitance: 

$$
\begin{align} \label{eq:BB_exitance}
    M_{BB, \tilde{\nu}}(T) = 2\pi hc^2\tilde{\nu}^3 \frac{1}{\exp{\frac{hc\tilde{\nu}}{k_B T}} - 1}, 
\end{align}
$$

where $\tilde{\nu}$ represents the wavenumber given as the reciprocal of the wavelength $1/\lambda$, $h = 6.6261\times 10^{-34} \textrm{J}\cdot\textrm{Hz}^{-1}$ is the Planck constant, $c=2.9979\times 10^{8}$ m/s is the speed of light, and $k_{B} = 1.3806\times 10^{-23}\textrm{J}\cdot\textrm{K}^{-1}$ is the Boltzmann constant. Finally, $T$ denotes the absolute temperature of the black body. For more on black body radiation, click [here]({% link HSTI/_posts/2023-03-16-black_body_exitance_spec.md %}).


A black body radiation source is used in the lab and the precise spectrum can then be calculated from Eq. (\ref{eq:BB_exitance}). Because we're working with transmission measurements, it is then possible to calculate the spectrum of the light incident on the SFPI as the product of the black body source and the FTIR transmission spectrum of the sample. Fig. 1 gives a schematic representation of how the black body spectrum firstly is transmitted through a sample (in this case a gas cell with methanol vapor, but i can be anything transmissive) and how it is converted to a interferogram as recorded by the hyperspectral thermal camera. In these experiments we are only going to consider light hitting the center of the microbolometer sensor to avoid dealing with spatial variations across the sensor and the spectral bending effects associated with light rays of non-perpendicular incidence. 


<center><img src="/HSTI/images/Estimating_system_matrix/Camera_FPI_BB_v5_brown.png" alt="Experimental setup" width="100%" height="100%">
<figcaption><b>Fig 1:</b> Illustration of how a transmission spectrum of methanol vapor is turned into an interferogram. (1): Light from a black body source passes through (2) a gas cell containing methanol vapor and produces (3) a transmission spectrum unique to methanol. The light then enters (4) the scanning Fabry-Pérot interferometer which only transmit (5) a certain distribution of wavelengths depending on its mirror separation. For a given mirror separation, (6) the thermal camera captures an image and stores it in a data cube. From the spectral axis of the data cube it is then possible to extract (7) the methanol interferogram. </figcaption></center>
 


46 of different materials have been measured as well the pure black body without any material in front of it. The camera is only sensitive in the range from ≈ 1250 cm<sup>-1</sup>, ($\lambda = 8$ µm) to ≈ 650 cm<sup>-1</sup>, ($\lambda = 15.38$ µm) but to make sure not to leave anything important out, data from 1300 cm<sup>-1</sup>, ($\lambda = 7.69$ µm) to 600 cm<sup>-1</sup>, ($\lambda = 16.67$ µm) is included. The FTIR spectra of all materials can be found [here](/HSTI/images/Estimating_system_matrix/ftir_specs.png). The light incident on the SFPI is found as the product of the black body emission given by Eq. (\ref{eq:BB_exitance}) and the FTIR transmission spectrum as depicted by Fig. 2. Some of the materials are imaged multiple times at different black body temperatures, and the interferograms of every single measurement (114 in total) are depicted [here](/HSTI/images/Estimating_system_matrix/interferograms.png) along with the exitance spectra [here](/HSTI/images/Estimating_system_matrix/EVERY_BB_ftir.png). 


<center><img src="/HSTI/images/Estimating_system_matrix/ammonia_ftir.png" alt="FTIR spectrum of ammoina" width="100%" height="100%">
<figcaption><b>Fig 2:</b> Pure FTIR transmission spectrum of ammonia and after being multiplied by the exitance spectrum of a 150 ºC black body. </figcaption></center>

## Data preprocessing

An inherent challenge of the hyperspectral camera is the fact that at no point during the image capture, do we know the absolute mirror separation. We only know the relative displacement of the mirrors based on the interferograms of three laser diodes mounted around the mirror perimeter. To solve this we need to have a spectral reference point which all data cubes can be aligned to. For this, a 8.226 µm bandpass filter is placed in front of a hot plate set to ≈ 75 ºC. Both are positioned in the frame to be just above the black body. The SFPI goes through three transmission orders during the sweep, and the second (middle) order is used for the alignment. This is "defined" to occur at a mirror separation (MS) of 8.13 µm. The spectral resolution of the data cube is note necessary high enough to capture the exact position of the maximum of the 2nd transmission order. The central peak is therefore fitted with a Gaussian with 10 times more data points compared to the number of spectral channels in the data cube. The relative displacement which is calculated based on the laser diode interferograms is then offset until the position of the fitted Gaussian aligns with an MS of 8.13 µm. The wavelength of the laser diodes have been experimentally determined to be 680 nm.

Fig. 3 illustrates the interferograms before and after the alignment. Apart from the alignment of spectral axes, the camera also does not save the same number of spectral channels in each cube. This means that when all data cubes have been loaded and spectrally aligned, they must be interpolated along the MS axis. A linear scale is chosen with its starting value corresponding to the highest "initial MS" in the data set, and similarly the end point is chosen to correspond to the lowest "final MS". The number of interpolation points is chosen to correspond to the lowest number of spectral channels across the data set, which usually is ≈ 150. Only now are we able to compare measurements across data cubes and we can continue with our journey towards the perfect fit. 

<center><img src="/HSTI/images/Estimating_system_matrix/bandpass_alignment.png" alt="bandpass interferograms" width="100%" height="100%">
<figcaption><b>Fig 3:</b> Interferograms of bandpass filter with central wavelength of 8.226 µm. The first plot show interferograms depicted against the "step number" which is the spectral designation given to each spectral channel in the cube. The plot below show the interferograms after alignment and interpolation.  </figcaption></center>

############################################################################

MORE DETAILS AND ILLUSTRATIONS ARE NEED FOR THIS PART AS WELL AS MORE OBJECTIVE EVALUATION OF THE PERFORMENCE OF THIS METHOD

############################################################################


## Solving for the system matrix

My initial attempt to find the response matrix is by turning it into a least squares problem. The unknown system matrix is described by the matrix $\mathbf{A}$, the spectra of the incident light is stored as the columns of the matrix $\mathbf{X}$, and the recorded interferograms are represented by the columns of the matrix $\mathbf{B}$. The problem can therefore be formulated as

$$
\begin{align} \label{eq:AXB}
    \mathbf{AX} = \mathbf{B}, 
\end{align}
$$

where we want to solve for $\mathbf{A}$. 

The known matrices are represented graphically in Fig. 4

<center><img src="/HSTI/images/Estimating_system_matrix/X_B.png" alt="Matrices for AX=B" width="100%" height="100%">
<figcaption><b>Fig 4:</b> The exitance spectra are stored in the columns of $\mathbf{X}$ and the interferograms of each sample is stored in the columns of $\mathbf{B}$. Notice that the interferograms of $\mathbf{B}$ have been mean centered, but not further processed.  </figcaption></center>

This system is hugely under-determined as the number of rows in $\mathbf{X}$ is 2801, and the number of rows in $\mathbf{B}$ is ≈ 150 (The camera simply captures as many images as it can during a sweep, and the total number changes from run to run). The dimensions of $\mathbf{A}$ then becomes $m\times n = 2801\times 150$ which means that there are many more variables to solve for compared to the number of equations. Finding a solution is not a problem since there are an infinite number of solutions satisfying $\mathbf{AX} = \mathbf{B}$, but finding a solution which is physical and can be used for other spectra not in the data set turns out to be quite a challenge. To give the solver the best chance of finding a satisfactory solution we are going to need as many different samples as possible covering as large a part of the spectrum as possible. 


However, we are working completely blind when it comes to finding a realistic solution of $\mathbf{A}$. The Airy function can be used to calculate the transmission of a theoretical SFPI for any given combination of mirror separation and wavelength. 

$$
\begin{align} \label{eq:airy}
	\Gamma = \frac{1}{1 + F\sin^2{2\pi d \tilde{\nu}}}
\end{align}
$$

Here, $\Gamma$ is the transmission of the SFPI at the mirror separation $d$ and wavenumber $\tilde{\nu}$. $F$ is the coefficient of finesse defined as

$$
\begin{align} \label{eq:F}
	F = \frac{4r^2}{(1-r^2)^2}, 
\end{align}
$$

with $r$ being the reflectance of the mirror. In this case the mirrors have a reflectance of $r = 0.8$ resulting in $F=19.75$. The airy function reaches a maximum of 1 whenever $2\pi d \tilde{\nu} = m \pi$ where $m = 0, 1, 2, \dots$. The conditions for transmission can therefore be expressed as

$$
\begin{align} \label{eq:transmission_condition}
	d = \frac{m}{2\tilde{\nu}}, \qquad	d = m \frac{\lambda}{2}, \qquad \lambda = \frac{2}{m} d, \qquad  \tilde{\nu} = \frac{m}{2d}
\end{align} 
$$

Fig. 5 shows the transmission calculated using the airy function in Eq. (\ref{eq:airy}) for all combinations wavelengths and mirror separations in this study.  

<center><img src="/HSTI/images/Estimating_system_matrix/initial_guess_A.png" alt="Airy matrices" width="100%" height="100%">
<figcaption><b>Fig 5:</b> Transmission of SFPI at various mirror separations and wavelengths calculated based on the Airy function given in Eq. (\ref{eq:airy}). </figcaption></center>

The airy function can serve as a good initial estimate for $\mathbf{A}$. The objective function we are trying to minimize can therefore be written as follows

\begin{align} \label{eq:cost_function}
	\textrm{minimize:}||\mathbf{AX} - \mathbf{B}||^2 + \gamma ||\mathbf{A} - \mathbf{\hat{A}}||^2, 
\end{align} 

where $\mathbf{\hat{A}}$ is the initial guess for a solution, and $\gamma > 0$ is a regularization parameter.

As described in [this Stack Exchange post](https://math.stackexchange.com/questions/4760280/how-to-solve-matrix-equation-mathbfax-mathbfb-for-mathbfa-based-o), it is possible to solve the problem directly using

$$
\begin{align} \label{eq:direct_solve}
	\mathbf{A} = (\mathbf{B}\mathbf{X}^T + \gamma_{init}\mathbf{\hat{A}})(\mathbf{X}\mathbf{X}^T + \gamma_{reg} \mathbf{M})^{-1}
\end{align} 
$$

where $\gamma_{init}$ and $\gamma_{reg}$ are regularization parameters for weighting the initial guess and regularization matrix $\mathbf{M}$ respectively. In the most basic case, $\mathbf{M}$ is usually set to the identity matrix, $\mathbf{I}$. However, this yields some pretty bad - or at least nonphysical - results. Fig. 6 shows solutions to $\mathbf{A}$ based on Eq. (\ref{eq:direct_solve}) with different values of $\gamma_{init}$ and $\gamma_{reg}$.    

<center><img src="/HSTI/images/Estimating_system_matrix/newA_I_reg.png" alt="Calculated A matrix, identity regularization" width="100%" height="100%">
<figcaption><b>Fig 6:</b> $\mathbf{A}$ calculated using Eq. (\ref{eq:direct_solve}) with $\mathbf{M} = \mathbf{I}$ and with Airy function as initial guess. </figcaption></center>

To no surprise it appears that a larger $\gamma_{init}$ leads to the final solution resembling the Airy function more closely. There are however some slight differences in their shape. Notice how the 2nd order of the Airy function "terminates" just above column 2000. This is also the case for all of the calculated solutions of $\mathbf{A}$ except the one with $\gamma_{init} = 1 \times 10^0$ and $\gamma_{reg} = 1 \times 10^{-3}$. Here the second order crosses the border slightly below column 2000. Also, the orders do no reach the edges as for the rest of the solutions. This is to be expected of the true solution, as the camera is not sensitive to all the wavelengths included in the data. 

#### Random starting guess
I would therefore like to see, if it is possible to find a solution which resembles the Airy function even without including it as the initial guess. Fig. 7 shows solutions of $\mathbf{A}$ for different values of $\gamma_{init}$ and $\gamma_{reg}$, but this time with a random initial guess. Now it is actually possible to find a solution to the problem which is reminiscent of the Airy function - even without providing it to the solver in the first place. It is however also evident that the solutions are quite sensitive to the choice of regularization parameters.   

<center><img src="/HSTI/images/Estimating_system_matrix/newA_I_reg_random_guess_smaller.png" alt="Calculated A matrix, identity regularization, random initial guess" width="100%" height="100%">
<figcaption><b>Fig 7:</b> $\mathbf{A}$ calculated using Eq. (\ref{eq:direct_solve}) with $\mathbf{M} = \mathbf{I}$ and with RANDOM initial guess. </figcaption></center>


#### Random starting guess and new regularization matrix

Another regularization matrix is introduced and has the form of

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

This form of regularization aims to suppress oscillations in the solution along the "x-axis" as it is derived from the 2nd order difference method. Roughly speaking it states that if we are looking at the $j^\textrm{th}$ element in the $i^\textrm{th}$ row of $\mathbf{A}$, then $-\mathbf{A}\_{i, j-1} + 2\mathbf{A}\_{i, j} - \mathbf{A}\_{i, j+1} = 0$. Then the higher the value of $\gamma\_{reg}$, the stronger this constraint is enforced. Fig. 8 show the results using this type of regularization and appears to giv a result closer to what is expected compared to when using the identity matrix for regularization.   

<center><img src="/HSTI/images/Estimating_system_matrix/newA_M_reg_random_guess_smaller.png" alt="Calculated A matrix, identity regularization, random initial guess" width="100%" height="100%">
<figcaption><b>Fig 8:</b> $\mathbf{A}$ calculated using Eq. (\ref{eq:direct_solve}) with $\mathbf{M} = $ Eq. (\ref{eq:M_reg}) and with RANDOM initial guess. </figcaption></center>

So it is possible to find a solution which comes close to what is expected theoretically. But how close is it actually. Some deviation from theory are to be expected, but to get a better feeling for how different the solutions are, I have overlaid the Airy matrix on top of one of the solutions for $\mathbf{A}$ with a random initial guess (Fig. 9). I have also found a theoretical solution using the transfer matrix method (TMM) (MORE INFORMATION ABOUT THIS SHOULD PROBABLY BE GIVEN IN ANOTHER POST). The least squares solution has been plotted in gray-scale, while only the maxima of the theoretical matrices are displayed in color. Notice here, that there is almost a perfect fit between the TMM matrix and the solution, whereas the Airy matrix in comparison deviates much more. This indicates that the TMM estimate is actually quite close to what would be the true solution.  

<center><img src="/HSTI/images/Estimating_system_matrix/airy_overlay.png" alt="Airy and TMM solution overlay on least squares solution" width="100%" height="100%">
<figcaption><b>Fig 9:</b> $\mathbf{A}$ calculated with 2nd order difference regularization, random initial guess and $\gamma_{init} = 1$ and $\gamma_{reg} = 10$. </figcaption></center>





