---
layout: single
classes: wide
title:  "Can a camera really be TOO fast?!"
date:   2023-03-30
---

A recent update to the thermal camera has drastically improved the speed at which it captures a thermal image. However, it might be a little too fast for it to keep up with itself. Fig. 1 illustrates the spectra of an Acktar Fractal black coated sample as well as a piece of polyoxymethylene (POM). Both Fig. 1a and 1c show the scene recorded at approximately the same mirror separation, but 1a is sampled using the 'high mirror speed', while 1c is captured with the 'slow mirror speed'. The only preprocessing performed on both images is subtraction of the first band from all layers of the cube. The two do not look that dissimilar from each other, but looking at the extracted spectra in Fig. 1b and 1d, we notice a difference. The sampling points in 1b (the fast mirror speed) look more irregularly spaced compared to 1d. 

<center><img src="/HSTI/images/fast_camera/fast_slow_comparison.svg" alt="Comparison between fast ans slow sampling rates" width="80%" height="80%">
<figcaption><b>Fig 1</b> Comparison between hyperspectral data cubes captured with a fast mirror speed (a) and (b), as well as the usual, slow mirror speed (c) and (d). The samples in the image are Akctar fractal black coated stainless steel and pieces of POM heated to 60 °C. The black boxes in (b) and (d) indicate where of the laser diode interferograms in Fig. 3 are sampled.</figcaption></center>

Looking further into how the data is captured, we turn our attention to the interferograms, which reveal how the mirrors have moved during the sweep. The camera sweeps its mirrors when capturing a hyperspectral thermal image. To keep track of how far the mirrors have moved (and to ensure they move in parallel with respect to the starting position), it uses some red laser diodes tuned to 655 nm. The light reflected inside the mirror cavity, and the interferogram is measured using a photodiode. As the mirrors move apart, the reflected light fluctuates in intensity as the light undergoes constructive and destructive interference depending on the mirror separation. 

Fig. 2. illustrates the interferogram of a single laser diode during the fast sweep (2a) and the slow sweep (2b). Once again in the fast speed, there appear to be an irregular sampling distance. This is also present in the slow sweep, but much less pronounced. 

<center><img src="/HSTI/images/fast_camera/laser_diode_fast_slow.svg" alt="fast and slow interferograms" width="80%" height="80%">
<figcaption><b>Fig 2</b> A single laser diode interferogram taken at a fast mirror speed (a) and a slow speed (b). </figcaption></center>

To investigate this further, we will look at the euclidean distance between the sample points in the two plots. This is done using the formula:

\begin{align} \label{eq:SNV}
    d_i = \sqrt{(x_{i+1} - x_i)^2 + (y_{i+1} - y_i)^2},
\end{align}

where $d_i$ is the distance between the $i$th and $(i+1)$th sampling points, and $x$ refer to the x-coordinate and $y$ the y-coordinate. The result of this is illustrated in Fig. 3 for the fast sampling in 3a and the slow in 3b. Only a smaller interval is shown here to more easily see the differences between the plots. Also, grey lines are drawn for every 10th step - which is also where the images are captured during the sweep. It is clear that the distance between sampling points are affected heavily by the image capturing event. Even for the slow speed, a small increase in distance is noticeable, but not nearly as much as for the fast sampling rate. 

<center><img src="/HSTI/images/fast_camera/laser_diode_euclidean.svg" alt="Euclidean distance between sample points" width="80%" height="80%">
<figcaption><b>Fig 3</b> The euclidean distance between the sample points in Fig. 2. (a) is for the fast mirror speed, while (b) is for the slow mirror speed. The grey lines indicates the positions at which the camera captures the images for the cube. The interval which is depicted here corresponds to the black rectangle indicated in Fig. 1b and 1d.</figcaption></center>
