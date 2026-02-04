<!-- Translation completed: 2026-02-04 -->
<!-- Original command: cadimport -->

# cadimport

**语法** | **描述**
---|---
stepimport("filename",scale_factor); | Add new structures from a specified CAD 文件. The list of supported 文件 formats can be found in the Knowledge Base article on [CAD 导入](https://optics.ansys.com/hc/en-us/articles/360034398374). SCALE_FACTOR (optional):

**示例**

The following 脚本 commands is used to create a 3D geometry based on the STEP 文件 provided in the Knowledge Base article on [CAD 导入](https://optics.ansys.com/hc/en-us/articles/360034398374).
    文件名 = "stepimport.step";  
    cadimport(文件名);
The following 脚本 commands is used to create a 3D geometry based on the SolidWork 文件 provided in the Knowledge Base article on [CAD 导入](https://optics.ansys.com/hc/en-us/articles/360034398374), using a scaling factor of \\(10^{-6}\\).
    文件名 = "Caliper.SLDPRT";  
    cadimport(文件名, -6);

The following 脚本 commands is used to create a 3D geometry based on the STEP 文件 provided in the Knowledge Base article on [CAD 导入](https://optics.ansys.com/hc/en-us/articles/360034398374).
    文件名 = "stepimport.step";  
    cadimport(文件名);
The following 脚本 commands is used to create a 3D geometry based on the SolidWork 文件 provided in the Knowledge Base article on [CAD 导入](https://optics.ansys.com/hc/en-us/articles/360034398374), using a scaling factor of \\(10^{-6}\\).
    文件名 = "Caliper.SLDPRT";  
    cadimport(文件名, -6);

**另请参阅**

[List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834), [stlimport](https://optics.ansys.com/hc/en-us/articles/360034924733), [stepimport](https://optics.ansys.com/hc/en-us/articles/360034404734-stepimport-Script-command)
