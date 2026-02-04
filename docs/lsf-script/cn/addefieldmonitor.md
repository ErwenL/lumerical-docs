<!--
Translation from English documentation
Original command: addefieldmonitor
Translation date: 2026-02-04 22:49:04
-->

# addefieldmonitor

添加 一个 [electric field 监视器](/hc/en-us/articles/360034918793) 到 该 仿真 环境. This 命令 需要 该 存在 的 一个 CHARGE 求解器 region 在 该 对象 tree.

**语法** |  **描述**  
---|---  
addefieldmonitor; |  添加 一个 electric field 监视器 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addefieldmonitor(struct_data); |  Adds an electric field monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 commands 将 添加 一个 2D y-normal electric field 监视器 到 该 仿真 环境, 设置 its 维度, 启用 保存 该 electrostatic potential, 和 save 该 数据 在 一个 .mat 文件.
    
    
    addefieldmonitor;
    设置("name","E_field");
    设置("监视器 类型",6);  # 2D y-normal
    设置("x",0);
    设置("x跨度",5e-6);
    设置("y",0);
    设置("z",0);
    设置("y跨度",5e-6);
    设置("record electrostatic potential",1);
    设置("save 数据",1);
    文件名 = "electric_field.mat";
    设置("文件名",文件名);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ addbandstructuremonitor ](/hc/en-us/articles/360034924653-addbandstructuremonitor) , [ addchargemonitor ](/hc/en-us/articles/360034924613-addchargemonitor) , [ addjfluxmonitor ](/hc/en-us/articles/360034924673-addjfluxmonitor)
