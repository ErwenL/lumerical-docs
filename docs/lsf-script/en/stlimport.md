# stlimport

Adds a structure to the simulation environment with structure geometry loaded from
specified STL file.

| **Syntax**                                                 | **Description**                                                                               |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| stlimport(filename,scalingFactor, vertexRadius,debugFlag); | Add a new structure from specified STL type CAD file. This function does not return any data. |

| Parameter     |          | Default value | Type          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------- | -------- | ------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filename      | required |               | string        | Name of the STL CAD file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| scalingFactor | optional | 1e-6          | number        | An STL file does not contain a unit. When imported to Lumerical's software, the unit is micron by default. To have the unit in nanometer, set scaling_factor 1e-9.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| vertexRadius  | optional | 1e-12         | length (in m) | Vertices may be shared by multiple triangles so the same vertex may be loaded multiple times for different triangles. The vertexRadius is the minimum distance between two vertices so that they are considered to be distinct vertices.                                                                                                                                                                                                                                                                                                                                                                  |
| debugFlag     | optional | false         | boolean       | If true, the following data will be printed to the script prompt: -Input Vertex Count (total number of vertices in the file) -Triangles (total number of triangles) -Filtered Vertices (number of unique vertices) -Vertex Collisions (Input Vertex Count minus Filtered Vertices) -Invalid Triangles -Expected Vertex Collisions If the number of invalid triangles is larger than 0, try adjusting the vertexRadius parameter and importing the object again. Note: If there are a large number of triangles in the STL file, the script function can take longer to run when debugFlag is set to true. |

**Example**

The following script commands can be used to create a 3D geometry based on the .stl file
provided in this KB page:
[ Import - STL ](https://optics.ansys.com/hc/en-us/articles/360034901953-Import-STL) .

```
filename = "stlimport_assembly.stl";
stlimport(filename);
set("material","Si (Silicon)");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md) ,
[ readstltriangles ](./readstltriangles.md)
