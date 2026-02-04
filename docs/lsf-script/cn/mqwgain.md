# mqwgain

mqwgain 脚本命令使用 4x4 k.p 电子带结构方法 [1-3] 计算多量子阱结构中 TE 和 TM 模式的增益和自发辐射。导带是抛物线形的，而重空穴和轻空穴价带根据 4x4 k.p 方法混合，它们是非抛物线的。

求解器包括常见 III-V 半导体、三元合金和四元合金的材料数据库。材料属性可以自动为任意合金成分生成，也可以手动输入。支持的材料列于下表中：

**III-V 半导体** | **三元合金** | **四元合金**
---|---|---
AlAs | AlxGa1-xAs | InxGa1-xAsyP1-y
GaAs | AlxGa1-xP | AlxGayIn1-x-yAs
InAs | AlxIn1-xP |
AlP | GaAsxP1-x |
GaP | InxAl1-xAs |
InP | InAsxP1-x |
 | InxGa1-xAs |
 | InxGa1-xP |

使用数据库材料时，三元合金 P(AxB1−xD) 的属性根据公式从基础材料（P(AD) 和 P(BD)）的属性插值得到

$$ P\left(A_x B_{1-x}D\right)=xP\left(AD\right)+\left(1-x\right)P\left(BD\right)+x\left(1-x\right)C, $$

其中 x 是成分分数，C 是弯曲参数（二次系数）。

AxB1-xCyD1-y 型四元合金（两个 III 族和两个 V 族元素）由三元合金成分的插值组成 [4]：

$$ P\left(A_xB_{1-x}C_yD_{1-y}\right)=\frac{x\left(1-x\right)\left[\left(1-y\right)P\left(A_xB_{1-x}D\right)+yP\left(A_xB_{1-x}C\right)\right]+y\left(1-y\right)\left[xP\left(AC_yD_{1-y}\right)+\left(1-x\right)P\left(BC_yD_{1-y}\right)\right]}{x\left(1-x\right)+y\left(1-y\right)}, $$

用于成分分数 x 和 y。例如，使用 InxGa1−xP、InxGa1−xAs、InAsyP1−y 和 GaAsyP1−y 的属性组合来定义 InxGa1−xAsyP1−y 的属性。

AxByC1-x-yD 型四元合金（三个 III 族元素和一个 V 族元素）由三元合金成分的插值组成 [4]：

$$ P\left(A_xB_yC_{1-x-y}D\right)=\frac{xyP\left(A_{1-u}B_uD\right)+y(1-x-y)P\left(B_{1-v}C_{v}D\right)+x(1-x-y)P\left(A_{1-w}C_{w}D\right)}{xy+y(1-x-y)+x(1-x-y)}, $$

用于成分分数 x 和 y，u = (1-x+y)/2，v = (2-x-2y)/2，w = (2-2x-y)/2。例如，使用 Al1-uGauAs、Ga1-vInvAs 和 Al1-wInwAs 的属性组合来定义 AlxGayIn1-x-yAs 的属性。

**语法** | **描述**
---|---
result = mqwgain(stack_properties, simulation_parameters, config); | stack_properties：定义 MQW 堆叠几何和材料属性的结构体。simulation_parameters：定义要计算输出的模拟参数的结构体。config：配置模拟行为的结构体。结果：在多个分区的情况下为结构体或结构体单元，每个结构体包含 4 个数据集：空间带图、(E,k) 空间中的带结构、每个 (E,k) 状态的空 间波函数以及发射系数。
result = mqwgain(stack_properties, simulation_parameters); | 与上述相同，但对 config 结构体中的字段使用所有默认值。

## 堆叠属性

**stack_properties** 是具有以下字段的结构体：

**字段** | **默认值** | **单位** | **类型** | **描述**
---|---|---|---|---
gamma |  | eV | 标量 | 由于带内弛豫率引起的线宽展宽。表示洛伦兹峰的半高全宽。
neff |  |  | 矩阵 | 有效指数 vs 频率。两列矩阵：第一列是频率（Hz），第二列是有效指数。有效指数值将线性插值到模拟的光子频率网格上。
length |  | m | 矩阵 | 每层的厚度，Nx1 数组（N 层）
material |  |  | 单元 | 材料定义，长度为 N 的单元数组。指定材料属性的选项描述见下文。
strain | 0 | (a0-a)/a | 矩阵 | 每层的应变（作为分数），负值表示压应变。Nx1 数组（N 层）。
vb | 未包含 |  | 结构体 | 价带绝对能量的规范。如果未定义，则默认使用 material.vb 字段。
eps | 量子力学平均值覆盖 MQW 堆叠材料 |  | 标量 | 相对静态介电常数。使用激子模型时需要。

**stack_properties.material** 是单元数组（每层一个元素），每个元素是一个结构体。结构体可以通过两种方式定义。

首先，通过调用 buildmqwmaterial 脚本命令自动生成：

**系数** | **单位** | **描述**
---|---|---
eg | eV | 带隙
ep | eV | 光学矩阵元的能量参数
me | 1/m0 | 电子有效质量
gamma1 |  | Luttinger 参数
gamma2 |  | Luttinger 参数
gamma3 |  | Luttinger 参数
ac | eV | 导带形变势
av | eV | 价带形变势
b | eV | 价带形变势
c11 | N/m2 | 弹性刚度系数
c12 | N/m2 | 弹性刚度系数
lc | m | 晶格常数
vb | eV | 价带绝对能量（所有层应有共同的参考）
eps |  | 相对静态介电常数

其次，使用 **stack_properties.material**：

**系数** | **类型** | **描述**
---|---|---
database_material | 字符串 | 材料名称
x | 0 | 材料成分（如果是三元或四元）
y | 0 | 材料成分（如果是四元）

## 堆叠属性

**stack_properties.vb** 是具有以下字段的结构体：

**字段** | **默认值** | **单位** | **类型** | **描述**
---|---|---|---|---
method | palankovski |  | 字符串 | 计算价带偏移的方法。如果指定为 "direct"，则必须提供偏移（见 offsets）。
offsets |  | eV | 矩阵 | 直接指定的价带偏移，Nx1 数组（N 层）。

**simulation_parameters** 是具有以下字段的结构体：

**字段** | **默认值** | **单位** | **类型** | **描述**
---|---|---|---|---
T |  | K | 标量 | 模拟温度。使用激子模型并假设完全耗尽量子阱（价带满、导带空）时，将忽略此参数。
V |  | V | 矩阵 | 静电势 vs 位置。两列矩阵，第一列指定位置（m），第二列指定电势（eV）。电势值将线性插值到模拟网格上。假设第一层从 z=0 开始。
kt | linspace(0,2*pi/a*0.1,51) | 1/m | 矩阵 | 用于带结构计算的横向 k 值。开启激子模型时只考虑 kt 点数，而忽略这些值，而是根据求解器使用的特殊求积方法定义。
stackpartitions | 空矩阵 |  | 矩阵 | 大小为（分区数）x 2 的矩阵，每行表示使用 1 基索引的起始和结束层索引。起始和结束层应该是阻挡层。例如，[1,3;3,5] 表示两个分区，第一个分区包含层 (1,2,3)，第二个分区包含层 (3,4,5)，其中层 1、3 和 5 表示阻挡层。
cdetect |  | 1/m3 | 矩阵 | 载流子密度数组。大小为（分区数）x（不同密度配置文件数）的矩阵。如果有多个分区，这允许定义空间相关密度，每个分区有不同的密度。如果没有分区，每个密度配置文件是表示整个堆叠平均密度的标量。使用激子模型并假设量子阱完全耗尽（价带满、导带空）时，将忽略此参数。
phfreq |  | Hz | 矩阵 | 光子频率数组。

**config** 是具有以下字段的结构体：

**字段** | **默认值** | **单位** | **类型** | **描述**
---|---|---|---|---
bcs | 见下文 | 见下文 | 结构体 | 边界条件结构体。
dz | 1e-10 | m | 标量 | 网格间距 ≥ 1Å。
numeigenvalues | 30 |  | 标量 | 每个 kt 处特征求解器要计算的最大带数。
numqwsubbandsCB | 2 |  | 标量 | 用于激子混合的导带子带最大数量。增加此值会导致更准确但更长的模拟。通常每耦合阱应使用约 2-4 个子带。
numqwsubbandsVB | 2 |  | 标量 | 用于激子混合的价带子带最大数量。增加此值会导致更准确但更长的模拟。这不包括自旋，因此实际子带数是此值的 2 倍。通常每耦合阱应使用约 2-4 个子带。
numqwsubbands | 2 |  | 标量 | 用于激子混合的子带（导带和价带）最大数量。（此字段已弃用。建议使用 numqwsubbandsCB/VB。）
materialdb |  |  | 字符串或结构体 | 指定材料数据库路径的字符串或空结构体（使用默认数据库）。
cbvalley | Gamma |  | 字符串 | 选择用于材料属性插值的导带谷："Gamma"、"X"、"L" 或 "All"（默认是 "Gamma"；"All" 选项使用最小带隙选择）。
reusebandstructure | false |  | 布尔值 | 如果有分区且此选项为 true，将重用第一个分区中计算的 MQW 带结构，从而减少模拟时间。当分区具有相似的带图（最多一个常数偏移）时，这是一个很好的近似。
exciton | false |  | 布尔值 | 开启激子模型。
wfthetadependence | false |  | 布尔值 | 开启量子阱平面中激子波函数的角依赖性。

**config.bcs** 是具有以下字段的结构体：

**字段** | **默认值** | **单位** | **类型** | **描述**
---|---|---|---|---
pmlactive | false |  | 布尔值 | 在边界处启用完美匹配层。
pmlcutoff | [1e-2,1e-2] |  | 矩阵 | 阈值比（PML 概率密度）/(MQW 概率密度)，导带一个，价带一个，拒绝位于 PML 中过多的导带和价带概率密度的本征态，2x1 数组。低于此阈值的 QW 束缚态。
pmllength | [10e-9,10e-9] | m | 矩阵 | 左右边界的 PML 厚度，2x1 数组。
pmlcoefficient | [0.5+1i*0.5,0.5+1i*0.5,-1+1i*1.4,-1+1i*1.4] |  | 矩阵 | PML 复坐标拉伸系数。前两个元素用于导带的左右 PML，后两个用于价带。
hwcutoff | [5e-4,5e-4] | \(A^{-3/2}\) | 矩阵 | 阈值波函数斜率，导带一个，价带一个，拒绝在左右硬壁边界处衰减不足的本征态，2x1 数组。低于此阈值的 QW 束缚态。

**result** 是每个分区的结构体单元（如果有分区），或如果没有分区则为结构体，结构体包含以下字段：

**语法** | **类型** | **描述**
---|---|---
banddiagram | 数据集 | 包括应变但不包括量子限制效应（即子带）的导带和价带边。
bandstructure | 数据集 | 导带和价带的 (E,kt) 带图。关闭激子模型时，属性为：conduction_band、valence_band_lo 和 valence_band_up，其中价带中的 4x4 k.p 基变换为两个 2x2 基（lo 表示下，up 表示上）。更多信息请参阅参考文献 [1] 和 [2]。开启激子模型时，属性为：conduction_band、valence_band，价带中的 4x4 k.p 基（基未变换）。参数为 kt 和 subband。
wavefunction | 数据集 | 每个 (E,kt) 点的空间波函数。开启激子模型时，属性为：conduction_band_1、valence_band_lo_1、valence_band_lo_2、valence_band_up_1、valence_band_up_2，其中价带中的 4x4 k.p 基被拆分为两个 2x2 基（lo 表示下，up 表示上），每个 2x2 基中的向量用 1 和 2 指定。更多信息请参阅参考文献 [1] 和 [2]。开启激子模型时，属性为：conduction_band_1、valence_band_1、valence_band_2、valence_band_3、valence_band_4，价带中的 4x4 k.p 基（基未变换），4x4 基中的向量用 1、2、3 和 4 指定。参数为 coordinate、kt 和 subband。
ome | 数据集 | 光学矩阵元。关闭激子时：动量矩阵元除以自由电子质量的模的平方。单位为 \(eV\)。属性为 ome_lo_TE、ome_lo_TM、ome_up_TE、ome_up_TM，其中 TE 和 TM 表示光学模式，up 和 lo 表示与 bandstructure 和 wavefunction 相同的 2x2 基。参数为 kt（横向波向量）、CBsubband（导带子带索引）和 VBsubband（价带子带索引）。开启激子时：单位为 \(1/nm^2\) 的每单位面积振子强度。属性为 ome_TE 和 ome_TM，其中 TE 和 TM 表示光学模式。参数为激子轨道量子数（orbital）和角动量量子数（angularMomentum）。
emission | 数据集 | 单位为 [1/m] 的增益和自发辐射系数。属性为：spontaneous_TE、spontaneous_TM、stimulated_TE、stimulated_TM，其中 TE 和 TM 表示电磁模式。参数为：频率/能量/波长和 ndensity（电荷密度）。发射系数针对整个堆叠厚度（包括阻挡层）计算。如果只关心量子阱厚度（不包括阻挡层），这些系数应通过乘以（总长度）/(总 QW 长度) 进行缩放。确保发射系数仅适用于用于计算与增益区域模式重叠的厚度是很重要的。使用分区时，不同分区之间会有重叠的阻挡层，例如 simulation_parameters.stackpartitions = [1,3;3,5]，其中 1、3 和 5 是阻挡层。在这种情况下，每个分区的发射系数再次适用于该分区的总厚度，这意味着相对于模式重叠区域厚度可能存在一些重复计算。为了避免这种情况，发射系数可以缩放以仅适用于量子阱，或适用于不与相邻分区重叠的分区的部分。开启激子模型时，属性变为：absorption_TE、absorption_TM。这些是单位为 [1/m] 的吸收系数（负增益）。由于假设量子阱中的载流子密度完全耗尽，因此不计算自发辐射。
ex | 数据集 | 激子能量 Ex。激子能量是激子轨道量子数（orbital）和角动量量子数（angularMomentum）的函数。
phix | 数据集 | 动量（平面内波向量）空间中的激子波函数 PhiX。波函数系数用导带子带索引（cSubband）、价带子带索引（vSubband）、横向波向量（kt）、角动量量子数（angularMomentum）和轨道量子数（orbital）参数化。

## 材料定义

材料参数对于准确计算 MQW 带结构和发射特性很重要。许多参数用于模拟材料的光学和电子行为。化合物半导体的合金的一些参数无法从实验中获得，必须从已知值的插值生成。实验结果可能取决于生长条件和层厚度，可能需要调整一些材料参数以获得与测量结果的一致性。

Lumerical 提供了 MQW 增益求解器的默认材料数据库。当层材料通过名称和成分分数定义时，这些参数会自动使用。以下代码将第 2 层的材料设置为 Al0.41Ga0.59As

```
materials = cell(3);
#...
materials{2} = struct;
materials{2}.database_material = "AlGaAs";
materials{2}.x = 0.41;
```

您也可以选择使用自己的材料数据库（格式相同）而不是 Lumerical 提供的默认数据库。通过在模拟配置结构体中指定该数据库的路径，您可以指示求解器使用这些材料定义，例如：

```
config.materialdb = "/home/auser/myfolder/my_material_db.json";
```

使用这种方法，可以修改化合物半导体的材料参数，但求解器使用的默认插值仍将应用于生成三元和四元半导体的参数。层材料的分配不会改变。

或者，可以使用 buildmqwmaterial 命令直接从材料数据库（默认或自定义）中读取材料定义，并作为结构体加载到脚本工作区中。例如：

```
mymat = buildmqwmaterial("/home/auser/my_folder/my_material_db.json", 300, "InAlAs", 0.47);
```

将从材料数据库中读取必要的属性，并在 T=300K 下构建成分分数 x=0.47 的 In0.47Al0.53As 的材料定义。结果是一个包含 MQW 求解器所需系数的结构体。具有这些字段的结构体可以分配给材料层并由求解器直接使用，例如：

```
materials = cell(3);
#...
materials{2} = buildmqwmaterial("/home/auser/my_folder/my_material_db.json", 300, "InAlAs", 0.47);
```

### 参考文献

[1] D. Ahn 等，J. Appl. Phys. 64, 4056 (1988)

[2] S. L. Chuang，光电子器件物理

[3] Chuang，Phys. Rev. B, 43, 9649 (1991)

[4] Vurgaftman 等，J. Appl. Phys., 89, 5815 (2001)

[5] C. Y.-P. Chao 等，Phys. Rev. B, 48, 8210 (1993)

### 另请参阅

- [buildmqwmaterial](./buildmqwmaterial.md)
- [mqwindex](./mqwindex.md)
- [边发射激光器示例](https://apps.lumerical.com/mqw-edge-emitting-laser.html)
- [MQW 产品参考手册](./MQW%20产品参考手册.md)
