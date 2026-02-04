<!--
Translation from English documentation
Original command: invfft
Translation date: 2026-02-03
-->

# invfft

计算矩阵的 1D、2D 或 3D 逆快速傅里叶变换 (FFT)。在 1D 情况下，变换由下式给出

$$E_x[m]=\text{invfft}(E_w)=\frac{1}{N}\sum_{n-1}^NE_w[n]. e^{-(\frac{2\pi i}{N})(n-1)(m-1)} $$

逆 FFT、FFT 和所有相关函数都有一个选项（下面的 option 1）来控制用于存储频域数据的格式。在处理频谱数据时，无法在格式之间切换；没有在格式之间转换的函数。这意味着如果使用 option1=n 用 fft 生成频谱，那么如果要将相同的频谱数据传递给 invfft，也必须使用 option1=n。类似地，如果对 fft 使用 option1=n，那么还需要对 fftw 使用 option1=n 以获得与频谱对应的正确频率向量。invfft 和 fftk 的工作方式相同。

**语法** |  **描述**
---|---
out = invfft(Ew);  |  返回 Ew 的逆快速傅里叶变换。Ew 可以是 1D、2D 或 3D。
out = invfft(Ew,option1,option2);  |  option1 此选项控制用于存储频域数据的格式。选项为：

  * 1 ：标准 FFT（零频率位于矩阵的第一个元素）。这是默认选项。
  * 2 ：零频率是第一个元素，但仅存储包括 Nyquist 频率在内的数据。此选项仅适用于实值的一维时间/空间信号。
  * 3 ：FFT 被移位，因此零频率是频谱的中心元素（更准确地说，这意味着零频率点位于元素 floor(N/2 + 1) 处，其中 N 是采样数）。

option2 此选项是 1、2 或 3 元素向量，具体取决于 Ex 是 1D、2D 还是 3D。对于每个维度，指定 0、1 或 N 的值以获得所需的零填充选项。

  * 0：无零填充
  * 1：零填充到比 Ex 长度长 2 的下一个 2 的幂（默认）
  * N：如果 N > Ex 的长度，则零填充到长度 N，其中 Ex 的长度是特定维度的长度。如果 N <= Ex 的长度，它将零填充到比 Ex 长度长 2 的下一个 2 的幂。为了获得最快的结果，N 应该是 2 的幂，可以例如输入为 2^12。

**示例**

此示例显示 x2=invfft(fft(x)) 返回 x。只有在使用不带零填充的标准 fft 时，x2 才等于 x。在 plot 命令中，1 被添加到 x2 以便在图形中可见两条线。

    t=linspace(0,100,1000);
    x=sin(t)+sin(t/10);
    k=fft(x,1,0);
    x2=invfft(k,1,0);
    plot(t,x,x2+1,"t");

**相关命令**

- [List of commands](./List-of-commands.md)
- [fft](./fft.md)
- [fftw](./fftw.md)
- [fftk](./fftk.md)
