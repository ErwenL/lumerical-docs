# colormatch

Returns the X, Y and Z tristimulus values calculated for a given spectral power
distribution (power per unit area per unit wavelength) and a selected set of color
matching functions. The colormatch function assumes that the units of wavelength for the
spectral power distribution are nanometers, for example, W/(m 2 nm). The available color
functions are the CIE 1931 and CIE 1964.

The X, Y, Z values have dimensions of power per unit area, in the units used for the
spectral power distribution. The expressions for calculating the X, Y and Z values are:

$$ \\begin{aligned} X &=\\int I(\\lambda) \\overline{x}(\\lambda) d \\lambda \\\\ Y
&=\\int I(\\lambda) \\overline{y}(\\lambda) d \\lambda \\\\ Z &=\\int I(\\lambda)
\\overline{z}(\\lambda) d \\lambda \\end{aligned} $$

where I(͛λ) is the spectral power distribution and \\( \\overline{x} \\), \\(
\\overline{y} \\) ,\\( \\overline{z} \\) are the color matching functions.

References:

[ https://en.wikipedia.org/wiki/CIE_1931_color_space ](https://en.wikipedia.org/wiki/CIE_1931_color_space)

CIE Proceedings (1932), 1931. Cambridge: Cambridge University Press.

CIE Proceedings (1964) Vienna Session, 1963, Vol. B, pp. 209-220 (Committee Report
E-1.4.1), Bureau Central de la CIE, Paris.

| **Syntax**                               | **Description**                                                                                                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cm = colormatch(spec, lam, "functions"); | Returns X, Y, Z for the spectrum spec evaluated at the wavelength values in lam (units of meters), using the selected color functions. If no functions are specified, the "CIE 1931" set is used. |

**Example**

This example shows how to calculate the X, Y, Z values for a given spectral power
distribution.

```
# create a dummy spectrum
lambda = linspace(300e-9,700e-9,500); # note SI units (meters)
spectrum = exp(-(lambda-450e-9)^2/(30e-9)^2); 
plot(lambda*1e9,spectrum,"wavelength(nm)","test spectrum");
 
?cm64 = colormatch(spectrum,lambda,"CIE 1964");
result:
14.3731 
6.07161 
79.5907
?cm36 = colormatch(spectrum,lambda); # "CIE 1931" is assumed if no color matching functions are specified
result:
13.1613 
2.99189 
72.2623
```

The following figure shows the plot of the test spectrum created by the example code.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ plot ](./plot.md) ,
[ colormatchfunction ](./colormatchfunction.md) , [ colormatchxy ](./colormatchxy.md) ,
[ colormatchuv ](./colormatchuv.md)
