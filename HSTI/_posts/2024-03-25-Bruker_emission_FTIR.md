---
layout: single
classes: wide
title:  "Bruker Emission FTIR measurements"
date:   2024-03-25
---

__Short description of results from emission measurements__

Bruker agreed to perform some emission FTIR measurement on various samples. One of the goals is to see if this can help explain why it has been so difficult to differentiate between the plastic samples and why POM is so spectrally "outstanding". 

The emissivity of the samples is estimated based on a reference black body. In this case, Bruker opted for candle soot as this should have a rather flat spectral emissivity. Fig. 1 show the comparisons between the candle soot reference measurement and a theoretical black body curve. The larger deviations are probably due to the instrument instrument. Some of the typical absorption lines from water and $\textrm{CO}_2$ are visible (albeit only small contributions). The larger peaks I think is due to the response of the detector as it is also seen in many of the other samples depicted in Fig 2.    

<center><img src="/HSTI/images/Bruker_emission_FTIR/single_channel_candle_soot.png" alt="Single channel measurement of candle soot" width="100%" height="100%">
<figcaption><b>Fig 1:</b> Single channel measurement of 100 ºC candle soot compared to a theoretical black body.</figcaption></center>

In theory, as long as the reference is a "true" black body, the instrument characteristics should disappear when calculating the emissivity... But a perfect black body is too much to ask for in practice as many of the other sample actually turn out to have even higher emissivity than the reference sample (Fig. 2). Rust and Acktar Ultrablack would all seem to be good choices for new reference samples, but in these measurements, Bruker stuck with the candle soot (I guess because they know it spectrally).  

<center><img src="/HSTI/images/Bruker_emission_FTIR/single_channel_150.png" alt="Single channel comparisons" width="100%" height="100%">
<figcaption><b>Fig 2:</b> Single channel measurement of all samples at 150 ºC. </figcaption></center>

Single channel measurements of all samples can be found [here](/HSTI/images/Bruker_emission_FTIR/single_channel.png). The emissivity of most samples have been calculated based on the single channel measurements and can be found [here](/HSTI/images/Bruker_emission_FTIR/emissivities.png).

Fig. 3, 4, and 4 depict the theoretical emission spectra (emissivity multiplied with black body) and simulated interferograms. Here we notice why POM has been so easy to recognize compared to the other plastics. It has much larger variations in its emission spectrum, and as it has previously been hypothesized ([here]({% link HSTI/_posts/2023-02-22-PS_PP_PE_POM_imaging.md %}))_,_ the absorption/emission lines of the other plastics are obscured by the black body emission - the signal variations are simply too week comparatively. To enhance the differences between the plastics, Acktar Ultrablack was used as a reference sample in the measurements from Aarhus. For all plastics except POM, the interferograms more or less look like that of a black/grey body emitter which is also what was observed experimentally. The spectral features of POM also line up with what has previously been seen.    

<center><img src="/HSTI/images/Bruker_emission_FTIR/spectral_radiance_POM_HDPE.png" alt="Single channel comparisons" width="100%" height="100%">
<figcaption><b>Fig 3:</b> <b>a)</b> Emissivities of HDPE and POM multiplied with a theoretical black body at 60 ºC. <b>b)</b> Simulated interferograms of the two spectra from <b>a)</b>. </figcaption></center>

<center><img src="/HSTI/images/Bruker_emission_FTIR/spectral_radiance_PET_PP.png" alt="Single channel comparisons" width="100%" height="100%">
<figcaption><b>Fig 4:</b> <b>a)</b> Emissivities of PET and PP multiplied with a theoretical black body at 60 ºC. <b>b)</b> Simulated interferograms of the two spectra from <b>a)</b>. </figcaption></center>

<center><img src="/HSTI/images/Bruker_emission_FTIR/spectral_radiance_PC_PEEK.png" alt="Single channel comparisons" width="100%" height="100%">
<figcaption><b>Fig 5:</b> <b>a)</b> Emissivities of Polycarbonate and PEEK multiplied with a theoretical black body at 60 ºC. <b>b)</b> Simulated interferograms of the two spectra from <b>a)</b>. </figcaption></center>


If we compare the ATR measurements from Aarhus (Fig. 6) with the emission measurements, we also see that ATR absorption cannot replace the emissivity measurements. They appear to not be capturing the same thing. However, I find it difficult to evaluate how much the spectral profile of the candle soot influences the emissivity measurements. If it is spectrally flat, then it is only an offset in the emissivities, but since it is a reference, it can add some features of its own.  

<center><img src="/HSTI/images/Bruker_emission_FTIR/atr_comparison.png" alt="ATR comparisons" width="100%" height="100%">
<figcaption><b>Fig 6:</b> <b>a)</b> ATR measurements of the different plastics types used for the plastic article from Aarhus <b>b)</b> FTIR emissivity measurements of the same plastics as in <b>a)</b>. </figcaption></center>