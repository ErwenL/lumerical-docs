# sourceintensity

Returns the source power divided by the area of the source. In 3D simulations, the units
will be in Watts/m 2 if CW norm is used, and Watts/m 2 /Hertz 2 if No norm is used. This
function is often used when normalizing power measurements from simulations with a TFSF
source.

In the case of multiple sources, the sourceintensity(f) command will return the sum of
all sourceintensity from all sources.

| **Syntax**                              | **Description**                                                                                                                                                                                                                                                                           |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = sourceintensity(f);               | Returns the source intensity at the vector of frequency points f (f is the frequency in Hz).                                                                                                                                                                                              |
| out = sourceintensity(f, option);       | The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2. |
| out = sourceintensity(f, option, name); | This function makes it possible to perform the normalization using the spectrum of one source, rather than the sum of all the sources.                                                                                                                                                    |

**Examples**

This example shows how to use the transmission , sourcepower and sourceintensity
functions to measure the power injected by a TFSF source. Notice that the monitor is 1/4
the area of the source.

```
newproject;          # create new simulation
save("test");
addfdtd;         # add simulation region
set("mesh accuracy",4);
set("x span",2.5e-6);
set("y span",2.5e-6);
set("z span",2.5e-6);
addtfsf;         # add source
set("x span",2e-6);
set("y span",2e-6);
set("z span",2e-6);
set("wavelength span",0);
addpower;         # add monitor (1/4 area of source)
set("x span",1e-6);
set("y span",1e-6);
run;            # run simulation
m="monitor";       
f=getdata(m,"f");     # get frequency vector
T=transmission(m);     # get power transmission (fraction of source power)
sp=sourcepower(f);     # get power injected by source (Watts)
I=sourceintensity(f);   # get source intensity (Watts/m^2)
area = getdata("source","area"); # get source area (it's not exactly 2um^2 due to finite sized mesh)
# output results
?"Transmitted power (fraction of source power): " +num2str(T);
?"Transmitted power (Watts): " +num2str(T*sp);
?"Source power (Watts): "+num2str(sp);
?"Source intensity (Watts/um^2): " + num2str(I*1e-12);
?"Ensure Intensity*Area=Power: " + num2str(I*area/sp);
> Transmitted power (fraction of source power): 0.235078
> Transmitted power (Watts): 1.24415e-015
> Source power (Watts): 5.2925e-015
> Source intensity (Watts/um^2): 1.30714e-015
> Ensure Intensity*Area=Power: 1
```

**See Also**

[ sourcenorm ](./sourcenorm.md) , [ sourcepower ](./sourcepower.md) ,
[ sourceintensity_avg ](https://optics.ansys.com/hc/en-us/articles/360034925393-sourceintensity-avg)
,
[ sourceintensity_pavg ](https://optics.ansys.com/hc/en-us/articles/360034925413-sourceintensity-pavg)
, [ dipolepower ](./dipolepower.md) , [ transmission ](./transmission.md) ,
[ cwnorm ](./cwnorm.md) , [ nonorm ](./nonorm.md) ,
[ Units and normalization ](https://optics.ansys.com/hc/en-us/articles/360034397034)
