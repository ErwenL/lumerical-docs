<!--
Translation from English documentation
Original command: addimportgen
Translation date: 2026-02-04 22:49:29
-->

# addimportgen

添加 一个 (optical) generation region 到 该 仿真 环境 其中 该 generation profile has been imported into Finite Element IDE. This 命令 需要 一个 CHARGE 求解器 region 到 为 present 在 该 对象 tree.

**语法** |  **描述**  
---|---  
addimportgen; |  添加 一个 import generation 对象 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addimportgen(struct_data); |  Adds tan import generation object and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
Once 该 import generation 对象 是 created, 该 optical generation 数据 可以 为 imported 从 一个 matlab (.mat) 文件 使用 该 GUI 或 通过 assigning 一个 dataset 到 该 对象 使用 该 [ importdataset ](/hc/en-us/articles/360034409114-importdataset) 脚本 命令. The .mat 文件 必须 contain 一个 3D 矩阵 G containing 该 generation 数据 在 一个 rectilinear grid 和 该 three coordinate vectors x, y, z. The dataset 可以 为 either 一个 rectilinear 或 一个 unstructured dataset.

**示例**

The following 脚本 命令 将 添加 一个 import generation 对象 到 该 CHARGE 求解器 region 和 将 load 一个 analytic 3D optical generation 数据 into it.
    
    
    addimportgen;
    设置("name","gen_opt");
    设置("x",0);
    设置("y",0);
    设置("z",0);
    # 创建 coordinate vectors 和 3D 矩阵 用于 doping profile
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    G = 矩阵(11,2,101) + 1e27;  # assume uniform generation rate 的 1e21 /cm3 (1e27 /m3)
    # 创建 dataset
    gen = rectilineardataset("gen",x,y,z);
    gen.addparameter("一个",1);  # 添加 一个 dummy 参数
    gen.addattribute("G",G);
    # load 数据 into doping 对象
    select("CHARGE::gen_opt");  
    importdataset(gen);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ linspace ](/hc/en-us/articles/360034409254-linspace) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ select ](/hc/en-us/articles/360034928593-select) , [ importdataset ](/hc/en-us/articles/360034409114-importdataset) , [ addbulkgen ](/hc/en-us/articles/360034404634-addbulkgen) , [ adddeltachargesource ](/hc/en-us/articles/360034404654-adddeltachargesource)
