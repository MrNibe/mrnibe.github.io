---
layout: single
classes: wide
title:  "How to combine interferograms of different gasses... Theoretically at least"
date:   2024-01-18
---

What happens if we use the hyperspectral LWIR camera to measure a mixture of gasses? Let's say that we know the interferograms of the gasses individually, but not their combination. We are only going to work with this theoretically, meaning that we a just going to use a system matrix calculated from TMM and only considering how different FTIR spectra will be recorded into interferograms. 

Since the FTIR spectra are measures of transmission, when we have multiple gasses combined, we need to multiply their transmission.

$$
\begin{align} \label{eq:ftir_cmb}
	\mathbf{t} = \mathbf{t}^{(1)}\odot\mathbf{t}^{(2)}\odot... = \prod_{i=1}^{K}\mathbf{t}^{(i)}, 
\end{align} 
$$  

where $K$ is the total number of different transmission spectra. The interferogram which is recorded by the camera is then the dot product of $\mathbf{t}$ and the system matrix $\mathbf{A}$. Let's constrain ourselves to only have a single gas in the first place.

$$
\begin{align} \label{eq:interferogram_single}
	\mathbf{s}^{(1)} = \mathbf{At} = \begin{bmatrix}
	a_{1,1}t_1^{(1)} &+& a_{1,2}t_2^{(1)} &+& \dots &+& a_{1,N}t_N^{(1)} \\
	a_{2,1}t_1^{(1)} &+& a_{2,2}t_2^{(1)} &+& \dots &+& a_{2,N}t_N^{(1)}\\
	\vdots & & \vdots & & \dots & & \vdots\\
	a_{M,1}t_1^{(1)} &+& a_{M,2}t_2^{(1)} &+& \dots &+& a_{M,N}t_N^{(1)}\\
	\end{bmatrix} 
\end{align} 
$$  

Let's now see what happens if we add two additional gasses. The combined interferogram then becomes

$$
\begin{align} \label{eq:interferogram_multi_spec}
	\mathbf{s_{cmb}} = \mathbf{At} = \begin{bmatrix}
	a_{1,1}t_1^{(1)}t_1^{(2)}t_1^{(3)} &+& a_{1,2}t_2^{(1)}t_2^{(2)}t_2^{(3)} &+& \dots &+& a_{1,N}t_N^{(1)}t_N^{(2)}t_N^{(3)} \\
	a_{2,1}t_1^{(1)}t_1^{(2)}t_1^{(3)} &+& a_{2,2}t_2^{(1)}t_2^{(2)}t_2^{(3)} &+& \dots &+& a_{2,N}t_N^{(1)}t_N^{(2)}t_N^{(3)}\\
	\vdots & & \vdots & & \dots & & \vdots\\
	a_{M,1}t_1^{(1)}t_1^{(2)}t_1^{(3)} &+& a_{M,2}t_2^{(1)}t_2^{(2)}t_2^{(3)} &+& \dots &+& a_{M,N}t_N^{(1)}t_N^{(2)}t_N^{(3)}\\
	\end{bmatrix} 
\end{align} 
$$  


There does not seem to be an easy method of combining individual interferograms, $\mathbf{s}^{(1)}$, $\mathbf{s}^{(2)}$, and $\mathbf{s}^{(3)}$ to arrive at $\mathbf{s_{cmb}}$. It is therefore not possible to mix two or more interferograms to estimate the result of combining gasses (at least not linearly). 

<!---

We see that if we know the interferograms for the individual gasses, we cannot quite add them nor multiply them together to arrive at the same solution as $\mathbf{s_{cmb}}$. However, we need not much adjustment to do so. Addition clearly does not work, but if we multiply two interferograms together $\mathbf{s}^{(1)}\odot\mathbf{s}^{(2)}$, then we realize that the contribution of the system matrix is included twice. To account for this we need to know the contribution of each row in $\mathbf{A}$ to the interferogram. We'll define

$$
\begin{align} \label{eq:interferogram_ones}
	\mathbf{z} = \mathbf{A}\mathbf{1},  
\end{align} 
$$  
where $\mathbf{1}$ is a column vector of 1's making each element of $\mathbf{z}$ the sum of the corresponding row of $\mathbf{A}$. This means that we can combine the interferograms of $K$ individual gasses like

$$
\begin{align} \label{eq:interferogram_cmb}
	\mathbf{s_{cmb}} = \frac{\prod_{i=1}^{K}\mathbf{s}^{(i)}}{\mathbf{z}^{K-1}}  
\end{align} 
$$  

Note that all operations of Eq. \ref{eq:interferogram_cmb} is done element-wise. 

-->

#### What happens if the concentration changes for a single gas?

We're going to go a bit further. What happens to the transmission if the concentration of the gas changes? From Lambert Beer's law, we know that the absorbance can be calculated as

$$
\begin{align} \label{eq:Lambert_beer}
	A = \alpha d c  
\end{align} 
$$

$\alpha$ is the extinction coefficient $[\textrm{L}\cdot\textrm{mol}^{-1}\cdot\textrm{cm}^{-1}]$, $d$ is the pathlenght, and $c$ is the concentration. In many of the experiments we have performed the gases have been in the same gas cell, and therefore the only parameter that changes for each gas is its concentration. The transmission can then be calculated as

$$
\begin{align} \label{eq:transmission}
	t = 10^{-A} \Rightarrow A = - \textrm{log}_{10}(t)
\end{align} 
$$

This off course can be expanded to be applicable for an entire spectrum. We therefore see, that a linear change in $c$ does not result in a linear change in $t$ and therefore not a linear change in $\mathbf{s}$ either. 

But can't we just try converting $\mathbf{s}$ to absorbance? That would look something like this: 

$$
\begin{align} \label{eq:interferogram_single_log10}
	\textrm{log}_{10}\left(\mathbf{s}^{(1)}\right) = \begin{bmatrix}
	\textrm{log}_{10}(a_{1,1}t_1^{(1)} &+& a_{1,2}t_2^{(1)} &+& \dots &+& a_{1,N}t_N^{(1)}) \\
	\textrm{log}_{10}(a_{2,1}t_1^{(1)} &+& a_{2,2}t_2^{(1)} &+& \dots &+& a_{2,N}t_N^{(1)})\\
	\vdots & & \vdots & & \dots & & \vdots\\
	\textrm{log}_{10}(a_{M,1}t_1^{(1)} &+& a_{M,2}t_2^{(1)} &+& \dots &+& a_{M,N}t_N^{(1)})\\
	\end{bmatrix} 
\end{align} 
$$  

The minus sign is omitted since we no longer work in absolute transmission and all values usually are above 1. This might help the interpretation later, but I have a hard time seeing whether this would even work, so let's try with some data. 

Let's convert the recorded FTIR transmission spectrum to absorption using Eq. \ref{eq:transmission} (Fig. 1)

<center><img src="/HSTI/images/Combining_interferograms_theoretically/butane_propane_abs.png" alt="butane_propane_abs" width="80%" height="80%">
<figcaption><b>Fig 1:</b> Absorption spectrum of a butane/propane mixture calculated from FTIR transmission measurements.  </figcaption></center>

This will serve as the 'reference concentration'. Since the absorption is linearly proportional to the concentration, it is possible to emulate other concentrations simply by scaling. After scaling the corresponding transmission spectra can then be calculated again based in Eq. \ref{eq:transmission}. This is done for a number of different concentrations and the results are presented in Fig. 2. The intensity at a single band (950 cm<sup>-1</sup>) is plotted as a function of the fractional concentrations. Notice here how the relationship is not linear - as expected.  

<center><img src="/HSTI/images/Combining_interferograms_theoretically/butane_propane_T.png" alt="butane/propane transmission" width="100%" height="100%">
<figcaption><b>Fig 2:</b> Transmission spectra of butane/propane mixture at different total concentrations. A fraction of 1 corresponds to the raw FTIR measurement.  </figcaption></center>


How do the different transmission spectra then map to the interferograms recorded by the camera? Fig 3. illustrates how the intensity at a single band (11.5 µm mirror separation) is changing as a function of concentration and it is concluded that it follows the same trend as for the FTIR transmission spectra. 


<center><img src="/HSTI/images/Combining_interferograms_theoretically/butane_propane_interferogram.png" alt="butane/propane interferogram" width="100%" height="100%">
<figcaption><b>Fig 3:</b> Interferograms based on the different transmission spectra presented in Fig. 2. </figcaption></center>


Finally, we see how the intensity changes with concentration as the interferograms are converted by taking their logarithm. We see now that the relationship between the intensity at a given band and the concentration now is linear (Fig. 4). 

<center><img src="/HSTI/images/Combining_interferograms_theoretically/butane_propane_log_interferogram.png" alt="butane/propane logarithmic interferogram" width="100%" height="100%">
<figcaption><b>Fig 3:</b> Logarithmic interferograms based on the different transmission spectra presented in Fig. 2. </figcaption></center>