<!-- Translation completed: 2026-02-04 -->
<!-- Original command: which -->

# which

**语法** | **描述**
---|---
out = which("filename"); | 返回 the pathname of the 文件 "文件名" as a 字符串.  Use ?which("文件名"); to display the result to the screen.

**示例**

Gets the full 路径 and 文件名 of the 文件 results.txt. 
    文件 = "results.txt";    # set 文件 name
    写入(文件,"my data 文件"); # create 文件
    ?fullPath = which(文件);   # get full name and 路径
     C:/Program Files/Lumerical/FDTD/scripts/results.txt

Gets the full 路径 and 文件名 of the 文件 results.txt. 
    文件 = "results.txt";    # set 文件 name
    写入(文件,"my data 文件"); # create 文件
    ?fullPath = which(文件);   # get full name and 路径
     C:/Program Files/Lumerical/FDTD/scripts/results.txt

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getpath ](/hc/en-us/articles/360034411054-getpath) , [ addpath ](/hc/en-us/articles/360034931833-addpath) , [ pwd ](/hc/en-us/articles/360034931773-pwd) , [ currentfilename ](/hc/en-us/articles/360034931793-currentfilename) , [ fileexists ](/hc/en-us/articles/360034931633-fileexists)
