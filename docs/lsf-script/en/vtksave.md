# vtksave

Saves a Lumerical dataset into the VTK format. The command only saves rectilinear and
unstructured datasets. The “filename” will have .vtr appended for rectilinear dataset,
.vtu appended for unstructured dataset. The freely available data visualization program
Paraview can then be used to create sophisticated plots of your data.

| **Syntax**                    | **Description**                                     |
| ----------------------------- | --------------------------------------------------- |
| vtksave(“filename”, dataset); | Save the dataset in vtk file of the name specified. |

**Examples**

The following simple example gets the result E, a rectilinear dataset and saves into the
VTK format.

```
E = getresult("monitor2", "E");
vtksave("beam.vtr", E);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ datasets ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets) ,
[ rectilineardataset ](./rectilineardataset.md) , [ matlabsave ](./matlabsave.md) ,
[ Advanced visualizations with ParaView ](https://optics.ansys.com/hc/en-us/articles/360034416774-Paraview)
