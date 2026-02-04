<!--
Translation from English documentation
Original command: polar
Translation date: 2026-02-04 22:50:14
-->

# polar

创建 polar plots. All 数据 设置 必须 为 sampled 在 该 same 数组 的 angle 值. 

See polar2 用于 数据 设置 该 是 sampled 在 different arrays 的 theta 值. 

**语法** |  **描述**  
---|---  
out = polar(theta,rho)  |  创建 一个 polar coordinate plot 的 该 angle theta versus 该 radius rho. theta 是 该 angle 从 该 x-axis 到 该 radius 向量 specified 在 radians; rho 是 该 长度 的 该 radius 向量.  Theta 和 rho 可以 为 vectors 的 该 same 长度, 或 如果 该 长度 的 theta 是 n, 那么 rho 可以 为 一个 nxm 矩阵, 该 corresponds 到 m 设置 的 rho 值.  The figure 数字 是 returned.   
polar(theta,rho1,rho2,rho3)  |  创建 一个 polar plot 使用 three curves. theta, rho1, rho2, rho3 必须 为 的 该 same 长度. The figure 数字 是 returned.   
polar(theta,rho,"x label", "y label", "title")  |  创建 一个 polar plot 使用 axis labels 和 一个 title. The figure 数字 是 returned.   
polar(theta,rho,"x label", "y label", "title", "options");  |  创建 一个 polar plot 使用 desired options. Options 可以 为 为 

  * greyscale 
  * polar (use 使用 plot 命令 到 generate 该 same plot as 该 polar 脚本 命令) 
  * any comma separated list 的 该 above 

返回 该 figure 数字.   
  
**示例**

创建 一个 simple polar plot. 
    
    
    theta = linspace(0,2*pi,100);
    r = cos(theta);
    polar(theta,r);

The following figure shows 该 output 的 该 该 example code. 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ polar2 ](/hc/en-us/articles/360034931173-polar2) , [ legend ](/hc/en-us/articles/360034931233-legend) , [ image ](/hc/en-us/articles/360034931253-image) , [ closeall ](/hc/en-us/articles/360034410594-closeall) , [ setplot ](/hc/en-us/articles/360034931293-setplot) , [ exportfigure ](/hc/en-us/articles/360034410574-exportfigure) , [ polarimage ](/hc/en-us/articles/360034931193-polarimage) , [ plot ](/hc/en-us/articles/360034410474-plot)
