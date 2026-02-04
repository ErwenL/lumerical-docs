<!--
Translation from English documentation
Original command: addeme
Translation date: 2026-02-03 22:47:05
-->

# addeme

向 MODE 仿真环境中添加一个 [本征模展开（EME）求解器区域](/hc/en-us/articles/360034917013)。

**Syntax** |  **Description**  
---|---  
addeme; |  向仿真环境中添加一个 EME 求解器区域。此函数不返回任何数据。  
addeme(struct_data); |  添加一个 EME 求解器区域，并使用包含“属性”和值对的结构体设置其属性。有关示例，请参阅 [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) 脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将添加一个 EME 求解器区域，设置其尺寸和其他属性，并运行仿真。该脚本假设仿真环境已设置好几何结构。
    
    
    addeme;
    # set dimension
    set("x min",-8e-6);
    set("y",0);
    set("y span",5.5e-6);
    set("z",0.5e-6);
    set("z span",7e-6);
    # set cell properties
    set("number of cell groups",3);
    set("group spans",[3e-6; 10e-6; 3e-6]);
    set("cells",[1; 19; 1]);
    set("subcell method",[0; 1; 0]);   # 0 = none,  1 = CVCS
    # set up ports: port 1
    select("EME::Ports::port_1");
    set("use full simulation span",1);
    set("y",0);
    set("y span",5.5e-6);
    set("z",0);
    set("z span",7e-6);
    set("mode selection","fundamental mode");
    # set up ports: port 2
    select("EME::Ports::port_2");
    set("use full simulation span",1);
    set("y",0);
    set("y span",5.5e-6);
    set("z",0);
    set("z span",7e-6);
    set("mode selection","fundamental mode");
    run;

**参见**

- [select](./select.md)
- [run](./run.md)
- [addvarfdtd](./addvarfdtd.md)
- [addfde](./addfde.md)
