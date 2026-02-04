<!--
Translation from English documentation
Original command: bar
Translation date: 2026-02-04 22:49:36
-->

# bar

Plots 一个 bar chart. 

**语法** |  **描述**  
---|---  
out = bar(y);  |  创建 一个 bar plot 其中 each bar corresponds 到 one 元素 在 y, 该 必须 为 一个 1D 数组. The figure 数字 是 returned.   
bar(x,y);  |  x 是 一个 nx1 矩阵.  y 是 一个 nxm 矩阵.  创建 m bar plots 使用 n bars 在 该 same figure 用于 该 elements 在 y at positions given 通过 x. The figure 数字 是 returned.   
bar(x,y, "x label", "y label", "title");  |  创建 一个 bar plot 的 y vs x 使用 axis labels 和 一个 title, 返回 该 figure 数字. The figure 数字 是 returned.   
  
**示例**

The following example generates 该 two bar plots shown below. 
    
    
    x = linspace(0,1,10);
    y1 = exp(-((x-0.2)/0.4)^2);
    y2 = exp(-((x-0.7)/0.3)^2);
    y = [y1,y2];
    bar(y1); # bar plot 用于 y1, 其中 each bar 是 labeled 从 1 到 10
    bar(x,y); # bar plot 用于 y1 和 y2 at locations specified 通过 x

|   
---|---  
  
**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ histc ](/hc/en-us/articles/360034410494-histc) , [ plot ](/hc/en-us/articles/360034410474-plot)
