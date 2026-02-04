<!--
Translation from English documentation
Original command: addfeemsolver
Translation date: 2026-02-03 23:47:46
-->

# addfeemsolver

向仿真环境中添加一个[FEEM求解器区域](/hc/en-us/articles/360034918393)。

**Syntax** |  **Description**  
---|---  
addfeemsolver; |  向仿真环境中添加一个FEEM求解器区域。此函数不返回任何数据。  
addfeemsolver(struct_data);  |  添加一个FEEM求解器区域，并使用包含"属性"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例1**

以下脚本命令将向对象树添加一个FEEM求解器，并打印其所有属性的名称。
    
    
    addfeemsolver;
    ?set;

**示例2**

以下脚本命令将添加一个FEEM求解器区域并将其分配给一个仿真区域。
    
    
    addfeemsolver;
    set("solver geometry","simulation region 1");

**参见**

- [addfeemmesh](./addfeemmesh.md)
