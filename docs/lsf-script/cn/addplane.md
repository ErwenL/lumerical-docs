<!--
Translation from English documentation
Original command: addplane
Translation date: 2026-02-04 22:49:29
-->

# addplane

# 

添加 一个 plane wave 源 到 该 仿真 环境.

## For FDTD 和 MODE

**语法** |  **描述**  
---|---  
addplane; |  添加 一个 plane wave 源 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addplane(struct_data); |  Adds a plane wave source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 plane wave 源 在 该 仿真 环境 该 将 propagate 在 该 negative z direction. The 脚本 将 设置 该 维度 (和 position) 的 该 源 和 将 define 该 频率 range.
    
    
    addplane;
    设置("injection axis","z");
    设置("direction","backward");
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("y跨度",5e-6);
    设置("z",3e-6);
    设置("波长 start",0.3e-6);
    设置("波长 stop",1.2e-6);

## For DGTD:

添加 一个 plane wave 源 到 该 'DGTD' 求解器 在 Finite Element IDE. A DGTD 求解器 region 必须 为 present 在 该 对象 tree 用于 此 命令 到 work.

**语法** |  **描述**  
---|---  
addplane; |  添加 一个 plane wave 源 到 该 'DGTD' 求解器. This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 plane wave 源 到 该 'DGTD' 求解器 already present 在 该 对象 tree 和 print 该 name 的 all 的 its 属性.
    
    
    addplane;?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 plane wave 源 到 该 'DGTD' 求解器, change its name, 和 设置 up its 属性. The 脚本 那么 设置 该 solid named "2D rectangle" as 该 injection surface.
    
    
    addplane; 
    设置("name","plane_wave");# 设置 该 propagation directionset("direction definition","axis");设置("direction","backward");设置("angle theta",30);设置("angle phi",60);
    # 设置 该 polarization angleset("polarization angle",90);
    # 设置 该 injection surfaceset("surface 类型","solid");设置("solid","2D rectangle");

### **参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ addplane ](/hc/en-us/articles/360034924413-addplane) , [ addgaussian ](/hc/en-us/articles/360034404434-addgaussian) , [ addtfsf ](/hc/en-us/articles/360034404454-addtfsf) , [ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver)
