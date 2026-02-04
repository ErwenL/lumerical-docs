<!--
Translation from English documentation
Original command: addemabsorptionmonitor
Translation date: 2026-02-03 22:44:07
-->

# addemabsorptionmonitor

向有限元 IDE 中的 'DGTD' 求解器添加一个 [吸收监视器](/hc/en-us/articles/360034918573)。该监视器报告监视器体积内吸收的功率。此命令要正常工作，对象树中必须存在 DGTD 求解器区域。

**Syntax** |  **Description**  
---|---  
addemabsorptionmonitor; |  向 'DGTD' 求解器添加一个吸收监视器。此函数不返回任何数据。  
addemabsorptionmonitor(struct_data); |  添加一个吸收监视器，并使用包含“属性”和值对的结构体设置其属性。有关示例，请参阅 [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) 脚本命令页面。此函数不返回任何数据。  
  
**示例 1**

以下脚本命令将向对象树中已存在的 'DGTD' 求解器添加一个吸收监视器，并打印监视器的所有可用属性。
    
    
    addemabsorptionmonitor;
    ?set;

**示例 2**

以下脚本命令将向 'DGTD' 求解器添加一个吸收监视器，更改其名称，将其频率范围设置为与源相同，并将其分配给名为 "nanoparticle" 的固体。
    
    
    addemabsorptionmonitor; 
    set("name","Pabs");
    set("use source limits",1);
    set("reference source","plane_wave");  
    set("volume type","solid");
    set("volume solid","nanoparticle");

注意：上述脚本假设对象树中已存在名为 "nanoparticle" 的固体和名为 "plane_wave" 的源。  
---  
  
**参见**

- [adddgtdsolver](./adddgtdsolver.md)
- [addemfieldmonitor](./addemfieldmonitor.md)
- [addemfieldtimemonitor](./addemfieldtimemonitor.md)
