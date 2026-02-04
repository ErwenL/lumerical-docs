<!--
Translation from English documentation
Original command: copytoclipboard
Translation date: 2026-02-04 22:49:48
-->

# copytoclipboard

Copies 该 选中的 对象 into 该 system clipboard. Equivalent 到 'Ctrl-C'. 

**语法** |  **描述**  
---|---  
copytoclipboard;  |  Copies 选中的 对象 到 该 system clipboard   
  
**示例**

This example shows 如何 到 use 该 copy/paste 到 clipboard functions 到 copy 一个 对象 从 一个 different 仿真 文件 into 该 current 仿真 文件. 
    
    
    # specify 文件 和 对象 names
    current_file = currentfilename;
    template_file = "C:\temp\myObjects.fsp";
    object_name = "my_grating";
    save; #save current 文件; # save current 文件
    load(template_file);    # load template 文件
    select(object_name);    # select 对象
    copytoclipboard;      # copy 对象 到 clipboard
    load(current_file);     # load original 文件
    pastefromclipboard;     # paste 对象 into 文件

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ pastefromclipboard ](/hc/en-us/articles/360034411314-pastefromclipboard) , [ copy ](/hc/en-us/articles/360034408434-copy)
