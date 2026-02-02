# colormatchxy

Returns the x and y chromaticity values calculated for a given spectral power distribution (power per unit area per unit wavelength) and a selected set of color matching functions. The colormatchxy function assumes that the units of wavelength for the spectral power distribution are nanometers, for example, W/(m  2  nm). The available color functions are the CIE 1931 and CIE 1964.

The x and y values are dimensionless and they are related to the X, Y, and Z values by:

$$ x=\frac{X}{X+Y+Z}, y=\frac{Y}{X+Y+Z} $$

**Syntax** |  **Description**  
---|---  
cmxy = colormatchxy(colormatch(spec, lam, "functions")); |  Returns x, y for the spectrum spec evaluated at the wavelength values in lam (units of meters), using the selected color functions. If no functions are specified, the "CIE 1931" set is used.  
  
**Example**

This example shows how to calculate the x, y values for a given spectral power distribution.
    
    
    # create a dummy spectrum  
    lambda = linspace(300e-9,700e-9,500); # note SI units (meters)  
    spectrum = exp(-(lambda-450e-9)^2/(30e-9)^2);   
    plot(lambda*1e9,spectrum,"wavelength(nm)","test spectrum");  
      
    ?cmxy64 = colormatchxy( colormatch(spectrum,lambda,"CIE 1964") );  
    result:  
    0.14368   
    0.0606946   
    ?cmxy36 = colormatchxy( colormatch(spectrum,lambda) );  
    result:  
    0.148857   
    0.033839

The following figure shows the plot of the test spectrum created by the example code.

### Related Publications

  1. <https://en.wikipedia.org/wiki/CIE_1931_color_space>
  2. CIE Proceedings (1932), 1931. Cambridge: Cambridge University Press.
  3. CIE Proceedings (1964) Vienna Session, 1963, Vol. B, pp. 209-220 (Committee Report E-1.4.1), Bureau Central de la CIE, Paris.



### See Also

[ List of commands ](/hc/en-us/articles/360037228834) , [ plot ](/hc/en-us/articles/360034410474-plot) , [ colormatchfunction ](/hc/en-us/articles/360034926733-colormatchfunction) , [ colormatch ](/hc/en-us/articles/360034926753-colormatch) , [ colormatchuv ](/hc/en-us/articles/360034406514-colormatchuv)
