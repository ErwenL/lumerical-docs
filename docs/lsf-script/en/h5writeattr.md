# h5writeattr

Write a matrix or string as an attribute of a group or a dataset to an HDF5 file.

| **Syntax**                                                                                         | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| h5writeattr("filename", "location_name", "attribute_name", data);                                  | Create an attribute named "attribute_name" to a group or dataset named " location_name" within an HDF5 file named "filename" from the given data. Will create the HDF5 file named "filename" if it does not exist. If there is no group or dataset called “location_name”, a new group called “location_name” will be created. If the attribute named "attribute_name" already exists in the given group/dataset within the HDF5 file, the attribute will be overwritten. Otherwise, the attribute is simply added to the existing group/dataset within the HDF5 file.                                                                                                                                         |
| h5writeattr("filename", "location_name", "attribute_name", data, ["access_mode"]);                 | Optional argument: "append" or "overwrite" "append": The attribute named "attribute_name" is added to a group or dataset named "location_name" in the HDF5 file "filename" if the attribute does not exist yet. Otherwise, it is overwritten. This command creates a HDF5 file named “filename” if it does not exist. If there is no group or dataset named “location_name”, a new group called “location_name” will be created. The "append" option is set by default. "overwrite": If the HDF5 file named "filename" already exists, the file is overwritten completely. Otherwise, it will be created. The file will only contain the group named "location_name" and the attribute named "attribute_name". |
| h5writeattr("filename", "location_name", "attribute_name", data, [{"datatype": "datatype_name"}]); | Optional argument. This struct indicates the data type in which the data is stored in the HDF5 file. Possible options: {“datatype”: “short”}: data is stored as short integers {“datatype”: “int”}: data is stored as integers {“datatype”: “long long”}: data is stored as long long integers {“datatype”: “double”}: data is stored as doubles The data struct is not applicable to string values. In that case, the command will throw an error.                                                                                                                                                                                                                                                            |

| **Parameter**                 | **Type**      | **Description**                                                                                                                                                                                                                                                     |
| ----------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filename                      | string        | Name of the HDF5 file.                                                                                                                                                                                                                                              |
| location_name                 | string        | Name of a group or dataset.                                                                                                                                                                                                                                         |
| attribute_name                | string        | Name of the attribute.                                                                                                                                                                                                                                              |
| data                          | matrix/string | Real/ complex matrix or string.                                                                                                                                                                                                                                     |
| access_mode                   | string        | Optional argument. Only the strings "append" and "overwrite" are valid options.                                                                                                                                                                                     |
| {"datatype": "datatype_name"} | struct        | Optional argument. Not available for string values. If given, the string “datatype” is a mandatory field in the struct. The field can only have the string values “short”, “int”, “long long”, and “double”. The latter is the default data type for matrix values. |

**Example**

Write a real matrix as an attribute to a group within an HDF5 file by firstly using the
default data type and secondly the integer data type.

```
a = [1, 2, pi; 4, 5, 2*pi];
h5writeattr("testfile.h5", "test_group", "double_matrix", a);
h5writeattr("testfile.h5", "test_group", "int_matrix", a, {"datatype":"int"});
```

Reading the data using [ h5readattr ](./h5readattr.md) gives the following results.

```
?h5readattr("testfile.h5", "/test_group", "double_matrix");
result:
1  2  3.14159
4  5  6.28319

?h5readattr("testfile.h5", "/test_group", "int_matrix");
result:
1  2  3
4  5  6
```

Overwrite the existing HDF5 file by replacing the existing data with a group "new_group"
containing the attribute "vector".

```
b = [2, 3, 5, 7, 11, 13];
h5writeattr("testfile.h5", "new_group", "vector", b, "overwrite");
```

Applying
[ h5info ](https://optics.ansys.com/hc/en-us/articles/360034927413-h5info-Script-command)
and [ h5readattr ](./h5readattr.md) to the HDF5 file shows a single group with a single
attributes. The attribute contains the given 1D real matrix.

```
info = h5info("testfile.h5");
?info.Groups;
Cell array with 1 elements

info.Groups{1}.Attributes;
Cell array with 1 elements
?h5readattr("testfile.h5", "/new_group", "vector");
result: 
2  3  5  7  11  13
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ h5write ](https://optics.ansys.com/hc/en-us/articles/19055251802899) ,
[ h5info ](./h5info.md) , [ h5read ](./h5read.md) , [ h5readattr ](./h5readattr.md) ,
[ Reading HDF5 files ](https://optics.ansys.com/hc/en-us/articles/360034936913-HDF5-files)
