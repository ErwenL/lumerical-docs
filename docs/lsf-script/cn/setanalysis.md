<!--
Translation from English documentation
Original command: setanalysis
Translation date: 2026-02-03
-->

# setanalysis

设置 MODE 的 FDE 和 FEEM 分析窗口中的计算参数。

**语法** | **描述**
---|----
?setanalysis; | 列出分析窗口中的所有参数。
setanalysis("property", value); | 将"property"设置为 value。

**示例**

对第一个模式进行频率扫描并绘制色散图：

```lsf
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

**另请参见**

- [mesh](./mesh.md)
- [findmodes](./findmodes.md)
- [frequencysweep](./frequencysweep.md)
- [analysis](./analysis.md)
- [getanalysis](./getanalysis.md)
