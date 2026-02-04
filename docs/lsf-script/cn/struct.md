<!--
Translation from English documentation
Original command: struct
Translation date: 2026-02-04 22:50:15
-->

# 结构体

创建 一个 结构 数组. Any 数据 类型 (such as 矩阵, 字符串, dataset) 可以 为 added 到 结构 arrays.

Since Lumerical 2019b R4 version, users 可以 also declare 一个 结构 数组 通过 使用 该 braces declaration method.

**语法** |  **描述**  
---|---  
一个 = {"one" : "fish", "two" : "fish", "red" : "fish", "blue" : "fish"} |  创建 和 initializes 一个 结构 数组.  
一个 = 结构体; |  创建 一个 结构 数组.  
一个.一个 = "字符串"; |  添加 一个 字符串 field 到 该 结构 数组.  
一个.b = 矩阵(5,5); |  添加 一个 field 的 矩阵 的 5x5 到 该 结构 数组.  
  
**示例**

A 结构 可以 为 created 和 initialized quickly as follows:
    
    
    C = {"一个" : [1, 4, 9],  
         "b" : "一个 字符串",  
         "d" : 矩阵(5, 5),  
         "e" : getresult("监视器", "T")};

The above 结构 数组 可以 also 为 declared more pedantically:
    
    
    C = 结构体;  
    C.一个 = [1, 4, 9];   
    C.b = "一个 字符串";  
    C.d = 矩阵(5,5);   
    C.e = getresult("监视器","T");

Both 结构 arrays 是 equivalent 和 将 produce 该 same output:
    
    
    ?C;  
    Struct 使用 fields:  
    一个  
    b  
    d  
    e  
    
    ?C.一个;  
    result:   
    1 4 9   
      
    ?C.一个(2);  
    result:   
    4  
    
    ?C.b;  
    一个 字符串  
    
    ?C.d;  
    result:   
    0 0 0 0 0   
    0 0 0 0 0   
    0 0 0 0 0   
    0 0 0 0 0   
    0 0 0 0 0   
    
    ?C.e;  
    T vs lambda/f
    

When two 或 more 对象 share 该 same 参数, 一个 "结构体" 可以 为 used 用于 all 的 them:
    
    
        addrect;  
        props = 结构体;  
        props.x = 1e-6;  
        props.y = 2e-6;  
        setnamed("rectangle",props);  
        addprofile;  
        设置(props);

In 该 above example, both 该 geometry "rectangle" 和 该 profile 监视器 have 该 same x 和 y 值, so 该 "结构体" 使用 given "x,y" 可以 为 applied 到 them 在 setnamed 和/或 设置.

"结构体" 可以 also 为 used 到 设置 该 属性 directly
    
    
     addcircle( {"name":"c1","x": 1e-6,"y": 2e-6,"radius":0.5e-6});  
     mystruct = {"name":"c2","x":-1e-6,"y":-2e-6,"radius":0.5e-6};  
     addcircle(mystruct);

The above scripts 将 创建 two circles "c1" 和 "c2" located 在 quadrants I 和 III 使用 该 same radius.

**参见**

[Datasets](/hc/en-us/articles/360034409554-Datasets), [matrixdataset](/hc/en-us/articles/360034409454-matrixdataset), [rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset), [单元格](/hc/en-us/articles/360034929913-单元格), [isfield](/hc/en-us/articles/360034932293), [getfield](/hc/en-us/articles/360034411674), [setfield](/hc/en-us/articles/360034932313), [isstruct](/hc/en-us/articles/360034411654)
