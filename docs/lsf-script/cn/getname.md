<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getname -->

# getname

**语法** | **描述**
---|---
?getname(a); | 返回 the name of the 数据集 of the 变量 a.
?a.getname; | 返回 the name of the 数据集 of the 变量 a.

**示例**

The following is a short 示例 in which we create a 矩阵 数据集 named tt and assign it to 变量 named T. Using the getname 脚本 命令 the name of the 数据集 can be obtained. 
    T = matrixdataset("tt"); 
    T.setname("test");
    ?getname(T);
    test
    ?T.getname;
    test

The following is a short 示例 in which we create a 矩阵 数据集 named tt and assign it to 变量 named T. Using the getname 脚本 命令 the name of the 数据集 can be obtained. 
    T = matrixdataset("tt"); 
    T.setname("test");
    ?getname(T);
    test
    ?T.getname;
    test

**另请参阅**

[ setname ](/hc/en-us/articles/360034929353-setname) , [ Datasets ](/hc/en-us/articles/360034409554-Datasets)
