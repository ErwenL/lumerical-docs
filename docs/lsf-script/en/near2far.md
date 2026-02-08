# near2far

Calculates the far field at the specified points using the provided near field monitor
data.

| **Syntax**                              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = near2far(nearfield, farfield, n); | Calculates the far field using the provided near field monitor data at the specified far field points. The input unstructured data set specifying the near fields must contain an attribute named 'E' parametrized by frequency. The output is an unstructured data set with an attribute named 'E' containing the far field. The far field frequencies are determined by the near field frequencies while the far field points, connectivity matrix and surface normals associated with the output data set are taken from the unstructured data set specifying the far field points. |

| **Parameter** |          | **Default value** | **Type**              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------- | -------- | ----------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nearfield     | required |                   | unstructured data set | Near field data in the format returned by DFT monitors. The electric field can be sampled on a segmented line or on a triangulated surface. If sampled on a segmented line, the electric field is assumed to come from a 2D simulation and the 2D integral kernel is used for the far field projection. Similarly, if the electric field is sampled on a triangulated surface, it is assumed to come from a 3D simulation and the 3D integral kernel is used for the projection (see the provided reference). |
| farfield      | required |                   | unstructured data set | Far field points to be used in the projection. If the near fields are sampled on segmented line, the far field points must be specified using a segmented line. Similarly, if the near fields are sampled on a triangulated surface, the far field points must be sampled on a triangulated surface. The command createsphericalsurface can be used to easily create an unstructured data set with a segmented line or a triangulated surface.                                                                |
| n             | optional | 1.0               | number or vector      | Background refractive index of the far field medium. It can be a single number or a vector with the same length as the near field frequency parameter.                                                                                                                                                                                                                                                                                                                                                        |

## Note: Far field integration For integration of far field over a range of angles, the script command quadtri can be used. See [ quadtri ](./quadtri.md) for more information.

**Example**

This example performs a far field projection on a sphere using the near field data
collected from a monitor named "monitor".

```
surf = createsphericalsurface;
E_near = getresult("DGTD::monitor","fields");
E_far = near2far(E_near,surf);
visualize(E_far); 
```

For more information on how far field projections are computed please refer to:

John B. Schneider, Understanding the Finite-Difference Time-Domain Method, Chapter 14:
Near-to-Far-Field Transformation, 2010 Available at:
[ http://www.eecs.wsu.edu/~schneidj/ufdtd/ ](http://www.eecs.wsu.edu/~schneidj/ufdtd/)

**See Also**

[ createsphericalsurface ](./createsphericalsurface.md) ,
[ List of commands ](../lsf-script-commands-alphabetical.md) ,
