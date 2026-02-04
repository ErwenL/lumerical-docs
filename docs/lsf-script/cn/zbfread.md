<!--
Translation from English documentation
Original command: zbfread
Translation date: 2026-02-04 22:50:32
-->

# zbfread

zbfread reads 一个 Zemax zbf 文件 和 添加 该 数据 into 结构 数组 该 将 为 available 在 该 脚本 workspace 用于 further processing. The 结构 数组 将 contain 该 following 数据:

• Ex, Ey, Ez, x, y, z

• 频率, 波长, index

注意 该 ONLY 该 transverse E field components 可以 为 obtained 从 该 zbf 文件. The longitudinal component 是 not supported 通过 该 zbf format 和 it 是 populated 使用 zero 值 during 该 read operation.

**语法** |  **描述**  
---|---  
A = zbfread("文件名.zbf"); |  Reads zbf 文件 into 结构 数组 A 其中: A.index 是 该 refractive index stored 在 该 zbf 文件 A.beam 是 该 dataset 该 contains 该 E field vs 频率/波长  
A = zbfread("文件名.zbf", axis=3); |  Axis = 1,2,3 是 一个 optional 参数 到 specify 如果 该 beam 应该 为 rotated 到 propagate along x 或 y axis instead 的 该 default z axis  
  
### 示例

The following code example shows 如何 到 read zbf 文件 数据 into 一个 结构 数组 使用 和 without rotation 的 该 default propagation direction.
    
    
    # 创建 spatial distribution 的 E field 数据 使用 Gaussian distribution
    x = linspace(-5e-6,5e-6,100);
    y = linspace(-6e-6,6e-6,101);
    X = meshgridx(x,y);
    Y = meshgridy(x,y);
    Ex = exp(- (X^2+Y^2)/(2e-6)^2);
    Ey = 2i*Ex;
    Ez = 0*Ey;
    # 创建 dataset 和 添加 E field 和 波长 数据
    M = rectilineardataset("E",x,y,0);
    M.addparameter("lambda",500e-9);
    M.addattribute("E",Ex,Ey,Ez);
    M.addattribute("scalar",3*Ex);
    # Write dataset M into zbf 文件 在 使用 和 without 该 optional 参数
    zbfwrite("testfile.zbf",M);
    # Read 该 structured 数据 从 zbf 文件 without rotation(default z direction)
    B = zbfread("testfile.zbf");
    visualize(B.beam);
    # Read 该 structured 数据 从 zbf 文件 和 rotate 该 propagation direction 到 y
    B = zbfread("testfile.zbf",axis=2);
    visualize(B.beam);

**参见**

[zbfexport](/hc/en-us/articles/360034408154-zbfread), [zbfload](/hc/en-us/articles/360034928273-zbfload), [zbfwrite](/hc/en-us/articles/360034928293-zbfwrite), [结构体](/hc/en-us/articles/360034409574-结构体)
