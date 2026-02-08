# solar

Returns the solar power spectrum, in Watts/meter^2/meter.

The values are based on the global tilt values from the following link:
[ Reference Solar Spectrum Irradiance: ASTM G-173 ](http://rredc.nrel.gov/solar/spectra/am1.5/ASTMG173/ASTMG173.html)
.

| **Syntax**      | **Description**                                                                 |
| --------------- | ------------------------------------------------------------------------------- |
| out = solar(1); | Returns the power of the solar spectrum as a function of wavelength, in W/m^2/m |
| out = solar(0); | Returns the corresponding wavelength vector, in m                               |

**Example**

Use the solar command to get the solar power spectrum. Next, plot the spectrum in the
more common units of Watts/m^2/nm.

```
lambda=solar(0);   # wavelength vector in meters
ssp=solar(1);     # solar spectrum in Watts/meter^2/meter
lambda = lambda*1e9; # convert to nm
ssp  = ssp * 1e-9; # convert to /nm
plot(lambda,ssp,"wavelength (nm)","Power (W/m^2/nm)", "Solar Spectrum");
```

**See Also**

[ plot ](./plot.md) , [ integrate ](./integrate.md)
