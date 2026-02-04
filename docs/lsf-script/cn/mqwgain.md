<!--
Translation from English documentation
Original command: mqwgain
Translation date: 2026-02-04 22:50:14
-->

# mqwgain

The 脚本 命令 mqwgain 计算 gain 和 spontaneous emission 用于 TE 和 TM modes 在 multiple quantum well structures 使用 该 4x4 k.p electronic band 结构 method [1-3]. The conduction band 是 parabolic, while heavy 和 light hole valence bands 是 mixed according 到 该 4x4 k.p method 和 they 是 nonparabolic.

The 求解器 includes 一个 材料 database 的 common III-V semiconductors, ternary alloys, 和 quaternary alloys. Material 属性 可能 为 generated automatically 用于 arbitrary alloy compositions 或 可能 为 input manually. The supported materials 是 listed 在 该 table below:

**III-V semiconductors** |  **Ternary alloys** |  **Quaternary Alloys**  
---|---|---  
AlAs |  AlxGa1-xAs |  InxGa1-xAsyP1-y  
GaAs |  AlxGa1-xP | AlxGayIn1-x-yAs  
InAs |  AlxIn1-xP |   
AlP |  GaAsxP1-x |   
GaP |  InxAl1-xAs |   
InP |  InAsxP1-x |   
|  InxGa1-xAs |   
|  InxGa1-xP |   
  
When database materials 是 used, 该 属性 的 ternary alloys P(AxB1−xD) 是 interpolated 从 该 对应的 属性 的 该 base materials (P(AD) 和 P(BD)) according 到 该 formula

$$ P\left(A_x B_{1-x}D\right)=xP\left(AD\right)+\left(1-x\right)P\left(BD\right)+x\left(1-x\right)C, $$

其中 x 是 该 composition fraction 和 C 是 该 bowing 参数 (quadratic coefficient).

Quaternary alloys 的 类型 AxB1-xCyD1-y (two group III 和 two group V elements) 是 composed 从 该 interpolation 的 ternary alloy constituents [4]:

$$ P\left(A_xB_{1-x}C_yD_{1-y}\right)=\frac{x\left(1-x\right)\left[\left(1-y\right)P\left(A_xB_{1-x}D\right)+yP\left(A_xB_{1-x}C\right)\right]+y\left(1-y\right)\left[xP\left(AC_yD_{1-y}\right)+\left(1-x\right)P\left(BC_yD_{1-y}\right)\right]}{x\left(1-x\right)+y\left(1-y\right)}, $$

用于 composition fractions x 和 y. For example, 一个 combination 的 该 属性 的 InxGa1−xP, InxGa1−xAs, InAsyP1−y, 和 GaAsyP1−y 是 used 到 define 该 属性 的 InxGa1−xAsyP1−y.

Quaternary alloys 的 类型 AxByC1-x-yD (three group III elements 和 one group V 元素) 是 composed 从 该 interpolation 的 ternary alloy constituents [4]:

$$ P\left(A_xB_yC_{1-x-y}D\right)=\frac{xyP\left(A_{1-u}B_uD\right)+y(1-x-y)P\left(B_{1-v}C_{v}D\right)+x(1-x-y)P\left(A_{1-w}C_{w}D\right)}{xy+y(1-x-y)+x(1-x-y)}, $$

用于 composition fractions x 和 y 和 u = (1-x+y)/2, v = (2-x-2y)/2, w = (2-2x-y)/2. For example, 一个 combination 的 该 属性 的 Al1-uGauAs, Ga1-vInvAs, 和 Al1-wInwAs, 是 used 到 define 该 属性 的 AlxGayIn1-x-yAs.

**语法** |  **描述**  
---|---  
result = mqwgain(stack_properties, simulation_parameters, config); |  stack_properties: 结构体 使用 fields 该 define MQW stack geometry 和 材料 属性. simulation_parameters: 结构体 使用 fields 该 define 仿真 参数 用于 该 该 output 将 为 calculated. config: 结构体 使用 fields 该 configure 该 behavior 的 该 仿真. result: 结构体 或 一个 单元格 的 structs 在 case 的 multiple partitions, 其中 each 结构体 contains 4 datasets: spatial band diagram, band 结构 在 (E,k) space, spatial wave functions 用于 each (E,k) state, 和 emission coefficients.  
result = mqwgain(stack_properties, simulation_parameters); |  same as above, but 使用 all default 值 用于 该 fields 在 该 config 结构体.  
  
## Stack 属性

**stack_properties** 是 一个 结构体 使用 该 following fields:

**Field** |  **Default** |  **Units** |  **Type** |  **描述**  
---|---|---|---|---  
gamma |  |  eV |  Scalar |  Linewidth broadening due 到 intraband relaxation rate. Represents full width at half maximum 的 一个 Lorentzian.  
neff |  |  |  Matrix |  Effective index vs. 频率. Two-column 矩阵: 该 first column 是 该 频率 (Hz), 和 该 second column 是 该 effective index. Effective index 值 将 为 linearly interpolated onto 该 photon 频率 grid 用于 该 仿真.  
长度 |  |  m |  Matrix |  The thickness 的 each layer, Nx1 数组 (N layers)  
材料 |  |  |  Cell |  Material definitions, 长度 N 单元格 数组. See below 用于 一个 description 的 options 到 specify 材料 属性.  
strain |  0 |  (a0-一个)/一个 |  Matrix |  Strain 在 each layer as 一个 fraction, negative 值 用于 compressive strain. Nx1 数组 (N layers).  
vb |  Not included |  |  Struct |  Specification 用于 valence band absolute energy. If not defined, 那么 材料.vb field 是 used 通过 default.  
eps |  quantum mechanical average over MQW stack materials |  |  Scalar |  Relative static permittivity. Needed 当 exciton model 是 used.  
  
**stack_properties.材料** 是 一个 单元格 数组 (one 元素 per layer) 其中 each 元素 是 一个 结构体. The 结构体 可以 为 defined 在 2 ways.

First, automatically generated 通过 calling [ buildmqwmaterial ](/hc/en-us/articles/360034926553-buildmqwmaterial) 脚本 命令:

**Coefficient** |  **Units** |  **描述**  
---|---|---  
eg |  eV |  Band gap  
ep |  eV |  Energy 参数 用于 该 optical 矩阵 元素  
me |  1/m0 |  Electron effective mass  
gamma1 |  |  Luttinger 参数  
gamma2 |  |  Luttinger 参数  
gamma3 |  |  Luttinger 参数  
ac |  eV |  Conduction band deformation potential  
av |  eV |  Valence band deformation potential  
b |  eV |  Valence band deformation potential  
c11 |  N/m2 |  Elastic stiffness coefficient  
c12 |  N/m2 |  Elastic stiffness coefficient  
lc |  m |  Lattice constant  
vb |  eV |  Valence band absolute energy (all layers 应该 have 一个 common reference)  
eps |  |  Relative static permittivity  
  
Second, 使用 **stack_properties.材料:**

**Coefficient** |  **Type** |  **描述**  
---|---|---  
database_material |  String |  Name 的 该 材料  
x |  0 |  Material composition (如果 ternary 或 quaternary)  
y |  0 |  Material composition (如果 quaternary)  
  
## Stack 属性

**stack_properties.vb** 是 一个 结构体 使用 该 following fields:

**Field** |  **Default** |  **Units** |  **Type** |  **描述**  
---|---|---|---|---  
method |  palankovski |  |  String |  Method 用于 calculating valence band offsets. If “direct” 是 specified, 该 off设置必须 为 provided (see offsets)。  
off设置|  |  eV |  Matrix |  Directly specified valence band offsets, Nx1 数组 (N layers)。  
  
**simulation_parameters** 是 一个 结构体 使用 该 following fields:

**Field** |  **Default** |  **Units** |  **Type** |  **描述**  
---|---|---|---|---  
T |  |  K |  Scalar |  Simulation temperature. This 参数 是 ignored 当 该 exciton model 是 used 和 full depletion 的 该 quantum wells 是 assumed (valence band full, conduction band empty).  
V |  |  V |  Matrix |  Electrostatic potential vs. position. A two-column 矩阵, 使用 position (m) specified 在 该 first column 和 potential (eV) specified 在 该 second column. Potential 值 将 为 linearly interpolated onto 该 仿真 grid. The first layer 是 assumed 到 start at z=0.  
kt |  linspace(0,2*pi/一个*0.1,51) |  1/m |  Matrix |  Transverse k 值 是 used 在 该 band 结构 calculation. When 该 exciton model 是 turned 在 only 该 数字 的 kt points 是 considered, while 该 值 是 ignored 和 instead defined based 在 一个 special quadrature method used 通过 该 求解器.  
stackpartitions |  empty 矩阵 |  |  Matrix |  Matrix 的 size (数字 的 partitions) x 2, 其中 each row represents 该 start 和 end layer index 用于 one partition 使用 1-based indexing. Start 和 end layers 应该 为 barriers. For example, [1,3;3,5] represents two partitions 其中 该 first partition contains layers (1,2,3) 和 该 second partition contains layers (3,4,5), 其中 layers 1, 3, 和 5 represent barriers.  
cden |  |  1/m3 |  Matrix |  Carrier density 数组. Matrix 的 size (数字 的 partitions) x (数字 的 different density profiles). If there 是 more than one partition 此 enables defining spatially dependent density, 其中 each partition has 一个 different density. If there 是 no partitioning, each density profile 是 一个 scalar representing 该 average density over 该 entire stack. This 参数 是 ignored 当 该 exciton model 是 used 和 full depletion 的 该 quantum wells 是 assumed (valence band full, conduction band empty).  
phfreq |  |  Hz |  Matrix |  Photon 频率 数组.  
  
**config** 是 一个 结构体 使用 该 following fields:

**Field** |  **Default** |  **Units** |  **Type** |  **描述**  
---|---|---|---|---  
bcs |  See below |  See below |  Struct |  Boundary conditions 结构体.  
dz |  1e-10 |  m |  Scalar |  Grid spacing ≥ 1Å.  
numeigenvalues |  30 |  |  Scalar |  The maximum 数字 的 bands 到 计算 通过 该 eigensolver at each kt.  
numqwsubbandsCB |  2 |  |  Scalar |  The maximum 数字 的 conduction subbands 到 use 用于 exciton mixing. Increasing 此 值 results 在 一个 more accurate but longer 仿真. In general, around 2-4 subbands per coupled well 应该 为 used.  
numqwsubbandsVB |  2 |  |  Scalar |  The maximum 数字 的 valence subbands 到 use 用于 exciton mixing. Increasing 此 值 results 在 一个 more accurate but longer 仿真. This does not include spin, so 该 actual 数字 的 subbands 是 2x 此 值. Generally, around 2-4 subbands per coupled well 应该 为 used.  
numqwsubbands |  2 |  |  Scalar |  The maximum 数字 的 subbands (both conduction 和 valence) 到 use 用于 exciton mixing. (This field 是 deprecated. Recommend 使用 numqwsubbandsCB/VB instead.)  
materialdb |  |  |  String 或 结构体 |  A 字符串 specifying 该 path 到 该 材料 database 或 empty 结构体 用于 该 default database.  
cbvalley |  Gamma |  |  String |  Choose 该 conduction band valley 用于 interpolation 的 材料 属性: “Gamma”, “X”, “L”, 或 “All” (default 是 “Gamma”; option “All” uses 该 lowest band gap 到 select).  
reusebandstructure |  false |  |  Boolean |  If there 是 partitioning 和 此 option 是 true, 该 MQW band 结构 calculated 在 该 first partition 将 为 reused 在 all other partitions, reducing 仿真 时间. This 是 一个 good approximation whenever partitions have 一个 similar band diagram (up 到 一个 constant shift).  
exciton |  false |  |  Boolean |  Turns 在 exciton model.  
wfthetadependence |  false |  |  Boolean |  Turns 在 该 angular dependence 的 该 exciton wave 函数 在 该 plane 的 quantum wells.  
  
**config.bcs** 是 一个 结构体 使用 该 following fields:

**Field** |  **Default** |  **Units** |  **Type** |  **描述**  
---|---|---|---|---  
pmlactive |  false |  |  Boolean |  Enable perfectly matched layer at boundaries.  
pmlcutoff |  [1e-2,1e-2] |  |  Matrix |  Threshold ratio (PML probability density)/(MQW probability density), one 用于 conduction 和 one 用于 valence bands, 到 reject eigenstates 使用 excess conduction 和 valence band probability densities located 在 该 PMLs, 2x1 数组. The QW bound states 是 那些 below 此 threshold.  
pmllength |  [10e-9,10e-9] |  m |  Matrix |  PML thickness 用于 left 和 right boundaries, 2x1 数组.  
pmlcoefficient |  [0.5+1i*0.5,0.5+1i*0.5,-1+1i*1.4,-1+1i*1.4] |  |  Matrix |  PML complex coordinate stretching coefficients. First two elements 是 用于 left 和 right PML 用于 该 conduction band 和 该 other two 用于 该 valence band.  
hwcutoff |  [5e-4,5e-4] |  \\( A^{-3/2} \\) |  Matrix |  Threshold wave 函数 slope, one 用于 conduction 和 one 用于 valence bands, 到 reject eigenstates 该 do not decay enough at 该 left 和 right hard-wall boundaries, 2x1 数组. The QW bound states 是 那些 below 此 threshold.  
  
**result** 是 一个 单元格 的 structs 用于 each partition 如果 there 是 partitioning, 或 一个 结构体 如果 there 是 no partitioning, 其中 structs contain 该 following fields:

**语法** |  **Type** |  **描述**  
---|---|---  
banddiagram |  dataset |  Conduction 和 valence band edge including strain, but not including quantum confinement effects (i.e. subbands).  
bandstructure |  dataset |  (E,kt) band diagram 用于 conduction 和 valence bands. With 该 exciton model turned off 该 attributes 是: conduction_band, valence_band_lo, 和 valence_band_up, 其中 该 4x4 k.p basis 在 该 valence band 是 transformed into two 2x2 bases (lo 用于 lower 和 up 用于 upper). For more information look at references [1] 和 [2]. With 该 exciton model turned 在 该 attributes 是: conduction_band, valence_band, 使用 该 4x4 k.p basis 在 该 valence band (该 basis 是 not transformed). Parameters 是 kt 和 subband.  
wavefunction |  dataset |  Spatial wavefunction 用于 each (E,kt) point. With 该 exciton model turned 在 该 attributes 是: conduction_band_1, valence_band_lo_1, valence_band_lo_2, valence_band_up_1, valence_band_up_2, 其中 该 4x4 k.p basis 在 该 valence band 是 split into two 2x2 bases (lo 用于 lower 和 up 用于 upper) 和 该 vectors 在 each 2x2 basis 是 designated 使用 1 和 2. For more information look at references [1] 和 [2]. With 该 exciton model turned 在 该 attributes 是: conduction_band_1, valence_band_1, valence_band_2, valence_band_3, valence_band_4, 使用 该 4x4 k.p basis 在 该 valence band (该 basis 是 not transformed) 和 该 vectors 在 该 4x4 basis designated 使用 1, 2, 3, 和 4. Parameters 是 coordinate, kt, 和 subband.  
ome |  dataset |  Optical 矩阵 元素. With excitons turned off: Magnitude squared 的 该 momentum 矩阵 元素 divided 通过 该 free electron mass. In 该 units 的 \\(eV\\). Attributes 是 ome_lo_TE, ome_lo_TM, ome_up_TE, ome_up_TM, 其中 TE 和 TM designate optical modes 和 up 和 lo refer 到 该 2x2 bases, same as 用于 该 bandstructure 和 wavefunction. Parameters 是 kt (transverse wave 向量), CBsubband (conduction band subband index) 和 VBsubband (valence band subband index). With excitons turned 在: Oscillator strength per unit area 在 该 units 的 \\(1/nm^2\\). Attributes 是 ome_TE 和 ome_TM 其中 TE 和 TM designate optical modes. Parameters 是 该 exciton orbital quantum 数字 (orbital) 和 angular momentum quantum 数字 (angularMomentum).  
emission |  dataset |  Gain 和 spontaneous emission coefficients 在 该 units 的 [1/m]. Attributes 是: spontaneous_TE, spontaneous_TM, stimulated_TE, stimulated_TM, 其中 TE 和 TM stand 用于 electromagnetic modes. Parameters 是: 频率/energy/波长 和 ndensity (电荷 density). Emission coefficients 是 calculated 用于 该 total stack thickness, including barriers. If only 该 quantum well thickness 是 的 interest, excluding barriers, 这些 coefficients 应该 为 scaled 通过 multiplying 使用 (total 长度)/(total QW 长度). It 是 important 到 ensure 该 emission coefficients apply only 到 该 thickness used 用于 该 calculation 的 该 mode overlap 使用 该 gain region. When 使用 partitioning, there 将 为 overlapping barriers between different partitions, e.g. simulation_parameters.stackpartitions = [1,3;3,5], 其中 1, 3, 和 5 是 barriers. In 该 case emission coefficients 用于 each partition again apply 到 该 total thickness 的 该 partition, meaning there 可能 为 some double-counting 使用 respect 到 该 mode overlap region thickness. To avoid 此, emission coefficients 可以 为 scaled 到 apply 到 quantum wells only, 或 到 apply 到 一个 portion 的 该 partition 该 does not overlap 使用 adjacent partitions. When 该 exciton model 是 turned 在 该 attributes become: absorption_TE, absorption_TM. These represent 该 absorption coefficients (negative gain) 在 该 units 的 [1/m]. The spontaneous emission 是 not calculated due 到 该 assumption 的 该 depleted carrier density 在 该 quantum wells.  
ex |  dataset |  Exciton energies Ex. Exciton energies 是 一个 函数 的 exciton orbital quantum 数字 (orbital) 和 angular momentum quantum 数字 (angularMomentum).  
phix |  dataset |  Exciton wavefunctions PhiX 在 该 momentum (在-plane wavevector) space. The wave 函数 coefficients 是 parametrized 在 terms 的 conduction band subband index (cSubband), valence band subband index (vSubband), transverse wave 向量 (kt), 和 angular momentum quantum 数字 (angularMomentum), 和 orbital quantum 数字 (orbital).  
  
## Material Definitions

Material 参数 是 important 用于 该 accurate calculation 的 该 MQW band 结构 和 emission characteristics. Many 参数 是 used 到 model 该 optical 和 electronic 材料 behavior. Some 参数 用于 alloys 的 compound semiconductors 是 not available 从 experiments 和 必须 为 generated 从 interpolation 的 known 值. Experimental results 可能 depend 在 growth conditions 和 layer thickness, 和 adjustment 的 some 材料 参数 可能 为 necessary 到 obtain agreement 使用 measurements.

Lumerical provides 一个 default 材料 database 使用 该 MQW gain 求解器. These 参数 是 used automatically 当 该 layer materials 是 defined 通过 一个 name 和 composition fraction. The following code 设置 该 材料 在 layer 2 as Al  0.41  Ga  0.59  As
    
    
    materials = 单元格(3); 
    #... 
    materials{2} = 结构体; 
    materials{2}.database_material = "AlGaAs"; 
    materials{2}.x = 0.41; 

You 可以 also choose 到 use your own 材料 database (在 该 same format) instead 的 该 default 材料 database supplied 通过 Lumerical. By specifying 该 path 的 该 database 在 该 仿真 configuration 结构体, you 可以 instruct 该 求解器 到 use 那些 材料 definitions, e.g.
    
    
    config.materialdb = "/home/auser/myfolder/my_material_db.json"; 

Using 此 approach, 该 材料 参数 的 该 compound semiconductors 可以 为 modified, but 该 default interpolation used 通过 该 求解器 将 still 为 applied 到 generate 参数 用于 ternary 和 quaternary semiconductors. The assignment 的 materials 到 layers does not change.

Alternately, 一个 材料 definition 可以 为 read directly 从 一个 材料 database (default 或 自定义) 和 loaded as 一个 结构体 into 该 脚本 workspace 使用 该 [buildmqwmaterial ](/hc/en-us/articles/360034926553-buildmqwmaterial) 命令. For example,
    
    
    mymat = buildmqwmaterial("/home/auser/myfolder/my_material_db.json", 300, "InAlAs", 0.47);  

将 read 该 necessary 属性 从 该 材料 database 和 build 一个 材料 definition at T=300K 使用 composition fraction x=0.47 用于 In  0.47  Al  0.53  As. The result 是 一个 结构 使用 该 coefficients required 通过 该 MQW 求解器. A 结构体 使用 这些 fields 可以 为 assigned 到 一个 材料 layer 和 used directly 通过 该 求解器, e.g.
    
    
    materials = 单元格(3); 
    #... 
    materials{2} = buildmqwmaterial("/home/auser/myfolder/my_material_db.json", 300, "InAlAs", 0.47);

### References

[1] D. Ahn et al., J. Appl. Phys. 64, 4056 (1988)

[2] S. L. Chuang, Physics 的 Optoelectronic Devices

[3] Chuang, Phys. Rev. B, 43, 9649 (1991)

[4] Vurgaftman et al., J. Appl. Phys., 89, 5815 (2001)

[5] C. Y.-P. Chao et al., Phys. Rev. B, 48, 8210 (1993)

### 参见

[ buildmqwmaterial](/hc/en-us/articles/360034926553-buildmqwmaterial), [mqwindex](/hc/en-us/articles/360041072553), [edge emitting laser example](https://apps.lumerical.com/mqw-edge-emitting-laser.html), [MQW product reference manual](/hc/en-us/articles/360038463833)
