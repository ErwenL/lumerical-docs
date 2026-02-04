<!--
Translation from English documentation
Original command: emepropagate
Translation date: 2026-02-04 22:49:48
-->

# emepropagate

Propagates fields 用于 EME profile 监视器 和 计算 s-矩阵 和 用户 s-矩阵 results, as well as any error diagnostic results 当 在 Analysis mode 使用 EME 求解器. This 是 equivalent 到 clicking 该 "eme propagate" button. 

**语法** |  **描述**  
---|---  
emepropagate;  |  Propagate fields 和 s-矩阵 results. This 是 equivalent 到 该 "eme propagate" button 在 该 graphical 用户 interface.   
  
**示例**

This code 将 设置 up 该 group spans column 在 该 EME 分析 window 那么 propagate 使用 该 EME 求解器. 
    
    
    # 设置 group spans 到 1 micron  
    setemeanalysis("group spans",[1e-6;1e-6;1e-6]);  
    
    # propagate eme  
    emepropagate;

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ Spot size converter ](**%20to%20be%20defined%20**) , [ emesweep ](/hc/en-us/articles/360034405114-emesweep) , [ getemesweep ](/hc/en-us/articles/360034405134-getemesweep)
