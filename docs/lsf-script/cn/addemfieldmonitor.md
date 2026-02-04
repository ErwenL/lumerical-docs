<!--
Translation from English documentation
Original command: addemfieldmonitor
Translation date: 2026-02-03 22:59:29
-->

# addemfieldmonitor

向使用'DGTD'求解器的仿真中添加一个频域[EM（电磁）场监视器](https://optics.ansys.com/hc/en-us/articles/360034918553)。除了EM场数据外，监视器还会报告通过监视器表面的净通量。此命令要求对象树中存在DGTD求解器区域才能工作。

**Syntax** |  **Description**  
---|---  
addemfieldmonitor; |  向'DGTD'求解器添加一个频域EM场监视器。此函数不返回任何数据。  
  
**示例1**

以下脚本命令将向对象树中已存在的'DGTD'求解器添加一个频域EM场监视器，并打印监视器的所有可用属性。
    
    
    addemfieldmonitor;
    ?set;

**示例2**

以下脚本命令将向'DGTD'求解器添加一个频域EM场监视器，更改其名称，将其频率范围设置为与源相同，并将其分配给名为"2D rectangle"的实体。
    
    
    addemfieldmonitor; 
    set("name","T");
    set("use source limits",1);
    set("reference source","plane_wave");  
    set("surface type","solid");
    set("solid","2D rectangle");

注意：上述脚本假设对象树中已存在名为"2D rectangle"的实体和名为"plane_wave"的源。
---
  
**参见**

- [adddgtdsolver](./adddgtdsolver.md)
- [addemabsorptionmonitor](./addemabsorptionmonitor.md)
- [addemfieldtimemonitor](./addemfieldtimemonitor.md)
