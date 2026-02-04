# fftk

返回与 x 的函数的傅里叶变换相关的空间波矢量 kx。

$$ k=\text{fftk}(x)=\frac{2\pi}{dx.M}[0,...,(M-1)] $$

其中 M=length(x)。

fftk 及所有相关函数都有一个选项（下面的选项 1），用于控制用于存储频域数据的格式。处理频谱数据时无法在格式之间切换；没有在格式之间转换的函数。这意味着如果使用 option1=n 通过 fft 生成频谱，则如果要将相同的频谱数据传递给 invfft，也必须使用 option1=n。同样，如果对 fft 使用 option1=n，则还需要对 fftw 使用 option1=n 以获取与频谱对应的正确频率向量。invfft 和 fftk 的工作方式相同。

**语法** | **描述**
---|---
out = fftk(x); | 返回与 x 的函数的傅里叶变换相关的空间波矢量 kx。
fftk(x,option1,option2); | option1

- 1：标准 FFT（零频率位于矩阵的第一个元素）。这是默认选项。

- 2：零频率是第一个元素，但移除高于奈奎斯特频率的频率。

- 3：FFT 被移位，使零频率位于频谱的中心元素（更准确地说，这意味着零频率点位于元素 floor(N/2 + 1) 处，其中 N 是采样数）。可以看到正频率和负频率

option2

- 0：无零填充。
- 1：零填充到大于 Ex 长度.next power of 2（默认）。
- N：如果 N > length(t)，则零填充到长度 N。如果 N <= length(t)，则零填充到大于 t 长度.next power of 2。为获得最快结果，N 应该是 2 的幂，例如，可以输入为 2^12。

**示例**

如果 Ex 是空间场值的 2D 矩阵，其中 Ex 包含沿轴向量 x 和 y 的场值，则以下代码将显示 Ex 的场及其傅里叶变换的图像。

```powershell
image(x,y,Ex);
Ix = abs( fft(Ex) )^2;
kx = fftk(x);
ky = fftk(y);
image(kx,ky,Ix);
```

**另请参阅**

[命令列表](../命令列表.md)、[fft](./fft.md)、[fftw](./fftw.md)、[invfft](./invfft.md)