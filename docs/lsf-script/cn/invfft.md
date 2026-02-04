<!--
Translation from English documentation
Original command: invfft
Translation date: 2026-02-04 22:50:01
-->

# invfft

Computes 该 1D, 2D 或 3D inverse Fast Fourier Transform (FFT) 的 一个 矩阵. In 该 1D case 该 transform 是 given 通过 

$$E_x[m]=\text{invfft}(E_w)=\frac{1}{N}\sum_{n-1}^NE_w[n]. e^{-(\frac{2\pi i}{N})(n-1)(m-1)} $$ 

The inverse FFT, FFT 和 all related functions have 一个 option (option 1 below) 该 controls 该 format used 到 store 该 频率 domain 数据. When working 使用 spectral 数据 it 是 not possible 到 switch between formats; there 是 no functions 到 转换 between formats. This implies 该 如果 you use option1=n 到 produce 一个 spectrum 使用 fft, 那么 you 必须 also use option1=n 如果 you want 到 pass 该 same spectral 数据 到 invfft. Similarly, 如果 you use option1=n 用于 fft, 那么 you also need 到 use option1=n 使用 fftw 到 获取 该 proper 频率 向量 对应的 到 your spectrum. invfft 和 fftk work 在 该 same way. 

**语法** |  **描述**  
---|---  
out = invfft(Ew);  |  返回 该 inverse fast Fourier transform 的 Ew. Ew 可以 1D,2D 或 3D.   
out = invfft(Ew,option1,option2);  |  option1  This option controls 该 format used 到 store 该 频率 domain 数据. The options 是: 

  * 1 : 该 standard FFT (zero 频率 是 at 该 first 元素 的 该 矩阵). This 是 该 default option. 
  * 2 : zero 频率 是 该 first 元素, but only 数据 up 到 和 including 该 Nyquist 频率 是 stored. This option 是 only useful 用于 real valued, 1D 时间/spatial signals. 
  * 3 : 该 FFT 是 shifted so zero 频率 是 该 central 元素 的 该 spectrum (more precisely, 此 means 该 zero 频率 point 是 at 元素 floor(N/2 + 1), 其中 N 是 该 数字 的 samples). 

option2  This option 是 either 一个 1, 2 或 3 元素 向量 depending 在 whether Ex 是 1D, 2D 或 3D. For each 维度, specify 一个 值 的 either 0, 1 或 N 到 obtain 该 desired 0 padding options. 

  * 0: no zero padding 
  * 1: zero padding up 到 该 next power 的 2 longer than 该 长度 的 Ex (default) 
  * N: zero pad up 到 长度 N 如果 N > 长度(Ex), 其中 长度 的 Ex 是 该 长度 在 一个 specific 维度. If N <= 长度(Ex), it 将 zero pad up 到 该 next power 的 2 longer than 该 长度 的 Ex. For 该 fastest results, N 应该 为 一个 power 的 2 和 可以 为 entered, 用于 example, as 2^12. 

  
  
**示例**

This example shows 该 x2=invfft(fft(x)) 返回 x. x2 将 only 为 equal 到 x 如果 该 standard fft without zero padding 是 used. In 该 plot 命令, 1 是 added 到 x2 so 该 both lines 是 visible 在 该 plot. 
    
    
    t=linspace(0,100,1000);
    x=sin(t)+sin(t/10);
    k=fft(x,1,0);
    x2=invfft(k,1,0);
    plot(t,x,x2+1,"t");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ fft ](/hc/en-us/articles/360034926133-fft) , [ fftw ](/hc/en-us/articles/360034926153-fftw) , [ fftk ](/hc/en-us/articles/360034406014-fftk)
