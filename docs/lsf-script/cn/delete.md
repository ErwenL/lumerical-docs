<!--
Translation from English documentation
Original command: delete
Translation date: 2026-02-03 22:45:35
-->

# delete

删除选中的对象。

**Syntax** |  **Description**  
---|---  
delete;  |  删除选中的对象。此函数不返回任何数据。   
  
**示例**

创建一个对象然后删除它，仅作说明。
    
    
    addrect;
    set("name","substrate");
    select("substrate");
    delete;

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [groupscope](./groupscope.md)
