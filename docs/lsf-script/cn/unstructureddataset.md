<!--
Translation from English documentation
Original command: unstructureddataset
Translation date: 2026-02-04 22:50:15
-->

# unstructureddataset

创建 一个 empty dataset 该 是 associated 使用 arbitrary x/y/z coordinate 在 space, 和 使用 additional 矩阵, 一个 connectivity 矩阵 到 connect them. The connectivity 矩阵 comes after x, y, 和 z. Like rectilinear datasets, unstructured data设置可以 为 parameterized, 和 可以 contain 一个 arbitrary 数字 的 attributes (see [ addattribute) ](/hc/en-us/articles/360034929873-addattribute) 和 参数 (see [ addparameter) ](/hc/en-us/articles/360034409494-addparameter) 。

See [ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) 用于 more information. For data设置该 是 not associated 使用 该 x/y/z coordinates (ex。 transmission as 一个 函数 的 频率), see [ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) .

**语法** |  **描述**  
---|---  
unstructureddataset(x,y,z,C); |  创建 一个 empty unstructured dataset associated 使用 该 coordinates x/y/z 和 一个 connectivity 矩阵 到 connect them. Arguments 'x', 'y' 和 'z' 必须 为 该 same 长度; equivalent 到 该 total 数字 的 points. The 参数 'C' 应该 为 一个 矩阵 的 integers 其中 该 数字 的 rows equal 到 数字 的 shapes 在 该 mesh, 该 数字 的 columns 应该 为 2 (line segments), 3 (triangles) 或 4 (tetrahedra), 和 值 应该 为 integers.  
  
**示例**

Below 是 一个 simple example 的 该 usage 的 unstructured dataset. x, y 和 z vectors represent arbitrary points 在 space 和 C represent 该 connectivity 矩阵 该 connects them. The 值 用于 该 vectors 可以 为 loaded 从 该 [ unstructured_charge_example.mat ](/hc/article_attachments/360046127873/unstructured_charge_example.mat) 文件. It 是 possible 到 further 脚本 此 process 和 import 该 数据 到 一个 对象, eg, np density grid attribute, see 该 [ importdataset ](/hc/en-us/articles/360034409114-importdataset) 命令.
    
    
    # constructing 一个 unstructured dataset
    matlabload("unstructured_charge_example.mat"); # taking 该 数据 从 一个 CHARGE 仿真. The 数据 可以 为 从 一个 different 源
    x = 电荷.x;
    y = 电荷.y;
    z = 电荷.z;
    C = 电荷.elements;
    数据 = unstructureddataset("test",x,y,z,C);
    V_cathode = 电荷.V_cathode;
    V_anode = 电荷.V_anode;
    n = pinch(电荷.n);
    p = pinch(电荷.p);
    数据.addparameter("V_cathode",V_cathode);
    数据.addparameter("V_anode",V_anode);
    数据.addattribute("n",n);
    数据.addattribute("p",p);
    visualize(数据);

This next example 创建 一个 unstructured dataset (使用 该 name "Absorption") 该 contains 2 数据 attributes: 该 power absorption Pabs, 和 该 refractive index n. Both attributes 是 一个 函数 的 该 spatial 参数 x/y/z 和 频率 f. Connectivity 矩阵 cm has also been specified. To allow 该 用户 到 access 该 频率 参数 在 terms 的 频率 或 波长 , both 频率 (f) 和 波长 (c/f) 是 added as interdependent 参数.
    
    
    Absorption = unstructureddataset("Absorption",x,y,z,cm);
    Absorption.addparameter("lambda",c/f,"f",f);
    Absorption.addattribute("Pabs",Pabs);
    Absorption.addattribute("refractive index",n);
    visualize(Absorption); # visualize 此 dataset 在 该 Visualizer

This example shows 如何 到 define 一个 equilaterial triangle 在 该 plane z=0
    
    
    x = [0;1;2];
    y = [0;sqrt(3);0];
    z = [0;0;0];
    C = [1,3,2];
    ds = unstructureddataset(x,y,z,C);

**参见**

[ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ addattribute ](/hc/en-us/articles/360034929873-addattribute) , [ addparameter ](/hc/en-us/articles/360034409494-addparameter) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets) , [ getparameter ](/hc/en-us/articles/360034409514-getparameter) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ 结构体 ](/hc/en-us/articles/360034409574-结构体)
