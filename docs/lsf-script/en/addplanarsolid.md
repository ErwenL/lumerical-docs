# addplanarsolid

Adds a planar solid primitive with the specified vertices. Planar solids offer a very
convenient option to create custom, complex 3D geometries. You can find more information
about planar solids in this page:
[ Structures - Planar solid](https://optics.ansys.com/hc/en-us/articles/360034901573-Structures-Planar-solid).

| **Syntax**                   | **Description**                                                                                                                                                                                                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addplanarsolid;              | Adds an empty planar solid object.                                                                                                                                                                                                                                                       |
| addplanarsolid(vtx, fct);    | Adds a planar solid object whose vertices are defined by 'vtx' and whose facets are defined by 'fct'                                                                                                                                                                                     |
| addplanarsolid(struct_data); | Adds an empty planar solid object and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The example below adds a planar solid cut-face box using two methods. The first method
uses the facet table as a cell array and the second method uses the facet table a
matrix.

```
method_type = 1;  # choose 1 or 2 to switch between methods
vtx = [0,0,0;
    1,0,0;
    1,1,0;
    0,1,0;
    0,0,2;
    1,0,2;
    1,1,2;
    0,1,2]*1e-6;
# Method 1: facet table as cell array
a = cell(7);
for (i = 1:7) {
 a{i} = cell(1);
}
a{1}{1} = [1,4,3,2];
a{2}{1} = [1,5,8,4];
a{3}{1} = [1,2,6,5];
a{4}{1} = [2,3,6];
a{5}{1} = [3,8,6];
a{6}{1} = [3,4,8];
a{7}{1} = [5,6,8];
if (method_type == 1) {
 addplanarsolid(vtx,a);
}
# Method 2: facet table as matrix
b = matrix(4,1,7); # max four points per polygon, max 1 polygon per facet
for (i = 1:7) { 
  fpoly = a{i}{1}; 
  for (j = 1:length(fpoly)) { 
    b(j,1,i) = fpoly(j); 
    }
  }
if (method_type == 2) { 
  addplanarsolid; 
  set('vertices',vtx); # must be done first 
  set('facets',b);
  }
```

**See Also**

[ List of commands](../lsf-script-commands-alphabetical.md)
