<!--
Translation from English documentation
Original command: adddiffusion
Translation date: 2026-02-03 22:25:38
-->

# adddiffusion

向仿真环境中添加一个 [扩散掺杂区域](/hc/en-us/articles/360034918673)。此命令要求对象树中存在 CHARGE 求解器区域。

**Syntax** |  **Description**  
---|---  
adddiffusion; |  在仿真环境中添加一个扩散掺杂区域。此函数不返回任何数据。  
adddiffusion(struct_data); |  添加一个扩散掺杂区域，并使用包含“属性”和值对的结构体设置其属性。有关示例，请参阅 [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) 脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将添加一个 n 型扩散掺杂对象并设置其属性。掺杂剂引入的面由“source face”属性定义，峰值掺杂浓度由“concentration”属性定义。“junction width”属性定义了掺杂浓度从（峰值）浓度下降到掺杂对象其他面的低“ref concentration”的距离。
    
    
    adddiffusion;
    set("name","nwell");
    # set dimensionset("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",1e-6);
    set("z",5e-6);
    set("z span",1e-6);
    # set doping profile
    set("dopant type","n");
    set("source face",6);  # upper z
    set("junction width",0.2e-6);
    set("concentration",1e25);  # SI unit (/m3)

下图显示了生成的掺杂分布。

有关掺杂对象本身（包括扩散参数）的更多信息，请参阅[本文](https://support.lumerical.com/hc/en-us/articles/360034918673)。

**参见**

- [set](./set.md)
- [adddope](./adddope.md)
