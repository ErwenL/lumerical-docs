<!--
Translation Status: Completed
Source: docs/lsf-script/en/rm.md
Last Updated: 2026-02-03
-->

# rm

删除文件。可以指定路径。

**语法** |  **说明**  
---|---  
del("filename"); rm("filename"); |  删除文件"filename"。此函数不返回任何数据。  
  
**注意**：此命令不能在[安全模式](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode)下使用。

**示例**

删除文件。
    
    
    del("project_name.fsp") # 删除当前工作目录中的文件
    del("C:\Downloads\project_name.fsp") # 删除指定路径中的文件

**另请参见**

- [delete](./delete.md)
- [rm](./rm.md)
