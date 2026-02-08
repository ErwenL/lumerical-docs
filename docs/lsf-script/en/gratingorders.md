# gratingorders

Returns a matrix data set with the propagating grating orders, a unit vector in the
direction of the wave vector (or k-vector) of each order, and the grating angles. The
grating orders are the same as those used by the gratingprojection command to perform a
projection.

| **Syntax**                                             | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = gratingorders(period, source, frequency, index); | Returns a matrix data set with the propagating grating orders (integers n and m), a unit vector in the direction of the k-vector of each order (call them **u** (n,m)) and their corresponding angles (theta and phi). The parameters of the data set are n,m and frequency. Indexes n and m correspond to the first and second periodicity directions specified by the input periodicity vectors. The attributes of the data set are the unit vectors **u** (n,m) and their corresponding angles (theta and phi). The grating angles are defined with respect to the normal incidence direction of the source (call it the **n** -axis). The first angle (theta) is an elevation from the **n** -axis and the and the second angle (phi) is a rotation around the **n** -axis starting from the first periodicity vector. Angle phi is only returned when two periodicity vectors are specified. |

| **Parameter** |          | **Default value** | **Type**         | **Description**                                                                                                                                              |
| ------------- | -------- | ----------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| period        | required |                   | vector           | [3x1] or [3x2] matrix with the periodicity vectors. These are typically retrieved using the getperiodicity command.                                          |
| source        | required |                   | vector           | [3x1] vector with the normalized source k-vector. This is typically retrieved using the getsourcedirection command.                                          |
| frequency     | required |                   | vector           | Vector of frequencies (in Hz).                                                                                                                               |
| index         | optional | 1.0               | number or vector | Refractive index of the background medium (typically the substrate or superstrate). It can be a scalar or a vector of the same size as the frequency vector. |

**Example**

This example shows how to find the propagating grating orders from a DGTD simulation
with periodic boundary conditions. The source k-vector and frequency are obtained from
and plane wave source object named "source" and a frequency domain monitor named
"monitor", respectively.

```
# frequency vector of the near fields
fields = getresult("DGTD::monitor","fields");
frequency = fields.f; 
# periodicity vectors
period = getperiodicity("DGTD");
# source k-vector
source_k = getsourcedirection("DGTD::source");
# propagating grating orders
go = gratingorders(period,source_k,frequency,1.0);
visualize(go); 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ getperiodicity ](./getperiodicity.md) ,
[ getsourcedirection ](./getsourcedirection.md) ,
[ gratingprojection ](./gratingprojection.md)
