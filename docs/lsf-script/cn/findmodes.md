# findmodes

使用当前计算设置计算结构支持的模式。此函数是"计算模式"按钮的脚本等效项。每个模式将保存为名为 "modeX" 的 D-CARD，其中 X 是找到的第 X 个模式。D-CARD 保存有效折射率和模式分布等数据。

**语法** | **描述**
---|---
n=findmodes; | n 将等于找到的模式数。

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

**另请参阅**

[命令列表](../命令列表.md)、[setanalysis](./setanalysis.md)、[mesh](./mesh.md)、[selectmode](./selectmode.md)、[frequencysweep](./frequencysweep.md)、[coupling](./coupling.md)、[overlap](./overlap.md)、[bestoverlap](./bestoverlap.md)、[propagate](./propagate.md)