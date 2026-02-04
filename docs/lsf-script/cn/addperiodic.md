<!--
Translation from English documentation
Original command: addperiodic
Translation date: 2026-02-04 09:09:45
-->

# addperiodic

向有限元IDE中的'DGTD'求解器添加周期性（或布洛赫）边界条件。此命令要求对象树中存在DGTD求解器区域。

**语法** |  **描述**  
---|---  
addperiodic; |  向'DGTD'求解器添加周期性边界条件。此函数不返回任何数据。  
   
**示例1**

以下脚本命令将向对象树中已存在的'DGTD'求解器添加周期性边界条件，并打印边界条件的所有可用属性。
    
    
    addperiodic;
    ?set;

**示例2**

以下脚本命令将向'DGTD'求解器的x方向添加周期性边界条件。
    
    
    addperiodic; 
    set("x periodic",1);

**参见**

* [adddgtdsolver](https://optics.ansys.com/hc/en-us/articles/360034925013-adddgtdsolver)
* [addpml](https://optics.ansys.com/hc/en-us/articles/360034404934-addperiodic)
* [addpmc](https://optics.ansys.com/hc/en-us/articles/360034924913-addpmc)
* [addpec](https://optics.ansys.com/hc/en-us/articles/360034924893-addpec)
* [addabsorbing](https://optics.ansys.com/hc/en-us/articles/360034924873-addabsorbing)
