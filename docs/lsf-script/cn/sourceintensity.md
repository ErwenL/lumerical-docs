# sourceintensity

返回源功率除以源的面积。在3D模拟中，如果使用CW归一化，单位将是Watts/m²；如果使用No归一化，单位将是Watts/m²/Hertz²。此函数通常用于对带有TFSF源的模拟中的功率测量进行归一化。

对于多源情况，sourceintensity(f)命令将返回所有源的sourceintensity之和。

**语法** | **描述**
---|---
`out = sourceintensity(f);` | 在频率点向量f处返回源强度（f为以Hz为单位的频率）。
`out = sourceintensity(f, option);` | 额外的参数option可以是1或2。如果为2，则根据来自与x min、y min或z min处的边界相交的监视器的对称或反对称边界，尽可能展开数据。option的默认值为2。
`out = sourceintensity(f, option, name);` | 此函数可以使用一个源的频谱进行归一化，而不是所有源的总和。

**示例**

此示例展示如何使用transmission、sourcepower和sourceintensity函数来测量TFSF源注入的功率。请注意，监视器的面积是源面积的1/4。

```lsf
newproject;          # 创建新模拟
save("test");
addfdtd;         # 添加模拟区域
set("mesh accuracy",4);
set("x span",2.5e-6);
set("y span",2.5e-6);
set("z span",2.5e-6);
addtfsf;         # 添加源
set("x span",2e-6);
set("y span",2e-6);
set("z span",2e-6);
set("wavelength span",0);
addpower;         # 添加监视器（源面积的1/4）
set("x span",1e-6);
set("y span",1e-6);
run;           # 运行模拟
m="monitor";       
f=getdata(m,"f");     # 获取频率向量
T=transmission(m);     # 获取功率透射率（源功率的分数）
sp=sourcepower(f);     # 获取源注入的功率（Watts）
I=sourceintensity(f);   # 获取源强度（Watts/m^2）
area = getdata("source","area"); # 获取源面积（由于有限尺寸网格，不完全是2um^2）
# 输出结果
?"Transmitted power (fraction of source power): " +num2str(T);
?"Transmitted power (Watts): " +num2str(T*sp);
?"Source power (Watts): "+num2str(sp);
?"Source intensity (Watts/um^2): " + num2str(I*1e-12);
?"Ensure Intensity*Area=Power: " + num2str(I*area/sp);
> Transmitted power (fraction of source power): 0.235078
> Transmitted power (Watts): 1.24415e-015
> Source power (Watts): 5.2925e-015
> Source intensity (Watts/um^2): 1.30714e-015
> Ensure Intensity*Area=Power: 1
```

**另请参阅**

[sourcenorm](./sourcenorm.md), [sourcepower](./sourcepower.md), [sourceintensity_avg](./sourceintensity_avg.md), [sourceintensity_pavg](./sourceintensity_pavg.md), [dipolepower](./dipolepower.md), [transmission](./transmission.md), [cwnorm](./cwnorm.md), [nonorm](./nonorm.md), [单位和归一化](./Units_and_Normalization.md)
