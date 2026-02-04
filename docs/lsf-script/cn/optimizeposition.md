# optimizeposition

optimizeposition 命令计算在使用 FDE 求解器时导致指定模式与 d-card 之间最大重叠的 x 偏移、y 偏移和 z 偏移。

x 偏移、y 偏移和 z 偏移对应于 d-card 配置文件中的 x、y 和 z 偏移。

此函数还填充重叠和功率耦合，以及 x 偏移、y 偏移和 z 偏移位置，类似于在 GUI 中单击 "Optimize position" 按钮时，在特征求解器分析窗口的重叠分析选项卡中。

有关重叠和耦合计算的更多详细信息，请参阅 overlap 函数。

**语法** | **描述**
---|---
out = optimizeposition(mode number, d-card number); | 

  * mode number：模式列表中的模式编号
  * d-card number：d-card 在 deck 中的编号

请注意，必须选择 "shift d-card center" 选项才能使用此函数。

**示例**

此示例演示如何使用 optimizeposition 命令计算指定模式与 d-card 之间导致最大重叠的 x 偏移、y 偏移和 z 偏移，打印偏移值以及应用偏移后的最优重叠和功率耦合。

```
setanalysis("shift d-card center",1);
shift = optimizeposition(4,1); # 找到 x、y、z 偏移，使模式列表中的第 4 个模式与 deck 中的第 1 个模式之间达到最优重叠

?"x shift:"+num2str(shift(1));
?"y shift:"+num2str(shift(2));
?"z shift:"+num2str(shift(3));

out = overlap("mode4","global_mode1",shift(1),shift(2),shift(3));
?"maximum overlap:"+num2str(out(1));
?"maximum power coupling:"+num2str(out(2));
```

**另请参阅**

- [命令列表](./命令列表.md)
- [copydcard](./copydcard.md)
- [findmodes](./findmodes.md)
- [coupling](./coupling.md)
- [overlap](./overlap.md)
- [bestoverlap](./bestoverlap.md)
- [propagate](./propagate.md)
- [expand](./expand.md)
- [setanalysis](./setanalysis.md)
