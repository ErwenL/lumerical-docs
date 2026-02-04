<!--
Translation from English documentation
Original command: sroughness
Translation date: 2026-02-04 22:50:15
-->

# sroughness

返回 一个 矩阵 containing 一个 rough surface characterized 通过 一个 RMS amplitude. 

**语法** |  **描述**  
---|---  
out= sroughness(x_span, y_span, sigma_rms, corr_x, corr_y, seed);  |  返回 一个 矩阵 containing 一个 rough surface characterized 通过 一个 RMS amplitude ‘sigma_rms’ 和 correlation lengths ‘corr_x’ 和 ‘corr_y’. The roughness 是 generated 通过 creating 一个 random 矩阵 的 值 在 K space defined 通过 ‘x_span’ 和 ‘y_span’. A Gaussian filter 是 applied 到 此 矩阵, 那么 一个 Fourier transform 是 used 到 transform 该 矩阵 back 到 real space. Due 到 该 way 该 Fourier transform 是 setup, 该 roughness 将 为 periodic 使用 period x, y跨度. This 是 convenient 用于 some application, particularly 当 使用 periodic boundary conditions. The 参数 ‘seed’ defined 该 random seed 值 used 到 generate 该 surface.   
  
**示例**

This 是 一个 simple example 的 一个 rough surface created 使用 sroughness: 
    
    
    x_span = 400e-6;
    y_span = 400e-6;
    sigma_rms = 0.3;
    corr_length_x = 40e-6;
    corr_length_y = 40e-6;
    seed_process = 1;
    # 计算 该 数字 的 points 在 x 和 y
    Nx = 100;
    Ny = 100;
    # initialize required variables
    x_wafer = linspace(-x_span/2,x_span/2,Nx);
    y_wafer = linspace(-y_span/2,y_span/2,Ny);
    neff_xy_wafer = sroughness( x_wafer, y_wafer, sigma_rms, corr_length_x, corr_length_y, seed_process );
    image(x_wafer/1e-6, y_wafer/1e-6, neff_xy_wafer, "x (um)", "y(um)", "Rough surface");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 长度 ](/hc/en-us/articles/360034925653-长度) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ splitstring ](/hc/en-us/articles/360034926093-splitstring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper)
