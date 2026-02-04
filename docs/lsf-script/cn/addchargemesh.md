<!--
Translation from English documentation
Original command: addchargemesh
Translation date: 2026-02-04 22:46:39
-->

# addchargemesh

添加 a [mesh constraint (override region)](/hc/en-us/articles/360034397994) to the 'CHARGE' 仿真. A CHARGE 求解器 region must be present in the 对象 tree for this 命令 to work.

**语法** |  **描述**  
---|---  
addchargemesh; |  添加 a mesh constraint to the 'CHARGE' 仿真 environment. This 函数 does not 返回 any 数据.  
addchargemesh(struct_data); |  Adds a mesh constraint and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 commands will 添加 a mesh constraint to the CHARGE 求解器 region in Finite Element IDE, name it, 设置 its dimension, and 设置 the maximum edge length for any 元素 within the volume.
    
    
    addchargesolver;
    addchargemesh;
    设置("name","mesh_SCR");
    # 设置 dimension
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("y跨度",5e-6);
    设置("z",0);
    设置("z跨度",10e-6);
    # restrict maximum edge length for elements
    设置("max edge length",5e-9);

**参见**

- [List of commands](../lsf-脚本-commands-alphabetical.md)
- [addchargesolver](./addchargesolver.md)
- [设置](./设置.md)
