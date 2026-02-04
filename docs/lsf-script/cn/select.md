<!-- Translation completed: Tue Feb 03 2026 -->
<!-- Original: select -->

# select

在当前组范围内选择具有给定名称的对象。失败的 select 命令将产生与 unselectall 命令相同的结果。

**语法** |  **描述**  
---|---  
select("name");  |  在当前组范围内选择名称为"name"的对象。此函数不返回任何数据。  
select("group name::name");  |  选择名为"group name"的组中名称为"name"的所有对象。名为"group name"的组必须在当前组范围内。  
  
**示例**

添加两个对象并选择第一个对象进行其他设置。
    
    
    addrect;
    set("name","substrate");
    addring;
    select("substrate");

**另请参阅**

- [操作对象](./index.md)
- [groupscope](./groupscope.md)
- [unselectall](./unselectall.md)
