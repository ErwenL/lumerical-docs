<!--
Translation from English documentation
Original command: addheatfluxmonitor
Translation date: 2026-02-04 22:49:29
-->

# addheatfluxmonitor

添加 一个 [heat flux 监视器](/hc/en-us/articles/360034398274) 到 该 HEAT 求解器 region. The 监视器 可以 only 为 added 如果 该 仿真 环境 already has 一个 'HEAT' 求解器 present.

**语法** |  **描述**  
---|---  
addheatfluxmonitor; |  添加 一个 heat flux 监视器 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addheatfluxmonitor(struct_data); |  Adds a heat flux monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 2D y-normal heat flux 监视器 到 该 HEAT 求解器 region 和 设置 its 维度.
    
    
    addheatfluxmonitor;
    设置("name","heat");
    设置("监视器 类型",6);  # 2D y-normal
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("z",0);
    设置("z跨度",10e-6);

**参见**

[设置](/hc/en-us/articles/360034928773-设置), [ addtemperaturemonitor](/hc/en-us/articles/360034924333-addtemperaturemonitor)
