<!--
Translation from English documentation
Original command: exportsweep
Translation date: 2026-02-04 22:49:48
-->

# exportsweep

Exports S-参数 results 从 一个 S-参数 sweep task 到 一个 .dat 文件 该 可以 为 loaded 通过 该 [Optical N-Port S-参数](**%20to%20be%20defined%20**) 元素 在 INTERCONNECT.

**语法** |  **描述**  
---|---  
exportsweep("sweep_name","文件名","format"); |  Exports S-参数 results 从 该 specified S-参数 sweep task 到 一个 .dat 文件 使用 specified 文件 name 在 该 current working directory. The "format" 可以 为 either "lumerical" 或 "touchstone" formats, 和 如果 not specified 该 "lumerical" format 将 为 used. The "touchstone" format 将 为 format v1.1.  If 该 maximum passivity over 该 频率 range 是 larger than 1.03 或 该 maximum reciprocity error over 该 频率 range exceeds 0.03, 一个 warning message 将 appear 在 该 脚本 prompt 当 you export 该 数据. If 一个 文件 的 该 same name already exists, 该 existing 文件 将 为 overwritten. This 函数 does not 返回 any 数据.  
  
注意 该 Touchstone format v1.1 doesn't handle different modes, so 该 数字 的 "ports" 是 really 该 数字 的 effective ports (端口/mode combinations).

**示例**

The following code 可以 为 used 到 export S-参数 数据 到 一个 Touchstone 文件 called s_params.s4p.
    
    
    exportsweep("s-参数 sweep","s_params.s4p", "touchstone"); 

**参见**

[addsweep](/hc/en-us/articles/360034930413-addsweep), [runsweep](/hc/en-us/articles/360034931413-runsweep), [getsweepresult](/hc/en-us/articles/360034409814-getsweepresult), [S-参数 矩阵 sweep](/hc/en-us/articles/360034403214-S-参数-矩阵-sweep)
