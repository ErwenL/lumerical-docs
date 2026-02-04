<!--
Translation from English documentation
Original command: addwaveguide
Translation date: 2026-02-04 09:15:20
-->

# addwaveguide

在仿真空间中添加波导对象。

**语法** |  **描述**  
---|---  
addwaveguide; |  在仿真空间中添加波导。此函数不返回任何数据。  
addwaveguide(struct_data); |  添加波导，并使用包含"属性"和值对的struct设置其属性。此函数不返回任何数据。  
   
**示例**

以下脚本命令将使用4个极点创建弯曲波导。关于波导对象如何使用极点生成波导形状的详细信息，请参阅此KB页面：[结构 - 波导](/hc/en-us/articles/360034382234-Structures-Waveguide)。
    
    
    addwaveguide;  
    
    set("base width",600e-9);  
    set("base height",220e-9);  
    set("base angle",70);  
    
    pole = [0,0; 1,9; 6,9.8; 10,10]*1e-6;  
    set("poles",pole);  
       
    set("material","Si (Silicon) - Palik");

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
