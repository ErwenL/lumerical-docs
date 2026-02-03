<!--
Translation from English documentation
Original command: adddevice
Translation date: 2026-02-03 10:54:25
-->

# adddevice

向仿真环境中添加一个 CHARGE 求解器区域。 

注意：'adddevice' 命令已弃用，将在未来版本中移除。请参考 [addchargesolver](/hc/en-us/articles/360034924473-addchargesolver) 作为替代。   
---  
**Syntax** |  **Description**  
---|---  
adddevice;  |  向仿真环境中添加一个 CHARGE 求解器区域。此函数不返回任何数据。   
  
**示例**

以下脚本命令将添加一个 2D y-normal CHARGE 求解器区域，设置其尺寸，并运行仿真。该脚本假设仿真环境已设置好几何形状和边界条件。 
    
    
    adddevice;
    set("solver geometry",1);  #  2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);
    run;

**参见**

- [List of commands](./list-of-commands.md)
- [set](./set.md)
- [run](./run.md)
