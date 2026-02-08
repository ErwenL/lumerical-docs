# extractstructure

Creates an a polygon (in 2D) or a planar solid (in 3D) using the finite-element
geometric data stored in an unstructured dataset.

| **Syntax**                                                                                                    | **Description**                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| extractstructure(D);                                                                                          | Creates a polygon for 2D data and a planar solid for 3D data. The parameter D is the input unstructured dataset. This function does not return any data.     |
| extractstructure(D, Rel_Coplanar_Tol);                                                                        | Same as the above command, but the relative tolerance to merge coplanar elements will be set to the value specified.                                         |
| extractstructure(D, Rel_Coplanar_Tol, Smoothing_Pass_Count);                                                  | Same as the above command, but uses Laplacian smoothing on the surface mesh. The number of iteration is defined by the value specified.                      |
| extractstructure(D, Rel_Coplanar_Tol, Smoothing_Pass_Count, Smoothing_Angle_Coplanar_Tol);                    | Same as the above command, but the allowed angular difference between triangles around a vertex where the vertex can be moved is set to the value specified. |
| extractstructure(D, Rel_Coplanar_Tol, Smoothing_Pass_Count, Smoothing_Angle_Coplanar_Tol, Allow_Tessalation); | Same as the above command, but allows re-triangulation of the facets.                                                                                        |

| **Parameters**               | **Type**             | **Description**                                                                                                                                               |
| ---------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| D                            | unstructured dataset | Input data that is used to create the structure.                                                                                                              |
| Rel_Coplanar_Tol             | number               | (optional) Relative tolerance to merge coplanar elements. The default value is 1e-6.                                                                          |
| Smoothing_Pass_Count         | number               | (optional) In 3D only. Enables Laplacian smoothing on the surface mesh before surface extraction. The default value is 0 and the maximum allowed value is 20. |
| Smoothing_Angle_Coplanar_Tol | number               | (optional) Sets the allowed angular difference between triangles around a vertex where the vertex can be moved. The default value is 0.001.                   |
| Allow_Tessalation            | number               | (optional) In 3D only. Allows re-triangulation of the facets.                                                                                                 |

**Example**

Run the script file
[extract_2d.lsf](/hc/article_attachments/360045274574/extract_2d.lsf) with the CHARGE
project file [geom2d.ldev](/hc/article_attachments/360046126993/geom2d.ldev) for a 2D
example of this command. Here, we use the ID of the "CHARGE" solver region to single out
any part of the structure with ID = 3, which would correspond to the semiconductor
material in this example and then construct an object (polygon) in that shape.

**See Also**

[Dataset builder](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder),
[Datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
