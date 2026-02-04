<!--
Translation from English documentation
Original command: del
Translation date: 2026-02-04 22:49:48
-->

# del

Deletes 一个 文件. A path 可以 为 specified.

**语法** |  **描述**  
---|---  
del("文件名"); rm("文件名"); |  Deletes 该 文件 "文件名". This 函数 does not 返回 any 数据.  
  
**Note** : This command cannot be used while in [safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**示例**

Deletes 一个 文件.
    
    
    del("project_name.fsp") # deletes 该 文件 在 该 current working directory
    del("C:\Downloads\project_name.fsp") # deletes 该 文件 在 一个 path specified

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ delete ](/hc/en-us/articles/360034928573-delete) , [ rm ](/hc/en-us/articles/360034931533-rm)
