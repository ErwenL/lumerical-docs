<!--
Translation 从 English documentation
Original 命令: adddiffusion
Translation date: 2026-02-04 23:30:37
-->

# adddiffusion

添加 一个 [diffusion doping region](/hc/en-us/articles/360034918673) 到 该 仿真 环境。 This 命令 需要 一个 CHARGE 求解器 region 到 为 present 在 该 对象 tree。

**语法** | **描述**
---|---
adddiffusion; | 添加 一个 diffusion doping region 在 该 仿真 环境。 This 函数 does not 返回any 数据。
adddiffusion(struct_data); |  Adds a diffusion doping region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  

**示例**

The following 脚本 命令 将 添加 一个 n-类型 diffusion doping 对象 和 设置 its 属性。 The face 其中 该 dopants 是 introduced 是 defined 通过 该 "源 face" 属性 和 该 peak doping 是 defined 通过 该 "concentration" 属性。 The "junction width" 属性 defines 该 distance over 该 该 doping drops 从 该 (peak) concentration 到 该 low "ref concentration" at 该 other faces 的 该 doping 对象。


    adddiffusion;
    设置("name","nwell");
    # 设置 dimensionset("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("y跨度",1e-6);
    设置("z",5e-6);
    设置("z跨度",1e-6);
    # 设置 doping profile
    设置("dopant 类型","n");
    设置("源 face",6);  # upper z
    设置("junction width",0.2e-6);
    设置("concentration",1e25);  # SI unit (/m3)

The figure below shows 该 resulting doping profile.

More information about the doping object itself, including the diffusion parameters can be found in [this article](https://support.lumerical.com/hc/en-us/articles/360034918673).

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ adddope ](/hc/en-us/articles/360034404594-adddope)
