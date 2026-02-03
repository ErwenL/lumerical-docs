<!--
Translation from English documentation
Original command: h5info
Translation date: 2026-02-03 10:57:40
-->

# h5info

返回 HDF5 文件的结构信息。 

**Syntax** |  **Description**  
---|---  
info = h5info("filename");  |  返回一个结构体 "info"，其中包含名为 "filename" 的 HDF5 文件的结构信息。   
  
**参数** |  **类型** |  **描述**  
 ---|---  
 filename  |  string  |  HDF5 文件的名称。
  
**示例**
    
    
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

包含 HDF5 文件信息的结构体具有以下字段： 

**所属** |  **字段** |  **描述**  
---|---|---  
File  |  Attributes  |  包含文件属性列表的结构体。   
Datasets  |  包含文件中数据集列表的结构体。   
Datatypes  |  包含文件中数据类型列表的结构体。   
Filename  |  string containing the name of the file.   
Groups  |  structure containing a list of the top-level groups.   
Name  |  string containing the path to the root. The value is always "/".   
Groups  |  Attributes  |  structure containing a list of the attributes of the group.   
Datasets  |  structure containing a list of the datasets in the group.   
Datatypes  |  structure containing a list of the datatypes in the group.   
Groups  |  structure containing a list of the sub-groups within the group.   
Name  |  string containing the name (path) of the group.   
Datasets  |  Attributes  |  structure containing a list of the attributes of the dataset.   
Dataspace  |  structure containing information about the size of the dataset.   
Datatype  |  structure containing information about the dataset type.   
Name  |  string containing the name (path) of the dataset.   
Propertylist  |  structure containing various properties of the dataset such as fill value, filter, etc.   
Datatypes  |  Class  |  string containing the HDF5 class of the datatype.   
Name  |  string containing the name of the datatype.   
Size  |  size of the datatype in bytes.   
Type  |  string describing the type of the datatype.   
  
**See Also**

[ h5read ](/hc/en-us/articles/360034407214-h5read) , [ h5readattr ](/hc/en-us/articles/360034927433-h5readattr) , [ Reading HDF5 files ](/hc/en-us/articles/360034936913-HDF5-files)
