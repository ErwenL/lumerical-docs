# overlap

返回由 FDE 求解器计算或由 FDTD 或 varFDTD 模拟中的频率监视器记录的两个模式之间的重叠和功率耦合，或 rectilinear 数据集中记录的场分布。

重叠测量两个场分布（模式）之间重叠的电磁场比例。这也是可以在模式 1 中传播的模式 2 的功率比例（对于前向和后向传播的场）。取整个公式的绝对值以确保其为正。

$$ {\text { overlap }=\left| \operatorname{Re} \left[\frac{(\int \mathbf{E}_{1} \times \mathbf{H}_{2}^{*} \cdot d \mathbf{S}) (\int \mathbf{E}_{2} \times \mathbf{H}_{1}^{*} \cdot d \mathbf{S} ) }{\int \mathbf{E}_{1} \times \mathbf{H}_{1}^{*} \cdot d \mathbf{S} }\right] \frac{1}{ \operatorname{Re} ( \int \mathbf{E}_{2} \times \mathbf{H}_{2}^{*} \cdot d \mathbf{S} )} \right| } $$

**语法** | **描述**
---|---
out = overlap(mode2, mode1); | 

  * mode2、mode1：计算重叠的模式，输入可以是
    1. FDE 中的模式 D-CARD，字符串输入，例如 'mode1'、'mode2'
    2. FDTD 中频率监视器的名称，字符串输入，例如 'm1'、'm2'
    3. Rectilinear 数据集，详见下文
  * out(1)：模式重叠
  * out(2)：模式功率耦合

out = overlap(mode2, mode1, x, y,z); | 可以在计算重叠之前调整模式对齐方式。

  * x 偏移
  * y 偏移
  * z 偏移

偏移应用于列出的第二个模式，即本例中的 'mode1'。所有输入（FDE 模式名称、频率监视器、rectilinear 数据集）也适用于具有对齐调整的语法。

## 使用 Rectilinear 数据集

从 2024R2.3 开始，除监视器名称和 D-CARD 外，还支持具有任意场分布的 rectilinear 数据集。

但是，rectilinear 数据集不能与其他输入类型混合，但是，可以使用 getresult 脚本命令从模式中提取数据，如下例所示。

使用 rectilinear 数据集时，它们应包含属性名称 'E' 和 'H'，将分别用作电场和磁场。如果未找到属性名称 'E'，则假设数据集的第一个属性为电场。如果未找到属性 'H'，则假设电场属性之后的第一个属性为磁场。

**示例**

此示例演示如何使用 overlap 命令计算两个模式之间的重叠和功率耦合。

```
copydcard("mode1","test_mode1");copydcard("mode2","test_mode2");
out = overlap("test_mode1","test_mode2");
?out(1);  # 重叠
?out(2);  # 功率耦合

# 与上面相同的结果，但使用 rectilinear 数据集
EH1 = getresult("mode1","E"); # getresult 用于提取 E 和 H 数据
H1 = getresult("mode1","H");
EH1.addattribute("H",H1.H);
EH2 = getresult("mode2","E");
H2 = getresult("mode2","H");
EH2.addattribute("H",H2.H);
out2 = overlap(EH1,EH2);
?out2(1); # 重叠
?out2(2); # 功率耦合
```

**另请参阅**

- [命令列表](./命令列表.md)
- [copydcard](./copydcard.md)
- [findmodes](./findmodes.md)
- [coupling](./coupling.md)
- [bestoverlap](./bestoverlap.md)
- [propagate](./propagate.md)
- [expand](./expand.md)
- [expand2](./expand2.md)
- [optimizeposition](./optimizeposition.md)
