<!--
Translation from English documentation
Original command: adddgtdsolver
Translation date: 2026-02-03 21:21:22
-->

# adddgtdsolver

向仿真环境中添加一个 [DGTD 求解器区域](/hc/en-us/articles/360034397874)。

**Syntax** |  **Description**  
---|---  
adddgtdsolver; |  向仿真环境中添加一个 DGTD 求解器区域。此函数不返回任何数据。  
adddgtdsolver(struct_data); |  添加一个 DGTD 求解器区域，并使用包含“属性”和值对的结构体设置其属性。有关示例，请参阅 [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) 脚本命令页面。此函数不返回任何数据。  
  
**示例 1**

以下脚本命令将向对象树中添加一个 DGTD 求解器，并打印其所有属性的名称。
    
    
    adddgtdsolver;
    ?set;

**示例 2**

以下脚本命令将添加一个 DGTD 求解器区域，将其分配给仿真区域，并设置仿真时间。
    
    
    adddgtdsolver;
    set("solver geometry","simulation region 1"); 
    set("simulation time",100e-15);  # 100 fs

**参见**

- [adddgtdmesh](./adddgtdmesh.md)
