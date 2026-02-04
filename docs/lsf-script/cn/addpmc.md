<!--
Translation from English documentation
Original command: addpmc
Translation date: 2026-02-04 22:49:29
-->

# addpmc

添加 一个 PMC (perfect electrical conductor) 边界条件 到 该 DGTD 或 FEEM 求解器 在 Finite Element IDE. A DGTD 或 FEEM 求解器 region 必须 为 present 在 该 对象 tree 用于 此 命令 到 work. If both solvers 是 present 那么 该 intended 求解器's name 必须 为 provided as 一个 参数 到 该 脚本 命令.

**语法** |  **描述**  
---|---  
addpmc; |  添加 一个 PMC 边界条件 到 该 DGTD 或 FEEM 求解器 (whichever 是 present 在 该 对象 tree). This 函数 does not 返回 any 数据.  
addpmc("solver_name"); |  添加 一个 PMC 边界条件 到 该 desired 求解器 defined 通过 该 参数 "solver_name". The options 是 "DGTD" 和 "FEEM". This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 PMC 边界条件 到 该 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 边界条件.
    
    
    addpmc;
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 PMC 边界条件 到 该 DGTD 求解器, name it, 和 assign it 到 该 -y 和 +y boundaries 的 该 仿真 region.
    
    
    addpmc("DGTD"); 
    设置("name","PMC_y");
    设置("surface 类型","仿真 region");
    设置("y最小值",1);
    设置("y最大值",1);

**参见**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver) , [ addpml ](/hc/en-us/articles/360034924913-addpmc) , [ addpec ](/hc/en-us/articles/360034924893-addpec) , [ addperiodic ](/hc/en-us/articles/360034404934-addperiodic) , [ addabsorbing ](/hc/en-us/articles/360034924873-addabsorbing)
