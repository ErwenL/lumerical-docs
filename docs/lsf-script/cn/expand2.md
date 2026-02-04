# expand2

返回在两个任意 DFT 监视器、D-CARD 或两个直线数据集中记录的场之间的非共轭形式展开系数。非共轭形式的系数定义如下：

$$ \begin{array}{l}{a=0.25^{*}\left(\frac{\int d \mathbf{S} \cdot \mathbf{E}_{1} \times \mathbf{H}_{2}}{N}+\frac{\int d \mathbf{S} \cdot \mathbf{E}_{2} \times \mathbf{H}_{1}}{N}\right)} \\\ {b=0.25^{*}\left(\frac{\int d \mathbf{S} \cdot \mathbf{E}_{1} \times \mathbf{H}_{2}}{N}-\frac{\int d \mathbf{S} \cdot \mathbf{E}_{2} \times \mathbf{H}_{1}}{N}\right)} \\\ {N=0.5 * \int d \mathbf{S}\cdot \mathbf{E}_{2} \times \mathbf{H}_{2}} \\\ {P=0.5^{*} \int d \mathbf{S} \cdot \mathbf{E}_{1} \times \mathbf{H}_{1}}\end{array} $$

有关如何使用此命令、参数定义以及如何解释结果的更多详细信息，请参阅 [使用模式扩展监视器](https://optics.ansys.com/hc/en-us/articles/360034902433-Using-Mode-Expansion-Monitors)。

**语法** | **描述**
---|---
expand2(mode1,mode_ref,x,y,z); | 输出两个模式场之间的非共轭形式展开系数

- mode1, mode_ref：场信息，其中 \\(\mathbf{E}_{1},\mathbf{H}_{1}\\) 包含在 mode1 中，\\(\mathbf{E}_{2},\mathbf{H}_{2}\\) 包含在 mode_ref 中。可以是以下格式之一：
    - 频域监视器名称，字符串输入，例如 "monitor1"
    - 包含场信息的模式 D-CARD，字符串输入，例如 "mode1"
    - 直线数据集，更多信息见下文
- x,y,z：monitor1 的场相对于 monitor_ref 的场的空间位移

## 使用直线数据集

从 2024R2.3 开始，除了监视器名称和 D-CARD 外，还支持具有任意场分布的直线数据集。

直线数据集 **不能** 与其他输入类型混合使用，但是可以使用 [getresult 脚本命令](https://optics.ansys.com/hc/en-us/articles/360034409854-getresult-Script-command) 从模式中提取数据，如下例所示。

使用直线数据集时，它们应包含属性名称 "E" 和 "H"，分别用作电场和磁场。如果未找到属性名称 "E"，则假定数据集的第一个属性为电场。如果未找到属性 "H"，则假定电场属性之后的数据集第一个属性为磁场。

**示例**

以下脚本将监视器 "R" 的场展开到参考监视器 "R_ref" 上（非共轭形式）：

```powershell
M = expand2("R","R_ref",0,0,0);
f = getdata("R","f");
a = pinch(M,1,1);
b = pinch(M,1,2);
n = pinch(M,1,3);
p = pinch(M,1,4);
S11 = b;
```

以下脚本首先使用 getresult 将监视器 "R" 和参考监视器 "R_ref" 的场转换为直线数据集，然后将 "R" 的场展开到 "R_ref" 上（非共轭形式）。结果与上述相同。

```powershell
# 使用直线数据集的示例
#首先，使用 getresult 从监视器获取直线数据集
#这些数据集也可以从其他地方导入
EH1 = getresult("R","E");
H1 = getresult("R","H");
EH1.addattribute("H",H1.H);
EH2 = getresult("R_ref","E");
H2 = getresult("R_ref","H");
EH2.addattribute("R_ref",H2.H);

M = expand2(EH1,EH2,0,0,0);
f = EH1.f;
a = pinch(M,1,1);
b = pinch(M,1,2);
n = pinch(M,1,3);
p = pinch(M,1,4);
S11 = b;
```

**另请参阅**

[命令列表](../命令列表.md)、[使用模式扩展监视器](https://optics.ansys.com/hc/en-us/articles/360034902433-Using-Mode-Expansion-Monitors)、[setexpansion](./setexpansion.md)、[removeexpansion](./removeexpansion.md)、[expand](./expand.md)