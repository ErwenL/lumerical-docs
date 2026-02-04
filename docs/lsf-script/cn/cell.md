<!--
Translation from English documentation
Original command: cell
Translation date: 2026-02-04 22:49:36
-->

# 单元格

创建 一个 单元格 数组 变量 使用 specified 数字 的 elements. The 单元格 数组 元素 可以 为 any 数据 类型, such as 矩阵, 字符串, 和 dataset.

Since Lumerical 2019b R4 version, users 可以 also declare 一个 单元格 通过 使用 该 braces 和 square brackets declaration method.

**语法** |  **描述**  
---|---  
一个 = {"一个", "b", 1, 2.3} |  创建 和 initializes 一个 单元格 数组.  
一个 = 单元格(n); |  创建 一个 单元格 数组 使用 n elements.  
一个{n} = "字符串"; |  添加 一个 字符串 到 该 specified 元素 的 该 单元格 数组.  
一个{n} = 矩阵(5,5); |  添加 一个 field 的 矩阵 的 5x5 到 该 specified 元素 的 该 单元格 数组.  
一个.append(值); |  Appends 一个 值 到 该 end 的 该 单元格 数组.  
一个.insert(值,index); |  Inserts 一个 值 at index, pushing all elements after 该 index back, 和 extending 该 单元格 数组 长度 通过 1. The index 必须 为 less than 或 equal 到 该 current 数组 长度, 否则 一个 error 将 为 thrown.  
一个.remove(index); |  Removes 一个 值 at 该 specified index, pulling all elements after 该 index forward, 和 shortening 该 数组 长度 通过 1. The index 必须 为 less than 或 equal 到 该 current 数组 长度, 否则 一个 error 将 为 thrown.  
一个.pop; |  Removes 和 返回 该 last 值 从 该 单元格 数组.  
一个.clear; |  Removes all items 从 该 单元格 数组.  
  
**示例**

A 单元格 可以 为 created 和 initialized quickly as follows:
    
    
    myCell = {"一个", "b", 1, 2.3};   
      
    # 单元格 使用 结构体  
    myCellWithStruct = {"一个", {"b" : 2, "c" : 3}};

The above 单元格 可以 also 为 declared more pedantically:
    
    
    myCell = 单元格(4);  
    myCell{1} = "一个";  
    myCell{2} = "b";  
    myCell{3} = 1;  
    myCell{4} = 2.3;  
    
    # 单元格 使用 结构体  
    myCellWithStruct = 单元格(2);  
    myCellWithStruct{1} = "一个";  
    myCellWithStruct{2} = 结构体;  
    myCellWithStruct{2}.b = 2;  
    myCellWithStruct{2}.c = 3;

The above declaration methods 是 equivalent 和 将 produce 该 same output:
    
    
    ?myCell;  
    Cell 数组 使用 4 elements  
    
    ?myCell{1};  
    一个  
    
    ?myCellWithStruct;  
    Cell 数组 使用 2 elements  
    
    ?myCellWithStruct{1};  
    一个  
    
    ?myCellWithStruct{2};  
    Struct 使用 fields:  
    b  
    c  
    
    ?myCellWithStruct{2}.b;  
    result:   
    2  

Items 可以 为 added, removed, 和 appended 从 该 单元格 数组 使用 数组 functions:
    
    
    myCell.append(“c”); #Append “c” 到 该 end 的 该 单元格 数组  
    ?myCell{5}; #The 数组 将 为 {“一个”,”b”,1,2.3,”c”} after append  
    result:  
    c  
    ?myCell;  
    Cell 数组 使用 5 elements  
      
    myCell.insert(2,矩阵(2,2)); #添加 一个 2x2 矩阵 filled 使用 zeroes at index 2  
      
    ?myCell{2}; #The 数组 将 为 {“一个”, 矩阵(2,2), ”b” ,1,2.3,”c”} after insertion  
    0 0   
    0 0   
      
    myCell.remove(2); #Remove 该 newly added 矩阵 at index 2  
    ?myCell(2); #The 数组 将 为 {“一个”,”b”,1,2.3,”c”} after removal  
    b  
      
    ?myCell;  
    Cell 数组 使用 5 elements  
      
    popped = myCell.pop; #Remove 该 last 元素 (“c”) 和 assign it 到 新的 变量 “popped”  
    ?myCell;  
    Cell 数组 使用 4 elements  
    ?popped;  
    c  
      
    myCell.clear; #Clear all elements 的 单元格 数组  
    ?myCell;  
    Cell 数组 使用 0 elements

When two 或 more 对象 have similar 属性, such as spatial location 的 "x" 和 "y", one 可以 define 一个 "单元格" 使用 "x" 和 "y", 和 获取 their 值:
    
    
        propxy = {"x","y"};  
        out1 = getnamed("rectangle",propxy);  
        out2 = getnamed("监视器",propxy);  
        ?out1.x;  
        ?out2.y; 

In 该 above example, geometry "rectangle" 和 监视器 "监视器" both have "x" 和 "y" 属性.

**参见**

[Datasets](/hc/en-us/articles/360034409554-Datasets), [matrixdataset](/hc/en-us/articles/360034409454-matrixdataset), [rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset), [结构体](/hc/en-us/articles/360034409574-结构体), [splitstring](/hc/en-us/articles/360034926093-splitstring)
