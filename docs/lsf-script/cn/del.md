<!--
Translation from English documentation
Original command: del
Translation date: 2026-02-03 22:40:51
-->

# del

删除文件。可以指定路径。

**Syntax** |  **Description**  
---|---  
del("filename"); rm("filename"); |  删除文件"filename"。此函数不返回任何数据。  
  
**注意**：在[安全模式](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode")下无法使用此命令。

**示例**

删除文件。
    
    
    del("project_name.fsp") # deletes the file in the current working directory
    del("C:\Downloads\project_name.fsp") # deletes the file in a path specified

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [delete](./delete.md)
- [rm](./rm.md)
