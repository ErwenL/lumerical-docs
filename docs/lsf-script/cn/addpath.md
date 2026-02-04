<!--
Translation from English documentation
Original command: addpath
Translation date: 2026-02-04 01:11:02
-->

# addpath

向路径中添加目录。

当脚本文件和仿真文件位于不同目录时，此命令会很有帮助。当前工作目录通常设置为仿真文件的位置。addpath可用于将脚本文件的位置添加到路径中，从而可以无需每次提供完整路径即可调用这些脚本。

**语法** |  **描述**  
---|---  
addpath("directory"); |  向路径中添加目录。此函数不返回任何数据。  
   
**示例**

向路径中添加第二个目录。
    
    
    ?getpath;
    ./  
    C:/Program Files/Lumerical/2020a/scripts
    addpath("C:/demo");
    ?getpath;
    ./  
    C:/Program Files/Lumerical/2020a/scripts  
    C:/demo

清除路径。
    
    
    clearpath;
    ?getpath;
    ./

**参见**

* [getpath](https://optics.ansys.com/hc/en-us/articles/360034411054-getpath)
* [which](https://optics.ansys.com/hc/en-us/articles/360034411094-which)
* [pwd](https://optics.ansys.com/hc/en-us/articles/360034931773-pwd)
* [clearpath](https://optics.ansys.com/hc/en-us/articles/360034931853-clearpath)
