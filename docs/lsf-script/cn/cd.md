<!--
Translation from English documentation
Original command: cd
Translation date: 2026-02-04 22:49:36
-->

# cd

Changes 该 directory. The directory 是 其中 该 文件 是 saved 通过 default. 

**语法** |  **描述**  
---|---  
cd;  |  Opens 一个 window 到 browse 到 一个 directory.  This 函数 does not 返回 any 数据.   
cd("directory");  |  Changes 该 working directory 到 "directory". Whenever you open 一个 fsp 文件 或 run 一个 脚本 文件, it 将 设置 该 working directory 到 该 directory 的 该 文件 opened.   
  
**示例**

Moves 到 该 subdirectory "数据". 
    
    
    ?pwd;
    C:\demo
    path=pwd;
    cd(path+"\数据");
    ?pwd;
    C:\demo\数据

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ pwd ](/hc/en-us/articles/360034931773-pwd)
