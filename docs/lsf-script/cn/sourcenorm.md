# sourcenorm

返回用于在cwnorm状态下归一化标准傅里叶变换量数据的源归一化频谱。有关更多信息，请参阅[单位和归一化](./Units_and_Normalization.md)页面。

**语法** | **描述**
---|---
`out = sourcenorm(f);` | 在频率点向量f处返回用于在cwnorm状态下归一化数据的源归一化频谱。（f是以Hz为单位的频率）如果归一化状态设置为'CWNorm (average)'：$$ s(\omega)=\operatorname{sourcenorm}(\omega)=\frac{1}{N} \sum_{sources} \int \exp (i \omega t) s_{j}(t) d t $$

* $s_{j}(t)$：对象树中第j个活动源的时间信号
* N是活动源的数量

如果归一化状态设置为'CWNorm (first)'：$$ s(\omega)= \int \exp (i \omega t) s_{1}(t) d t $$
`out = sourcenorm(f, name);` | 当输入源名称的额外参数时，它使用您选择的特定源，而不是对象树中的第一个源或所有源的平均值。

**示例**

此示例展示如何再现源属性窗口的频率/波长选项卡中显示的源频谱图。

```lsf
lambda1 = 0.4e-6; # 起始波长  
lambda2 = 0.7e-6; # 结束波长  
f=linspace(c/lambda2,c/lambda1,1000);  

# 获取源频谱  
spectrum=sourcenorm(f);  
spectrum=abs(spectrum)^2;  
spectrum=spectrum/max(spectrum);  

# 获取源时域信号  
time = getdata("source","time");  
time_signal = getdata("source","time_signal");  

plot(c/f*1e6,spectrum, "wavelength (um)","spectrum vs wavelength");  
plot(f/1e12,spectrum, "frequency (THz)","spectrum vs frequency");  
plot(time*1e15,time_signal,"time (fs)","amplitude","Source time signal");
```

**另请参阅**

[sourcenorm2_avg](./sourcenorm2_avg.md), [sourcenorm2_pavg](./sourcenorm2_pavg.md), [sourcepower](./sourcepower.md), [cwnorm](./cwnorm.md), [nonorm](./nonorm.md), [单位和归一化](./Units_and_Normalization.md)
