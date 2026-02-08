# setanalysis

Sets calculation parameters in MODE' FDE and FEEM analysis window.

| **Syntax**                      | **Description**                                  |
| ------------------------------- | ------------------------------------------------ |
| ?setanalysis;                   | Lists all the parameters in the analysis window. |
| setanalysis("property", value); | Sets"property" to value.                         |

**Example**

To perform a frequency sweep on the first mode and plot the dispersion:

```
switchtolayout;  
findmodes;  
  
selectmode(1);  
setanalysis("track selected mode",1);  
setanalysis("detailed dispersion calculation",1);  
  
frequencysweep;  

D=getdata("frequencysweep","D");  
f=getdata("frequencysweep","f_D");  
plot(c/f*1e6,D*1e6,"Wavelength (um)", "Dispersion (ps/nm/km)");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ mesh ](./mesh.md) ,
[ findmodes ](./findmodes.md) , [ frequencysweep ](./frequencysweep.md) ,
[ analysis ](./analysis.md) , [ getanalysis ](./getanalysis.md)
