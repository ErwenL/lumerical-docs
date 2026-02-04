<!--
Translation from English documentation
Original command: plot
Translation date: 2026-02-04 22:50:14
-->

# plot

创建 line plots. All 数据 设置 必须 为 sampled 在 该 same position 向量.

See  plotxy  用于 数据 设置 该 是 sampled 在 different position vectors.

**语法** |  **描述**  
---|---  
out = plot(x,y); |  创建 一个 plot 的 y vs x, y 和 x 是 both 1D vectors 使用 该 same 长度. The figure 数字 是 returned.  
plot(x,y); |  x 是 一个 nx1 矩阵. y 是 一个 nxm 矩阵. This 将 generate 一个 graph 使用 m lines. (y(1:n,1) vs x, y(1:n,2) vs x, etc)  
plot(x,y1,y2,y3); |  创建 一个 plot 使用 3 curves, x,y1, y2, y3 必须 为 该 same 长度, 返回 该 figure 数字.  
plot(x,y, "x label", "y label", "title"); |  创建 一个 plot 的 y vs x 使用 axis labels 和 一个 title, 返回 该 figure 数字.  
plot(x,y, "x label", "y label", "title", "options"); |  创建 一个 plot 使用 desired options. Options 是 listed 在 该 table below. 返回 该 figure 数字.  
  
Plot options. May include multiple plot options 在 一个 single 字符串, such as 
    
    
    "plot 类型=line, color=blue, pen=--, linewidth=2"

plot 类型 |  line point bar  
---|---  
marker style |  x o + s (square) d (diamond)  
pen |  \-- : -. -..  
x axis location |  top bottom  
y axis location |  left right  
color |  blue red etc.  
greyscale |   
plot lines |   
plot bar |   
plot points |   
marker size (default=4) | #  
linewidth (default=1) | #  
  
**示例**

This example 将 generate 一个 figure 使用 two lines: sin(x) 和 (sin(x))^2.
    
    
    x=linspace(0,10,100);
    y1=sin(x);
    y2=y1^2;
    plot(x,y1,y2,"x","y","title");
    legend("sin(x)", "sin(x)^2");

The following figure shows 该 output 的 该 该 example code.

This example 将 generate 一个 figure 使用 two lines: sin(x) 和 sin(x)^2 使用 more plotting options.
    
    
    x=linspace(0,10,100);
    y1=sin(x);
    y2=y1^2;
    plot(x,y1,"x","y","title", "plot 类型=line, color=red, pen=-., linewidth=2");
    holdon;
    plot(x,y2,"x","y","title", "plot 类型=line, color=blue, pen=--, linewidth=2");
    legend("sin(x)", "sin(x)^2");

The following figure shows 该 output 的 该 该 example code.

**参见**

[plotxy](/hc/en-us/articles/360034931093-plotxy), [holdon](/hc/en-us/articles/360034931113-holdon), [legend](/hc/en-us/articles/360034931233-legend), [image](/hc/en-us/articles/360034931253-image), [closeall](/hc/en-us/articles/360034410594-closeall), [setplot](/hc/en-us/articles/360034931293-setplot), [exportfigure](/hc/en-us/articles/360034410574-exportfigure), [visualize](/hc/en-us/articles/360034410514-visualize), [vectorplot](/hc/en-us/articles/360034410614-vectorplot), [polar](/hc/en-us/articles/360034931153-polar)
