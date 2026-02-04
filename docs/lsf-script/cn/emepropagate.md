<!--
Translation from English documentation
Original command: emepropagate
Translation date: 2026-02-03 23:47:32
-->

# emepropagate

为EMEprofile监视器传播场并计算s矩阵和用户s矩阵结果，以及使用EME求解器在分析模式下的任何错误诊断结果。这相当于点击"eme propagate"按钮。 

**Syntax** |  **Description**  
---|---  
emepropagate;  |  传播场和s矩阵结果。这相当于图形用户界面中的"eme propagate"按钮。   
  
 **示例**

此代码将在EME分析窗口中设置组跨度列，然后使用EME求解器进行传播。
    
    
     #设置组跨度为1微米
    setemeanalysis("group spans",[1e-6;1e-6;1e-6]);  
    
     #传播eme
    emepropagate;

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [emesweep](./emesweep.md)
- [getemesweep](./getemesweep.md)
