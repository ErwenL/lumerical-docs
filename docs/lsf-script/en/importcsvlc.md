# importcsvlc

This command adds a LC grid attribute or analysis group containing a liquid crystal
structure and LC grid attribute with data imported from a specified csv (comma separated
value) file without using the GUI import wizard. The arguments allow you to make the
same choices that are available in the GUI. For more information about the GUI import
wizard, see [Import object - Liquid crystal from CSV](**%20to%20be%20defined%20**).

| **Syntax**                                                           | **Description**                                                                                                                                                                                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| importcsvlc(filename);                                               | Import the csv file from the specified filename. All arguments after the filename are optional.                                                                                                                                              |
| out = importcsvlc(filename,option);                                  | Import the csv file but specify if it should be imported as a single grid attribute or added to an analysis group LC structure.                                                                                                              |
| out = importcsvlc(filename,option,exported_from_xz_plane);           | Import the csv file and specify if it was originally exported from the x-z plane. This option only applies to 2D datasets but is critical to get the orientation of the LC structure correct when it is imported into FDTD in the x-y plane. |
| out = importcsvlc(filename,option,exported_from_xz_plane,rotations); | Import the csv file with additional axis rotations.                                                                                                                                                                                          |

| **Parameter**          | **Default value** | **Type** | **Description**                                                                                                                                                                                                                                              |
| ---------------------- | ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| filename               | required          | string   | The name of the csv file to import. May contain complete path to file, or path relative to current working directory                                                                                                                                         |
| option                 | true              | boolean  | When set to 1 (true) the import will create an analysis group structure with the grid attribute and a rectangle, the same as when using the graphical import. When set to 0 (false) it will import only the grid attribute. This argument is optional        |
| exported_from_xz_plane | true              | boolean  | Applies to 2D datasets only. This indicates that the data was originally exported from the x-z plane and this should be accounted for when it is imported into the x-y plane.                                                                                |
| rotations              | [0,0,0]           | matrix   | The optional argument allows you to specify 3 rotations around the x, y and z axes respectively that are used exactly the same way as the graphical import wizard. The matrix must have 3 elements and each value will be rounded to the nearest 90 degrees. |

**Example**

The following script command will import the grid attribute from file "myfile.csv" into
an LC analysis group and rotate 90 degrees about the x axis.

```
importcsvlc("myfile.csv",true,true,[90,0,0]);
```

For more examples on creating LC grid attribute from script visit this kB page:
[LC rotation](https://optics.ansys.com/hc/en-us/articles/360034915153-LC-Rotation).

**See Also**

[addgridattribute](./addgridattribute.md), [cleardataset](./cleardataset.md),
[importdataset](./importdataset.md)
