<!--
Translation from English documentation
Original command: czt
Translation date: 2026-02-03 10:57:45
-->

# czt

返回一组数据的线性调频Z变换。czt函数通常比标准fft函数更方便，因为可以指定任意范围的k。 

$$ E_k[m]=czt(E_x,x,k)=\sum_nE_x[n].e^{ix[n]k[m]} $$ 

$$ E_k[m1,m2]=czt(E_x,x1,x2,k1,k2)=\sum_{n1,n2}E_x[n1,n2].e^{ix1[n1]k1[m1]+ix2[n2]k2[m2]} $$ 

**Syntax** |  **Description**  
---|---  
out = czt(Ex,t,w);  |  返回Ex（t的函数）在每个所需角频率w处的线性调频Z变换。注意w必须是线性间隔的角频率集合，但可以覆盖任何范围。也可以进行逆变换，即out=czt(Ex,w,t)，详见下面的插值示例。E可以是一个矩阵，其中两个维度之一与length相同。Z变换沿着与length匹配的维度计算，输出向量将是一个矩阵，其中匹配的维度长度为length(kx)，另一个维度与E相同。此功能允许通过单个函数调用计算多个一维Z变换。   
czt(Ex,x,y,kx,ky);  |  二维线性调频Z变换。kx和ky必须是线性间隔的波数集合，但可以覆盖任何范围。   
  
**Example**

This example uses the czt function to determine the frequency components of a signal, as shown in the following figure. 
    
    
    t=linspace(0,50,1000);   # sec
    f=linspace(0,3,200);    # Hz
    x_t=sin(t) + cos(t*2*pi);  # x(t)
    x_f=czt(x_t,t,f*2*pi);   # x(f)
    plot(f,abs(x_f),"f (Hz)"); 

The following is an example of Fourier based interpolation. We can use the fftw function to create the w vector (option3, which shifts the data, is required). A factor of 1/N is necessary for the inverse transform. Also, notice the minus sign on the w vector for the inverse transform. It is possible to use czt to re-sample 2D data. 
    
    
    initial_res = 21;
    final_res = 200;
    # Initial data
    t=linspace(-10,10,initial_res);
    y=sin(t)*exp(-t^2/30);
    plot(t,y,"t","y","Initial");
    # fourier transform
    w=fftw(t,3);
    y_w=czt(y,t,w);
    plot(w,abs(y_w)^2,"w","y_w");
    # re-sample data at 10x
    t_hi=linspace(min(t),max(t),final_res);
    y_hi=1/length(w)*czt(y_w,-w,t_hi); # inverse transform
    plot(t_hi,real(y_hi),"t","y","Final");

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [fft](../en/fft.md)
- [fftw](../en/fftw.md)
