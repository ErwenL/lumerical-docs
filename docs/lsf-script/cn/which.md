<!--
Translation from English documentation
Original command: which
Translation date: 2026-02-04 22:50:31
-->

# 该

返回 该 full 文件 pathname 用于 该 specified 文件. 

This 函数 可以 为 helpful 当 you have added several directories 到 该 Lumerical path 变量 和 you want 到 check 该 files 是 being accessed. 

**语法** |  **描述**  
---|---  
out = 该("文件名");  |  返回 该 pathname 的 该 文件 "文件名" as 一个 字符串.  Use ?该("文件名"); 到 display 该 result 到 该 screen.   
  
**示例**

获取 该 full path 和 文件名 的 该 文件 results.txt. 
    
    
    文件 = "results.txt";    # 设置 文件 name
    write(文件,"my 数据 文件"); # 创建 文件
    ?fullPath = 该(文件);   # 获取 full name 和 path
     C:/Program Files/Lumerical/FDTD/scripts/results.txt

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ getpath ](/hc/en-us/articles/360034411054-getpath) , [ addpath ](/hc/en-us/articles/360034931833-addpath) , [ pwd ](/hc/en-us/articles/360034931773-pwd) , [ currentfilename ](/hc/en-us/articles/360034931793-currentfilename) , [ fileexists ](/hc/en-us/articles/360034931633-fileexists)
