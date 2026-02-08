# h5info

Returns information about the structure of an HDF5 file.

| **Syntax**                 | **Description**                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------- |
| info = h5info("filename"); | Returns a struct "info" that contains information about the structure of the HDF5 file named "filename." |

| **Parameter** | **Type** | **Description**        |
| ------------- | -------- | ---------------------- |
| filename      | string   | name of the HDF5 file. |

**Examples**

```
filename = "samplefile.h5";
info = h5info(filename);
?info;
> Struct with fields:
> Attributes
> Datasets
> Datatypes
> FileName
> Groups
> Name
```

The struct containing the information about the HDF5 file has the following fields:

| **Belongs to** | **Field**                                                                               | **Description**                                               |
| -------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| File           | Attributes                                                                              | structure containing a list of the attributes of the file.    |
| Datasets       | structure containing a list of the datasets in the file.                                |                                                               |
| Datatypes      | structure containing a list of the datatypes in the file.                               |                                                               |
| Filename       | string containing the name of the file.                                                 |                                                               |
| Groups         | structure containing a list of the top-level groups.                                    |                                                               |
| Name           | string containing the path to the root. The value is always "/".                        |                                                               |
| Groups         | Attributes                                                                              | structure containing a list of the attributes of the group.   |
| Datasets       | structure containing a list of the datasets in the group.                               |                                                               |
| Datatypes      | structure containing a list of the datatypes in the group.                              |                                                               |
| Groups         | structure containing a list of the sub-groups within the group.                         |                                                               |
| Name           | string containing the name (path) of the group.                                         |                                                               |
| Datasets       | Attributes                                                                              | structure containing a list of the attributes of the dataset. |
| Dataspace      | structure containing information about the size of the dataset.                         |                                                               |
| Datatype       | structure containing information about the dataset type.                                |                                                               |
| Name           | string containing the name (path) of the dataset.                                       |                                                               |
| Propertylist   | structure containing various properties of the dataset such as fill value, filter, etc. |                                                               |
| Datatypes      | Class                                                                                   | string containing the HDF5 class of the datatype.             |
| Name           | string containing the name of the datatype.                                             |                                                               |
| Size           | size of the datatype in bytes.                                                          |                                                               |
| Type           | string describing the type of the datatype.                                             |                                                               |

**See Also**

[ h5read ](./h5read.md) , [ h5readattr ](./h5readattr.md) ,
[ Reading HDF5 files ](https://optics.ansys.com/hc/en-us/articles/360034936913-HDF5-files)
