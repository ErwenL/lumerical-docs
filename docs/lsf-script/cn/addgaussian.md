<!--
Translation from English documentation
Original command: addgaussian
Translation date: 2026-02-04 22:49:29
-->

# addgaussian

添加 一个 [Gaussian 源](/hc/en-us/articles/360034382854) 到 该 仿真 环境.

**语法** |  **描述**  
---|---  
addgaussian; |  添加 一个 Gaussian 源 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addgaussian(struct_data); |  Adds a Gaussian source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 Gaussian 源 在 该 仿真 环境 该 将 propagate 在 该 negative z direction. The 脚本 将 设置 该 维度 (和 position) 的 该 源 和 将 define 该 beam waist radius 使用 scalar approximation.
    
    
    addgaussian;
    设置("injection axis","z");
    设置("direction","backward");
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("y跨度",5e-6);
    设置("z",10e-6);
    设置("use scalar approximation",1);
    设置("waist radius w0",0.5e-6);
    设置("distance 从 waist",-5e-6);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ addplane ](/hc/en-us/articles/360034924413-addplane) , [ addtfsf ](/hc/en-us/articles/360034404454-addtfsf)
