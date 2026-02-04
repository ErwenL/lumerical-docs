<!--
Translation from English documentation
Original command: savedcard
Translation date: 2026-02-04 22:50:14
-->

# savedcard

Saves d-card 数据 到 一个 Lumerical 数据 文件 (ldf) 文件. D-cards 是 generally used 到 store 监视器 数据, but 可以 also 为 used 到 store 数据 从 求解器 对象.

Data is saved in the nonorm state. See the [ units and normalization ](https://optics.ansys.com/hc/en-us/articles/360034397034) section of the reference guide for more information.

**语法** |  **描述**  
---|---  
savedcard("文件名"); |  Saves all current d-cards (local 和 global) 到 该 specified ldf 文件. This 函数 does not 返回 any 数据.  
savedcard("文件名", "name1", "name2",...); |  Saves only 该 d-cards 使用 该 specified names, "name1", "name2", etc.  
  
**示例**

This example shows 如何 到 save all 数据 从 该 监视器 named xy_monitor.
    
    
    ?getdata; # view all d-cards
    savedcard("monitor_data","::model::xy_monitor");

This example shows 如何 到 save 该 required 数据 after performing 一个 频率 sweep 在 MODE. This 是 equivalent 到 该 GUI option "Export 用于 Interconnect".
    
    
    savedcard("FileName", "::model::FDE::数据::frequencysweep");

**参见**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ copydcard ](https://optics.ansys.com/hc/en-us/articles/360034930233-copydcard) , [ savedata ](https://optics.ansys.com/hc/en-us/articles/360034411174-savedata) , [ loaddata ](https://optics.ansys.com/hc/en-us/articles/360034411214-loaddata) , [ matlabsave ](https://optics.ansys.com/hc/en-us/articles/360034928113-matlabsave)
