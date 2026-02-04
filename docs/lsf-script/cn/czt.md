<!--
Translation from English documentation
Original command: czt
Translation date: 2026-02-04 22:49:48
-->

# czt

返回 该 chirped z-transform 的 一个 设置 的 数据. The czt 函数 是 often more convenient than 该 standard fft functions because you 可以 specify 一个 arbitrary range 的 k. 

$$ E_k[m]=czt(E_x,x,k)=\sum_nE_x[n].e^{ix[n]k[m]} $$ 

$$ E_k[m1,m2]=czt(E_x,x1,x2,k1,k2)=\sum_{n1,n2}E_x[n1,n2].e^{ix1[n1]k1[m1]+ix2[n2]k2[m2]} $$ 

**语法** |  **描述**  
---|---  
out = czt(Ex,t,w);  |  返回 该 chirped z-transform 的 Ex, 函数 的 t, at each desired angular 频率 w. 注意 该 w 必须 为 一个 linearly spaced 设置 的 angular frequencies but 可以 cover any range. It 是 also possible 用于 inverse transform, ie out=czt(Ex,w,t), see 该 interpolation example below 用于 details. E 可以 为 一个 矩阵 其中 one 的 该 two dimensions 是 该 same as 长度. The Z-transform 是 computed along 该 维度 该 matches 长度, 和 该 output 向量 将 为 一个 矩阵 其中 该 matched 维度 是 长度(kx) 和 该 other 维度 是 该 same as E. This functionality allows 到 compute multiple 1D Z-transforms 使用 一个 single 函数 call.   
czt(Ex,x,y,kx,ky);  |  The two dimensional chirped z-transform. kx 和 ky 必须 为 linearly spaced 设置 的 wavenumbers but 可以 cover any range.   
  
**示例**

This example uses 该 czt 函数 到 determine 该 频率 components 的 一个 signal, as shown 在 该 following figure. 
    
    
    t=linspace(0,50,1000);   # sec
    f=linspace(0,3,200);    # Hz
    x_t=sin(t) + cos(t*2*pi);  # x(t)
    x_f=czt(x_t,t,f*2*pi);   # x(f)
    plot(f,abs(x_f),"f (Hz)"); 

The following 是 一个 example 的 Fourier based interpolation. We 可以 use 该 fftw 函数 到 创建 该 w 向量 (option3, 该 shifts 该 数据, 是 required). A factor 的 1/N 是 necessary 用于 该 inverse transform. Also, notice 该 minus sign 在 该 w 向量 用于 该 inverse transform. It 是 possible 到 use czt 到 re-sample 2D 数据. 
    
    
    initial_res = 21;
    final_res = 200;
    # Initial 数据
    t=linspace(-10,10,initial_res);
    y=sin(t)*exp(-t^2/30);
    plot(t,y,"t","y","Initial");
    # fourier transform
    w=fftw(t,3);
    y_w=czt(y,t,w);
    plot(w,abs(y_w)^2,"w","y_w");
    # re-sample 数据 at 10x
    t_hi=linspace(min(t),max(t),final_res);
    y_hi=1/长度(w)*czt(y_w,-w,t_hi); # inverse transform
    plot(t_hi,real(y_hi),"t","y","Final");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ fft ](/hc/en-us/articles/360034926133-fft) , [ fftw ](/hc/en-us/articles/360034926153-fftw)
