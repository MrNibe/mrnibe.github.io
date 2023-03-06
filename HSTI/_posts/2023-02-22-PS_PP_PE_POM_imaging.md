---
layout: single
classes: wide
title:  "Imaging plastics - Preliminary study of PP, PE, PS and POM using hyperspectral thermal imaging"
date:   2023-02-23
---

In this experiment, a hyperspectral thermal camera (HSTC) is used to measure different kinds of plastics: Polypropalene (PP, container 1 from *the wall of plastic*, Polyethylene (PE, container 2), Polystyrene (PS, container 165) and Polyoxymethylene (POM, container 63). The aim is to investigate whether it is possible to extract information about their emission spectra using the HSTC and compare to absorption measurements using attenuated total reflection (ATR).  

## Experimental setup
The HSTC is pointed vertically down onto an aluminum block placed on a hotplate set to 70 °C (Fig. 1). The distance between the front of the camera and the surface of the aluminum block is ≈ 40 cm. Once the block has reached its predetermined temperature, different plastic samples are placed on top of it and left to reach temperature equilibrium after ≈ 10. The sample surface temperature is assumed to be the same as the internal temperature of the aluminum block for the purposes of further data analysis, although the surface temperature in reality differs from that of the block.

<center><img src="/HSTI/images/preliminary_plastics_and_vanta_black/experimental_setup.svg" alt="Experimental setup" width="50%" height="50%">
<figcaption><b>Fig 1</b> Schematic drawing of experimental setup with the hyperspectral thermal camera pointing at plastic samples laying on top of an aluminum block heated to 70 °C. A Fabry-Pérot Interferometer (FPI) mounted in the lens provides the hyperspectral capabilities to the otherwise regular thermal camera. (Not to scale)</figcaption></center>



## A note on data processing

\begin{align} \label{eq:estimate_interferogram}
    \mathbf{i} = \mathbf{\Lambda}\mathbf{s},
\end{align}

Several different techniques are used when looking at the hyperspectral data cubes. One of them is standard normal variate (SNV), which is applied to the spectral axis to eliminate intensity differences and emphasize differences in spectral features:    

\begin{align} \label{eq:SNV}
    \mathrm{SNV}(\mathbf{i}) = \frac{\mathbf{i} - \bar{\mathbf{i}}}{\mathrm{STD}(\mathbf{i})}
\end{align}

where $\bar{\mathbf{i}}$ denote the average of $\mathbf{i}$ and $\mathrm{STD}(\mathbf{i})$ is the standard deviation.

A spatial median filter with a kernel size of 3 pixels is usually applied to each image of the data cube. Furthermore, the spectral axis is often smoothed using a Savitzky–Golay filter with a length of 11 samples, $2^\textrm{nd}$ order polynomial fit and $0^\textrm{th}$ derivative. 



## Results and discussion
The HSTC is sensitive to radiation of wavelengths between 8-16 µm (625-1250 cm<sup>-1</sup>). The absorption spectra of the plastics are measured using ATR. From Kirchhoff's radiation law it follows that the emissivity and the absorption of a sample in thermal equilibrium are equal. The ATR measurements are therefore used as the incident spectrum in Eq. \eqref{eq:estimate_interferogram} to calculate the estimated interferograms (Fig. XX).

Only PP and PE is investigated in the first HSTI and their interferograms are averaged across a $25\times25$ pixel region (Fig. XX). The interferograms from the two plastics are comparable and do not show the expected spectral features as predicted in Fig. XX}. It is hypothesized that this is caused by the plastic having a high emissivity intrinsically. The radiation emitted by a black body is described by its exitance:

\begin{align} \label{eq:BB_exitance_nu}
    L_{BB}(\tilde{\nu}, T) = 2hc^2\tilde{\nu}^3 \frac{1}{\exp{\frac{hc\tilde{\nu}}{k_B T}} - 1}, 
\end{align}

where $h$ is Planck's constant, $c$ the speed of light, and $k_B$ the Boltzmann constant. 

The emissivity is defined as the ratio between the exitance of an object and that of a perfect black body emitter (Eq. \eqref{eq:BB_exitance_nu}):

\begin{equation}\label{eq:emissivity}
    \varepsilon  =  \frac{L}{L_{BB}} = \alpha 
\end{equation}

Here, $\varepsilon$ is the enissivity, $L$ is the exitance of the emitter. From Kirchhoff's radiation law it follows that the emissivity is equal to the absorption, $\alpha$.


If the intrinsic emissivity (and hereby also the absorption) of the plastic samples is $\varepsilon_0 = 0.9$, then the total, wavenumber dependent emissivity becomes:

\begin{align} \label{eq:total_emissivity}
    \varepsilon_\textrm{tot}(\tilde{\nu}) = \varepsilon_0 + \varepsilon_\textrm{ATR}(\tilde{\nu}),
\end{align}

with $\varepsilon_\textrm{ATR}(\tilde{\nu}) = \alpha_\textrm{ATR}(\tilde{\nu}) $ being the emissivity/absorption measured using ATR. The emission spectrum of the plastics then becomes

\begin{align} \label{eq:ATR_exitance}
L(\tilde{\nu}, T) = (\varepsilon_0 +  \varepsilon_\textrm{ATR}(\tilde{\nu}))L_{BB}(\tilde{\nu},T)
\end{align} 

The adjusted emission spectra calculated based on Eq. \eqref{eq:ATR_exitance} are presented in Fig. XX along with simulated interferograms based on the new emission spectra. 
 




## Original article











The Hyperspectral Thermal Camera (HSTC) is sensitive to radiation of wavelengths between 8−16 μm corresponding to 625-1250 cm<sup>-1</sup>. Several types of plastics have absorption lines in this part of the electromagnetic spectrum. The types of plastic investigated in this post are Polypropalene (PP), Polyethylene (PE), Polystyrene (PS) and Polyoxymethylene (POM). Their absorption spectra have been measured with Attenuated Total Reflectance (ATR) spectroscopy and the theoretical Scanning Fabry-Pérot (SFPI) interferograms have been calculated. The results are presented below:

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/FTIR_ATR_+_interferograms.png" alt="Plastic ATR spectra">
    <figcaption>Fig. 1: ATR spectra with accompanying simulated SFPI interferograms.</figcaption>
</figure>

It appears that there are plenty of spectral features, which should be detectable by the HSTC. However, this is not immediately the case, when taking a image of two plastics: PP and PE. Fig. 2 illustrates an image from the hyperspectral data cube of the two plastics along with their mean spectra as indicated by the colored squares. Standard Normal Variate (SNV) has been applied to the data before sampling the two plastic spectra. This is done to minimize intensity difference and enhance spectral differences between the two. However, they appear to be very similar and almost impossible to tell apart.   

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/similar_plastics_PE_PP.png" alt="PP and PE interferograms">
    <figcaption>Fig. 2: Image from hyperspectral data cube of PP and PE placed on a 70°C aluminum block. SNV has been applied to the data to remove intensity differences. </figcaption>
</figure>

The data cube has been pre-processed using the following techniques:
```python
cube = hsti.median_filter_cube(cube, 3)
cube = savgol_filter(cube, window_length = 11, polyorder = 2, deriv=0, axis= 2)
cube = hsti.autoscale(cube)
cube = hsti.debend(cube, mirror_seps)
```
## Why doesn't this work when the ATR spectra suggest it should be possible?

One explanation could be that the plastic has an intrinsically high emissivity. It is therefore suspected that the spectral features might drown in the black body radiation curve. 

$$\varepsilon = \alpha =  \frac{L}{L_{BB}}, \qquad \alpha = \alpha_{measurement} + \alpha_{offset}, \qquad \varepsilon = \varepsilon_{measurement} + \varepsilon_{offset}$$

The absoption measurements are all relative to themselves meaning that a large offset might be present. If e.i. the absorption in inherently high, then changes will be small in comparison and harder to detect. The effect is now investigated by implementing this offset resulting in 'new' spectra calculated as:

$$L = (\alpha_{measurement} + \alpha_{offset})L_{BB}$$

with

$$L_{BB} = \frac{2hc^2}{\lambda^5}\frac{1}{\textrm{exp}\left[\frac{hc}{\lambda k_B T -1} \right]}$$

If the base emissivity of the plastic is assumed to be $$\varepsilon_{offset} \approx 0.9$$, then the emission spectra and respective interferograms are presented in Fig. 3. Now the spectral differences are much less pronounced in the interferograms.  

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/FTIR_ATR_+_interferograms_BB.png" alt="Plastic ATR spectra with grey-body radiation">
    <figcaption>Fig. 3: ATR spectra with accompanying simulated SFPI interferograms, now with added grey-body curve with emissivity of 0.9.</figcaption>
</figure>

## Correcting data using vanta black as approximate black body.
In order to remove the high emissivity 'background' of the plastic samples, an aluminum sample covered in vanta black is used as a reference. Fig. 4 illustrates this sample placed on top of a 70°C aluminum block with the extracted interferogram presented on the right. The preprocessing is the same as what is presented in Fig. 2. Just below the vanta-black are four different types of plastic. From the left: Polystyrene (PS), Polypropalene (PP), Polyethylene (PE), and Polyoxymethylene (POM). 

**!!Notice that the preprocessing now has changed!!** 
Instead of applying SNV, the first band is set equal to 0 as described by the following code block

```python
cube = hsti.median_filter_cube(cube, 3)
cube = savgol_filter(cube, window_length = 11, polyorder = 2, deriv=0, axis= 2)
cube = hsti.subtract_band(cube, 0)
cube = hsti.debend(cube, mirror_seps_PS)
```

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/vanta_black.png" alt="Hyperspectral thermal image of vanta black and plastic samples">
    <figcaption>Fig. 4: Hyperspectral thermal image of vanta black sample along with some plastic samples. From the left: PS, PP, PE and POM.</figcaption>
</figure>

Now that the vanta black spectrum has been extracted, it is used as the reference and we want to look at the differences between the vanta black spectrum and the rest of the cube:

$$\mathbf{Cube}_{new} = \mathbf{s}_{vanta\_black} - \mathbf{Cube}$$ 

Which results in the cube from where the image in Fig. 5 has been extracted.

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/vanta_black_cube_subtracted.png" alt="Differences between vanta black and the rest of the cube">
    <figcaption>Fig. 5: Same data as in Fig. 4, but now illustrating the differences between the vanta black spectrum and the rest of the cube. The cutout section illustrates the crop performed on the image which will be used for the remainder of this post.</figcaption>
</figure>

## Principal component analysis (PCA)

The principal components (PCs) of Fig. 5 are calculated and presented in Fig. 6. Notice that the vast majority of the variance is explained by the first component. This is because the data has not been scaled. This also affects the loadings, which are presented in Fig. 7, where the first component has the same shape as the interferogram from the vanta black sample. This is off cause present in all pixels to some extend since it represents the black body radiation. The 2nd component might be very reminiscent of the POM spectrum since it is the only part of the image which 'light up' in this component. 

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/pca.png" alt="PCA of subtracted spectra">
    <figcaption>Fig. 6: PCA of data cube from Fig. 5. The percentages indicate how much of the total variance is explained by each component.</figcaption>
</figure>

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/pca_loadings.png" alt="PCA loadings">
    <figcaption>Fig. 7: PC loadings corresponding the the PCA scores presented in Fig. 6. </figcaption>
</figure>

## Compare individual plastic interferograms to simulations

The plastic interferograms are extracted and presented in Fig. 8. 

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/compensated_plastic_spectra.png" alt="Compensated spectra">
    <figcaption>Fig. 8: Interferogram of each plastic type. Each interferogram represents the difference between the plastic interferogram and the vanta black sample. </figcaption>
</figure>

Now, the extracted interferograms are compared to the simulated interferograms as presented in Fig. 1. SNV is applied to both the measured and simulated interferograms (not the entire cube - only the graph itself). Very good agreement between simulated and measured data is observed for the POM sample. PP also shows good agreement, but PE and PS less so.  

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/compare_to_sims.png" alt="Comparison between measured and simulated interferograms">
    <figcaption>Fig. 9: Comparison between measured and simulated interferograms. </figcaption>
</figure>