<!--
Translation from English documentation
Original command: addpml
Translation date: 2026-02-04 22:49:29
-->

# addpml

添加 一个 PML (perfectly matched layer) 边界条件 对象 到 该 DGTD 或 FEEM 求解器 在 Finite Element IDE. At least, one 的 这些 solvers 应该 为 present 在 该 Objects Tree 用于 此 命令 到 work.

**语法** |  **描述**  
---|---  
addpml; |  添加 一个 PML 边界条件 到 该 DGTD 或 FEEM 求解器. Use only 当 there 是 一个 single 求解器 在 该 Object Tree. This 函数 does not 返回 any 数据.  
addpml("DGTD"); addpml("FEEM"); |  When there 是 both DGTD 和 FEEM 在 该 Object Tree, you need 到 specify 该 求解器.  
  
**示例 1:**

The following 脚本 commands 将 添加 一个 PML 边界条件 到 该 'DGTD' 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 边界条件.
    
    
    addpml;
    ?设置;

NOTE: When there 是 both DGTD 和 FEEM solvers 在 该 Object Tree, running 该 脚本 without any "求解器" 参数 将 produce 该 following error:  
---  
  
**示例 2**

The following 脚本 commands 将 添加 一个 PML 边界条件 到 该 'DGTD' 求解器, name it, 和 设置 该 值 用于 sigma 和 alpha.
    
    
    adddgtdsolver;
    addpml({"name":"simple_pml", "sigma":5});

NOTE:  The PML 边界条件 automatically 获取 applied 到 该 shell regions 在 该 对应的 仿真 region.  
---  
  
**参见**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver) , [ addpmc ](/hc/en-us/articles/360034924913-addpmc) , [ addpec ](/hc/en-us/articles/360034924893-addpec) , [ addperiodic ](/hc/en-us/articles/360034404934-addperiodic) , [ addabsorbing ](/hc/en-us/articles/360034924873-addabsorbing)
