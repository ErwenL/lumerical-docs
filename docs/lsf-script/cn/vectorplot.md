<!-- Translation completed: 2026-02-04 -->
<!-- Original command: vectorplot -->

# vectorplot

**语法** | **描述**
---|---
vectorplot(E); | Creates a 向量 plot of the 数据集

**示例**

This 示例 will generate a 向量 plot of the 数据集 E.
    x = linspace(-1,1,10);
    y = x;
    z = x;
    X = meshgrid3dx(x,y,z);
    Y = meshgrid3dy(x,y,z);
    Z = meshgrid3dz(x,y,z);
    Ex = exp( -X^2-Y^2-Z^2);
    Ey = 0*Ex;
    Ez = 0*Ex;
    E = rectilineardataset("E",x,y,z);
    E.addattribute("E",Ex,Ey,Ez);
    vectorplot(E);
The following figure shows the 输出 of the the 示例 code.

This 示例 will generate a 向量 plot of the 数据集 E.
    x = linspace(-1,1,10);
    y = x;
    z = x;
    X = meshgrid3dx(x,y,z);
    Y = meshgrid3dy(x,y,z);
    Z = meshgrid3dz(x,y,z);
    Ex = exp( -X^2-Y^2-Z^2);
    Ey = 0*Ex;
    Ez = 0*Ex;
    E = rectilineardataset("E",x,y,z);
    E.addattribute("E",Ex,Ey,Ez);
    vectorplot(E);
The following figure shows the 输出 of the the 示例 code.

**另请参阅**

[ List of commands](/hc/en-us/articles/360037228834), [ plotxy](/hc/en-us/articles/360034931093-plotxy), [ legend](/hc/en-us/articles/360034931233-legend), [ image](/hc/en-us/articles/360034931253-image), [ closeall](/hc/en-us/articles/360034410594-closeall), [ setplot](/hc/en-us/articles/360034931293-setplot), [ exportfigure](/hc/en-us/articles/360034410574-exportfigure), [ plot ](/hc/en-us/articles/360034410474-plot)
