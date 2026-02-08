# findmodes

Calculates the modes supported by the structure using the current calculation settings.
This function is the script equivalent to the "Calculate Modes" button. Each mode will
be saved as a D-CARD named "modeX", where X is the xth mode found. The D-CARD saves data
such as effective index and mode profile.

| **Syntax**   | **Description**                               |
| ------------ | --------------------------------------------- |
| n=findmodes; | n will be equal to the number of modes found. |

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

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ setanalysis ](./setanalysis.md) , [ mesh ](./mesh.md) ,
[ selectmode ](./selectmode.md) , [ frequencysweep ](./frequencysweep.md) ,
[ coupling ](./coupling.md) , [ overlap ](./overlap.md) ,
[ bestoverlap ](./bestoverlap.md) , [ propagate ](./propagate.md)
