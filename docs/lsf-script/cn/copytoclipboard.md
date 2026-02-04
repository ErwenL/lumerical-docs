<!-- Translation completed: 2026-02-04 -->
<!-- Original command: copytoclipboard -->

# copytoclipboard

    current_file = currentfilename;
    template_file = "C:\temp\myObjects.fsp";
    object_name = "my_grating";
    保存; #保存 current 文件; # 保存 current 文件
    加载(template_file);    # 加载 template 文件
    select(object_name);    # select object
    copytoclipboard;      # copy object to clipboard
    加载(current_file);     # 加载 original 文件
    pastefromclipboard;     # paste object into 文件

**语法** | **描述**
---|---
copytoclipboard; | Copies selected objects to the system clipboard

**示例**

This 示例 shows how to use the copy/paste to clipboard functions to copy an object from a different 仿真 文件 into the current 仿真 文件. 

This 示例 shows how to use the copy/paste to clipboard functions to copy an object from a different 仿真 文件 into the current 仿真 文件. 

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ pastefromclipboard ](/hc/en-us/articles/360034411314-pastefromclipboard) , [ copy ](/hc/en-us/articles/360034408434-copy)
