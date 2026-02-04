<!--
Translation from English documentation
Original command: readdata
Translation date: 2026-02-04 22:50:14
-->

# readdata

Reads 一个 文件 使用 数据 在 一个 row/column format. User 可以 import numerical 值 stored 在 text files 使用 该 readdata 命令. The 数据 必须 为 correctly formatted so each row has 该 same 数字 的 columns. Readdata 将 ignore any line 该 begins 使用 一个 letter. The supported 文件 format 是  ASCII. 

**语法** |  **描述**  
---|---  
M=readdata("文件名.txt");  |  Will load 该 text 文件 文件名 into 矩阵 变量 M. Any lines starting 使用 一个 letter 是 ignored.  注意: This 函数 将 check 用于 该 文件 在 该 current working directory. If 该 文件 到 read 从 是 在 一个 different directory, either specify 该 full path 或 change 该 current working directory.   
  
**示例**

If you have 一个 text 文件 called  testfile.txt  使用 该 following 数据: 

Time Value 

0.0 3.2e-6 

1.0 2.8e10 

2.0 4.1e5 

3.0 3.3 

The first rows contains 该 column headers, 和 该 next four rows contain 数据. In 此 case, readdata 将 ignore 该 first line, 和 import 该 数据 as 一个 4x2 矩阵. 
    
    
    M=readdata("testfile.txt");
    ?M;
    result: 
    0 3.2e-006 
    1 2.8e+010 
    2 4.1e+005 
    3 3.3 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ rm ](/hc/en-us/articles/360034931533-rm) , [ write ](/hc/en-us/articles/360034411134-write) , [ read ](/hc/en-us/articles/360034931933-read) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ fileexists ](/hc/en-us/articles/360034931633-fileexists)
