<!--
Translation from English documentation
Original command: smithchart
Translation date: 2026-02-04 22:50:14
-->

# smithchart

Plots impedance 值 在 一个 Smith chart. The default impedance used 用于 normalization 是 50 Ohms; 此 可以 为 modified 在 该 plot settings once 该 plot has been created.

**语法** |  **描述**  
---|---  
out = smithchart(Z); |  创建 一个 curve 在 一个 Smith chart 使用 该 impedance 值 在 该 数组 Z. The 数组 Z 必须 为 的 该 form NX1 或 1XN.  
out = smithchart(Z1,Z2,Z3); |  创建 three curves 在 一个 Smith chart 使用 该 impedance 值 在 该 arrays Z1, Z2 和 Z3. Each 数组 必须 为 的 该 form NX1 或 1XN, but they do not have 到 为 的 该 same 维度.  
out = smithchart(Z, "title", "aspect ratio", norm_Z); |  创建 一个 Smith chart 使用 一个 title, 一个 given aspect ratio 和 一个 normalized impedance norm_Z. The aspect ratio 必须 为 字符串 该 是 either "1:1" 或 "fill scene".  
  
**示例**

创建 一个 simple Smith chart
    
    
    Z1 = 50*(3+1i*linspace(-50,50,101)); # re(Z) = 3 circle
    Z2 = 50*(linspace(0,50,101)+0.75i); # im(Z) = 0.75 line
    smithchart(Z1,Z2,"示例 的 Smith chart", "1:1", 50); # Normalized impedance 50 Ohms
    #The plot 属性 可以 also 为 设置 使用 setplot:
    smithchart(Z1,Z2);
    setplot("title", "示例 的 Smith chart");
    setplot("aspect ratio", "1:1");
    setplot("normalized impedance", 50);

The following figure shows 该 output 的 该 example code.

**参见**

[ List 的 commands](/hc/en-us/articles/360037228834), [polar](/hc/en-us/articles/360034931153-polar), [ setplot ](/hc/en-us/articles/360034931293-setplot)
