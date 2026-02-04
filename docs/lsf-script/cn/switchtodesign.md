<!--
Translation from English documentation
Original command: switchtodesign
Translation date: 2026-02-04 22:50:15
-->

# switchtodesign

Switches INTERCONNECT 到 DESIGN mode. The DESIGN mode allows you 到 添加 和 modify circuit elements 用于 一个 新的 仿真. Once 一个 仿真 是 run, 该 求解器 goes into ANALYSIS mode 和 no elements 可以 为 added 或 modified. While 在 ANALYSIS mode, any 命令 到 modify 或 添加 elements 将 返回 error. You 必须 switch 到 DESIGN mode 用于 该. 注意 该 any available results 将 为 lost once 该 求解器 是 switched back 到 DESIGN mode. 

**语法** |  **描述**  
---|---  
switchtodesign;  |  Switches INTERCONNECT 从 ANALYSIS 到 DESIGN mode.  This 函数 does not 返回 any 数据.   
  
**示例**

The following 脚本 commands 将 first run 一个 INTERCONNECT 仿真. The 求解器 将 go 到 ANALYSIS mode. The "switchtodesign" 命令 是 那么 used 到 go 到 DESIGN mode so 该 该 仿真 "bitrate" 可以 为 changed 在 该 next line. 
    
    
    run;
    switchtodesign;
    setnamed('::Root Element','bitrate',2e10);  # bit rate 设置 到 20 Gbit/sec

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ switchtolayout ](/hc/en-us/articles/360034923993-switchtolayout) , [ layoutmode ](/hc/en-us/articles/360034924033-layoutmode) , [ designmode ](/hc/en-us/articles/360034924053-designmode)
