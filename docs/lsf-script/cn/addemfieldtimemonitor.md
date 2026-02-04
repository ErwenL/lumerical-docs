<!--
Translation from English documentation
Original command: addemfieldtimemonitor
Translation date: 2026-02-03 23:01:34
-->

# addemfieldtimemonitor

向使用'DGTD'求解器的仿真中添加一个时域[EM（电磁）场监视器](/hc/en-us/articles/360034918493)。此命令要求对象树中存在DGTD求解器区域才能工作。

**Syntax** |  **Description**  
---|---  
addemfieldtimemonitor; |  向'DGTD'求解器添加一个时域EM场监视器。此函数不返回任何数据。  
addemfieldtimemonitor(struct_data); |  添加一个时域EM场监视器，并使用包含"属性"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例1**

以下脚本命令将向对象树中已存在的'DGTD'求解器添加一个时域EM场监视器，并打印监视器的所有可用属性。
    
    
    addemfieldtimemonitor;
    ?set;

**示例2**

以下脚本命令将向'DGTD'求解器添加一个时域EM场监视器，更改其名称，并将其分配给名为"2D rectangle"的实体。
    
    
    addemfieldtimemonitor; 
    set("name","time");
    set("geometry type","surface");
    set("surface type","solid");
    set("solid","2D rectangle");

注意：上述脚本假设对象树中已存在名为"2D rectangle"的实体。
---  

**示例3**

以下脚本命令将向'DGTD'求解器添加一个'点'时域EM场监视器并设置其位置。
    
    
    addemfieldtimemonitor; 
    set("name","time");
    set("geometry type","point");
    set("x",1e-6);
    set("y",0);
    set("z",0);

**参见**

- [adddgtdsolver](./adddgtdsolver.md)
- [addemfieldmonitor](./addemfieldmonitor.md)
- [addemabsorptionmonitor](./addemabsorptionmonitor.md)
