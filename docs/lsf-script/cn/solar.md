<!--
Translator: Claude
Translation Date: 2026-02-03
Status: Completed
-->
# solar

返回太阳光谱功率，单位为瓦特/平方米/米。

这些值基于以下链接中的全局倾斜值：[参考太阳光谱辐照度：ASTM G-173](http://rredc.nrel.gov/solar/spectra/am1.5/ASTMG173/ASTMG173.html)。

**语法** | **描述**
---|---
out = solar(1); | 返回作为波长函数的太阳能光谱功率，单位为W/m^2/m
out = solar(0); | 返回相应的波长向量，单位为m

**示例**

使用solar命令获取太阳光谱功率。接下来，用更常用的单位瓦特/平方米/纳米绘制光谱。

```
lambda=solar(0);  # 以米为单位的波长向量
ssp=solar(1);     # 以瓦特/平方米/米为单位的太阳光谱
lambda = lambda*1e9; # 转换为纳米
ssp  = ssp * 1e-9; # 转换为/纳米
plot(lambda,ssp,"波长 (nm)","功率 (W/m^2/nm)", "太阳光谱");
```

**另请参阅**

[ plot ](plot.html) , [ integrate ](integrate.html)
