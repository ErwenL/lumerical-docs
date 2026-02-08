# frequencysweep

Performs a frequency sweep using the current settings within the frequency analysis tab.
Produces a D-CARD called "frequencysweep" that contains dispersion, effective index, and
other data for as a function of frequency.

The
[selectmode](https://optics.ansys.com/hc/en-us/articles/360034405234-selectmode-Script-command)
command can be used to select one or more modes to be used for the frequency sweep.

| **Syntax**      | **Description**                                                                              |
| --------------- | -------------------------------------------------------------------------------------------- |
| frequencysweep; | Perform a frequency sweep with the current settings. This function does not return any data. |

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

To perform a frequency sweep on the first three mode and plot the effective index

```
switchtolayout;  
findmodes;  
selectmode([1,2,3]);  
  
frequencysweep;  
neff_sweep = getdata(“FDE::data::frequencysweep”, “neff”);  
freq_sweep = getdata(“FDE::data::frequencysweep”, “f”);  
lambda_sweep = c/freq_sweep;  
plot(lambda_sweep*1e6,real(neff_sweep), “Wavelength(um)”, “Real Effective Index”);  
legend(“Mode 1”, “Mode 2”, “Mode 3”);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ setanalysis ](./setanalysis.md) , [ mesh ](./mesh.md) , [ findmodes ](./findmodes.md)
, [ selectmode ](./selectmode.md)
