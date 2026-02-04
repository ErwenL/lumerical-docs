<!--
Translation from English documentation
Original command: addelectricalcontact
Translation date: 2026-02-03 22:39:59
-->

# addelectricalcontact

向 CHARGE 求解器添加一个新的电接触边界条件 [[边界条件（电仿真）](/hc/en-us/articles/360034918833-Boundary-Conditions-Electrical-Simulation-)]。在添加电接触边界条件之前，对象树中必须存在 CHARGE 求解器区域。

**Syntax** |  **Description**  
---|---  
addelectricalcontact; |  向 CHARGE 求解器添加一个电接触边界条件。此函数不返回任何数据。  
  
**示例 1**

以下脚本命令将向对象树中已存在的求解器添加一个电接触边界条件，并打印边界条件的所有可用属性。
    
    
    addelectricalcontact;
    ?set;

**示例 2**

以下脚本命令将创建一个电边界条件，将固定的稳态电压分配给名为阴极的固体。对象树必须已存在 CHARGE 求解器和名为 'cathode' 的几何体。
    
    
    addelectricalcontact;
    set("name","cathode");
    set("bc mode","steady state");
    set("sweep type","single");
    set("voltage",0.2);  # setting the voltage to 0.2 V
    set("surface type","solid");
    set("solid","cathode");

**示例 3**

以下脚本命令将创建一个名为阴极的稳态电接触边界条件，并在预定义的一组电压上应用电压扫描。对象树必须已存在 CHARGE 求解器和名为 'cathode' 的几何体。
    
    
    addelectricalcontact;
    set("name","cathode");
    set("bc mode","steady state");
    set("sweep type","value");
    V = [0, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6];
    set("value table",V);
    set("surface type","solid");
    set("solid","cathode");

**示例 4**

以下脚本命令将设置一个瞬态电接触边界条件，其中电压在 t = 0 时为 0 V，在 t = 10 ps 和 100 ps 之间（tslew = 90 ps）阶跃至 1 V，并保持 1 V 直到 t = 500 ps。该边界条件分配给名为阴极的固体。
    
    
    addelectricalcontact;
    set("name","cathode_trans");
    set("bc mode","transient");
    tstep = [0, 10e-12, 100e-12, 500e-12];
    V = [0, 0, 1, 1];
    set("transient voltage time steps",tstep);
    set("transient voltage table",V);
    set("surface type","solid");
    set("solid","cathode");

**参见**

- [addsurfacerecombinationbc](./addsurfacerecombinationbc.md)
