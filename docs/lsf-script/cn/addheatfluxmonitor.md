<!--
Translation from English documentation
Original command: addheatfluxmonitor
Translation date: 2026-02-04 00:12:33
-->

# addheatfluxmonitor

向HEAT求解器区域添加一个[热通量监视器](/hc/en-us/articles/360034398274)。只有在仿真环境中已存在'HEAT'求解器时才能添加此监视器。

**Syntax** |  **Description**  
---|---  
addheatfluxmonitor; |  向仿真环境添加热通量监视器。此函数不返回任何数据。  
addheatfluxmonitor(struct_data); |  添加热通量监视器，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将向HEAT求解器区域添加一个2D y-normal热通量监视器并设置其尺寸。
    
    
    addheatfluxmonitor;
    set("name","heat");
    set("monitor type",6);  # 2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);

**参见**

- [set](./set.md)
- [addtemperaturemonitor](./addtemperaturemonitor.md)
