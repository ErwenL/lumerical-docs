<!--
Translation from English documentation
Original command: zbfwrite
Translation date: 2026-02-04 22:50:32
-->

# zbfwrite

Zbfwrite writes 一个 4D dataset into 一个 Zemax zbf 文件 在 该 current directory. Data written into 该 zbf 文件:

  * Ex, Ey, Ez, x, y, z
  * 频率, 波长, index



[[注意:]] ONLY 该 transverse E field components 是 written 到 该 zbf 文件. The longitudinal component 是 not supported 通过 该 zbf format.

**语法** |  **描述**  
---|---  
zbfwrite("文件名",M); |  Writes dataset M into zbf 文件. The dataset 必须 include one 频率 或 波长 值. If 该 fourth 维度 是 named "f" 或 "频率", it 将 为 automatically converted into 波长. Any other name 将 为 assumed 到 carry 波长 information 和 it 将 not 为 converted.  
zbfwrite("文件名",M,index); |  The optional 参数 "index" 是 该 refractive index 该 将 为 written into zbf 文件. A default 值 的 "1" 是 used 如果 no "index" 是 provided.  
zbfwrite("文件名",M,index,"attributeName"); |  atributeName 是 一个 optional 参数 使用 default 值 = "". This specifies 该 向量 或 scalar attribute 到 write. If 一个 scalar attribute 是 written, it becomes 一个 "unpolarized" zbf 文件. If nothing 是 specified(default 值 =""), 那么 it 将 write 该 first 向量 attribute 在 该 dataset, 或 该 first scalar attribute 如果 there 是 no 向量 attribute.  
[[注意:]] The Zemax zbf 文件 需要 该 数据 到 为 saved 在 一个 uniform grid 的 dimensions 使用 一个 power 的 2 (使用 \\(2^n \times 2^m\\) points). The dataset 将 为 interpolated 在 一个 grid 使用 \\(n\\) 和 \\(m\\) defined so 该 mesh step 是 equal 到 或 less than 该 smallest mesh step 在 该 original 数据.  
---  
  
### 示例

The following code example shows 如何 到 创建 一个 dataset 使用 correct dimensions 和 write it into 一个 zbf 文件 使用 various optional 参数. The last section 的 该 code reads back 该 saved zbf 文件 into 该 结构 数组 和 plots 该 field profile, index, 和 波长.
    
    
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
    
    # Visualize 该 dataset before writing it into zbf 文件
    visualize(M);  
    
    # Write dataset M into zbf 文件 在 使用 和 without 该 optional 参数
    zbfwrite("testfile1.zbf",M);
    zbfwrite("testfile2.zbf",M,1);
    zbfwrite("testfile3.zbf",M,1,"E");
    zbfwrite("testfile4.zbf",M,2,"scalar");  
    
    # Read back 该 structured 数据 从 zbf 文件 和 visualize it
    B = zbfread("testfile4.zbf");
    visualize(B.beam);
    ?B.index;
    B_beam=B.beam;
    ?B_beam.波长;

**参见**

[ zbfexport ](/hc/en-us/articles/360034928293-zbfwrite) , [ zbfload ](/hc/en-us/articles/360034928273-zbfload) , [ zbfread ](/hc/en-us/articles/360034408154-zbfread) , [ List 的 commands ](/hc/en-us/articles/360037228834)
