<!-- Translation completed: Tue Feb 03 2026 -->
<!-- Original: savedcard -->

# savedcard

将 D-card 数据保存到 Lumerical 数据文件（ldf）中。D-card 通常用于存储监视器数据，但也可用于存储求解器对象的数据。

数据以非归一化状态保存。有关详细信息，请参阅参考指南中的[单位和归一化](https://optics.ansys.com/hc/en-us/articles/360034397034)部分。

**语法** |  **描述**  
---|---  
savedcard("filename"); |  将所有当前 D-card（本地和全局）保存到指定的 ldf 文件。此函数不返回任何数据。  
savedcard("filename", "name1", "name2",...); |  仅保存具有指定名称 "name1"、"name2" 等的 D-card。  
  
**示例**

此示例显示如何保存名为 xy_monitor 的监视器的所有数据。
    
    
    ?getdata; # view all d-cards
    savedcard("monitor_data","::model::xy_monitor");

此示例显示如何在 MODE 中进行频率扫描后保存所需数据。这相当于 GUI 选项"导出到 Interconnect"。
    
    
    savedcard("FileName", "::model::FDE::data::frequencysweep");

**另请参阅**

- [命令列表](./index.md)
- [copydcard](./copydcard.md)
- [savedata](./savedata.md)
- [loaddata](./loaddata.md)
- [matlabsave](./matlabsave.md)
