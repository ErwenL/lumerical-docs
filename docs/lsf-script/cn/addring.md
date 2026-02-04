<!--
Translation from English documentation
Original command: addring
Translation date: 2026-02-04 09:14:00
-->

# addring

向仿真环境中添加圆环图元。

**语法** |  **描述**  
---|---  
addring; |  向仿真环境中添加圆环图元。此函数不返回任何数据。  
addring(struct_data); |  添加圆环图元，并使用包含"属性"和值对的struct设置其属性。此函数不返回任何数据。  
   
**示例**

以下脚本命令将创建一个名为"new_ring"的半圆环，内半径为5微米，外半径为7微米，中心位于(x,y,z) = (1, 2, 0)微米。圆环厚度（z span）为10微米。
    
    
    addring;  
    set("name","new_ring");  
    set("x",1e-6);  
    set("y",2e-6);  
    set("inner radius",5e-6);  
    set("outer radius",7e-6);  
    set("z",0);  
    set("z span",10e-6);  
    set("theta start",0);  
    set("theta stop",180);

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
