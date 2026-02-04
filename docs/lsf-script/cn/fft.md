<!--
Translation from English documentation
Original command: fft
Translation date: 2026-02-04 22:49:49
-->

# fft

Computes 该 1D, 2D, 或 3D Fast Fourier Transform (FFT) 的 一个 矩阵. In 该 1D case, 该 transform 是 given 通过

$$ E_w[m]=\text{fft}(E_x)=\sum_{n-1}^NE_x[n]. e^{(\frac{2\pi i}{N})(n-1)(m-1)} $$

The FFT, inverse FFT, 和 all associated functions have 一个 option (option 1 below) 该 controls 该 format used 到 store 该 频率 domain 数据. When working 使用 spectral 数据 it 是 not possible 到 switch between formats; there 是 no functions 到 转换 between formats. This implies 该 如果 you use option 1=n 到 produce 一个 spectrum 使用 [[||fft]], 那么 you 必须 also use option 1=n 如果 you want 到 pass 该 same spectral 数据 到 [[||invfft]]. Similarly, 如果 you use option1 = n 用于 [[||fft]], 那么 you also need 到 use option 1=n 使用 [[||fftw]] 到 获取 该 proper 频率 向量 对应的 到 your spectrum. [[||invfft]] 和 [[||fftk]] work 在 该 same way.

**语法** |  **描述**  
---|---  
out = fft(Ex); |  返回 该 fast Fourier transform 的 Ex. Ex 可以 为 1D, 2D 或 3D.  
out = fft(Ex,option1,option2); |  option1 This option controls 该 format used 到 store 该 频率 domain 数据. The options 是:

  * 1 : 该 standard FFT (zero 频率 是 at 该 first 元素 的 该 矩阵). This 是 该 default option.
  * 2 : zero 频率 是 该 first 元素, but only 数据 up 到 和 including 该 Nyquist 频率 是 stored. This option 是 only useful 用于 real-valued, 1D 时间/spatial signals.
  * 3 : 该 FFT 是 shifted so zero 频率 是 该 central 元素 的 该 spectrum (more precisely, 此 means 该 zero 频率 point 是 at 该 元素 floor(N/2 + 1), 其中 N 是 该 数字 的 samples).

option2 This option 是 either 一个 1, 2 或 3 元素 向量 depending 在 whether Ex 是 1D, 2D 或 3D. For each 维度, specify 一个 值 的 either 0, 1 或 N 到 obtain 该 desired 0 padding options.

  * 0: no zero padding.
  * 1: zero padding up 到 该 next power 的 2 longer than 该 长度 的 Ex (default).
  * N: zero pad up 到 长度 N 如果 N > 长度(Ex), 其中 该 长度 的 Ex 是 该 长度 在 一个 specific 维度. If N <= 长度(Ex), it 将 zero pad up 到 该 next power 的 2 longer than 该 长度 的 Ex. For 该 fastest results, N 应该 为 一个 power 的 2 和 可以 为 entered, 用于 example, as 2^12.

  
  
注意: FFT Conventions There 是 different, but equivalent conventions 用于 defining Fourier transforms. Lumerical defines 该 forward FFT 使用 一个 positive sign 在 该 exponential term, 和 该 inverse FFT 使用 一个 negative sign 在 该 exponential term. However, some other packages (e.g. MATLAB) use 该 opposite convention, 使用 一个 negative sign 在 该 exponential 用于 该 forward FFT 和 一个 positive sign 在 该 exponential 用于 该 inverse FFT. To 转换 between 该 different FFT conventions, switch 该 [[||invfft]] 和 [[||fft]] 和 rescale 该 results. For 一个 signal y 使用 N elements, 此 可以 为 done as follows: fft(y,1,0) (Lumerical) \\(\Longleftrightarrow\\) ifft(y)*N (MATLAB) invfft(y,1,0) (Lumerical) \\(\Longleftrightarrow\\) fft(y)/N (MATLAB)  
---  
  
### 示例

This example transforms 一个 时间 signal 使用 60 和 100 rad/s angular 频率 components into 该 频率 domain. The 函数 [[||fftw]] 是 used 到 获取 该 correct 频率 向量. If 此 was 一个 spatial signal, 那么 [[||fftk]] 应该 为 used 在 place 的 [[||fftw]].
    
    
    t=linspace(0,1,1000);    # 时间 signal
    w1=100;           # 频率, 在 rad/s
    w2=60;            # 频率, 在 rad/s
    x=0.5*(sin(w1*t)+sin(w2*t)); # 该 signal
    plot(t,x,"时间","signal");
    o1=2;            # option 1
    o2=1;            # option 2
    y=fft(x,o1,o2);       # fft
    w=fftw(t,o1,o2);       # 频率 signal
    plot(w,abs(y),"freq (rad/sec)","amplitude");

This example shows 如何 到 计算 该 FFT 的 该 electric field intensity (i.e., combining all three field components) recorded 通过 一个 时间 监视器 在 该 attachment. If you want 到 filter 该 high-频率 数据, 设置 option1 到 2.
    
    
    # 获取 数据 从 point 时间 监视器
    m = "时间";
    t = getdata(m,"t");
    Ex = getdata(m,"Ex");
    Ey = getdata(m,"Ey");
    Ez = getdata(m,"Ez");
    # option1 = 1 -> standard fft
    # option1 = 2 -> remove high 频率 数据
    option1 = 2;
    # do fft 的 each component
    f  = fftw(t, option1)/2/pi;
    Exw = fft(Ex, option1);  # fft each component separately
    Eyw = fft(Ey, option1);
    Ezw = fft(Ez, option1);
    E2w = abs(Exw)^2+abs(Eyw)^2+abs(Ezw)^2; # combine field components
    plot(f/1e12,E2w,"f (THz)","|E(f)|^2","fft E^2 intensity"); 

The following figures show 该 resulting plot 用于 both 该 standard transform 和 该 option 到 remove 该 high-频率 数据 (option1 = 1 或 2).

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ invfft ](/hc/en-us/articles/360034406034-invfft) , [ fftw ](/hc/en-us/articles/360034926153-fftw) , [ fftk ](/hc/en-us/articles/360034406014-fftk) , [ czt ](/hc/en-us/articles/360034926173-czt)
