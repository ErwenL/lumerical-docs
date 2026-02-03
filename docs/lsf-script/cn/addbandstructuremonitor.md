<!--
Translation from English documentation
Original command: addbandstructuremonitor
Translation date: 2026-02-03
-->

# addbandstructuremonitor

向仿真环境添加一个[能带结构监视器](/hc/en-us/articles/360034398174)。此命令要求对象树中存在CHARGE求解器区域。

**Syntax** | **Description**
---|---
addbandstructuremonitor; | 向仿真环境添加能带结构监视器。此函数不返回任何数据。
addbandstructuremonitor(struct_data); | 添加能带结构监视器，并使用包含"property"和值对的结构体设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。

**Example**

以下脚本命令将向仿真环境添加一个沿z轴的能带结构监视器，设置其尺寸，并启用保存真空能级（Evac）的能带。

    addbandstructuremonitor;
    set("name","band");
    set("monitor type",4);  # linear z
    set("x",0);
    set("y",0);
    set("z",0);
    set("z span",5e-6);
    set("record Evac",1);

**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [addefieldmonitor](./addefieldmonitor.md)
- [addchargemonitor](./addchargemonitor.md)
- [addjfluxmonitor](./addjfluxmonitor.md)