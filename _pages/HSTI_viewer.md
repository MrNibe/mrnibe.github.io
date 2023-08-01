---
layout: single
classes: wide
title: "Hyperspectral image viewer"
permalink: /HSTI_viewer/
author_profile: true
---

I have made a hyperspectral image viewer/analyser has been programmed in python utilizing the Tkinter library. The program makes it possible to do some simple data processing as well as extracting mean spectra based on user definable colored selections. 

Here is an example of a hyperspectral thermal image of a collection of different gemstones being displayed in the viewer. 

<center><img src="/assets/images/hsti_viewer/example_screen_shot.png" alt="HSTI viewer" width="100%" height="100%">
<figcaption>Screen shot of hyperspectral viewer showing a hyperspectral thermal image of different gemstones. A red and green selection has been made to extract mean interferograms.</figcaption></center>

## Basic operations
### Loading an image
If the image comes out of the hyperspectral thermal camera, it is loaded using the *Select directory* button. Here, the directory containing the "/images/capture/" (this matches the standard data output of the camera) must be located. If the hyperspectral image is instead in ".pam" or ".npy" format, choose the *Select file* button instead. The numpy array must have exactly three dimensions where axis 2 (the third dimension) contains the spectral information. 

### Scrolling through the bands
Using the leftmost slider with *Band number* written above it, it is possible to scrub through the bands of the data cube. While moving the slider, the image of the viewer is updated. By default, the color range changes with every new band, but it is possible to fix the range by checking the *Manual color limits* check box in the bottom right corner. The accompanying slider can then be used set the lower and upper limits of the color range. 

### Extracting mean spectrum/interferograms
It is possible to use the mouse to draw a selection directly on the image on the right. By left clicking and dragging the mouse, a colored mask is drawn and shown on top of the image. Once the mouse button is released, the mean spectrum is plotted in the corresponding color in the plot on the right. The size of the brush (measured in pixels) can be changed with the slider, *Radius*, and the opacity of the mask can be changed with the *Selection opacity* slider. Right clicking on the image can be used to erase existing color mask, and the *Clear selection* button can be used to clear all selections at once and the *Invert selection* button converts all selections to the same color after which the mask is inverted. Different colors can be selected using the *Pick color* button. Once a color has been added to the mask, it will appear as a color swatch under the plot on the right. By clicking a swatch, the associated color is 'brought to the front' and is made active again - making it possible to add to the mask without having to enter the exact same RGB value again. 

### Removing data
It is possible to remove entire sections of a data cube based on a selection. Simply paint the parts of the image you would like to exclude from the analysis, then hit the *Remove data* button, and the data will be replaced by NaNs, effectively excluding them from the preprocessing.     

## Saving files
It is possible to save different forms of images using the viewer. The *Save current band* button saves the current band in the viewer as a 8-bit .tif file. *Save figure* saves the entire figure (both image, plot and color swatches) as a .png. *Save animation* saves the data cube as a .gif with 10 FPS. The *Save spectra* button saves all extracted spectra either as a .txt (default) or .csv file. The first column of the file contains the x-axis. The following columns are arranged from most recent to oldest markings on the color mask. This means that column 1 (0-indexing for the x-axis) is bottom leftmost color swatch, column 2 corresponds to the color swatch to its right and so on.

At this moment it is not possible to save preprocessing steps or color masks applied in the viewer. 

## Adding preprocessing and data analysis
The hyperspectral image viewer makes it possible to apply different forms of preprocessing to the entire image. 

### Apply NUC

### Autoscale

### Convert to wavelength 

### Debend cube

### Mean center bands

### Mean center spectra

### Normalize band norms

### Normalize by reference spectrum

### Normalize cube

### Normalize spectra

### Normalize spectra norms

### Savitzky-Golay filter

### Set first band to 0

### Spatial median filter

### Standard Normal Variate

### Subtract TMM reference spectrum

### Use selection as reference spectrum



## Principal Component Analysis
