<!--
Translation from English documentation
Original command: addsurfacerecombinationbc
Translation date: 2026-02-04 22:49:30
-->

# addsurfacerecombinationbc

添加 一个 新的 surface recombination 边界条件 到 该 CHARGE 求解器 [[Boundary Conditions (Electrical Simulation)](/hc/en-us/articles/360034918833-Boundary-Conditions-Electrical-Simulation-)]. A CHARGE 求解器 region 必须 为 present 在 该 对象 tree before 一个 surface recombination 边界条件 可以 为 added.

**语法** |  **描述**  
---|---  
addsurfacerecombinationbc; |  添加 一个 新的 surface recombination 边界条件 到 该 CHARGE 求解器. This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 surface recombination 边界条件 到 该 CHARGE 求解器 (already present 在 该 对象 tree) 和 print all available 属性 的 该 边界条件.
    
    
    addsurfacerecombinationbc;  
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 surface recombination 边界条件 到 该 existing CHARGE 求解器 和 assign it 到 该 interface (surfaces) between silicon 和 silicon dioxide. It 将 设置 该 surface recombination velocity 的 electrons 和 holes 到 100 cm/sec.
    
    
    addsurfacerecombinationbc;  
    
    设置("name","Si_SiO2");  
    设置("surface 类型","材料:材料");  
    设置("材料 1","Si (Silicon)");  
    设置("材料 2","SiO2 (Glass) - Sze");  
    设置("electron velocity",100e-2);   # m/sec  
    设置("hole velocity",100e-2);   # m/sec  
    设置("apply 到 majority carriers",1);

The "apply 到 majority carriers" option 应该 为 enabled 当 modeling surface recombination at semiconductor-oxide 或 semiconductor-semiconductor interfaces.

NOTE: The 'materials' folder 在 该 对象 tree 必须 already contain 该 materials used 在 该 脚本 commands 到 设置 up 该 边界条件.  
---  
  
**示例 3**

The following 脚本 commands 将 添加 一个 surface recombination 边界条件 到 该 interface (surfaces) between silicon 和 aluminum. It 将 设置 该 surface recombination velocity 的 electrons 和 holes 到 1e7 cm/sec.
    
    
    addsurfacerecombinationbc;  
    
    设置("name","Si_Al");  
    设置("surface 类型","材料:材料");  
    设置("材料 1","Si (Silicon)");  
    设置("材料 2","Al (Aluminium) - CRC");  
    设置("electron velocity",1e5);   # m/sec  
    设置("hole velocity",1e5);   # m/sec  
    设置("apply 到 majority carriers",0);

The "apply 到 majority carriers" option 应该 为 disabled 当 modeling surface recombination at semiconductor-metal interfaces.

**参见**

[addelectricalcontact](/hc/en-us/articles/360034404794-addelectricalcontact), [addmodelmaterial](/hc/en-us/articles/360034404974-addmodelmaterial)
