<!--
Translation from English documentation
Original command: addpml
Translation date: 2026-02-04 09:12:00
-->

# addpml

向有限元IDE中的DGTD或FEEM求解器添加PML（完美匹配层）边界条件对象。此命令要求对象树中至少存在其中一个求解器。

**语法** |  **描述**  
---|---  
addpml; |  向DGTD或FEEM求解器添加PML边界条件。仅当对象树中存在单个求解器时使用。此函数不返回任何数据。  
addpml("DGTD"); addpml("FEEM"); |  当对象树中同时存在DGTD和FEEM时，需要指定求解器。  
   
**示例1：**

以下脚本命令将向对象树中已存在的'DGTD'求解器添加PML边界条件，并打印边界条件的所有可用属性。
    
    
    addpml;
    ?set;

**注意**：当对象树中同时存在DGTD和FEEM求解器时，不带任何"solver"参数运行脚本将产生以下错误：  
---  
   
**示例2**

以下脚本命令将向'DGTD'求解器添加PML边界条件，为其命名并设置sigma和alpha的值。
    
    
    adddgtdsolver;
    addpml({"name":"simple_pml", "sigma":5});

**注意**：PML边界条件会自动应用于相应仿真区域的外壳区域。  
---  
   
**参见**

* [adddgtdsolver](https://optics.ansys.com/hc/en-us/articles/360034925013-adddgtdsolver)
* [addpmc](https://optics.ansys.com/hc/en-us/articles/360034924913-addpmc)
* [addpec](https://optics.ansys.com/hc/en-us/articles/360034924893-addpec)
* [addperiodic](https://optics.ansys.com/hc/en-us/articles/360034404934-addperiodic)
* [addabsorbing](https://optics.ansys.com/hc/en-us/articles/360034924873-addabsorbing)
