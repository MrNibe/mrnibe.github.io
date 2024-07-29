---
layout: single
classes: wide
title:  "Heated carbon composite samples"
date:   2024-07-24
---

The heating characteristics of six different carbon composite samples have been investigated by time series thermography. As depicted in Fig. 1, the samples are suspended in front of the thermal camera (not hyperspectral), and heated by a heat gun for 30 s after which the cooling is observed for 2 minutes. Initial experiments using a hot plate to heat one end of the samples were not suitable to detect the defect. This might be caused by the samples dissipate most of the heat energy before it can travel from the heated end to the defect. 

<center><img src="/HSTI/images/carbon_samples/IMG_1527.jpeg" alt="Signal reconstructions" width="70%" height="70%">
<figcaption><b>Fig 1:</b> Spectral reconstructions of incident spectrum based on NMF gradient decent. </figcaption></center>


The 'temperature' series for each of the samples is indicated in Fig. 2, which illustrate the intensity of the same part of the sample as a function of time. As seen in Fig. 2a, the sampling is not particularly uniform, which may be caused by the camera doing other things simultaneously - especially calculating new NUC parameters seems to be taxing on the CPU. The intend was to capture images every second, but as shown, this was not always possible. Here, the curves have been aligned such that the heating onsets at time 0 for all samples. To be able to compare the data cubes (time is now the 'spectral' axis), the data is interpolated, and the result is seen in Fig. 2b. 


<center><img src="/HSTI/images/carbon_samples/temperature_curves_interpolated.png" alt="Signal reconstructions" width="100%" height="100%">
<figcaption><b>Fig 2:</b> Spectral reconstructions of incident spectrum based on NMF gradient decent. </figcaption></center>

Videos of all samples can be observed in Fig. 3. 

<center>
<video autoplay loop muted playsinline width="100%" height="100%" controls>
  <source src="/HSTI/images/carbon_samples/Heated_carbon_samples.mp4" type="video/mp4">
</video>
<figcaption><b>Fig 3:</b> Heating sequence for all carbon samples. </figcaption></center>


