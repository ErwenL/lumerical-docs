<!--
Translation from English documentation
Original command: polar2
Translation date: 2026-02-04 22:50:14
-->

# polar2

创建 polar plots. In particular, 此 函数 是 used 当 该 数据 设置 是 sampled 在 different arrays 的 angle 值. 

**语法** |  **描述**  
---|---  
out = polar2(theta,rho)  |  创建 一个 polar coordinate plot 的 该 angle theta versus 该 radius rho. theta 是 该 angle 从 该 x-axis 到 该 radius 向量 specified 在 radians; rho 是 该 长度 的 该 radius 向量.  Theta 和 rho 可以 为 vectors 的 该 same 长度, 或 如果 该 长度 的 theta 是 n, 那么 rho 可以 为 一个 nxm 矩阵, 该 corresponds 到 m 设置 的 rho 值.  The figure 数字 是 returned.   
polar2(theta1,rho1,theta2,rho2)  |  创建 一个 plot 使用 two curves. The two 数据 设置 可以 为 sampled 在 different theta vectors.   
polar2(theta,rho,"x label", "y label", "title")  |  创建 一个 plot 的 y vs x 使用 axis labels 和 一个 title, 返回 该 figure 数字.   
polar2(theta,rho,"x label", "y label", "title", "options");  |  创建 一个 plot 使用 desired options. Options 可以 为 为 

  * greyscale 
  * polar (same as 该 polar 脚本 命令) 
  * any comma separated list 的 该 above 

返回 该 figure 数字.   
  
**示例**

Plot 在 polar coordinates two different 数据 设置. 
    
    
    theta1 = linspace(0,2*pi,100);
    r1 = cos(theta1);
    theta2 = linspace(0,pi,50);
    r2 = sin(theta2);
    polar2(theta1,r1,theta2,r2);

The following figure shows 该 output 的 该 该 example code. 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ polar ](/hc/en-us/articles/360034931153-polar) , [ legend ](/hc/en-us/articles/360034931233-legend) , [ image ](/hc/en-us/articles/360034931253-image) , [ closeall ](/hc/en-us/articles/360034410594-closeall) , [ setplot ](/hc/en-us/articles/360034931293-setplot) , [ exportfigure ](/hc/en-us/articles/360034410574-exportfigure) , [ polarimage ](/hc/en-us/articles/360034931193-polarimage) , [ plot ](/hc/en-us/articles/360034410474-plot)
