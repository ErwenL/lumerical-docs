<!--
Translation from English documentation
Original command: polarimage
Translation date: 2026-02-04 22:50:14
-->

# polarimage

创建 2D polar image plots. This 是 typically used 到 plot far field 数据. 

**语法** |  **描述**  
---|---  
polarimage(ux,uy,数据);  |  创建 一个 2D image plot. 数据 必须 为 的 维度 N x M 和 

  * ux 是 的 维度 N x 1, 其中 ux goes 从 -1 到 1 
  * uy 是 的 维度 M x 1, 其中 uy goes 从 -1 到 1 

  
out = polarimage(ux,uy,数据, "x label", "y label", "title");  |  创建 一个 2D image plot 使用 axis labels  Optionally 返回 该 figure 数字.   
polarimage(ux,uy,数据, "x label", "y label", "title", "options");  |  创建 一个 2D image plot 使用 axis labels 和 options, options 可以 为 

  * logplot 

  
  
**示例**

This example generates 一个 image 的 一个 simple 2D Gaussian 函数. 
    
    
    ux=linspace(-1,1,51);
    uy=linspace(-1,1,61);
    Ux=meshgridx(ux,uy);
    Uy=meshgridy(ux,uy);
    数据 = exp( 1-Ux^2-Uy^2);
    # plot 数据 使用 both 该 image 和 polarimage 脚本 functions
    image(ux,uy,数据,"ux","uy","Image plot");   
    polarimage(ux,uy,数据,"ux","uy","Polar Image plot");

The following figure shows 该 resulting figures. 

This example shows 如何 此 函数 might 为 used 使用 该 far field projection functions. 
    
    
    m="monitor1";   # 监视器 name
    ux=farfieldux(m); # position vectors
    uy=farfielduy(m);
    E2=farfield3d(m); # Far field E2 数据
    polarimage(ux,uy,E2,"ux","uy","far field |E|^2");  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ plot ](/hc/en-us/articles/360034410474-plot) , [ polar ](/hc/en-us/articles/360034931153-polar) , [ image ](/hc/en-us/articles/360034931253-image) , [ closeall ](/hc/en-us/articles/360034410594-closeall) , [ setplot ](/hc/en-us/articles/360034931293-setplot) , [ exportfigure ](/hc/en-us/articles/360034410574-exportfigure) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ List 的 commands ](/hc/en-us/articles/360037228834)
