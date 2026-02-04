<!--
Translation from English documentation
Original command: seteigensolver
Translation date: 2026-02-04 22:50:14
-->

# seteigensolver

Mode sources, mode expansion monitors, 和 ports 在 FDTD 和 MODE, 和 each individual 单元格 在 EME have embedded eigensolvers. This 脚本 命令 makes it possible 到 设置 该 属性 的 该 eigensolver without 使用 该 GUI.

Changing any 值 的 该 embedded eigensolver 使用 此 命令 将 automatically invalidate any existing mode 数据. This means 该 新的 updates based 在 overlap calculations 使用 previous modes 将 fail after 使用 此 命令. Therefore please call 此 命令 before making any calls 到 updatesourcemode 或 updatemodes.

**语法** |  **描述**  
---|---  
?seteigensolver; |  返回 一个 list 的 该 属性 的 该 embedded eigensolver  
seteigensolver("属性",值); |  This 将 设置 该 eigensolver 属性 的 该 currently 选中的 对象. Value 可以 为 一个 数字 或 字符串. This 函数 does not 返回 any 数据.  
  
**示例**

  1. Change 该 radius 的 curvature 用于 一个 mode expansion calculation, 和 计算 该 first 10 modes 该 可以 为 subsequently used 用于 mode expansion. Please open  ring_resonator2.lms  从 该 [ ring resonator example ](**%20to%20be%20defined%20**) 使用 该 varFDTD 求解器 在 MODE:


    
    
    select("expansion");
    
    
    seteigensolver("bent waveguide",true);
    seteigensolver("bend radius",10e-6);
    updatemodes(1:10);

2\. Change 该 数字 的 trial modes 用于 单元格 1 在 EME:
    
    
    select("EME::Cells::cell_1");  
    seteigensolver("数字 的 trial modes",25);

Also see 该 examples 在 该 [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) , 和 [ addport ](/hc/en-us/articles/360034924793-addport) 脚本 functions.

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ addmode ](/hc/en-us/articles/360034924353-addmode) , [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) , [ addport ](/hc/en-us/articles/360034924793-addport) , [ clearsourcedata ](/hc/en-us/articles/360034929093-clearsourcedata) , [ clearmodedata ](/hc/en-us/articles/360034408774-clearmodedata) , [ clearportmodedata ](/hc/en-us/articles/360034409194-clearportmodedata) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver) , [ updatemodes ](/hc/en-us/articles/360034929073-updatemodes) , [ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ updateportmodes ](/hc/en-us/articles/360034409174-updateportmodes)
