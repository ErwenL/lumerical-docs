# h5read

Reads data from an HDF5 file. The command supports a large number of dataset types such
as integer, float, double, string, compound, etc.

| **Syntax**                                 | **Description**                                                                       |
| ------------------------------------------ | ------------------------------------------------------------------------------------- |
| data = h5read("filename", "dataset_name"); | Reads data in the dataset named "dataset_name" within the HDF5 file named "filename." |

| **Parameter** | **Type** | **Description**                        |
| ------------- | -------- | -------------------------------------- |
| filename      | string   | name of the HDF5 file.                 |
| datasetname   | string   | name (path) of the dataset to be read. |

**Examples**

```
filename = "samplefile.h5";
info = h5info(filename);
dataset_name = info.Group{1}.Datasets{1}.Name;  # returns the name (path) of the first dataset in the first group
data = h5read(filename,dataset_name);
```

**See Also**

[ h5info ](./h5info.md) , [ h5readattr ](./h5readattr.md) ,
[ Reading HDF5 files ](https://optics.ansys.com/hc/en-us/articles/360034936913-HDF5-files)
