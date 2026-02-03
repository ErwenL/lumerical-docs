# importnk

Imports the refractive index (n and k) over an entire volume or surface from a file. This command only applies to import primitives. The function returns 1 if the data is successfully imported. It is possible to import anisotropic nk data.

**Syntax** |  **Description**  
---|---  
out = importnk(filename,file_units, x0,y0,z0,reverse_index_order); |  Import n (and k) data from filename in three dimensional (or two dimensional) simulations. All arguments after the filename are optional.  
  
**Parameter** |  **Default value** |  **Type** |  **Description**  
---|---|---|---  
filename |  required |  string |  name of the file with n (and k) data to import. May contain complete path to file, or path relative to current working directory  
file_units |  "m" |  string |  The optional string argument file_units can be "m", "cm, "mm", "microns" or "nm" to specify the units in the file.  
x0 |  0 |  number |  The optional arguments x0, y0 and z0 specify the data origin in the global coordinates of the Graphical Layout Editor. For example, you can define your volume with respect to a particular point in space, for example (0,0,-5) microns.  
y0 |  0 |  number |   
z0 |  0 |  number |   
reverse_index_order |  0 |  number |  The optional argument reverse_index_order can be set to 1 to reverse how the indices are interpreted in the file. It is best to verify the correct setting with a graphical import before using the script command.  
  
**Example**

See the [Import object - Spatial (n,k) data](/hc/en-us/articles/360034901993-Import-object-Spatial-n-k-data) example for file format.

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [importnk2](/hc/en-us/articles/360034408694-importnk2)
