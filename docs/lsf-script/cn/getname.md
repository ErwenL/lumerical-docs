<!--
Translation from English documentation
Original command: getname
Translation date: 2026-02-04 22:50:00
-->

# getname

The 脚本 命令 getname 是 used 到 获取 该 name 的 一个 datset. 

**语法** |  **描述**  
---|---  
?getname(一个);  |  返回 该 name 的 该 dataset 的 该 变量 一个.   
?一个.getname;  |  返回 该 name 的 该 dataset 的 该 变量 一个.   
  
**示例**

The following 是 一个 short example 在 该 we 创建 一个 矩阵 dataset named tt 和 assign it 到 变量 named T. Using 该 getname 脚本 命令 该 name 的 该 dataset 可以 为 obtained. 
    
    
    T = matrixdataset("tt"); 
    T.setname("test");
    ?getname(T);
    test
    ?T.getname;
    test

**参见**

[ setname ](/hc/en-us/articles/360034929353-setname) , [ Datasets ](/hc/en-us/articles/360034409554-Datasets)
