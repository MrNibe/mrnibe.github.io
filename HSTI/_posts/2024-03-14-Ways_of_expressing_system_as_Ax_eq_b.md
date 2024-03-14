---
layout: single
classes: wide
title:  "Ways of expressing the system as Ax=b"
date:   2024-03-14
---

There are a couple of ways in which the system can be expressed as an $\mathbf{Ax}=\mathbf{b}$ problem to solve for the incident spectrum. Some of what is written here is also described [here]({% link HSTI/_posts/2024-01-16-Calculating_frequency_spectrum.md %}). 

Now, lets start by defining the flux incident on the sensor

$$
\begin{align} \label{eq:fpi_flux}
	\mathbf{\Phi_{in}} = \mathbf{T_{SFPI}}\circ[\mathbf{t_{samp}}\odot\mathbf{m_{BB}}(T_{BB}) + \mathbf{r_{samp}}\odot\mathbf{m_{env}}(T_{env})] + \mathbf{R_{SFPI}} \circ \mathbf{m_{sens}}(T_{sens}) 
\end{align} 
$$ 

Here, $\circ$ and $\odot$ refer to element wise and row wise multiplication respectively.  $\mathbf{T\_{SFPI}}$ and $\mathbf{R\_{SFPI}}$ are matrices describing the transmittance and reflectance of the SFPI respectively. Each row of the matrices is denoted to a specific mirror separation, with each column ascribed to a specific wavelength/wavenumber. $T_{BB}$, $T_{env}$, and $T_{sens}$ are the temperatures of the black body behind the sample and the temperature of the environment. $\mathbf{m}$ is a vector describing the black-body emission spectrum where the subscripts refer to the source of radiation (black-body, environment, and sensor). $\mathbf{t_{samp}}$ and $\mathbf{r_{samp}}$ are the transmission and reflectance spectrum of the sample respectively. The length of the vectors are the same as the number of columns in $\mathbf{T\_{SFPI}}$ and $\mathbf{R\_{SFPI}}$. 

An argument could be made for also including a flux term from the sensor housing, objective, lenses and SFPI itself as they also have a temperature, which is most often different from the sensor temperature. A good estimate would probably be to approximate this term by another $\mathbf{m_{env}}(T_{env})$ or ideally by knowing the temperature inside the lens itself, but it has initially been left out.

What we want to solve for in the end is 

$$
\begin{align} \label{eq:x}
	\mathbf{x} = \mathbf{t_{samp}}\odot\mathbf{m_{BB}}(T_{BB}) + \mathbf{r_{samp}}\odot\mathbf{m_{env}}(T_{env})
\end{align} 
$$ 

which is the spectrum of the light entering the camera. 

The signal recorded by the camera is however not directly proportional to the incident flux. Rather, the signal is proportional to the difference in flux between the sensor and the incident radiation. That is

$$
\begin{align} \label{eq:signal}
	\mathbf{i} \propto [\mathbf{\Phi_{in}} - \mathbf{m_{sens}}(T_{sens})]\mathbf{s}
\end{align} 
$$ 

Here, $\mathbf{i}$ represent the interferogram that is recorded while moving the mirrors of the SFPI. The length of $\mathbf{i}$ is the same as the number of rows in  $\mathbf{T\_{SFPI}}$. The difference in flux is expressed by $[\mathbf{\Phi_{in}} - \mathbf{m_{sens}}(T_{sens})]$. Again the subtraction is done row-wise. $\mathbf{s}$ is the spectral response of the sensor (same number of elements as columns in $\mathbf{T\_{SFPI}}$). 

## Ax=b Configuration 1

The first way to rearrange the terms into an $\mathbf{Ax}=\mathbf{b}$ problem is by embedding the sensor response directly in the transmission matrix. That way we can write the system matrix as

$$
\begin{align} \label{eq:sys_matrix_1}
	\mathbf{A} = \mathbf{T_{SFPI}}\circ\mathbf{s}
\end{align} 
$$ 

The other terms not part of $\mathbf{x}$ is moved to the left-hand side of Eq. (\ref{eq:signal}).

 $$
\begin{align} \label{eq:Ax=b1}
	\mathbf{i} - [(\mathbf{R_{SFPI}} - \mathbf{1}) \circ \mathbf{m_{sens}}(T_{sens})]\mathbf{s}  = \mathbf{Ax}
\end{align} 
$$ 

In this variation there are no negative terms in neither $\mathbf{A}$ nor $\mathbf{x}$ as it is moved to $\mathbf{b}$ instead. Note that $[(\mathbf{R_{SFPI}} - \mathbf{1}) \circ \mathbf{m_{sens}}(T_{sens})]\mathbf{s}$ is exclusively negative since $\mathbf{R_{SFPI}}$ cannot be greater than 1. This way $\mathbf{A}$, $\mathbf{x}$, and $\mathbf{b}$ are all exclusively nonnegative.


## Ax=b Configuration 2

Here, we are going to work with the same system matrix as before, namely $\mathbf{A} = \mathbf{T_{SFPI}}\circ\mathbf{s}$. Additionally, it is assumed that the SFPI is lossless meaning $\mathbf{R\_{SFPI}} = \mathbf{1} - \mathbf{T\_{SFPI}}$. Eq. (\ref{eq:fpi_flux}) then becomes

$$
\begin{align} \label{eq:fpi_flux2}
	\mathbf{\Phi_{in}} &= \mathbf{T_{SFPI}}\circ[\mathbf{t_{samp}}\odot\mathbf{m_{BB}}(T_{BB}) + \mathbf{r_{samp}}\odot\mathbf{m_{env}}(T_{env})] + (\mathbf{1} - \mathbf{T_{SFPI}}) \circ \mathbf{m_{sens}}(T_{sens}) \\[1.2em]
	&= \mathbf{T_{SFPI}}\circ[\mathbf{x} - \mathbf{m_{sens}}(T_{sens})] + \mathbf{m_{sens}}(T_{sens}) 
\end{align} 
$$  


Eq. (\ref{eq:signal}) then becomes

$$
\begin{align} \label{eq:signal2}
	\mathbf{i} \propto (\mathbf{T_{SFPI}}\circ[\mathbf{x} - \mathbf{m_{sens}}(T_{sens})])\mathbf{s} = \mathbf{A}[\mathbf{x} - \mathbf{m_{sens}}(T_{sens})] = \mathbf{A}\mathbf{\chi}
\end{align} 
$$ 

We know (or at least are able to estimate $\mathbf{m_{sens}}(T_{sens})$) which means that if we find $\mathbf{\chi}$, we can calculate $\mathbf{x}$ by subtracting $\mathbf{m_{sens}}(T_{sens})$. The final $\mathbf{Ax}=\mathbf{b}$ then becomes:

$$
\begin{align} \label{eq:Ax=b2}
	\mathbf{i} = \mathbf{A\chi}
\end{align} 
$$ 

In this case, the negative terms are moved to $\mathbf{\chi}$ instead, making $\mathbf{i}$ and $\mathbf{A}$ purely nonnegative while $[\mathbf{x} - \mathbf{m_{sens}}(T_{sens})]$ can actually be negative if the net flux becomes negative. 

### Hey - that doesn't make sense!? If $\chi$ is negative, the $\mathbf{i}$ must be too?

Correct - There has been a small omission in all of the previous calculations models. As expressed in Eq. (\ref{eq:signal}), if the difference in flux becomes negative, so does the signal. But that is not the case with the real measurements. Since the images are represented by 10-bit values, the signal cannot be negative. This is achieved by applying an offset, which ensures that all (or at least most) of the values lies within the linear range of the sensor. This offset is referred to as the GSK-voltage in the camera settings. So that is why I could claim that $\mathbf{i}$ is purely nonnegative in the previous paragraph. I believe (and my logic might be flawed here) that this off-set should be accounted for in the second $\mathbf{Ax}=\mathbf{b}$ expression (Eq. \ref{eq:Ax=b2}) but not necessarily in the first (Eq. \ref{eq:Ax=b1}). 



