<!--
Translation from English documentation
Original command: addjfluxmonitor
Translation date: 2026-02-04 00:59:46
-->

# addjfluxmonitor

向仿真环境中添加电流通量监视器。此命令要求对象树中存在CHARGE求解器区域。

**语法** |  **描述**  
---|---  
addjfluxmonitor; |  向仿真环境中添加电流通量监视器。此函数不返回任何数据。  
addjfluxmonitor(struct_data); |  使用包含"属性"和值对的struct添加电流通量监视器并设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
   
**示例**

以下脚本命令将向仿真环境中添加一个2D y-normal电流通量监视器并设置其尺寸。
    
    
    addjfluxmonitor;
    set("name","current_flux");
    set("monitor type",7);  # 2D z-normal
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
* [addefieldmonitor](https://optics.ansys.com/hc/en-us/articles/360034924633-addefieldmonitor)
* [addchargemonitor](https://optics.ansys.com/hc/en-us/articles/360034924613-addchargemonitor)
* [addbandstructuremontor](https://optics.ansys.com/hc/en-us/articles/360034924653-addbandstructuremonitor)
