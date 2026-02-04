<!--
Translation from English documentation
Original command: addgaussian
Translation date: 2026-02-03 23:50:11
-->

# addgaussian

向仿真环境中添加一个[Gaussian source](/hc/en-us/articles/360034382854)（高斯源）。

**Syntax** |  **Description**  
---|---  
addgaussian; |  向仿真环境中添加一个高斯源。此函数不返回任何数据。  
addgaussian(struct_data); |  添加一个高斯源，并使用包含"属性"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将在仿真环境中添加一个高斯源，该源将沿负z方向传播。脚本将设置源的尺寸（和位置），并使用标量近似定义光束腰半径。
    
    
    addgaussian;
    set("injection axis","z");
    set("direction","backward");
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",10e-6);
    set("use scalar approximation",1);
    set("waist radius w0",0.5e-6);
    set("distance from waist",-5e-6);

**参见**

- [set](./set.md)
- [addplane](./addplane.md)
- [addtfsf](./addtfsf.md)
