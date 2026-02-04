<!--
Translation from English documentation
Original command: addimportedsource
Translation date: 2026-02-04 00:31:51
-->

# addimportedsource

向仿真环境添加一个导入源。

**Syntax** |  **Description**  
---|---  
addimportedsource; |  向仿真环境添加导入源。此函数不返回任何数据。  
addimportedsource(struct_data); |  添加导入源，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将向仿真环境添加导入源，为其分配名称，并从*.mat文件加载E场分布。
    
    
    addimportedsource;
    set("name","source2");
    # Load a field profile saved in Matlab file named myfile.mat
    select("source2");
    importdataset("myfile.mat");

要查看如何使用脚本命令基于监视器数据创建导入源的示例，请访问此知识库页面：[基于监视器数据的自定义源分布](/hc/en-us/articles/360034383034-Custom-source-profile-from-monitor-data)。

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [asapimport](./asapimport.md)
- [asapload](./asapload.md)
- [asapexport](./asapexport.md)
- [importdataset](./importdataset.md)
