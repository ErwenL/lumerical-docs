<!--
Translation from English documentation
Original command: cadimport
Translation date: 2026-02-04 22:49:36
-->

# cadimport

Adds a structure to the simulation environment with structure geometry loaded from specified [STEP or CAD file](https://optics.ansys.com/hc/en-us/articles/360034398374). This command is identical to [stepimport](https://optics.ansys.com/hc/en-us/articles/360034404734-stepimport-Script-command).

**语法** |  **描述**  
---|---  
stepimport("filename",scale_factor); |  Add new structures from a specified CAD file. The list of supported file formats can be found in the Knowledge Base article on [CAD import](https://optics.ansys.com/hc/en-us/articles/360034398374). SCALE_FACTOR (optional):

  * Allowed 值 是 3, 0, -3, -6, -9, 对应的 到 该 options 的 该 STEP import dialog 在 Ansys Lumerical Multiphysics™. For example, 该 值 -9 means 该 一个 文件 saved 在 米 将 为 read as 如果 在 纳米. Structures 将 为 imported as \\(10^{-9}\\) times 该 actual size.



  * When 'scale_factor' 是 omitted, 'no scaling' 是 applied

This 函数 does not 返回 any 数据.  
注意: How 到 handle 该 "Model size exceeds valid box" error The geometry 在 该 finite-元素 IDE cannot exceed 一个 maximum size, 一个 fixed 数字 的 长度 units. This error 可以 为 avoided 通过 changing 该 求解器 到 use 一个 larger 长度 unit, 或 通过 supplying 一个 smaller 'scale_factor' 参数.  
---  
  
**示例**

The following script commands is used to create a 3D geometry based on the STEP file provided in the Knowledge Base article on [CAD import](https://optics.ansys.com/hc/en-us/articles/360034398374).
    
    
    文件名 = "stepimport.step";  
    cadimport(文件名);

The following script commands is used to create a 3D geometry based on the SolidWork file provided in the Knowledge Base article on [CAD import](https://optics.ansys.com/hc/en-us/articles/360034398374), using a scaling factor of \\(10^{-6}\\).
    
    
    文件名 = "Caliper.SLDPRT";  
    cadimport(文件名, -6);

**参见**

[List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834), [stlimport](https://optics.ansys.com/hc/en-us/articles/360034924733), [stepimport](https://optics.ansys.com/hc/en-us/articles/360034404734-stepimport-Script-command)
