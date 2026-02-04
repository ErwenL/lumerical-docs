<!--
Translation from English documentation
Original command: addimport
Translation date: 2026-02-04 22:49:29
-->

# addimport

添加 一个 import primitive 到 该 仿真 环境. The import primitive 可以 为 used 到 创建 一个 3D geometry 通过 importing 一个 surface, 一个 image, 或 binary 数据. It 可以 also 为 used 到 创建 一个 n,k 材料.

**语法** |  **描述**  
---|---  
addimport; |  添加 一个 import primitive 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addimport(struct_data); |  Adds an import primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 commands 将 generate 一个 surface 数据 和 那么 use 该 数据 到 创建 一个 layer 的 glass whose top surface 是 defined 通过 该 generated 数据.
    
    
    # generate 一个 surface
    nx = 50;
    ny = 40;
    x = linspace(-6,6,nx);
    y = linspace(-5,5,ny);
    X = meshgridx(x,y);
    Y = meshgridy(x,y);
    Z = exp(-(X^2+Y^2)/4^2) * sin(pi*Y/2);
    # Remember 该 all units 是 SI. We defined 该 surface 在 微米
    # so all lengths 必须 为 multiplied 通过 1e-6
    x = x*1e-6; # switch 到 SI units
    y = y*1e-6; # switch 到 SI units
    Z = Z*1e-6; # switch 到 SI units
    # 创建 substrate layer 使用 一个 import 对象
    addimport;
    设置("材料","SiO2 (Glass) - Palik");
    # upper surface 和 reference height
    importsurface2(Z,x,y,1);
    设置("upper ref height",0e-6); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ importsurface ](/hc/en-us/articles/360034408654-importsurface) , [ importsurface2 ](/hc/en-us/articles/360034928993-importsurface2)
