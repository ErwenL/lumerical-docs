<!--
Translation from English documentation
Original command: h5writeattr
Translation date: 2026-02-04 22:50:00
-->

# h5writeattr

Write 一个 矩阵 或 字符串 as 一个 attribute 的 一个 group 或 一个 dataset 到 一个 HDF5 文件.

**语法** |  **描述**  
---|---  
h5writeattr("文件名", "location_name", "attribute_name", 数据); |  创建 一个 attribute named "attribute_name" 到 一个 group 或 dataset named " location_name" within 一个 HDF5 文件 named "文件名" 从 该 given 数据. Will 创建 该 HDF5 文件 named "文件名" 如果 it does not exist. If there 是 no group 或 dataset called “location_name”, 一个 新的 group called “location_name” 将 为 created. If 该 attribute named "attribute_name" already exists 在 该 given group/dataset within 该 HDF5 文件, 该 attribute 将 为 overwritten. Otherwise, 该 attribute 是 simply added 到 该 existing group/dataset within 该 HDF5 文件.  
h5writeattr("文件名", "location_name", "attribute_name", 数据, ["access_mode"]); |  Optional 参数: "append" 或 "overwrite" "append": The attribute named "attribute_name" 是 added 到 一个 group 或 dataset named "location_name" 在 该 HDF5 文件 "文件名" 如果 该 attribute does not exist yet. Otherwise, it 是 overwritten. This 命令 创建 一个 HDF5 文件 named “文件名” 如果 it does not exist. If there 是 no group 或 dataset named “location_name”, 一个 新的 group called “location_name” 将 为 created. The "append" option 是 设置 通过 default. "overwrite": If 该 HDF5 文件 named "文件名" already exists, 该 文件 是 overwritten completely. Otherwise, it 将 为 created. The 文件 将 only contain 该 group named "location_name" 和 该 attribute named "attribute_name".  
h5writeattr("文件名", "location_name", "attribute_name", 数据, [{"datatype": "datatype_name"}]); |  Optional 参数. This 结构体 indicates 该 数据 类型 在 该 该 数据 是 stored 在 该 HDF5 文件. Possible options: {“datatype”: “short”}: 数据 是 stored as short integers {“datatype”: “int”}: 数据 是 stored as integers {“datatype”: “long long”}: 数据 是 stored as long long integers {“datatype”: “double”}: 数据 是 stored as doubles The 数据 结构体 是 not applicable 到 字符串 值. In 该 case, 该 命令 将 throw 一个 error.  
  
**Parameter** |  **Type** |  **描述**  
---|---|---  
文件名 |  字符串 |  Name 的 该 HDF5 文件.  
location_name |  字符串 |  Name 的 一个 group 或 dataset.  
attribute_name |  字符串 |  Name 的 该 attribute.  
数据 |  矩阵/字符串 |  Real/ complex 矩阵 或 字符串.  
access_mode |  字符串 |  Optional 参数. Only 该 strings "append" 和 "overwrite" 是 valid options.  
{"datatype": "datatype_name"} |  结构体 |  Optional 参数. Not available 用于 字符串 值. If given, 该 字符串 “datatype” 是 一个 mandatory field 在 该 结构体. The field 可以 only have 该 字符串 值 “short”, “int”, “long long”, 和 “double”. The latter 是 该 default 数据 类型 用于 矩阵 值.  
  
**示例**

Write 一个 real 矩阵 as 一个 attribute 到 一个 group within 一个 HDF5 文件 通过 firstly 使用 该 default 数据 类型 和 secondly 该 integer 数据 类型.
    
    
    一个 = [1, 2, pi; 4, 5, 2*pi];
    h5writeattr("testfile.h5", "test_group", "double_matrix", 一个);
    h5writeattr("testfile.h5", "test_group", "int_matrix", 一个, {"datatype":"int"});

Reading 该 数据 使用 [ h5readattr ](/hc/en-us/articles/360034927433-h5readattr) gives 该 following results.
    
    
    ?h5readattr("testfile.h5", "/test_group", "double_matrix");
    result:
    1  2  3.14159
    4  5  6.28319
    
    ?h5readattr("testfile.h5", "/test_group", "int_matrix");
    result:
    1  2  3
    4  5  6

Overwrite 该 existing HDF5 文件 通过 replacing 该 existing 数据 使用 一个 group "new_group" containing 该 attribute "向量".
    
    
    b = [2, 3, 5, 7, 11, 13];
    h5writeattr("testfile.h5", "new_group", "向量", b, "overwrite");

Applying [ h5info ](/hc/en-us/articles/360034927413-h5info-Script-命令) 和 [ h5readattr ](/hc/en-us/articles/360034927433-h5readattr) 到 该 HDF5 文件 shows 一个 single group 使用 一个 single attributes. The attribute contains 该 given 1D real 矩阵.
    
    
    info = h5info("testfile.h5");
    ?info.Groups;
    Cell 数组 使用 1 elements
    
    info.Groups{1}.Attributes;
    Cell 数组 使用 1 elements
    ?h5readattr("testfile.h5", "/new_group", "向量");
    result: 
    2  3  5  7  11  13

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ h5write ](/hc/en-us/articles/19055251802899) , [ h5info ](/hc/en-us/articles/360034927413-h5info) , [ h5read ](/hc/en-us/articles/360034407214-h5read) , [ h5readattr ](/hc/en-us/articles/360034927433-h5readattr) , [ Reading HDF5 files ](/hc/en-us/articles/360034936913-HDF5-files)
