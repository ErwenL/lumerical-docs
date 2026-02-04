<!-- Translation completed: 2026-02-04 -->
<!-- Original command: cd -->

# cd

**语法** | **描述**
---|---
cd; | Opens a window to browse to a 目录.  This 函数 does not 返回 any data.
cd("directory"); | Changes the working 目录 to "目录". Whenever you open an fsp 文件 or run a 脚本 文件, it will set the working 目录 to the 目录 of the 文件 opened.

**示例**

Moves to the subdirectory "data". 
    ?pwd;
    C:\demo
    路径=pwd;
    cd(路径+"\data");
    ?pwd;
    C:\demo\data

Moves to the subdirectory "data". 
    ?pwd;
    C:\demo
    路径=pwd;
    cd(路径+"\data");
    ?pwd;
    C:\demo\data

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ pwd ](/hc/en-us/articles/360034931773-pwd)
