# frequencysweep

使用频率分析选项卡中的当前设置执行频率扫描。生成一个名为 "frequencysweep" 的 D-CARD，其中包含色散、有效折射率和其他数据，作为频率的函数。

[selectmode](./selectmode.md) 命令可用于选择一个或多个模式用于频率扫描。

**语法** | **描述**
---|---
frequencysweep; | 使用当前设置执行频率扫描。此函数不返回任何数据。

**示例**

对第一个模式执行频率扫描并绘制色散：

```powershell
switchtolayout;

findmodes;
selectmode(1);
setanalysis("track selected mode",1);
setanalysis("detailed dispersion calculation",1);

frequencysweep;
D=getdata("frequencysweep","D");
f=getdata("frequencysweep","f_D");

plot(c/f*1e6,D*1e6,"Wavelength (um)", "Dispersion (ps/nm/km)");
```

对前三个模式执行频率扫描并绘制有效折射率：

```powershell
switchtolayout;
findmodes;
selectmode([1,2,3]);

frequencysweep;
neff_sweep = getdata("FDE::data::frequencysweep", "neff");
freq_sweep = getdata("FDE::data::frequencysweep", "f");
lambda_sweep = c/freq_sweep;
plot(lambda_sweep*1e6,real(neff_sweep), "Wavelength(um)", "Real Effective Index");
legend("Mode 1", "Mode 2", "Mode 3");
```

**另请参阅**

[命令列表](../命令列表.md)、[setanalysis](./setanalysis.md)、[mesh](./mesh.md)、[findmodes](./findmodes.md)、[selectmode](./selectmode.md)