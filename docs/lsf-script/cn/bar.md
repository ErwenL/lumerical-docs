<!-- Translation completed: 2026-02-04 -->
<!-- Original command: bar -->

# bar

**语法** | **描述**
---|---
out = bar(y); | Creates a bar plot where each bar corresponds to one 元素 in y, which must be a 1D 数组. The figure 数字 is returned.
bar(x,y); | x is a nx1 矩阵.  y is a nxm 矩阵.  Creates m bar plots with n bars in the same figure for the 元素 in y at positions given by x. The figure 数字 is returned.
bar(x,y, "x label", "y label", "title"); | Creates a bar plot of y vs x with axis labels and a title, 返回 the figure 数字. The figure 数字 is returned.

**示例**

The following 示例 generates the two bar plots shown below. 
    x = linspace(0,1,10);
    y1 = exp(-((x-0.2)/0.4)^2);
    y2 = exp(-((x-0.7)/0.3)^2);
    y = [y1,y2];
    bar(y1); # bar plot for y1, where each bar is labeled from 1 to 10
    bar(x,y); # bar plot for y1 and y2 at locations specified by x
|   
---|---  

The following 示例 generates the two bar plots shown below. 
    x = linspace(0,1,10);
    y1 = exp(-((x-0.2)/0.4)^2);
    y2 = exp(-((x-0.7)/0.3)^2);
    y = [y1,y2];
    bar(y1); # bar plot for y1, where each bar is labeled from 1 to 10
    bar(x,y); # bar plot for y1 and y2 at locations specified by x
|   
---|---  

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ histc ](/hc/en-us/articles/360034410494-histc) , [ plot ](/hc/en-us/articles/360034410474-plot)
