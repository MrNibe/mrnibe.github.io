---
layout: single
classes: wide
title:  "What happens if you shine a laser at the camera... (－‸ლ)"
date:   2023-08-01
---

We had received some new mirrors from a Chinese manufacturer, but it turned out that they were not good enough for use in the Fabry-Pérot. Even though they had a transmission of ≈ 15% which was as requested, the reflectance was only ≈ 65% indicating huge absorption losses. So before sending them back, I figured I would try to use them as neutral density filters and get a measurement of a 10.6 µm laser to get a feel for how the spectral resolution of the Fabry-Pérot actually is. I found a small 0.4 W [L3 laser](https://www.accesslaser.com/product/l3-lasers/) from Laser Access Company. I set the power so low that the [indicator card](https://www.thorlabs.com/thorproduct.cfm?partnumber=VRC6S) would barely register the radiation (sensitivity of 0.05 mW/mm²). I then put one of the Chinese mirrors in front of the laser and then the hyperspectral thermal camera behind that. Even though the the light intensity should be reduced by at least 85% and by however big the absorption losses are in the Fabry-Pérot, the sensor still ended up overexposing... badly. Figure 1 illustrate the bloom effect the pixels experience in the spot, where the laser hit even after 5 minutes of relaxation time.    

<center><img src="/HSTI/images/laserspot.png" alt="Bloom spot on bolometer after 5 minutes" width="80%" height="80%">
<figcaption><b>Fig 1</b> Spot of pixels exhibiting bloom effect after being exposed to 10.6 µm laser light. </figcaption></center>

After two hours of relaxation time, the issue still persists as evident from figure 2... 

<center><img src="/HSTI/images/laserspot2hr.png" alt="Bloom spot on bolometer after 2 hours" width="80%" height="80%">
<figcaption><b>Fig 2</b> The same spot is still evident even after 2 hours. The darker image is due to increased sensor temperature. </figcaption></center>