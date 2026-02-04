<!-- Translation completed: 2026-02-04 -->
<!-- Original command: cell -->

# cell

    myCellWithStruct = {"a", {"b" : 2, "c" : 3}};
The above cell can also be declared more pedantically:
    myCell = cell(4);  
    myCell{1} = "a";  
    myCell{2} = "b";  
    myCell{3} = 1;  
    myCell{4} = 2.3;  
    myCellWithStruct = cell(2);  
    myCellWithStruct{1} = "a";  
    myCellWithStruct{2} = struct;  
    myCellWithStruct{2}.b = 2;  
    myCellWithStruct{2}.c = 3;
The above declaration methods are equivalent 和 will produce the same 输出:
    ?myCell;  
    Cell 数组 with 4 元素  
    ?myCell{1};  
    a  
    ?myCellWithStruct;  
    Cell 数组 with 2 元素  
    ?myCellWithStruct{1};  
    a  
    ?myCellWithStruct{2};  
    Struct with fields:  
    b  
    c  
    ?myCellWithStruct{2}.b;  
    result:   
    2  
Items can be added, removed, 和 appended from the cell 数组 with 数组 functions:
    myCell.append(“c”); #Append “c” to the end of the cell 数组  
    ?myCell{5}; #The 数组 will be {“a”,”b”,1,2.3,”c”} after append  
    result:  
    c  
    ?myCell;  
    Cell 数组 with 5 元素  
    myCell.insert(2,矩阵(2,2)); #Add a 2x2 矩阵 filled with zeroes at index 2  
    ?myCell{2}; #The 数组 will be {“a”, 矩阵(2,2), ”b” ,1,2.3,”c”} after insertion  
    0 0   
    0 0   
    myCell.remove(2); #Remove the newly added 矩阵 at index 2  
    ?myCell(2); #The 数组 will be {“a”,”b”,1,2.3,”c”} after removal  
    b  
    ?myCell;  
    Cell 数组 with 5 元素  
    popped = myCell.pop; #Remove the last 元素 (“c”) 和 assign it to new 变量 “popped”  
    ?myCell;  
    Cell 数组 with 4 元素  
    ?popped;  
    c  
    myCell.clear; #Clear all 元素 of cell 数组  
    ?myCell;  
    Cell 数组 with 0 元素
When two or more objects have similar properties, such as spatial location of "x" 和 "y", one can define a "cell" with "x" 和 "y", 和 get their 值:
        propxy = {"x","y"};  
        out1 = getnamed("rectangle",propxy);  
        out2 = getnamed("监视器",propxy);  
        ?out1.x;  
        ?out2.y; 
In the above 示例, geometry "rectangle" 和 监视器 "监视器" both have "x" 和 "y" properties.

**语法** | **描述**
---|---
a = {"a", "b", 1, 2.3} | Creates and initializes a cell 数组.
a = cell(n); | Creates a cell 数组 with n 元素.
a{n} = "string"; | Adds a 字符串 to the specified 元素 of the cell 数组.
a{n} = matrix(5,5); | Adds a 场 of 矩阵 of 5x5 to the specified 元素 of the cell 数组.
a.append(value); | Appends a 值 to the end of the cell 数组.
a.insert(value,index); | Inserts a 值 at index, pushing all 元素 after the index back, and extending the cell 数组 长度 by 1. The index must be less than or equal to the current 数组 长度, else an error will be thrown.
a.remove(index); | Removes a 值 at the specified index, pulling all 元素 after the index forward, and shortening the 数组 长度 by 1. The index must be less than or equal to the current 数组 长度, else an error will be thrown.
a.pop; | Removes and 返回 the last 值 from the cell 数组.
a.clear; | Removes all items from the cell 数组.

**示例**

A cell can be created and initialized quickly as follows:
    myCell = {"a", "b", 1, 2.3};   

A cell can be created and initialized quickly as follows:
    myCell = {"a", "b", 1, 2.3};   

**另请参阅**

[Datasets](/hc/en-us/articles/360034409554-Datasets), [matrixdataset](/hc/en-us/articles/360034409454-matrixdataset), [rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset), [struct](/hc/en-us/articles/360034409574-struct), [splitstring](/hc/en-us/articles/360034926093-splitstring)
