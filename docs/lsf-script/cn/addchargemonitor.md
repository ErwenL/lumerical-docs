<!--
Translation from English documentation
Original command: addchargemonitor
Translation date: 2026-02-03
-->

# addchargemonitor

向仿真环境添加[电荷监视器](/hc/en-us/articles/360034398154)。此命令要求对象树中存在CHARGE求解器区域。

**Syntax** | **Description**
---|---
addchargemonitor; | 向仿真环境添加电荷监视器。此函数不返回任何数据。
addchargemonitor(struct_data); | 添加电荷监视器，并使用包含"property"和值对的结构体设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。

**Example**

以下脚本命令将向仿真环境添加2D y法向电荷监视器，设置其尺寸，并启用将电荷数据保存到.mat文件。

    addchargemonitor;
    set("name","charge");
    set("monitor type",6);  # 2D y-normal
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("save data",1);
    filename = "charge_data.mat";
    set("filename",filename);

**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [addbandstructuremonitor](./addbandstructuremonitor.md)
- [addefieldmonitor](./addefieldmonitor.md)
- [addjfluxmonitor](./addjfluxmonitor.md)