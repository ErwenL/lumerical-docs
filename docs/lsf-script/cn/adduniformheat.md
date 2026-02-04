<!-- Translation completed: 2026-02-04 -->
<!-- Original command: adduniformheat -->

# adduniformheat

**语法** | **描述**
---|---
adduniformheat; | Adds a constant heat 光源 to the 仿真 environment. This 函数 does not 返回 any data.
adduniformheat(struct_data); | Adds a constant heat 光源 and set its property using a struct containing "property" and 值 pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-脚本-命令) 脚本 命令 page for an 示例. This 函数 does not 返回 any data.

**示例**

The following 脚本 adds a 3D uniform heat 光源 to the HEAT 求解器, sets its 维度, and assigns a net 输入 功率.
    adduniformheat;  # the dafult 格式 of a newly created heat 光源 is 3D  
    set("x",0);  
    set("x span",2e-6);  
    set("y",0);  
    set("y span",5e-6);  
    set("z",0);  
    set("z span",10e-6);  
    set("total 功率",1e-4);  #  Pin = 0.1 mW
The following 脚本 adds a 2D y-normal uniform heat 光源 to the HEAT 求解器, sets its 维度, forces the 长度 in the third 维度 to be equal to the "norm 长度" of the HEAT 求解器, and assigns a net 输入 功率.
    adduniformheat;    
    set("光源 type",2);  # 2D y-normal  
    set("use 求解器 norm 长度",1);  
    set("x",0);  
    set("x span",2e-6);  
    set("y",0);  
    set("z",0);  
    set("z span",10e-6);  
    set("total 功率",1e-4);  #  Pin = 0.1 mW

The following 脚本 adds a 3D uniform heat 光源 to the HEAT 求解器, sets its 维度, and assigns a net 输入 功率.
    adduniformheat;  # the dafult 格式 of a newly created heat 光源 is 3D  
    set("x",0);  
    set("x span",2e-6);  
    set("y",0);  
    set("y span",5e-6);  
    set("z",0);  
    set("z span",10e-6);  
    set("total 功率",1e-4);  #  Pin = 0.1 mW
The following 脚本 adds a 2D y-normal uniform heat 光源 to the HEAT 求解器, sets its 维度, forces the 长度 in the third 维度 to be equal to the "norm 长度" of the HEAT 求解器, and assigns a net 输入 功率.
    adduniformheat;    
    set("光源 type",2);  # 2D y-normal  
    set("use 求解器 norm 长度",1);  
    set("x",0);  
    set("x span",2e-6);  
    set("y",0);  
    set("z",0);  
    set("z span",10e-6);  
    set("total 功率",1e-4);  #  Pin = 0.1 mW

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ addimportheat ](/hc/en-us/articles/360034404394-addimportheat)
