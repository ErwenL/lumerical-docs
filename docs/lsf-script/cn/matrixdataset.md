<!--
Translation from English documentation
Original command: matrixdataset
Translation date: 2026-02-04 22:50:13
-->

# matrixdataset

创建 一个 empty 矩阵 dataset. Matrix data设置是 used 用于 数据 (attributes 和 参数) 该 don't have any spatial dependence (i。e. Reflection vs 频率). For data设置该 do have x/y/z spatial coordinates (i。e. electric fields), use [rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset) 或 [unstructureddataset](/hc/en-us/articles/360034929933-unstructureddataset).

Matrix data设置可以 为 parameterized, 和 可以 contain 一个 arbitrary 数字 的 attributes (see [addattribute)](/hc/en-us/articles/360034929873-addattribute) 和 参数 (see [addparameter)](/hc/en-us/articles/360034409494-addparameter)。

See [Dataset introduction](/hc/en-us/articles/360034409554-Datasets) 用于 more information.

**语法** |  **描述**  
---|---  
matrixdataset; |  创建 一个 empty dataset.  
matrixdataset("name"); |  创建 一个 empty dataset 使用 该 name "name".  
  
**示例**

This example uses 一个 矩阵 dataset 到 store cross section (sigma) 数据 as 一个 函数 的 频率. In 此 case, 该 cross section 数据 sigma 是 该 attribute, 和 频率 是 该 参数. To allow 该 用户 到 access 该 频率 参数 在 terms 的 频率 或 波长 , both 频率 (f) 和 波长 (c/f) 是 added as interdependent 参数.
    
    
    sigma = matrixdataset("cross_section");
    sigma.addparameter("lambda",c/f,"f",f); # 添加 参数 f 和 lambda
    sigma.addattribute("sigma",CS); # 添加 attribute CS
    visualize(sigma); # visualize 此 dataset 在 该 Visualizer

The following 脚本 code generates some example 数据, 那么 创建 一个 R(radius,height) dataset.
    
    
    # 创建 example results
    radius = 0:10; 
    height = 1:0.1:3;
    reflection = randmatrix(长度(radius),长度(height)); 
    # 创建 Reflection dataset
    R = matrixdataset("R"); # initialize dataset
    R.addparameter("radius",radius); # 添加 radius 参数
    R.addparameter("height",height); # 添加 height 参数
    R.addattribute("R",reflection); # 添加 reflection attribute
    # plot 数据
    image(radius,height,reflection); # use original matrices
    image(R.radius,R.height,R.R);  # use dataset
    # send dataset 到 visualizer
    visualize(R); 

**参见**

[rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset), [addattribute](/hc/en-us/articles/360034929873-addattribute), [addparameter](/hc/en-us/articles/360034409494-addparameter), [visualize](/hc/en-us/articles/360034410514-visualize), [datasets](/hc/en-us/articles/360034409554-Datasets), [getparameter](/hc/en-us/articles/360034409514-getparameter), [getattribute](/hc/en-us/articles/360034409534-getattribute), [matrixdataset](/hc/en-us/articles/360034409454-matrixdataset), [结构体](/hc/en-us/articles/360034409574-结构体)
