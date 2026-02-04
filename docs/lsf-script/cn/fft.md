# fft

计算矩阵的 1D、2D 或 3D 快速傅里叶变换 (FFT)。在 1D 情况下，变换由下式给出：

$$ E_w[m]=\text{fft}(E_x)=\sum_{n-1}^NE_x[n]. e^{(\frac{2\pi i}{N})(n-1)(m-1)} $$

FFT、逆 FFT 及所有相关函数都有一个选项（下面的选项 1），用于控制用于存储频域数据的格式。处理频谱数据时无法在格式之间切换；没有在格式之间转换的函数。这意味着如果使用 option 1=n 通过 [[||fft]] 生成频谱，则如果要将相同的频谱数据传递给 [[||invfft]]，也必须使用 option 1=n。同样，如果对 [[||fft]] 使用 option1 = n，则还需要对 [[||fftw]] 使用 option 1=n 以获取与频谱对应的正确频率向量。[[||invfft]] 和 [[||fftk]] 的工作方式相同。

**语法** | **描述**
---|---
out = fft(Ex); | 返回 Ex 的快速傅里叶变换。Ex 可以是 1D、2D 或 3D。
out = fft(Ex,option1,option2); | option1 此选项控制用于存储频域数据的格式。选项为：

- 1：标准 FFT（零频率位于矩阵的第一个元素）。这是默认选项。
- 2：零频率是第一个元素，但只存储包含奈奎斯特频率及以下的数据。此选项仅对实值 1D 时间/空间信号有用。
- 3：FFT 被移位，使零频率位于频谱的中心元素（更准确地说，这意味着零频率点位于元素 floor(N/2 + 1) 处，其中 N 是采样数）。

option2 此选项可以是 1、2 或 3 元素向量，具体取决于 Ex 是 1D、2D 还是 3D。对于每个维度，指定 0、1 或 N 的值以获得所需的零填充选项。

- 0：无零填充。
- 1：零填充到大于 Ex 长度.next power of 2（默认）。
- N：如果 N > length(Ex)，则零填充到长度 N，其中 Ex 的长度是特定维度的长度。如果 N <= length(Ex)，则零填充到大于 Ex 长度.next power of 2。为获得最快结果，N 应该是 2 的幂，例如，可以输入为 2^12。

注意：FFT 约定 定义傅里叶变换有不同的但等效的约定。Lumerical 在指数项中使用正号定义正向 FFT，在指数项中使用负号定义逆 FFT。然而，其他一些包（例如 MATLAB）使用相反的约定，在正向 FFT 的指数中使用负号，在逆 FFT 的指数中使用正号。要在不同的 FFT 约定之间切换，请切换 [[||invfft]] 和 [[||fft]] 并重新缩放结果。对于具有 N 个元素的信号 y，可以按以下方式完成：fft(y,1,0) (Lumerical) ⇔ ifft(y)*N (MATLAB) invfft(y,1,0) (Lumerical) ⇔ fft(y)/N (MATLAB)

### 示例

此示例将具有 60 和 100 rad/s 角频率分量的时间信号变换到频域。使用 [[||fftw]] 函数获取正确的频率向量。如果是空间信号，则应使用 [[||fftk]] 代替 [[||fftw]]。

```powershell
t=linspace(0,1,1000);    # 时间信号
w1=100;           # 频率，单位为 rad/s
w2=60;            # 频率，单位为 rad/s
x=0.5*(sin(w1*t)+sin(w2*t)); # 信号
plot(t,x,"time","signal");
o1=2;            # option 1
o2=1;            # option 2
y=fft(x,o1,o2);        # fft
w=fftw(t,o1,o2);        # 频率信号
plot(w,abs(y),"freq (rad/sec)","amplitude");
```

此示例显示如何计算附件中时间监视器记录的电场强度（即组合所有三个场分量）的 FFT。如果要过滤高频数据，请将 option1 设置为 2。

```powershell
# 从点时间监视器获取数据
m = "time";
t = getdata(m,"t");
Ex = getdata(m,"Ex");
Ey = getdata(m,"Ey");
Ez = getdata(m,"Ez");
# option1 = 1 -> 标准 fft
# option1 = 2 -> 移除高频数据
option1 = 2;
# 对每个分量进行 fft
f  = fftw(t, option1)/2/pi;
Exw = fft(Ex, option1);  # 分别对每个分量进行 fft
Eyw = fft(Ey, option1);
Ezw = fft(Ez, option1);
E2w = abs(Exw)^2+abs(Eyw)^2+abs(Ezw)^2; # 组合场分量
plot(f/1e12,E2w,"f (THz)","|E(f)|^2","fft E^2 intensity");
```

下图显示了标准变换和移除高频数据的选项（option1 = 1 或 2）的结果图。

**另请参阅**

[命令列表](../命令列表.md)、[invfft](./invfft.md)、[fftw](./fftw.md)、[fftk](./fftk.md)、[czt](./czt.md)