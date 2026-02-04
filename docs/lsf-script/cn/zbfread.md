<!-- Translation completed: 2026-02-04 -->
<!-- Original command: zbfread -->

# zbfread

    x = linspace(-5e-6,5e-6,100);
    y = linspace(-6e-6,6e-6,101);
    X = meshgridx(x,y);
    Y = meshgridy(x,y);
    Ex = exp(- (X^2+Y^2)/(2e-6)^2);
    Ey = 2i*Ex;
    Ez = 0*Ey;
    M = rectilineardataset("E",x,y,0);
    M.addparameter("lambda",500e-9);
    M.addattribute("E",Ex,Ey,Ez);
    M.addattribute("scalar",3*Ex);
    zbfwrite("testfile.zbf",M);
    B = zbfread("testfile.zbf");
    visualize(B.beam);
    B = zbfread("testfile.zbf",axis=2);
    visualize(B.beam);

**语法** | **描述**
---|---
A = zbfread("filename.zbf"); | Reads zbf 文件 into structure 数组 A where: A.index is the 折射率 stored in the zbf 文件 A.beam is the 数据集 that contains the E 场 vs 频率/波长
A = zbfread("filename.zbf", axis=3); | Axis = 1,2,3 is an optional 参数 to specify if the beam should be rotated to propagate along x or y axis instead of the default z axis

**示例**

The following code 示例 shows how to 读取 zbf 文件 data into a structure 数组 with and without rotation of the default 传播 direction.

The following code 示例 shows how to 读取 zbf 文件 data into a structure 数组 with and without rotation of the default 传播 direction.

**另请参阅**

[zbfexport](/hc/en-us/articles/360034408154-zbfread), [zbfload](/hc/en-us/articles/360034928273-zbfload), [zbfwrite](/hc/en-us/articles/360034928293-zbfwrite), [struct](/hc/en-us/articles/360034409574-struct)
