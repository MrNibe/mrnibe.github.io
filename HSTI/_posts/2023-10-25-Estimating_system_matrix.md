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

\begin{align} \label{eq:BB_exitance}
    M_{BB, \tilde{\nu}}(T) = 2\pi hc^2\tilde{\nu}^3 \frac{1}{\exp{\frac{hc\tilde{\nu}}{k_B T}} - 1}, 
\end{align}

where $\tilde{\nu}$ represents the wavenumber given as the reciprocal of the wavelength $1/\lambda$, $h = 6.6261\times 10^{-34} \textrm{J}\cdot\textrm{Hz}^{-1}$ is the Planck constant, $c=2.9979\times 10^{8}$ m/s is the speed of light, and $k\_{B} = 1.3806\times 10^{-23}\textrm{J}\cdot\textrm{K}^{-1}$ is the Boltzmann constant. Finally, $T$ denotes the absolute temperature of the black body. For more on black body radiation, click [here]({% link HSTI/_posts/2023-03-16-black_body_exitance_spec.md %}).


A black body radiation source is used in the lab and the precise spectrum can then be calculated from Eq. (\ref{eq:BB_exitance}). Because we're working with transmission measurements, it is then possible to calculate the spectrum of the light incident on the SFPI as the product of the black body source and the FTIR transmission spectrum of the sample. Fig. 1 gives a schematic representation of how the black body spectrum firstly is transmitted through a sample (in this case a gas cell with methanol vapor) and how it is converted to a interferogram as recorded by the hyperspectral thermal camera. In these experiments we are only going to consider light hitting the center of the microbolometer sensor to avoid dealing with spatial variations across the sensor and the spectral bending effects associated with light rays of non-perpendicular incidence. 


<center><img src="/HSTI/images/Estimating_system_matrix/Camera_FPI_BB_v5_brown.png" alt="Experimental setup" width="100%" height="100%">
<figcaption><b>Fig 1:</b> Illustration of how a transmission spectrum of methanol vapor is turned into an interferogram. (1): Light from a black body source passes through (2) a gas cell containing methanol vapor and produces (3) a transmission spectrum unique to methanol. The light then enters (4) the scanning Fabry-Pérot interferometer which only transmit (5) a certain distribution of wavelengths depending on its mirror separation. For a given mirror separation, (6) the thermal camera captures an image and stores it in a data cube. From the spectral axis of the data cube it is then possible to extract (7) the methanol interferogram. </figcaption></center>
 


46 of different materials have been measured as well the pure black body without any material in front of it. The camera is only sensitive in the range from ≈ 1250 cm<sup>-1</sup>, ($\lambda = 8$ µm) to ≈ 625 cm<sup>-1</sup>, ($\lambda = 16$ µm) so only this range is considered. The FTIR spectra of all materials can be found [here](/HSTI/images/Estimating_system_matrix/ftir_specs.png). The light incident on the SFPI is found as the product of the black body emission given by Eq. (\ref{eq:BB_exitance}) and the FTIR transmission spectrum as depicted by Fig. 2. Some of the materials are imaged multiple times at different black body temperatures, and the interferograms of every single measurement (114 in total) are depicted [here](/HSTI/images/Estimating_system_matrix/interferograms.png) along with the exitance spectra [here](/HSTI/images/Estimating_system_matrix/EVERY_BB_ftir.png). 


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

\begin{align} \label{eq:AXB}
    \mathbf{AX} = \mathbf{B}, 
\end{align}

where we want to solve for $\mathbf{A}$. 

The known matrices are represented graphically in Fig. 4

<center><img src="/HSTI/images/Estimating_system_matrix/X_B.png" alt="Matrices for AX=B" width="100%" height="100%">
<figcaption><b>Fig 4:</b> The exitance spectra are stored in the columns of $\mathbf{X}$ and the interferograms of each sample is stored in the columns of $\mathbf{B}$. Notice that the interferograms of $\mathbf{B}$ have been mean centered, but not further processed.  </figcaption></center>

This system is hugely under-determined as the number of rows in $\mathbf{X}$ is 2801, and the number of rows in $\mathbf{B}$ is ≈ 150 (The camera simply captures as many images as it can during a sweep, and the total number changes from run to run). The dimensions of $\mathbf{A}$ then becomes $m\times n = 2801\times 150$ which means that there are many more variables to solve for compared to the number of equations. Finding a solution is not a problem since there are an infinite number of solutions satisfying $\mathbf{AX} = \mathbf{B}$, but finding a solution which is physical and can be used for other spectra not in the data set turns out to be quite a challenge. To give the solver the best chance of finding a satisfactory solution we are going to need as many different samples as possible covering as large a part of the spectrum as possible. 


