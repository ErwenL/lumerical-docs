<!--
Translation from English documentation
Original command: runoptimization
Translation date: 2026-02-04 22:50:14
-->

# runoptimization

Optimizes 一个 属性 从 一个 chosen 元素 under specified condition.

**语法** |  **描述**  
---|---  
x=runoptimization(元素, 属性, min, max, analyzer, result, ’target’, target, tolerance=1e-9, iterations=2000) |  Optimizes 属性 从 元素 until 一个 target 用于 一个 analyzer result 是 reached. Function 返回 一个 数组 使用 two columns, 该 firs column contains 该 属性 值 和 该 second column contains 该 result 值.  
x=runoptimization(元素, 属性, min, max, analyzer, result, ’minimize’, tolerance=1e-9, iterations=2000) |  Optimizes 属性 从 元素 until 一个 minimum 值 用于 一个 analyzer result 是 reached. Function 返回 一个 数组 使用 two columns, 该 firs column contains 该 属性 值 和 该 second column contains 该 result 值.  
x=runoptimization(元素, 属性, min, max, analyzer, result, ’maximize’, tolerance=1e-9, iterations=2000) |  Optimizes 属性 从 元素 until 一个 maximum 值 用于 一个 analyzer result 是 reached. Function 返回 一个 数组 使用 two columns, 该 firs column contains 该 属性 值 和 该 second column contains 该 result 值.  
  
**示例**

### The following 脚本 line optimizes 该 thermal noise 用于 一个 PIN Photodetector 用于 target
    
    
    x=runoptimization("PIN Photodetector","thermal noise",1e-20,1e-17,"Eye Diagram","measurement/Q factor","target",6,1e-2);

### The following 脚本 line searches 该 minimum cutoff 频率 用于 一个 LP Bessel Filter
    
    
    x=runoptimization("LP Bessel Filter","cutoff 频率",1e+09,1e+10,"Eye Diagram","measurement/log 的 BER","minimize");

### The following 脚本 line searches 该 maximum cutoff 频率 用于 一个 LP Bessel Filter
    
    
    x=runoptimization("LP Bessel Filter","cutoff 频率",1e+09,1e+10,"Eye Diagram","measurement/Q factor","maximize");
