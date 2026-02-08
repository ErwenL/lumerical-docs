# colormatchuv

Returns the u' and v' chromaticity values calculated for a given spectral power
distribution (power per unit area per unit wavelength) and a selected set of color
matching functions. The colormatchuv function assumes that the units of wavelength for
the spectral power distribution are nanometers, for example, W/(m 2 nm). The available
color functions are the CIE 1931 and CIE 1964.

The u' and v' values are dimensionless and they are related to the X, Y and Z values by:

$$ u^{\\prime}=\\frac{4 X}{X+15 Y+3 Z}, v^{\\prime}=\\frac{9 Y}{X+15 Y+3 Z} $$

References:

[ https://en.wikipedia.org/wiki/CIE_1931_color_space ](%25LINK_CAPTION%25)

[ http://en.wikipedia.org/wiki/CIELUV ](%25LINK_CAPTION%25)

CIE Proceedings (1932), 1931. Cambridge: Cambridge University Press.

CIE Proceedings (1964) Vienna Session, 1963, Vol. B, pp. 209-220 (Committee Report
E-1.4.1), Bureau Central de la CIE, Paris.

| **Syntax**                                               | **Description**                                                                                                                                                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| cmuv = colormatchuv(colormatch(spec, lam, "functions")); | Returns u', v' for the spectrum spec evaluated at the wavelength values in lam (units of meters), using the selected color functions. If no functions are specified, the "CIE 1931" set is used. |

**Example**

This example shows how to calculate the u', v' values for a given spectral power
distribution.

```
# create a dummy spectrum
lambda = linspace(300e-9,700e-9,500); # note SI units (meters)
spectrum = exp(-(lambda-450e-9)^2/(30e-9)^2); 
plot(lambda*1e9,spectrum,"wavelength(nm)","test spectrum");
 
?cmuv64 = colormatchuv( colormatch(spectrum,lambda,"CIE 1964") );
result:
0.167023 
0.158749 
?cmuv36 = colormatchuv( colormatch(spectrum,lambda) );
result:
0.191558 
0.0979782
```

The following figure shows the plot of the test spectrum created by the example code.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ plot ](./plot.md) ,
[ colormatchfunction ](./colormatchfunction.md) , [ colormatch ](./colormatch.md) ,
[ colormatchxy ](./colormatchxy.md)
