<!--
Translation from English documentation
Original command: addimporttemperature
Translation date: 2026-02-04 22:49:29
-->

# addimporttemperature

添加 一个 import temperature 源 到 该 CHARGE 求解器 (only applicable 到 non-isothermal transport). The import temperature 对象 可以 为 used 到 import 一个 temperature map 用于 non-isothermal 仿真. A CHARGE 求解器 region 必须 为 present 在 该 对象 tree 用于 此 命令 到 work.

**语法** |  **描述**  
---|---  
addimporttemperature; |  添加 一个 import temperature 源 到 该 CHARGE 求解器. The 源 only 获取 applied 如果 该 "temperature dependence" 是 设置 到 "non-isothermal." This 函数 does not 返回 any 数据.  
addimporttemperature(struct_data); |  Adds an import temperature source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
Once 该 import temperature 源 是 created, 该 数据 可以 为 imported 从 一个 matlab (.mat) 文件 使用 该 GUI 或 通过 assigning 一个 dataset 到 该 对象 使用 该 [ importdataset ](/hc/en-us/articles/360034409114-importdataset) 脚本 命令. The dataset 可以 either 为 在 rectilinear 或 unstructured (finite-元素) format.

**示例**

The following 脚本 命令 将 添加 一个 import temperature 源 和 将 load 一个 analytic 3D temperature 数据 into it.
    
    
    addimporttemperature;
    设置("name","Tmap");
    # 创建 coordinate vectors 和 3D 矩阵 用于 temperature map
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    T = 矩阵(11,2,101) + 400;  # assume 该 temperature 是 400 K everywhere
    # 创建 dataset
    temperature = rectilineardataset("temp",x,y,z);
    temperature.addparameter("一个",1);  # 添加 一个 dummy 参数
    temperature.addattribute("T",T);
    # load 数据 into 源
    select("CHARGE::Tmap"); 
    importdataset(temperature);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ linspace ](/hc/en-us/articles/360034409254-linspace) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ select ](/hc/en-us/articles/360034928593-select) , [ importdataset ](/hc/en-us/articles/360034409114-importdataset) , [ addimportheat ](/hc/en-us/articles/360034404394-addimportheat)
