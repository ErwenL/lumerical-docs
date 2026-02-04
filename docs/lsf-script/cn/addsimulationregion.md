<!--
Translation from English documentation
Original command: addsimulationregion
Translation date: 2026-02-04 22:49:30
-->

# addsimulationregion

添加 一个 仿真 region 到 该 Finite Element IDE design 环境. Once created 该 仿真 region 可以 为 linked 到 any existing 求解器.

**语法** |  **描述**  
---|---  
addsimulationregion; |  添加 一个 仿真 region 到 该 Finite Element IDE design 环境. This 函数 does not 返回 any 数据.  
addsimulationregion(struct_data); |  Adds a simulation region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 2D y-normal 仿真 region, rename it, 设置 its 维度, 和 assign it 到 该 CHARGE 求解器 (assuming 该 it already exists 在 该 对象 tree).
    
    
    addsimulationregion;
    设置("name","CHARGE 仿真 region");
    设置("维度",2);  # 2D y-normal
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("z",0);
    设置("z跨度",10e-6);
    setnamed("CHARGE","仿真 region","CHARGE 仿真 region");

**参见**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver)
