<!--
Translation from English documentation
Original command: addeme
Translation date: 2026-02-04 22:49:04
-->

# addeme

添加 一个 [Eigenmode Expansion (EME) 求解器 region](/hc/en-us/articles/360034917013) 到 该 MODE 仿真 环境.

**语法** |  **描述**  
---|---  
addeme; |  添加 一个 EME 求解器 region 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addeme(struct_data); |  Adds an EME solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 EME 求解器 region, 设置 its 维度 和 other 属性, 和 run 该 仿真. The 脚本 assumes 该 该 仿真 环境 already has 该 geometry 设置 up.
    
    
    addeme;
    # 设置 维度
    设置("x最小值",-8e-6);
    设置("y",0);
    设置("y跨度",5.5e-6);
    设置("z",0.5e-6);
    设置("z跨度",7e-6);
    # 设置 单元格 属性
    设置("数字 的 单元格 groups",3);
    设置("group spans",[3e-6; 10e-6; 3e-6]);
    设置("cells",[1; 19; 1]);
    设置("subcell method",[0; 1; 0]);   # 0 = none,  1 = CVCS
    # 设置 up ports: 端口 1
    select("EME::Ports::port_1");
    设置("use full 仿真 span",1);
    设置("y",0);
    设置("y跨度",5.5e-6);
    设置("z",0);
    设置("z跨度",7e-6);
    设置("mode selection","fundamental mode");
    # 设置 up ports: 端口 2
    select("EME::Ports::port_2");
    设置("use full 仿真 span",1);
    设置("y",0);
    设置("y跨度",5.5e-6);
    设置("z",0);
    设置("z跨度",7e-6);
    设置("mode selection","fundamental mode");
    run;

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ select ](/hc/en-us/articles/360034928593-select) , [ run ](/hc/en-us/articles/360034931333-run) , [ addvarfdtd ](/hc/en-us/articles/360034924193-addvarfdtd) , [ addfde ](/hc/en-us/articles/360034404294-addfde)
