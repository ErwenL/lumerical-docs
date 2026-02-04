<!--
Translation from English documentation
Original command: adddope
Translation date: 2026-02-03 22:29:44
-->

# adddope

向仿真环境中添加一个 [恒定掺杂对象](/hc/en-us/articles/360034918653)。此命令要求对象树中存在 CHARGE 求解器区域。

**Syntax** |  **Description**  
---|---  
adddope; |  添加一个恒定掺杂区域。此函数不返回任何数据。  
adddope(struct_data); |  添加一个恒定掺杂区域，并使用包含“属性”和值对的结构体设置其属性。有关示例，请参阅 [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) 脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将添加一个 p 型恒定掺杂对象，并设置其尺寸和浓度。
    
    
    adddope;
    set("name","pwell");
    set("dopant type","p");
    set("concentration",1e25);  # SI unit (/m3)
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",1e-6);
    set("z",5e-6);
    set("z span",1e-6);

**参见**

- [set](./set.md)
- [adddiffusion](./adddiffusion.md)
