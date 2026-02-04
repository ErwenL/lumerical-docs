<!--
Translation from English documentation
Original command: setmaterial
Translation date: 2026-02-04 22:50:14
-->

# setmaterial

设置 属性 的 一个 材料 在 该 材料 database. This 命令 可以 only edit 该 属性 的 该 materials 该 是 NOT write protected.

**语法** |  **描述**  
---|---  
?setmaterial("materialname"); |  Displays 该 属性 names 的 该 specified 材料 该 可以 为 modified.  
setmaterial( "materialname", "propertyname", newvalue); |  设置 该 属性 named "propertyname" 的 该 材料 使用 该 name "materialname" 到 newvalue. The 参数 newvalue 可以 为 一个 数字 或 一个 字符串. The 参数 "propertyname" 和 "materialname" have 到 match correct 字符串 exactly. For example, setmaterial("Si","Mesh order",4); 将 设置 该 属性 "mesh order" 的 该 materials "Si" 到 4.  
setmaterial( "materialname", **_struct_**); |  Update multiple material properties at the same time using a [struct](https://support.lumerical.com/hc/en-us/articles/360034409574-struct-Script-command) of associated properties. Keys are given the respective "propertyname", and values assigned to the new value.  
  
**示例 使用 结构体**
    
    
    # 创建 一个 材料
    setmaterial(addmaterial("(n,k) Material"), "name", "myMaterial");  
    
    # 设置 该 材料 属性
    setmaterial("myMaterial", {"Refractive Index": 1.3, "Imaginary Refractive Index": 1.5});

**Conductive 材料 example**

This example 添加 一个 新的 Conductive 材料, 设置 该 name 到 "myMaterial", anisotropy 到 "Diagonal", 和 设置 该 permittivity 和 conductivity 属性 用于 该 材料.
    
    
    A=[4;5;6];
    B=[1;2;3];
    temp = addmaterial("Conductive");
    setmaterial(temp,"name","myMaterial");
    setmaterial("myMaterial", "Anisotropy", 1); # 启用 diagonal anisotropy
    setmaterial("myMaterial","Permittivity", A);
    setmaterial("myMaterial","Conductivity", B);

**Sampled 数据 材料 example**

This example shows 如何 到 创建 一个 新的 Sampled 数据 材料.

The sampled 数据 矩阵 必须 have 2 或 4 columns, 用于 isotropic 或 anisotropic materials. The first column 是 该 频率 向量, 在 Hz. The next column(s) 是 该 complex valued permittivity.

If you have refractive index 数据 (rather than permittivity), remember 该 permittivity 是 simply 该 square 的 该 refractive index.
    
    
    f = linspace(1000e12,300e12,30);   # 频率 向量
    eps = 2 + 1i*(1e6 / (2*pi*f*eps0)); # 创建 example permittivity 向量
    sampledData = [f,eps];        # collect f 和 eps 在 one 矩阵
    matName = "My 材料";
    temp = addmaterial("Sampled 数据");
    setmaterial(temp,"name",matName);        # rename 材料
    setmaterial(matName,"max coefficients",2);    # 设置 该 数字 的 coefficients
    setmaterial(matName,"sampled 数据",sampledData); # load 该 sampled 数据 矩阵

**Index perturbation 材料 example**

This example shows 如何 到 创建 一个 新的 Index perturbation 材料.

The Index perturbation 材料 可以 define index perturbation 用于 "np Density" 和/或 "Temperature". For 一个 "np Density" index perturbation:

  * "np density model": takes 一个 integer 或 字符串 值 的 [0, 1, 2], 'Drude', 'Soref 和 Bennet' 或 'Custom'
  * 用于 model 类型 "Custom": "n sensitivity table" 和 "p sensitivity table" take 一个 矩阵 参数



For 一个 "Temperature" index perturbation:

  * 用于 model 类型 "Linear sensitivity": users need 到 设置 individual 值 用于 'Tref', 'dn/dt' 和 'dk/dt'
  * 用于 model 类型 "Table 的 值": "temperature sensitivity table" takes 一个 矩阵 参数


    
    
    nSensitivity = [1.5, 1.5e-3, 1.5e-3;  1.6, 1.6e-3, 1.6e-3; 1.7, 1.7e-3, 1.7e-3];
    pSensitivity = [1, 1e-3, 1e-3;  1.2, 1.2e-3, 1.2e-3; 1.4, 1.4e-3, 1.4e-3];
    matName = "May 材料";
    temp = addmaterial("Index perturbation");
    setmaterial(temp, "name", matName);
    setmaterial(matName, "np density model", "Custom"); # use "Custom" model 类型
    setmaterial(matName, "n sensitivity table", nSensitivity); # 设置 n sensitivity table
    setmaterial(matName, "p sensitivity table", pSensitivity); # 设置 p sensitivity table

It 是 possible 到 define 该 color 的 该 材料 使用 命令 lines. An example 是 shown below. These 脚本 commands 将 创建 一个 材料, define 该 材料 color, 和 assign 该 材料 到 一个 rectangle 到 show 该 color change.

The 4 elements 在 该 矩阵 用于 该 新的 color 值 是 用于 该 red, green, blue, 和 alpha channels 的 该 color, respectively. These elements 可以 为 设置 between 0 到 1, 该 represents 一个 minimum 的 0 和 maximum 的 255. Alpha defines 该 opacity, setting 到 到 0 means transparent, 1 means 一个 solid color. For example, [1;0;0;1] would 为 solid red, [0;1;0;1] would 为 solid green, 和 [0;0;1;1] would 为 solid blue. More color channel 值 可以 为 found 使用 一个 online color picker tool.

注意 该 该 color opacity 可以 为 also defined 在 该 结构 对象 通过 overriding 该 材料 属性.
    
    
    mymaterial = addmaterial("PEC");
    setmaterial(mymaterial,"name", "test_material");
    setmaterial("test_material", "color", [1; 0.6; 0.4; 0.3] ); # R, G, B, alpha channel
    addrect;
    设置("材料", "test_material");
    设置("override color opacity 从 材料 database", 0);

**参见**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ addmaterial ](https://optics.ansys.com/hc/en-us/articles/360034930013-addmaterial) , [ deletematerial ](https://optics.ansys.com/hc/en-us/articles/360034409734-deletematerial) , [ getmaterial ](https://optics.ansys.com/hc/en-us/articles/360034930053-getmaterial) , [ getindex ](https://optics.ansys.com/hc/en-us/articles/360034409674-getindex) , [ getfdtdindex ](https://optics.ansys.com/hc/en-us/articles/360034409694-getfdtdindex) , [ importing arbitrary dispersive material ](**%20to%20be%20defined%20**)
