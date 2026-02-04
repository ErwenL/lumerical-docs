<!--
Translation from English documentation
Original command: vectorplot
Translation date: 2026-02-04 22:50:15
-->

# vectorplot

创建 一个 向量 plot 从 一个 rectilinear dataset. The rectilinear dataset 必须 为 一个 向量, like 该 E field, 和 it 必须 have no additional 参数 (i.e., 如果 you have E vs. x,y,z,f 和 f has two 或 more 值, 那么 该 命令 fails). Generally, it 是 easier 到 use visualize(E) 和 那么 select 该 向量 plot option 在 该 [visualizer](/hc/en-us/articles/360037222234).

**语法** |  **描述**  
---|---  
vectorplot(E); |  创建 一个 向量 plot 的 该 dataset  
  
**示例**

This example 将 generate 一个 向量 plot 的 该 dataset E.
    
    
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

The following figure shows 该 output 的 该 该 example code.

**参见**

[ List 的 commands](/hc/en-us/articles/360037228834), [ plotxy](/hc/en-us/articles/360034931093-plotxy), [ legend](/hc/en-us/articles/360034931233-legend), [ image](/hc/en-us/articles/360034931253-image), [ closeall](/hc/en-us/articles/360034410594-closeall), [ setplot](/hc/en-us/articles/360034931293-setplot), [ exportfigure](/hc/en-us/articles/360034410574-exportfigure), [ plot ](/hc/en-us/articles/360034410474-plot)
