---
layout: single
classes: wide
title:  "Black body exitance spectrum both in terms of wavelengths and wavenumbers"
date:   2023-03-16
---

A _black body_ is an idealized object, which absorbs all incident radiation. As described by Kirchhoff's radiation law, a black body also emits radiation at all wavelengths following Planck's law of thermal radiation. At any given temperature and wavelength, the black body emits the highest amount of radiation possibly by any object. The spectral exitance is an expression for the total power emitted into the hemisphere per area emitter: here described in terms of wavelengths

\begin{align} \label{eq:BB_exitance_lam}
    M_{BB, \lambda}(T) = \frac{2\pi hc^2}{\lambda^5} \frac{1}{\exp{\frac{hc}{k_B \lambda T}} - 1}, 
\end{align}

... and in terms of wavenumbers:

\begin{align} \label{eq:BB_exitance_nu}
    M_{BB, \tilde{\nu}}(T) = 2\pi hc^2\tilde{\nu}^3 \frac{1}{\exp{\frac{hc\tilde{\nu}}{k_B T}} - 1}, 
\end{align}

The two distributions are presented in Fig. 1. 

<center><img src="/HSTI/images/black_body_exitance/black_body_radiation.svg" alt="Experimental setup" width="100%" height="100%">
<figcaption><b>Fig 1</b> Spectral radiance in terms of both wavelengths and wavenumbers based on Eq. (1) and Eq. (2) respectively. </figcaption></center>

The position of the maxima is described by Wien's displacement law:

\begin{align} \label{eq:Wien_lam}
    \lambda_{max} T = 2897.8 \cdot \mu m \cdot K, 
\end{align} 

\begin{align} \label{eq:Wien_k}
     \frac{\tilde{\nu}_{max}}{T}= 1.960856 \cdot cm^{-1}/K, 
\end{align} 


It should be noted that the two expressions for spectral radiance have different units. This also means that their maxima occur at different parts of the spectrum. For example, at a temperature of 100 °C, the location of the maximum is found to 7.766 µm using Eq. (3). Using Eq. (4), the position of the maximum is calculated to 731.69 cm<sup>-1</sup>, which corresponds to an equivalent wavelength of 13.667 µm. Still, if the curves are integrated over the same interval of the spectrum, the total radiant power is still the same for the two representations. However, integrating the spectral exitance curves is not as straight forward, as no analytical solution exists. However, a solution can be approximated as described in the coming sections.  

## Total power within given band
**_The following derivation is based on the work of Duncan Lawson in <https://www.ijee.ie/articles/Vol20-6/IJEE1557.pdf>_**

The total power emitted throughout all wavelengths (total exitance) can be described via

\begin{align} \label{eq:stefan_boltzmann_law}
    \int_{0}^{\infty} M_{BB, \lambda}(T) d\lambda = \int_{0}^{\infty} M_{BB, \tilde{\nu}}(T) d\tilde{\nu} = \sigma T^4, 
\end{align}

where $\sigma = \frac{2\pi ^5 k_B^4}{15c^2h^3} = 5.67037\times 10^{-8}W\cdot m^{-2}\cdot K^{-4}$ is the Stefan-Boltzmann constant.

We want to find an expression for the energy contained within a given spectral band. This must be done for both the wavelength representation and wavenumber representation individually. Firstly the wavelength representation is considered.

### Wavelength representation

To find the power contained within a given spectral band, a _Black body radiation function_, $F$, is defined:

\begin{align} \label{eq:black_body_radiation_func}
    F_{\lambda_1}(T) = \frac{\int_{0}^{\lambda_1} M_{BB, \lambda}(T) d\lambda}{\int_{0}^{\infty} M_{BB, \lambda}(T) d\lambda} = \frac{\int_{0}^{\lambda_1} M_{BB, \lambda}(T) d\lambda}{\sigma T^4} 
\end{align}

This function describes the fraction of the exitance is contained between $\lambda = 0$ and $\lambda = \lambda_1$. To find the exitance between two wavelengths, $\lambda_1$ and $\lambda_2$, the following expression is used

\begin{align} \label{eq:band_fraction}
    F_{\lambda_1\rightarrow \lambda_2}(T) = F_{\lambda_2}(T) - F_{\lambda_1}(T) 
\end{align}

To solve the otherwise "unsolvable" black body intergral from Eq. (6), it is noted from Wien's displacement law that $\lambda T$ is constant for all wavelengths and temperatures. It is therefore only necessary to integrate with respect to $(\lambda T)$ instead of just $\lambda$. This allows us to rewrite Eq. (6):
\begin{align} \label{eq:black_body_radiation_func_long}
    F_{\lambda_1}(T) = \frac{1}{\sigma T^4} \int_{0}^{\lambda_1} \frac{2\pi hc^2}{\lambda^5} \frac{1}{\exp{\frac{hc}{k_B \lambda T}} - 1} d\lambda = \frac{1}{\sigma} \int_{0}^{\lambda_1} \frac{2\pi hc^2}{(\lambda T)^5} \frac{1}{\exp{\frac{hc}{k_B (\lambda T)}} - 1} T d\lambda 
\end{align}

\begin{align} \label{eq:black_body_radiation_func_lamT}
    F_{\lambda_1}(T) = \frac{1}{\sigma} \int_{0}^{\lambda_1 T} \frac{2\pi hc^2}{(\lambda T)^5} \frac{1}{\exp{\frac{hc}{k_B (\lambda T)}} - 1} d(\lambda T) = \frac{1}{\sigma} \int_{0}^{\lambda_1 T} \frac{2\pi hc^2}{x^5} \frac{1}{\exp{\frac{hc}{k_B x}} - 1} dx 
\end{align}


\begin{align} \label{eq:constants}
    C_1 =  2\pi hc^2 \qquad C_2 = \frac{hc}{k_B}
\end{align}

Change of variable with $z C_2/x$ 

\begin{align} \label{eq:black_body_radiation_func_z}
    F_{\lambda_1}(T) = \frac{C_1}{\sigma C_2^5} \int_{\infty}^{C_2 / (\lambda_1 T)} \frac{z^5}{\exp{(z)} - 1} \frac{-C_2}{z^2} dz = \frac{C_1}{\sigma C_2^4} \int_{C_2 / (\lambda_1 T)}^{\infty} \frac{z^3\exp{(-z)}}{1 - \exp{(-z)}} dz  
\end{align}

Since $z$ is always positive and less than 1, $(1-\exp{(-z)})^{-1}$ can be rewritten as an infinite sum using:

\begin{align} \label{eq:inf_sum}
   (1-\gamma)^{-1} = \sum_{n = 0}^{\infty} \gamma^n, \qquad  |\gamma| < 1   
\end{align}

\begin{align} \label{eq:black_body_radiation_func_inf_sum}
    F_{\lambda_1}(T) = \frac{C_1}{\sigma C_2^4} \int_{C_2 / (\lambda_1 T)}^{\infty} z^3\exp{(-z)}(1 + \exp{(-z)} + \exp{(-2z)} + \dots) dz  
\end{align}

\begin{align} \label{eq:black_body_radiation_func_inf_sum2}
    F_{\lambda_1}(T) = \frac{C_1}{\sigma C_2^4} \sum_{n = 1}^{\infty} \int_{C_2 / (\lambda_1 T)}^{\infty} z^3\exp{(-nz)} dz  
\end{align}

Performing repeated integration by parts on Eq. (14) yields the final expression for $F$

\begin{align} \label{eq:F_final}
    F_{\lambda_1}(T) = \frac{C_1}{\sigma C_2^4} \sum_{n = 1}^{\infty} \frac{\exp{(-nz)}}{n} \left (z^3 + \frac{3z^2}{n} + \frac{6z}{n^2} + \frac{6}{n^3} \right )  
\end{align}
with $z = C_2/\lambda_1 T$, $C_1 =  2\pi hc^2$ and $C_2 = \frac{hc}{k_B}$. Even just doing 5 iterations is enough to get a solution with an error in the order of $\times 10^{-10}$ and is much faster than doing numerical integration of the curve. 

## Wavenumber representation
Much of the same argumentation can be used when deriving the expression for the wavenumber representation starting from Eq. (2). Instead of $\lambda T$ being constant, now the constant part is $\tilde{\nu}/T$. This only changes some of the integration limits slightly, resulting in a final expression for $F_{\tilde{\nu}1}(T)$: 
\begin{align} \label{eq:F_final_k}
    F_{\tilde{\nu}1}(T) = \frac{C_1}{\sigma C_2^4} \sum_{n = 1}^{\infty} - \frac{\exp{(-nz)}}{n} \left (z^3 + \frac{3z^2}{n} + \frac{6z}{n^2} + \frac{6}{n^3} \right ) +  \frac{6}{n^4}
\end{align}
 with $z = \tilde{\nu}_1C_2/T$, $C_1 =  2\pi hc^2$ and $C_2 = \frac{hc}{k_B}$.


