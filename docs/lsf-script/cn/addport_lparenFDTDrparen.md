<!--
Translation from English documentation
Original command: addport_lparenFDTDrparen
Translation date: 2026-02-04 09:12:50
-->

# addport (FDTD)

向FDTD仿真区域下的端口组添加端口对象。必须存在仿真区域才能添加端口有关端口对象的更多信息，请参见[端口](/hc/en-us/articles/360034382554-Ports)。本主题介绍FDTD中的addport命令——有关INTERCONNECT命令的信息，请参见[addport (INTERCONNECT)](/hc/en-us/articles/360034408934-addport)。

**语法** |  **描述**  
---|---  
addport; |  添加端口。此函数不返回任何数据。  
addport(struct_data); |  添加端口，并使用包含"属性"和值对的struct设置其属性。此函数不返回任何数据。  
   
**示例**以下脚本添加FDTD仿真区域和端口，然后设置端口名称，并选择端口模式和源模式。
    
    
    addfdtd; # add FDTD simulation region
    addport; # add port
    # set up port
    set("name","input_port"); 
    seteigensolver("bent waveguide",true); 
    seteigensolver("bend radius",10e-6); 
    updateportmodes(1:2); # select the first 2 modes of the port
    # select the second mode of the port to be the source mode
    select("FDTD::ports"); # select the port group
    set("source port","input_port");
    set("source mode","mode 2");

**参见**

* [端口](https://optics.ansys.com/hc/en-us/articles/360034382554-Ports)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
* [geteigensolver](https://optics.ansys.com/hc/en-us/articles/360034408794-geteigensolver)
* [seteigensolver](https://optics.ansys.com/hc/en-us/articles/360034929113-seteigensolver)
* [updateportmodes](https://optics.ansys.com/hc/en-us/articles/360034409174-updateportmodes)
* [clearportmodedata](https://optics.ansys.com/hc/en-us/articles/360034409194-clearportmodedata)
