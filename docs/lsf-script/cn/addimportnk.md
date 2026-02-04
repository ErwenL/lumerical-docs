<!--
Translation from English documentation
Original command: addimportnk
Translation date: 2026-02-04 22:49:29
-->

# addimportnk

添加 一个 nk import 对象 到 该 FEEM 仿真 环境 其中 该 profile 的 该 材料 使用 一个 spatially varying index 可以 为 imported 从 一个 external Matlab 文件.

**语法** |  **描述**  
---|---  
addimportnk; |  添加 一个 import primitive 到 define 材料 使用 一个 spatially varying index profile 在 该 FEEM 求解器. This 函数 does not 返回 any 数据.  
addimportnk(struct_data); |  Adds an import primitive to define material with a spatially varying index profile in the FEEM solver and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
Once 该 nk import 对象 是 created, 该 数据 可以 为 imported 从 一个 matlab (.mat) 文件 使用 该 GUI 或 通过 assigning 一个 dataset 到 该 对象 使用 该 [ importdataset ](/hc/en-us/articles/360034409114-importdataset) 脚本 命令. The dataset 可以 为 在 rectilinear 或 unstructured (finite-元素) format.

**示例**

The following 脚本 命令 将 添加 一个 import (n,k) 对象 到 该 FEEM 求解器 region 和 将 load 一个 analytic 3D heat 数据 into it.
    
    
    addfeemsolver;
    addimportnk;
    # 创建 coordinate vectors 和 3D 矩阵 用于 nk input
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    nk = 矩阵(11,2,101)+3.45; # assume 该 index input 是 3.45 everywhere
    用于 (i=1:长度(x)){  
    # assume 该 index varies along x-axis 
    nk(i,:,:)=x(i)*1e5;}
    # 添加 waveguide
    addrect;
    setname('WG');
    设置('x最小值',-1e-6); 
    设置('x最大值',1e-6);
    设置('y跨度',2e-6); 
    设置('y',0);
    设置('z跨度',2e-6); 
    设置('z',1e-6);
    # 创建 dataset
    nkmaterial = rectilineardataset("nk import",x,y,z);
    nkmaterial.addparameter("lambda",1.55e-6); # (Required) 添加 any 参数
    nkmaterial.addattribute("nk",nk);
    # load 数据 into nk import
    select("FEEM::nk import");
    importdataset(nkmaterial);
    设置("volume 类型","solid");
    设置("volume solid","WG");
    设置("选中的 attribute","nk");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ addfeemsolver ](/hc/en-us/articles/360034925033-addfeemsolver) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ select ](/hc/en-us/articles/360034928593-select) , [ importdataset ](/hc/en-us/articles/360034409114-importdataset)
