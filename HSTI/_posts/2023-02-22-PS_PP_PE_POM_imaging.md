---
layout: single
classes: wide
title:  "Imaging plastics - Preliminary study of PP, PE, PS and POM using hyperspectral thermal imaging"
date:   2023-02-23
---

In this experiment, a hyperspectral thermal camera (HSTC) is used to measure different kinds of plastics: Polypropalene (PP, container 1 from *the wall of plastic*, Polyethylene (PE, container 2), Polystyrene (PS, container 165) and Polyoxymethylene (POM, container 63). The aim is to investigate whether it is possible to extract information about their emission spectra using the HSTC and compare to absorption measurements using attenuated total reflection (ATR).  

## Experimental setup
The HSTC is pointed vertically down onto an aluminum block placed on a hotplate set to 70 °C (Fig. 1). The distance between the front of the camera and the surface of the aluminum block is ≈ 40 cm. Once the block has reached its predetermined temperature, different plastic samples are placed on top of it and left to reach temperature equilibrium after ≈ 10 minutes. The sample surface temperature is assumed to be the same as the internal temperature of the aluminum block for the purposes of further data analysis, although the surface temperature in reality differs from that of the block.

<center><img src="/HSTI/images/preliminary_plastics_and_vanta_black/experimental_setup.svg" alt="Experimental setup" width="50%" height="50%">
<figcaption><b>Fig 1</b> Schematic drawing of experimental setup with the hyperspectral thermal camera pointing at plastic samples laying on top of an aluminum block heated to 70 °C. A Fabry-Pérot Interferometer (FPI) mounted in the lens provides the hyperspectral capabilities to the otherwise regular thermal camera. (Not to scale)</figcaption></center>



## A note on data processing

It is possible to estimate the FPI interferograms based on the spectrum of the incident light, $\mathbf{s}$, and a system matrix, $\mathbf{\Lambda}$. $\mathbf{s}$ is a column vector containing the spectrum of the incident light ether in terms of wavelengths or wavenumbers. The system matrix represents the combined FPI and microbolometer response at a combination of mirror separation distances and wavelengths/wavenumbers. The estimated interferogram is calculated using:

\begin{align} \label{eq:estimate_interferogram}
    \mathbf{i}_{estimate} = \mathbf{\Lambda}\mathbf{s}
\end{align}

Several different techniques are used when looking at the hyperspectral data cubes. One of them is standard normal variate (SNV), which is applied to the spectral axis to eliminate intensity differences and emphasize differences in spectral features:    

\begin{align} \label{eq:SNV}
    \mathrm{SNV}(\mathbf{i}) = \frac{\mathbf{i} - \bar{\mathbf{i}}}{\mathrm{STD}(\mathbf{i})}
\end{align}

where $\bar{\mathbf{i}}$ denote the average of $\mathbf{i}$ and $\mathrm{STD}(\mathbf{i})$ is the standard deviation.

A spatial median filter with a kernel size of 3 pixels is usually applied to each image of the data cube. Furthermore, the spectral axis is often smoothed using a Savitzky–Golay filter with a length of 11 samples, $2^\textrm{nd}$ order polynomial fit and $0^\textrm{th}$ derivative. 

## Results and discussion
The HSTC is sensitive to radiation of wavelengths between 8-16 µm (625-1250 cm<sup>-1</sup>). The absorption spectra of the plastics are measured using ATR. From Kirchhoff's radiation law it follows that the emissivity and the absorption of a sample in thermal equilibrium are equal. The ATR measurements are therefore used as the incident spectrum in Eq. \eqref{eq:estimate_interferogram} to calculate the estimated interferograms (Fig. 2).

<center><img src="/HSTI/images/preliminary_plastics_and_vanta_black/FTIR_ATR_+_interferograms_color.svg" alt="ATR and interferograms" width="80%" height="80%">
<figcaption><b>Fig 2</b>ATR spectra with accompanying simulated scanning FPI interferograms. The number preceding the plastic abbreviation indicate which container the specific plastic comes from.</figcaption></center>

### Why this doesn't work

Only PP and PE is investigated in the first HSTI and their interferograms are averaged across a $25\times25$ pixel region (Fig. 3). The interferograms from the two plastics are comparable and do not show the expected spectral features as predicted in Fig. 2. It is hypothesized that this is caused by the plastic having a high emissivity intrinsically. The radiation emitted by a black body is described by its exitance:

\begin{align} \label{eq:BB_exitance_nu}
    L_{BB}(\tilde{\nu}, T) = 2hc^2\tilde{\nu}^3 \frac{1}{\exp{\frac{hc\tilde{\nu}}{k_B T}} - 1}, 
\end{align}

where $h$ is Planck's constant, $c$ the speed of light, and $k_B$ the Boltzmann constant. 

The emissivity is defined as the ratio between the exitance of an object and that of a perfect black body emitter (Eq. \eqref{eq:BB_exitance_nu}):

\begin{equation}\label{eq:emissivity}
    \varepsilon  =  \frac{L}{L_{BB}} = \alpha 
\end{equation}

Here, $\varepsilon$ is the enissivity, $L$ is the exitance of the emitter. From Kirchhoff's radiation law it follows that the emissivity is equal to the absorption, $\alpha$.

<center><img src="/HSTI/images/preliminary_plastics_and_vanta_black/similar_plastics_PE_PP_color.svg" alt="Measured interferograms" width="100%" height="100%">
<figcaption><b>Fig 3</b> Image taken at 4.4 µm mirror separation of PP and LDPE placed on a 70 °C aluminum block. The two squares in (a) indicate the positions at which the graphs in (b) have been sampled. SNV, spatial median filter, and Savitzky–Golay filter have been applied to the data.</figcaption></center>

If the intrinsic emissivity (and hereby also the absorption) of the plastic samples is $\varepsilon_0 = 0.9$, then the total, wavenumber dependent emissivity becomes:

\begin{align} \label{eq:total_emissivity}
    \varepsilon_\textrm{tot}(\tilde{\nu}) = \varepsilon_0 + \varepsilon_\textrm{ATR}(\tilde{\nu}),
\end{align}

with $\varepsilon_\textrm{ATR}(\tilde{\nu}) = \alpha_\textrm{ATR}(\tilde{\nu}) $ being the emissivity/absorption measured using ATR. The emission spectrum of the plastics then becomes

\begin{align} \label{eq:ATR_exitance}
L(\tilde{\nu}, T) = (\varepsilon_0 +  \varepsilon_\textrm{ATR}(\tilde{\nu}))L_{BB}(\tilde{\nu},T)
\end{align} 

The adjusted emission spectra calculated based on Eq. \eqref{eq:ATR_exitance} are presented in Fig. 4 along with simulated interferograms based on the new emission spectra. 

<center><img src="/HSTI/images/preliminary_plastics_and_vanta_black/FTIR_ATR_+_interferograms_BB_color.svg" alt="ATR plus black body" width="80%" height="80%">
<figcaption><b>Fig 4</b> Plastic exitance spectra based on ATR spectra (Fig. 2) and intrinsic emissivity, $\varepsilon_0 = 0.9$. The exitance has then been used to estimate scanning FPI interferograms using Eq. \eqref{eq:estimate_interferogram}.</figcaption></center>

### Using Vanta black as reference sample

In an attempt to remove the contribution of the high emissivity plastic which hides the spectral features, a reference sample is brought in. This is a piece of aluminum which has been coated in _S-IR Vantablack_ by Surrey NanoSystems. This coating consists of carbon nanotubes which trap light, making it very absorptive with emissivities above 0.99 for wavelengths $>3$ µm. The Vantablack sample is placed beside the other plastics on the aluminum block, and its interferogram extracted (Fig. 5). In this case the relative intensities are important and the preprocessing is still a spatial median filter and Savitzky–Golay smoothing as described earlier, but instead of performing SNV, the first image in the data cube is subtracted from every band in the cube. This makes the entire first layer equal to 0, and the intensity of all subsequent bands is measured relative to this. Ideally, the Vantablack should be the highest intensity part of the data cube, but the cavities in the aluminum block enhance the thermal emission, making them comparatively brighter.

<center><img src="/HSTI/images/preliminary_plastics_and_vanta_black/vanta_black_color.svg" alt="Vantablack" width="100%" height="100%">
<figcaption><b>Fig 5</b> Image taken at 4.3 µm mirror separation of Vantablack sample placed on a 70 °C aluminum block. The black square in (a) indicate the $50\times 50$ pixel area from which the graph in (b) has been sampled. The cube has been preprocessed using spatial median filter, and Savitzky–Golay filter as well as subtracting the first band.</figcaption></center>


The extracted Vantablack interferogram, $\mathbf{i}_\textrm{Vantablack}$ (Fig. 5b), is used as the 'reference interferogram', and all other parts of the data cube must be compared to this. This is done by subtracting the interferogram from every pixel in the data cube from the Vantablack reference. 

\begin{align} \label{eq:vantablack_subtraction}
    \mathbf{i}_{c}(x,y) = \mathbf{i}_V - \mathbf{i}(x,y) 
\end{align} 

$\mathbf{i}_{c}(x,y)$ represents the corrected interferogram at position $(x,y)$ while $\mathbf{i}{(x,y)}$ is the interferogram at position $(x,y)$ before the correction. Doing this for every pixel in the data cube transforms the image from Fig.5a into Fig. 6a. A smaller section of the image has been cropped out to isolate the samples of PS, PP, PE, and POM (Fig. 6b).  


<center><img src="/HSTI/images/preliminary_plastics_and_vanta_black/vanta_black_cube_subtracted_color.svg" alt="Vantablack reference" width="100%" height="100%">
<figcaption><b>Fig 6</b> (a): Same slice of the data cube as in Fig. 5a but after correction using the Vantablack sample in conjunction with Eq. \ref{eq:vantablack_subtraction}. (b): The image is cropped according to the light grey square in (a) to isolate the plastic samples.</figcaption></center>

The average interferogram of each plastic is extracted in a similar manner to what is shown in Fig. 3, but now only a $10\times 10$ pixel area is used for averaging. In order to compare the simulated interferograms based on ATR with the extracted interferograms from the data cube, SNV is performed on each interferogram (_only_ the extracted interferograms - not the entire data cube). The results show varying agreement between simulations and measurements (Fig. 7). Listed in terms of increasing mean squared error (MSE) between simulation and measurement, the best fit is for POM, PP, PS and PE. In all cases it appears that the measurements do not capture the features around 7 - 8 µm mirror separation, which is otherwise indicated by the ATR based simulations. It is uncertain if this is caused by temperature differences between the samples or the if Vantablack sample has some unknown features in this range since its absorption spectrum is not known at the time of writing. Other reasons for disagreements could also be high emissivity of the plastic samples. As hypothesized earlier, the absorption features might be difficult to extract as they can be buried in a large emission background signal.     

<center><img src="/HSTI/images/preliminary_plastics_and_vanta_black/compare_to_sims_color.svg" alt="Comparison between measurements and simulations" width="100%" height="100%">
<figcaption><b>Fig 7</b> Comparisons between simulated interferograms based on ATR absorption measurements and Vantablack corrected interferograms from the data cube shown in Fig. 6. (a): Polypropalene, (b): Polyethylene, (c): Polyoxymethylene, (d): Polystyrene.</figcaption></center>
