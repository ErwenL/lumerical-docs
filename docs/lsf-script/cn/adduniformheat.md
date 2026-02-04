<!--
Translation from English documentation
Original command: adduniformheat
Translation date: 2026-02-04 22:49:36
-->

# adduniformheat

添加 一个 constant heat 源 到 该 HEAT 求解器 region. The input 是 defined as 该 net heat input 到 该 volume 在 units 的 Watt. The uniform heat 源 可以 either 为 2D 或 3D. The heat input per unit volume (W/m  3  ) 是 calculated 通过 dividing 该 net input power 通过 该 volume 的 该 (3D) 源. In 该 case 的 一个 2D 源 该 volume 的 该 源 是 defined 通过 setting 该 长度 在 该 third 维度 equal 到 either 该 "equivalent 长度" 的 该 源 或 该 "norm 长度" 的 该 HEAT 求解器.

**语法** |  **描述**  
---|---  
adduniformheat; |  添加 一个 constant heat 源 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
adduniformheat(struct_data); |  Adds a constant heat source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 添加 一个 3D uniform heat 源 到 该 HEAT 求解器, 设置 its 维度, 和 assigns 一个 net input power.
    
    
    adduniformheat;  # 该 dafult format 的 一个 newly created heat 源 是 3D  
    
    设置("x",0);  
    设置("x跨度",2e-6);  
    设置("y",0);  
    设置("y跨度",5e-6);  
    设置("z",0);  
    设置("z跨度",10e-6);  
    设置("total power",1e-4);  #  Pin = 0.1 mW

The following 脚本 添加 一个 2D y-normal uniform heat 源 到 该 HEAT 求解器, 设置 its 维度, forces 该 长度 在 该 third 维度 到 为 equal 到 该 "norm 长度" 的 该 HEAT 求解器, 和 assigns 一个 net input power.
    
    
    adduniformheat;    
    
    设置("源 类型",2);  # 2D y-normal  
    设置("use 求解器 norm 长度",1);  
    设置("x",0);  
    设置("x跨度",2e-6);  
    设置("y",0);  
    设置("z",0);  
    设置("z跨度",10e-6);  
    设置("total power",1e-4);  #  Pin = 0.1 mW

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ addimportheat ](/hc/en-us/articles/360034404394-addimportheat)
