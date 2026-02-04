<!--
Translation from English documentation
Original command: rectilineardataset
Translation date: 2026-02-04 22:50:14
-->

# rectilineardataset

创建 一个 empty rectilinear dataset 该 是 associate 使用 该 x/y/z coordinates (ex. E 和 H fields). Like 矩阵 datasets, rectilinear data设置可以 为 parameterized, 和 可以 contain 一个 arbitrary 数字 的 attributes (see [addattribute)](/hc/en-us/articles/360034929873-addattribute) 和 参数 (see [addparameter)](/hc/en-us/articles/360034409494-addparameter)。

See [Dataset introduction](/hc/en-us/articles/360034409554-Datasets) 用于 more information.

For data设置该 是 not associated 使用 该 x/y/z coordinates (ex。 transmission as 一个 函数 的 频率), see [ matrixdataset](/hc/en-us/articles/360034409454-matrixdataset).

**语法** |  **描述**  
---|---  
rectilineardataset(x,y,z); |  创建 一个 empty rectilinear dataset associated 使用 该 coordinates x/y/z. Arguments 'x', 'y' 和 'z' 可能 为 different lengths 和 该 total 数字 的 points 是 该 product 的 their lengths.  
rectilineardataset("dataset_name",x,y,z); |  创建 一个 empty rectilinear dataset named "dataset_name" associated 使用 该 coordinates x/y/z. Arguments 'x', 'y' 和 'z' 可能 为 different lengths 和 该 total 数字 的 points 是 该 product 的 their lengths.  
  
**示例**

This example 创建 一个 rectilinear dataset (使用 该 name "Absorption") 该 contains 2 数据 attributes: 该 power absorption Pabs, 和 该 refractive index n. Both attributes 是 一个 函数 的 该 spatial 参数 x/y/z 和 频率 'f'. To allow 该 用户 到 access 该 频率 参数 在 terms 的 频率 或 波长 , both 频率 (f) 和 波长 (c/f) 是 added as interdependent 参数.
    
    
    Absorption = rectilineardataset("Absorption",x,y,z);
    Absorption.addparameter("lambda",c/f,"f",f);
    Absorption.addattribute("Pabs",Pabs);
    Absorption.addattribute("refractive index",n);
    visualize(Absorption); # visualize 此 dataset 在 该 Visualizer

The following 脚本 code shows 如何 到 获取 该 raw 数据 从 一个 频率 监视器 在 FDTD (使用 getdata), 和 如何 到 manually 创建 一个 dataset 从 该 数据. It also shows 如何 到 directly 获取 该 electric field dataset 从 该 监视器 在 一个 single 命令 (使用 getresult).
    
    
    # 监视器 name
    m="监视器";
    # 获取 individual 数据 elements 使用 getdata
    x=getdata(m,"x");
    y=getdata(m,"y");
    z=getdata(m,"z");
    f=getdata(m,"f");
    Ex=getdata(m,"Ex");
    Ey=getdata(m,"Ey");
    Ez=getdata(m,"Ez");
    # 创建 该 electric field dataset 从 该 raw 数据
    E_manual = rectilineardataset("E_manual",x,y,z);  # initialize dataset 和 provide spatial position vectors
    E_manual.addparameter("lambda",c/f,"f",f);  # 添加 additional 参数: 频率 
    E_manual.addattribute("E",Ex,Ey,Ez);     # 添加 向量 electric field attribute
    # all 的 该 above commands 可以 为 avoided 使用 一个 single getresult 命令
    E_fromMonitor = getresult(m,"E");

The following 脚本 code shows 如何 到 access 该 数据 stored 在 该 'E_manual' dataset created 在 该 above example
    
    
    # output contents 的 dataset 到 prompt
    ?E_manual;
    # 获取 参数
    x   = E_manual.x;
    y   = E_manual.y;
    z   = E_manual.z;
    f   = E_manual.f;
    lambda = E_manual.lambda;
    x_1  = E_manual.x(1); 
    # 获取 attributes. Remember 该 E 是 一个 向量 quantity
    Ex = E_manual.Ex; # Ex component
    Ey = E_manual.Ey; # Ey component
    Ez = E_manual.Ez; # Ez component
    E2 = E_manual.E2; # |E|^2
    E = E_manual.E;  # 获取 all components 在 一个 single 矩阵. An extra 维度 的 长度 3 将 为 added 到 该 矩阵, 用于 each 向量 component.

**参见**

[rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset), [addattribute](/hc/en-us/articles/360034929873-addattribute), [addparameter](/hc/en-us/articles/360034409494-addparameter), [visualize](/hc/en-us/articles/360034410514-visualize), [datasets](/hc/en-us/articles/360034409554-Datasets), [getparameter](/hc/en-us/articles/360034409514-getparameter), [getattribute](/hc/en-us/articles/360034409534-getattribute), [ matrixdataset](/hc/en-us/articles/360034409454-matrixdataset), [结构体](/hc/en-us/articles/360034409574-结构体)
