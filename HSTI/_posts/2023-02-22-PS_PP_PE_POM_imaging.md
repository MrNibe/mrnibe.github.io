---
layout: single
classes: wide
title:  "Imaging plastics - Preliminary study of PP, PE, PS and POM using hyperspectral thermal imaging"
date:   2023-02-23
---

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

The principal components (PCs) of Fig. 5 are calculated and presented in Fig. 6. Notice that the vast majority of the variance is explained by the first component. This is because the data has not been scaled

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/pca.png" alt="PCA of subtracted spectra">
    <figcaption>Fig. 6: PCA of data cube from Fig. 5. The percentages indicate how much of the total variance is explained by each component.</figcaption>
</figure>

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/pca_loadings.png" alt="PCA loadings">
    <figcaption>Fig. 7: </figcaption>
</figure>

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/compensated_plastic_spectra.png" alt="Compensated spectra">
    <figcaption>Fig. 8: </figcaption>
</figure>

<figure>
    <img src="/HSTI/images/preliminary_plastics_and_vanta_black/compare_to_sims.png" alt="Comparison between measured and simulated interferograms">
    <figcaption>Fig. 9: </figcaption>
</figure>