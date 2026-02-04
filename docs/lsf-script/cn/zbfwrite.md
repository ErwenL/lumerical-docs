<!-- Translation completed: 2026-02-04 -->
<!-- Original command: zbfwrite -->

# zbfwrite

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
    visualize(M);  
    zbfwrite("testfile1.zbf",M);
    zbfwrite("testfile2.zbf",M,1);
    zbfwrite("testfile3.zbf",M,1,"E");
    zbfwrite("testfile4.zbf",M,2,"scalar");  
    B = zbfread("testfile4.zbf");
    visualize(B.beam);
    ?B.index;
    B_beam=B.beam;
    ?B_beam.波长;

**语法** | **描述**
---|---
zbfwrite("filename",M); | Writes 数据集 M into zbf 文件. The 数据集 must include one 频率 or 波长 值. If the fourth 维度 is named "f" or "频率", it will be automatically converted into 波长. Any other name will be assumed to carry 波长 information and it will not be converted.
zbfwrite("filename",M,index); | The optional 参数 "index" is the 折射率 that will be written into zbf 文件. A default 值 of "1" is used if no "index" is provided.
zbfwrite("filename",M,index,"attributeName"); | atributeName is an optional 参数 with default 值 = "". This specifies the 向量 or scalar 属性 to 写入. If a scalar 属性 is written, it becomes an "unpolarized" zbf 文件. If nothing is specified(default 值 =""), then it will 写入 the first 向量 属性 in the 数据集, or the first scalar 属性 if there is no 向量 属性.

**示例**

The following code 示例 shows how to create a 数据集 with correct 维度 and 写入 it into a zbf 文件 with various optional parameters. The last section of the code reads back the saved zbf 文件 into the structure 数组 and plots the 场 profile, index, and 波长.

The following code 示例 shows how to create a 数据集 with correct 维度 and 写入 it into a zbf 文件 with various optional parameters. The last section of the code reads back the saved zbf 文件 into the structure 数组 and plots the 场 profile, index, and 波长.

**另请参阅**

[ zbfexport ](/hc/en-us/articles/360034928293-zbfwrite) , [ zbfload ](/hc/en-us/articles/360034928273-zbfload) , [ zbfread ](/hc/en-us/articles/360034408154-zbfread) , [ List of commands ](/hc/en-us/articles/360037228834)
