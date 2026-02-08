# grating

Returns the fraction of transmitted power to each physical grating orders for a given
simulation. Results are normalized such that the sum of all the orders is equal to 1. To
convert these values into fractions of the source power, multiply by the the
transmission script function.

3D simulations: Data is returned in a NxMxP matrix where N,M are the number of grating
orders, and P is the number of frequency points.

2D simulations: Data is returned in a NxP matrix where N is the number of grating
orders, and P is the number of frequency points.

| **Syntax**                                         | **Description**                                                       |
| -------------------------------------------------- | --------------------------------------------------------------------- |
| out = grating("monitorname",f, index, direction ); | Returns the strength of all physical grating orders from monitorname. |

| **Parameter** |          | **Default value**           | **Type** | **Description**                                                                                                                                                                                      |
| ------------- | -------- | --------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| monitorname   | required |                             | string   | name of the monitor from which far field is calculated                                                                                                                                               |
| f             | optional | 1                           | vector   | Index of the desired frequency point. This can be a single number or a vector. Multithreaded projection to allow multiple frequency points to be calculated simultaneously was introduced in R2016b. |
| index         | optional | value at monitor center     | number   | The index of the material to use for the projection.                                                                                                                                                 |
| direction     | optional | direction of max power flow | number   | Direction: this can be +1 or -1.                                                                                                                                                                     |

The following table summarizes how to interpret the coordinate vector properties for
various monitor orientations.

| **Monitor orientation** | **Monitor surface normal** | **'N', 'ux', 'gratingn', 'gratingperiod1', 'gratingu1', 'gratingbloch1', correspond to** | **'M', 'uy', 'gratingm', 'gratingperiod2', 'gratingu2', 'gratingbloch2' correspond to** |
| ----------------------- | -------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| XY plane                | Z                          | x axis                                                                                   | y axis                                                                                  |
| XZ plane                | Y                          | x axis                                                                                   | z axis                                                                                  |
| YZ plane                | X                          | y axis                                                                                   | z axis                                                                                  |

**Example**

This 2D example plots the relative strength of the grating orders.

```
mname="T";          # monitor name
theta=gratingangle(mname);  # angle of each grating order
G=grating(mname);      # power to each order (fraction of transmitted power)
plot(theta,G,"theta (deg)","relative power","grating orders","plot points");
```

This 3D example calculates various grating quantities.

```
mname="T";       # monitor name
N=gratingn(mname);   # grating order numbers
M=gratingm(mname);
u1=gratingu1(mname);  # grating unit vectors (can be converted to theta,phi)
u2=gratingu2(mname);
G=grating(mname);   # power to each order (fraction of transmitted power)
T=transmission(mname); # total power transmitted through monitor (fraction of source power)
# Print all grating orders to prompt. Results will sum to 1.
# Then normalize grating results to the injected source power.
?G;  # grating results
?G*T; # normalized to source power
# find strength and direction of 0,0 grating order
nx=find(N,0); # find 0th grating order
ny=find(M,0); # find 0th grating order
?"Grating order 0,0 strength: " + num2str( G(nx,ny) );
?"Grating order 0,0 direction: Ux=" +num2str(u1(nx)) + " Uy=" +num2str(u2(ny));
# image all grating orders, using log scale
image(u1,u2,G,"ux","uy","Grating order strength","logplot");
```

Calculate the zeroth grating order transmission from a monitor that recorded multiple
frequency points. The grating function operates on one frequency point at a time, so a
for loop is required.

```
mname="T";       # monitor name
f=getdata(mname,"f");  # get frequency vector
T=transmission(mname); # get total transmission
G00 = matrix(length(f)); # initialize matrix
# get 0,0 grating order for each frequency
for (i=1:length(T)) {
 N=gratingn(mname,i);  # grating order numbers
 M=gratingm(mname,i); 
 temp=grating("T2",i);
 G00(i) = temp(find(N,0),find(M,0)); # select 0,0 grating order
}
plot(c/f*1e6,T,G00*T,"wavelength (um)","power");
legend("total transmission","0,0 grating transmission"); 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ gratingn ](./gratingn.md) , [ gratingperiod1 ](./gratingperiod1.md) ,
[ gratingbloch1 ](./gratingbloch1.md) , [ gratingu1 ](./gratingu1.md) ,
[ gratingangle ](./gratingangle.md) , [ gratingpolar ](./gratingpolar.md) ,
[ gratingvector ](./gratingvector.md)
