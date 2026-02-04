<!--
Translation from English documentation
Original command: addpmc
Translation date: 2026-02-04 09:11:33
-->

# addpmc

向有限元IDE中的DGTD或FEEM求解器添加PMC（完美磁导体）边界条件。此命令要求对象树中存在DGTD或FEEM求解器区域。如果两个求解器都存在，则必须将目标求解器的名称作为脚本命令的参数提供。

**语法** |  **描述**  
---|---  
addpmc; |  向对象树中存在的DGTD或FEEM求解器添加PMC边界条件。此函数不返回任何数据。  
addpmc("solver_name"); |  向参数"solver_name"定义的所需求解器添加PMC边界条件。选项为"DGTD"和"FEEM"。此函数不返回任何数据。  
   
**示例1**

以下脚本命令将向对象树中已存在的求解器添加PMC边界条件，并打印边界条件的所有可用属性。
    
    
    addpmc;
    ?set;

**示例2**

以下脚本命令将向DGTD求解器添加PMC边界条件，为其命名，并将其分配给仿真区域的-y和+y边界。
    
    
    addpmc("DGTD"); 
    set("name","PMC_y");
    set("surface type","simulation region");
    set("y min",1);
    set("y max",1);

**参见**

* [adddgtdsolver](https://optics.ansys.com/hc/en-us/articles/360034925013-adddgtdsolver)
* [addpml](https://optics.ansys.com/hc/en-us/articles/360034924913-addpmc)
* [addpec](https://optics.ansys.com/hc/en-us/articles/360034924893-addpec)
* [addperiodic](https://optics.ansys.com/hc/en-us/articles/360034404934-addperiodic)
* [addabsorbing](https://optics.ansys.com/hc/en-us/articles/360034924873-addabsorbing)
