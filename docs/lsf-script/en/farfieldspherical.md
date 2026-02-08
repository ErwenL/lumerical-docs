# farfieldspherical

Interpolates far field data (3D simulations) from E(ux,uy) to spherical coordinates
E(theta,phi) 1D array. The far field projections functions generally return the
projection as a function of ux,uy (direction cosines). farfieldspherical can be used to
interpolate this data into the more common units of theta, phi. See the farfield3d
documentation for information on interpreting ux, uy, na, nb for various monitor
orientations.

| **Syntax**                                        | **Description**                                                                       |
| ------------------------------------------------- | ------------------------------------------------------------------------------------- |
| out = farfieldspherical( E2, ux, uy, theta, phi); | Interpolate far field data to spherical coordinates. The output has a size of (MxN,1) |

| **Parameter** |          | **Default value** | **Type** | **Description**                                                                                                                                            |
| ------------- | -------- | ----------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E2            | required |                   | matrix   | E field data from farfield3d                                                                                                                               |
| ux            | required |                   | vector   | ux data from farfieldux. Note that the result should be a vector, so it is sufficient to perform the farfieldux script command for only 1 frequency point. |
| uy            | required |                   | vector   | uy data from farfielduy. Note that the result should be a vector, so it is sufficient to perform the farfieldux script command for only 1 frequency point. |
| theta         | required |                   | vector   | theta vector, in degrees. Must have length M or 1.                                                                                                         |
| phi           | required |                   | vector   | phi vector, in degrees. Must have length N or 1.                                                                                                           |

**Example**

Create a plot of the E2_far vs theta, for phi=0.

```
m="Monitor1";  # Monitor name
res = 201;    # projection resolution
E2 = farfield3d(m,1,res,res);
ux = farfieldux(m,1,res,res);
uy = farfielduy(m,1,res,res);
theta = linspace(-90,90,100); 
phi = 0;
plot(theta, farfieldspherical(E2,ux,uy,theta,phi) ,"theta", "E^2", "E^2 at phi=0");
```

Interpolate field data to a grid of theta and phi angles.

```
theta = linspace(-90,90,10);
phi = linspace(0,45,11);
Theta = meshgridx(theta,phi);
Phi = meshgridy(theta,phi);
E2_angle = farfieldspherical(E2,ux,uy,Theta,Phi);  
E2_angle = reshape(E2_angle, [length(theta), length(phi)]);  
image(theta, phi, E2_angle, "theta","phi","E2");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ farfield3d ](./farfield3d.md) , [ farfieldux ](./farfieldux.md) ,
[ farfielduy ](./farfielduy.md) ,
[ Far field projections - Direction unit vector coordinates ](https://optics.ansys.com/hc/en-us/articles/360034394294-FFP-Direction-unit-vector-coordinates)
, [ meshgridx ](./meshgridx.md) , [ meshgridy ](./meshgridy.md)
