<!--
Translation from English documentation
Original command: fftk
Translation date: 2026-02-04 22:49:49
-->

# fftk

返回 该 spatial wavevector kx associated 使用 该 Fourier transform 的 一个 函数 的 x. 

$$ k=\text{fftk}(x)=\frac{2\pi}{dx.M}[0,...,(M-1)] $$ 

其中 M=长度(x). 

fftk 和 all related functions have 一个 option (option 1 below) 该 controls 该 format used 到 store 该 频率 domain 数据. When working 使用 spectral 数据 it 是 not possible 到 switch between formats; there 是 no functions 到 转换 between formats. This implies 该 如果 you use option1=n 到 produce 一个 spectrum 使用 fft, 那么 you 必须 also use option1=n 如果 you want 到 pass 该 same spectral 数据 到 invfft. Similarly, 如果 you use option1=n 用于 fft, 那么 you also need 到 use option1=n 使用 fftw 到 获取 该 proper 频率 向量 对应的 到 your spectrum. invfft 和 fftk work 在 该 same way. 

**语法** |  **描述**  
---|---  
out = fftk(x);  |  返回 该 spatial wavevector kx associated 使用 一个 fourier transform 的 一个 函数 的 x..   
fftk(x,option1,option2);  |  option1 

  * 1 : 该 standard FFT (zero 频率 是 at 该 first 元素 的 该 矩阵). This 是 该 default option. 


  * 2 : zero 频率 是 该 first 元素, but frequencies above 该 Nyquist 频率 是 removed. 


  * 3 : 该 FFT 是 shifted so zero 频率 是 该 central 元素 的 该 spectrum (more precisely, 此 means 该 zero 频率 point 是 at 元素 floor(N/2 + 1), 其中 N 是 该 数字 的 samples). Both positive 和 negative frequencies 是 seen 

option2 

  * 0: no zero padding. 
  * 1: zero padding up 到 该 next power 的 2 longer than 该 长度 的 Ex (default). 
  * N: zero pad up 到 长度 N 如果 N > 长度(t). If N <= 长度(t), it 将 zero pad up 到 该 next power 的 2 longer than 该 长度 的 t. For 该 fastest results, N 应该 为 一个 power 的 2 和 可以 为 entered, 用于 example, as 2^12. 

  
  
**示例**

If Ex 是 一个 2D 矩阵 的 spatial field 值 其中 Ex contains 该 field 值 along 该 axis vectors x 和 y, 那么 该 following code 将 image 该 field 和 该 fourier transform 的 Ex. 
    
    
    image(x,y,Ex);
    Ix = abs( fft(Ex) )^2; 
    kx = fftk(x); 
    ky = fftk(y); 
    image(kx,ky,Ix); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ fft ](/hc/en-us/articles/360034926133-fft) , [ fftw ](/hc/en-us/articles/360034926153-fftw) , [ invfft ](/hc/en-us/articles/360034406034-invfft)
