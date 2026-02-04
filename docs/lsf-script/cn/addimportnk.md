<!--
Translation from English documentation
Original command: addimportnk
Translation date: 2026-02-04 00:53:23
-->

# addimportnk

向FEEM仿真环境添加一个nk导入对象，其中具有空间变化折射率的材料分布可以从外部Matlab文件导入。

**Syntax** |  **Description**  
---|---  
addimportnk; |  在FEEM求解器中添加导入图元以定义具有空间变化折射率分布的材料。此函数不返回任何数据。  
addimportnk(struct_data); |  在FEEM求解器中添加导入图元以定义具有空间变化折射率分布的材料，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
创建nk导入对象后，可以通过GUI从matlab（.mat）文件导入数据，或使用[importdataset](/hc/en-us/articles/360034409114-importdataset)脚本命令将数据集分配给对象。数据集可以是矩形数据集或非结构化（有限元）格式。

**示例**

以下脚本命令将向FEEM求解器区域添加导入(n,k)对象，并加载分析3D热数据。
    
    
    addfeemsolver;
    addimportnk;
    # create coordinate vectors and 3D matrix for nk input
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    nk = matrix(11,2,101)+3.45; # assume the index input is 3.45 everywhere
    for (i=1:length(x)){  
    # assume that index varies along x-axis 
    nk(i,:,:)=x(i)*1e5;}
    # add waveguide
    addrect;
    setname('WG');
    set('x min',-1e-6); 
    set('x max',1e-6);
    set('y span',2e-6); 
    set('y',0);
    set('z span',2e-6); 
    set('z',1e-6);
    # create dataset
    nkmaterial = rectilineardataset("nk import",x,y,z);
    nkmaterial.addparameter("lambda",1.55e-6); # (Required) add any parameter
    nkmaterial.addattribute("nk",nk);
    # load data into nk import
    select("FEEM::nk import");
    importdataset(nkmaterial);
    set("volume type","solid");
    set("volume solid","WG");
    set("selected attribute","nk");

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [addfeemsolver](./addfeemsolver.md)
- [rectilineardataset](./rectilineardataset.md)
- [select](./select.md)
- [importdataset](./importdataset.md)
