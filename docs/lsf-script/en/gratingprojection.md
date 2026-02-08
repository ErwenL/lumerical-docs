# gratingprojection

Takes the near fields from a frequency domain monitor together with the periodicity
vectors of the system, the source wave vector and the background refractive index and
performs a far field projection to determine the relative power in each propagating
grating order.

| **Syntax**                                                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = gratingprojection(nearfield, period, source, index); | Returns a matrix data set with all the projection results. The parameters of the data set are the grating orders (integers n and m) and frequency. Indexes n and m correspond to the first and second periodicity directions specified by the input periodicity vectors. The attributes of the data set are the same as those returned by the gratingorders command with the addition of the relative power into each propagating grating order (called projection). The projection result is normalized so that its sum over all grating orders is always equal to one. The frequency parameter is the same as that of the input field data. |

| **Parameter** |          | **Default value** | **Type**              | **Description**                                                                                                                                              |
| ------------- | -------- | ----------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| nearfield     | required |                   | unstructured data set | Field data from a frequency domain monitor.                                                                                                                  |
| period        | required |                   | vector                | Periodicity vector(s) as returned by the getperiodicity command.                                                                                             |
| source        | required |                   | vector                | Source unit wave vector as returned by the getsourcedirection command.                                                                                       |
| index         | optional | 1.0               | number or vector      | Refractive index of the background medium (typically the substrate or superstrate). It can be a scalar or a vector of the same size as the frequency vector. |

**Example**

This example demonstrates how to calculate the relative power into each propagating
grating order for a DGTD simulation with periodic boundary conditions. The near fields
are collected from a frequency domain monitor named "monitor". The source wave vector is
collected from a plane wave source named "source". The periodicity vectors are collected
from the DGTD simulation object.

```
# unstructured data set with the near field
fields = getresult("DGTD::monitor","fields");
# periodicity vector
period = getperiodicity("DGTD");
# normalized source k-vector
source_k = getsourcedirection("DGTD::source");
# grating projection
gp = gratingprojection(fields,period,source_k);
visualize(gp); 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ getperiodicity ](./getperiodicity.md) ,
[ getsourcedirection ](./getsourcedirection.md) , [ gratingorders ](./gratingorders.md)
