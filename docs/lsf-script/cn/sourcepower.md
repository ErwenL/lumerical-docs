# sourcepower

返回源注入到模拟中的功率。

**偶极子源**

sourcepower脚本函数返回偶极子源在均匀介质中辐射的功率。此量可以解析计算（请参阅[偶极子源](./Sources_Dipoles.md)）。实际辐射功率不由sourcepower函数给出。实际辐射功率高度依赖于周围材料，因为结构的反射会干扰来自偶极子的场，改变实际辐射功率。要获取实际辐射功率，请参阅[dipolepower](./dipolepower.md)脚本函数。

**其他源（高斯、平面波、模式等）**

sourcepower由以下方程确定。注意$P(f)^{\text{Source}}$是由源注入的E、H场确定的坡印廷矢量。积分在源的注入平面上求值。

$$ \text{source power}_{\text{no_norm}}(f)=\frac{1}{2} \int \text{Re}\left(P(f)^{\text{Source}}\right) \cdot d S $$

$$ \text{source power}_{\text{cw_norm}}(f)=\frac{\frac{1}{2} \int \text{Re}\left(P(f)^{\text{Source}}\right) \cdot d S}{ | \text{sourcenorm}\left.\right |^{ 2 }} $$

如上所述，sourcepower给出注入到模拟中的功率量。唯一的例外是如果模拟设置使得有辐射沿着源注入方向（粉红色箭头）穿过源的注入平面。在这种情况下，源注入的实际功率量将不由sourcepower给出。在这种情况下，入射辐射与源干扰，改变注入的功率量（类似于偶极子源发生的情况）。在大多数情况下，这意味着您的模拟设置不正确。

**注意：** 多源和CW归一化 对于多源情况，sourcepower(f)命令将返回所有源的sourcepower之和。由于sourcenorm的值取决于cwnorm选项的选择，计算的sourcepower也会受到影响。

**语法** | **描述**
---|---
`out = sourcepower(f);` | 在频率点向量f处返回用于归一化透射计算的源功率（频率以Hz为单位）。如果使用CW归一化，源功率的单位是Watts；如果不使用归一化，单位是Watts/Hertz²。
`out = sourcepower(f, option);` | 额外的参数option可以是1或2。如果为2，则根据来自与x min、y min或z min处的边界相交的监视器的对称或反对称边界，尽可能展开数据。option的默认值为2。
`out = sourcepower(f, option, name);` | 此选项允许您获取一个源的频谱，而不是所有源的总和。此选项仅在具有多个源的模拟中需要。

**示例**

此示例展示如何计算源注入的功率作为频率的函数。

```lsf
f=linspace(200e12,300e12,100);
sp=sourcepower(f); # 功率以Watts为单位，假设CW归一化已开启。
```

此示例展示如何使用transmission和sourcepower函数来计算平面波源注入的功率。

```lsf
newproject;
save("test");
 
# 模拟区域
addfdtd;
set("x span",1e-6); set("y span",1e-6); set("z span",1e-6);
set("x min bc","periodic"); set("y min bc","periodic");
 
# 平面波源
addplane;
set("z",-0.3e-6);
set("x span",2e-6); set("y span",2e-6);
set("center wavelength",500e-9);
set("wavelength span",0);
 
# 功率监视器
addpower; 
set("z",0.3e-6);        
set("x span",2e-6); set("y span",2e-6);
# 运行模拟 
run;            
# 获取结果 
m="monitor";      
f=getdata(m,"f");     # 获取频率向量
T=transmission(m);     # 获取功率透射率（源功率的分数）
sp=sourcepower(f);     # 获取源注入的功率（Watts）
 
# 输出结果
?"Transmitted power (fraction of source power): " +num2str(T);
?"Transmitted power (Watts): " +num2str(T*sp);
?"Source power (Watts): "+num2str(sp);
> Transmitted power (fraction of source power): 0.999986
> Transmitted power (Watts): 1.26203e-015
> Source power (Watts): 1.26204e-015
```

**另请参阅**

[sourcenorm](./sourcenorm.md), [sourcepower_avg](./sourcepower_avg.md), [sourcepower_pavg](./sourcepower_pavg.md), [dipolepower](./dipolepower.md), [transmission](./transmission.md), [sourceintensity](./sourceintensity.md), [cwnorm](./cwnorm.md), [nonorm](./nonorm.md)
