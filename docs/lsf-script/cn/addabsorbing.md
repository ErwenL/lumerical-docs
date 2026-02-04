<!--
Translation from English documentation
Original command: addabsorbing
Translation date: 2026-02-04
-->

# addabsorbing

向'DGTD'求解器添加吸收边界条件。对象树中必须存在DGTD求解器区域，此命令才能工作。

**语法** |  **描述**  
---|---  
addabsorbing; |  向'DGTD'求解器添加PML边界条件。此函数不返回任何数据。  
   
**示例 1**

以下脚本命令将向对象树中已存在的'DGTD'求解器添加吸收边界条件，并打印边界条件的所有可用属性。
    
    
    addabsorbing;
    ?set;

**示例 2**

以下脚本命令将向'DGTD'求解器添加吸收边界条件，为其命名，并将其分配到仿真区域的-z和+z边界。
    
    
    addabsorbing; 
    set("name","absorbing_z");
    set("surface type","simulation region");
    set("z min",1);
    set("z max",1);

**参见**

- [adddgtdsolver](./adddgtdsolver.md)
- [addpml](./addpml.md)
- [addpmc](./addpmc.md)
- [addpec](./addpec.md)
- [addperiodic](./addperiodic.md)
