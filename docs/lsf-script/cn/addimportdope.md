<!--
Translation from English documentation
Original command: addimportdope
Translation date: 2026-02-04 22:49:29
-->

# addimportdope

添加 一个 [doping region](/hc/en-us/articles/360034398054) 到 该 仿真 环境 该 可以 为 used 到 load 一个 自定义 doping profile. The 自定义 doping profile 可以 为 created analytically 使用 脚本 或 it 可以 为 imported 从 other sources such as process 仿真. This 命令 需要 一个 CHARGE 求解器 region 到 为 present 在 该 对象 tree.

**语法** |  **描述**  
---|---  
addimportdope; |  添加 一个 import doping region 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addimportdope(struct_data); |  Adds an import doping region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
Once 该 import doping 对象 是 created, 该 doping 数据 可以 为 imported 从 一个 matlab (.mat) 文件 使用 该 GUI 或 通过 assigning 一个 dataset 到 该 对象 使用 该 [ importdataset ](/hc/en-us/articles/360034409114-importdataset) 脚本 命令. The dataset 可以 为 一个 rectilinear 或 一个 unstructured dataset. Doping 数据 可以 为 imported into 该 求解器 workspace 从 other tools (e.g. process 仿真) 使用 该 [ Dataset builder ](/hc/en-us/articles/360034901713-Dataset-builder) .

**示例**

The following 脚本 命令 将 添加 一个 import doping 对象 到 该 CHARGE 求解器 region 和 将 load 一个 analytic 3D doping 数据 into it.
    
    
    addimportdope;
    设置("name","pepi");
    设置("x",0);
    设置("y",0);
    设置("z",0);
    # 创建 coordinate vectors 和 3D 矩阵 用于 doping profile
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    N = 矩阵(11,2,101) + 1e21;  # assume uniform doping concentration 的 1e15 /cm3 (1e21 /m3)
    # 创建 dataset
    doping = rectilineardataset("dope",x,y,z);
    doping.addparameter("一个",1);  # 添加 一个 dummy 参数
    doping.addattribute("N",N);
    # load 数据 into doping 对象
    select("CHARGE::pepi");
    importdataset(doping);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ linspace ](/hc/en-us/articles/360034409254-linspace) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ select ](/hc/en-us/articles/360034928593-select) , [ importdataset ](/hc/en-us/articles/360034409114-importdataset) , [ adddope ](/hc/en-us/articles/360034404594-adddope) , [ adddiffusion ](/hc/en-us/articles/360034924513-adddiffusion)
