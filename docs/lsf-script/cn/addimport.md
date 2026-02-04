<!--
Translation from English documentation
Original command: addimport
Translation date: 2026-02-04 00:26:54
-->

# addimport

向仿真环境添加一个导入图元。导入图元可用于通过导入表面、图像或二进制数据来创建3D几何形状。它也可用于创建n,k材料。

**Syntax** |  **Description**  
---|---  
addimport; |  向仿真环境添加导入图元。此函数不返回任何数据。  
addimport(struct_data); |  添加导入图元，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将生成表面数据，然后使用该数据创建一层玻璃，其顶面由生成的数据定义。
    
    
    # generate a surface
    nx = 50;
    ny = 40;
    x = linspace(-6,6,nx);
    y = linspace(-5,5,ny);
    X = meshgridx(x,y);
    Y = meshgridy(x,y);
    Z = exp(-(X^2+Y^2)/4^2) * sin(pi*Y/2);
    # Remember that all units are SI. We defined the surface in microns
    # so all lengths must be multiplied by 1e-6
    x = x*1e-6; # switch to SI units
    y = y*1e-6; # switch to SI units
    Z = Z*1e-6; # switch to SI units
    # create substrate layer with an import object
    addimport;
    set("material","SiO2 (Glass) - Palik");
    # upper surface and reference height
    importsurface2(Z,x,y,1);
    set("upper ref height",0e-6); 

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [importsurface](./importsurface.md)
- [importsurface2](./importsurface2.md)
