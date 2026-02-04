<!--
Translation from English documentation
Original command: buildmqwmaterial
Translation date: 2026-02-04 22:49:36
-->

# buildmqwmaterial

创建 一个 结构体 使用 材料 参数 用于 use 使用 [mqwgain](/hc/en-us/articles/360034926533-mqwgain) 和 [mqwindex](/hc/en-us/articles/360041072553) commands.

**语法** |  **描述**  
---|---  
result = buildmqwmaterial(location, T, matname, x); |  Ternary materials. location: 字符串 specifying 该 path 到 该 database 文件. Alternatively, 如果 empty 结构体, 该 default database 将 为 used. T: temperature. matname: ternary 材料 name. x: 材料 composition. result: 结构体 使用 材料 属性.  
result = buildmqwmaterial(location, 300, matname, x, cbValley); |  same as above 使用 该 additional 参数 cbValley 该 specifies 该 conduction band valleys 将 为 included 用于 该 interpolation 的 参数. Possible 值: “Gamma”, “X”, “L”, 或 “All” (default 是 “Gamma”; option “All” uses 该 lowest band gap 到 select).  
result = buildmqwmaterial(location, 300, matname, x, y); |  Quaternary 材料 使用 compositions x 和 y.  
result = buildmqwmaterial(location, 300, matname, x, y, cbValley); |  Quaternary 材料 使用 compositions x 和 y 和 该 valley mixing specifier.  
  
The supported materials 是 listed 在 该 table below:

**III-V semiconductors** |  **Ternary alloys** |  **Quaternary Alloys**  
---|---|---  
AlAs |  AlxGa1-xAs |  InxGa1-xAsyP1-y  
GaAs |  AlxGa1-xP |  AlxGayIn1-x-yAs  
InAs |  AlxIn1-xP |   
AlP |  GaAsxP1-x |   
GaP |  InxAl1-xAs |   
InP |  InAsxP1-x |   
|  InxGa1-xAs |   
|  InxGa1-xP |   
  
When database materials 是 used, 该 属性 的 ternary alloys P(AxB1−xD) 是 interpolated 从 该 对应的 属性 的 该 base materials (P(AD) 和 P(BD)) according 到 该 formula

$$ P\left(A_x B_{1-x}D\right)=xP\left(AD\right)+\left(1-x\right)P\left(BD\right)+x\left(1-x\right)C, $$

其中 x 是 该 composition fraction 和 C 是 该 bowing 参数 (quadratic coefficient).

Quaternary alloys 的 类型 AxB1-xCyD1-y (two group III 和 two group V elements) 是 composed 从 该 interpolation 的 ternary alloy constituents [1]:

$$ P\left(A_xB_{1-x}C_yD_{1-y}\right)=\frac{x\left(1-x\right)\left[\left(1-y\right)P\left(A_xB_{1-x}D\right)+yP\left(A_xB_{1-x}C\right)\right]+y\left(1-y\right)\left[xP\left(AC_yD_{1-y}\right)+\left(1-x\right)P\left(BC_yD_{1-y}\right)\right]}{x\left(1-x\right)+y\left(1-y\right)}, $$

用于 composition fractions x 和 y. For example, 一个 combination 的 该 属性 的 InxGa1−xP, InxGa1−xAs, InAsyP1−y, 和 GaAsyP1−y 是 used 到 define 该 属性 的 InxGa1−xAsyP1−y.

Quaternary alloys 的 类型 AxByC1-x-yD (three group III elements 和 one group V 元素) 是 composed 从 该 interpolation 的 ternary alloy constituents [1]:

$$ P\left(A_xB_yC_{1-x-y}D\right)=\frac{xyP\left(A_{1-u}B_uD\right)+y(1-x-y)P\left(B_{1-v}C_{v}D\right)+x(1-x-y)P\left(A_{1-w}C_{w}D\right)}{xy+y(1-x-y)+x(1-x-y)}, $$

用于 composition fractions x 和 y 和 u = (1-x+y)/2, v = (2-x-2y)/2, w = (2-2x-y)/2. For example, 一个 combination 的 该 属性 的 Al1-uGauAs, Ga1-vInvAs, 和 Al1-wInwAs, 是 used 到 define 该 属性 的 AlxGayIn1-x-yAs.

**result** 是 一个 结构体 使用 该 following fields:

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
vb |  eV |  Valence band absolute energy (all layers 应该 have common reference)  
eps |  |  Relative static permittivity  
  
**References**

[1] Vurgaftman et al., J. Appl. Phys., 89, 5815 (2001)

**示例**
    
    
    mymat = buildmqwmaterial(“/home/auser/myfolder/my_material_db.json”, 300, “InAlAs”, 0.47);

**参见**

[mqwgain](/hc/en-us/articles/360034926533-mqwgain), [mqwindex](/hc/en-us/articles/360041072553)
