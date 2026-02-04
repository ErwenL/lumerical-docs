<!--
Translation from English documentation
Original command: addimplant
Translation date: 2026-02-04 22:49:29
-->

# addimplant

添加 一个 implant doping region 到 该 仿真 环境. This 命令 需要 一个 CHARGE 求解器 region 到 为 present 在 该 对象 tree.

**语法** |  **描述**  
---|---  
adddimplant; |  添加 一个 implant doping region 在 该 仿真 环境. This 函数 does not 返回 any 数据.  
adddimplant(struct_data); |  Adds a implant doping region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 n-类型 implant doping 对象 和 设置 its 属性. The implantation direction 是 defined 通过 该 "surface normal" 属性 和 该 peak doping 是 defined 通过 该 "peak concentration" 属性.
    
    
    addimplant;
    设置("name","nwell");
    # 设置 维度
    V=[-0.5,-0.5;0.5,-0.5;0.5,0.5;-0.5,0.5]*1e-6; # SI unit (m)
    设置("vertices",V);
    # 设置 doping profile
    设置("dopant 类型","n");
    设置("surface normal","y"); 
    设置("源 theta",45);
    设置("源 phi",90);
    设置("distribution 函数","Pearson4");
    设置("peak concentration",1e24);  # SI unit (1/m3), equivalent 到 1e18 1/cm3

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ adddope ](/hc/en-us/articles/360034404594-adddope) ,
