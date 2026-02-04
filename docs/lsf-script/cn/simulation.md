<!--
Translation from English documentation
Original command: simulation
Translation date: 2026-02-04 22:50:14
-->

# 仿真

The 脚本 命令 仿真 返回 bandwidth related 仿真 属性. The 时间 domain simulator 将 try 到 accommodate 该 current channels into non-overlapping 仿真 bandwidths. Simulation 属性 include 该 center 频率, sample rate, 数字 的 samples, 频率 grid spacing, lower 和 upper 频率 limits. If 一个 single bandwidth 是 listed, 此 means all channels fit 在 该 same bandwidth, otherwise multiple bandwidths 是 required 到 accommodate all channels 使用 该 current sample rate. 

The 命令 also 返回 该 list 的 源 channels 在 该 current 仿真 before 该 仿真 estimate 该 仿真 bandwidths. This list includes 该 overlapped bandwidths. Simulation 属性 include 该 center 频率, sample rate, 数字 的 samples, 频率 grid spacing, lower 和 upper 频率 limits. If 一个 single bandwidth 是 listed, 此 means all channels fit 在 该 same bandwidth, otherwise multiple bandwidths 是 required 到 accommodate all channels 使用 该 current sample rate. 

This 函数 是 valid during 分析 或 run-时间 mode only. 

**语法** |  **描述**  
---|---  
out = 仿真(“bandwidth”);  |  返回 bandwidth related 仿真 属性.   
out = 仿真(“channels”);  |  返回 该 list 的 源 channels 在 该 current 仿真 before 该 仿真 estimate 该 仿真 bandwidths.   
out = 仿真(“single”);  |  返回 该 recommended setting 用于 仿真 使用 一个 single band (total field) 该 将 make sure all channels 是 merged into one 仿真 bandwidth.   
  
###  示例 

Access 仿真 属性 while 该 仿真 是 running, 该 circuit contains four laser sources. 
    
    
    #list 数字 的 simulated channels
    ?仿真("bandwidth");
    result: 
    1.9315e+014 1.6e+011 1024 1.5625e+008 1.9307e+014 1.9323e+014 
    1.9335e+014 1.6e+011 1024 1.5625e+008 1.9327e+014 1.9343e+01
    #list 数字 的 available channel sources
    ?仿真("channels");
    result: 
    1.931e+014 1.6e+011 1024 1.5625e+008 1.9302e+014 1.9318e+014 
    1.932e+014 1.6e+011 1024 1.5625e+008 1.9312e+014 1.9328e+014 
    1.933e+014 1.6e+011 1024 1.5625e+008 1.9322e+014 1.9338e+014 
    1.934e+014 1.6e+011 1024 1.5625e+008 1.9332e+014 1.9348e+014
    #list recommended setting 用于 single bandwidth
    ?仿真("single");
    result: 
    1.9325e+014 3.2e+011 2048 1.5625e+008 1.9309e+014 1.9341e+014

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834)
