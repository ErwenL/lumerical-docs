<!--
Translation from English documentation
Original command: addpyramid
Translation date: 2026-02-04 09:13:24
-->

# addpyramid

向仿真环境中添加[金字塔](/hc/en-us/articles/360034382254)图元。

**语法** |  **描述**  
---|---  
addpyramid; |  向仿真环境中添加金字塔图元。此函数不返回任何数据。  
addpyramid(struct_data);  |  添加金字塔图元，并使用包含"属性"和值对的struct设置其属性。此函数不返回任何数据。  
   
**示例**

以下脚本命令将向仿真环境中添加金字塔对象并设置其尺寸。
    
    
    addpyramid;
    set("name","my_pyramid");
    set("x span bottom",5e-6);
    set("x span top",3e-6);
    set("y span bottom",4e-6);
    set("y span top",3e-6);
    set("z span",1e-6);
    set("material","Si (Silicon) - Palik");

有关所添加金字塔对象的可编辑属性列表，请参见[金字塔 - 仿真对象](/hc/en-us/articles/360034382254)。

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
* [金字塔 - 仿真对象](https://optics.ansys.com/hc/en-us/articles/360034382254)
