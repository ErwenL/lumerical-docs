# sourcepower

Returns the power injected into the simulation by the source.

**Dipole sources**

The sourcepower script function returns the power the dipole source would radiate in a
homogeneous medium. This quantity can be calculated analytically (see
[ Dipole source](https://optics.ansys.com/hc/en-us/articles/360034382794-Sources-Dipoles)).
The actual radiated power is not given by the sourcepower function. The actual radiated
power is highly dependant on the surrounding materials since the reflections from the
structures will interfere with the fields from the dipole, changing the actual radiated
power. To get the actual radiated power, see the [ dipolepower ](./dipolepower.md)
script function.

**Other sources (Gaussian, plane wave, mode, etc)**

The sourcepower is determined from the equation below. Note that
\\(P(f)^{\\text{Source}}\\) is the Poynting vector determined from the E, H fields
injected by the source. The integral is evaluated over the injection plane of the
source.

$$ \\text {source power}\_{\\text {no_norm}}(f)=\\frac{1}{2} \\int
\\text{Re}\\left(P(f)^{\\text {Source}}\\right) \\cdot d S $$

$$ \\text {source power}\_{\\text {cw_norm}}(f)=\\frac{\\frac{1}{2} \\int
\\text{Re}\\left(P(f)^{\\text {Source}}\\right) \\cdot d S}{ | \\text
{sourcenorm}\\left.\\right |^{ 2 }} $$

As stated above, sourcepower gives the amount of power injected into the simulation. The
only exception is if the simulation is set up such that there is radiation that travels
through the injection plane of the source in the source injection direction (pink
arrow). In such cases, the actual amount of power injected by the source will not be
given by sourcepower . In this situation, the incident radiation interferes with the
source, changing the amount of injected power (similar to what happens for the dipole
source). In most cases, this means your simulation is not set up properly.

## \[[Notes:]\] Multiple sources and CW normalization In the case of multiple sources, the sourcepower(f) command will return the sum of all sourcepowers from all sources. Since the value of the sourcenorm depend on the choice of cwnorm option, the calculated sourcepower will also be affected by it.

| **Syntax**                          | **Description**                                                                                                                                                                                                                                                                                 |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = sourcepower(f);               | Returns the source power used to normalize transmission calculations at the vector of frequency points f (frequency in Hz). The unit of the source power is Watts if CW norm is used, and Watts/Hertz 2 if no norm is used.                                                                     |
| out = sourcepower(f, option);       | The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersects such a boundary at x min, y min, or z min. The default value of the option is 2. |
| out = sourcepower(f, option, name); | This option allows you to obtain the spectrum of one source, rather than the sum of all sources. This option is only needed for simulations with multiple sources.                                                                                                                              |

**Examples**

This example shows how to calculate the power injected by a source as a function of
frequency.

```
f=linspace(200e12,300e12,100);
sp=sourcepower(f); # power in Watts, assuming CW norm is on.
```

This example shows how to use the transmission and sourcepower functions to calculate
the power injected by a plane wave source.

```
newproject;
save("test");
 
# simulation region
addfdtd;
set("x span",1e-6); set("y span",1e-6); set("z span",1e-6);
set("x min bc","periodic"); set("y min bc","periodic");
 
# plane wave source
addplane;
set("z",-0.3e-6);
set("x span",2e-6); set("y span",2e-6);
set("center wavelength",500e-9);
set("wavelength span",0);
 
# power monitor
addpower; 
set("z",0.3e-6);        
set("x span",2e-6); set("y span",2e-6);
# run simulation 
run;            
# get results 
m="monitor";      
f=getdata(m,"f");     # get frequency vector
T=transmission(m);     # get power transmission (fraction of source power)
sp=sourcepower(f);     # get power injected by source (Watts)
 
# output results
?"Transmitted power (fraction of source power): " +num2str(T);
?"Transmitted power (Watts): " +num2str(T*sp);
?"Source power (Watts): "+num2str(sp);
> Transmitted power (fraction of source power): 0.999986
> Transmitted power (Watts): 1.26203e-015
> Source power (Watts): 1.26204e-015
```

**See Also**

[ sourcenorm ](./sourcenorm.md) ,
[ sourcepower_avg ](https://optics.ansys.com/hc/en-us/articles/360034925333-sourcepower-avg)
,
[ sourcepower_pavg ](https://optics.ansys.com/hc/en-us/articles/360034925353-sourcepower-pavg)
, [ dipolepower ](./dipolepower.md) , [ transmission ](./transmission.md) ,
[ sourceintensity ](./sourceintensity.md) , [ cwnorm ](./cwnorm.md) ,
[ nonorm ](./nonorm.md)
