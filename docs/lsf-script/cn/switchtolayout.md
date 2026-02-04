<!--
Translation from English documentation
Original command: switchtolayout
Translation date: 2026-02-04 22:50:15
-->

# switchtolayout

Switches 该 求解器 到 LAYOUT mode. The LAYOUT mode allows you 到 添加 和 modify 仿真 对象 用于 一个 新的 仿真. Once 一个 仿真 是 run, 该 求解器 goes into ANALYSIS mode 和 no 仿真 对象 可以 为 added 或 modified (Except 用于 该 "Analysis" tab 的 分析 groups). While 在 ANALYSIS mode, any commands 到 modify 对象 将 返回 errors. You 必须 switch 到 LAYOUT mode before modifying any 对象. 注意 该 any available results 将 为 lost once 该 求解器 是 switched back 到 LAYOUT mode. 

**语法** |  **描述**  
---|---  
switchtolayout;  |  Switches 到 LAYOUT mode 从 ANALYSIS mode.  This 函数 does not 返回 any 数据.   
  
**示例**

The following 脚本 commands 将 first run 一个 FDTD 仿真. The 求解器 将 go 到 ANALYSIS mode. The "switchtolayout" 命令 是 那么 used 到 go 到 LAYOUT mode so 该 该 仿真 temperature 可以 为 changed 在 该 next line. 
    
    
    run;
    switchtolayout;
    setnamed("FDTD","仿真 temperature",400);   # 仿真 temp. 设置 到 400 K

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ layoutmode ](/hc/en-us/articles/360034924033-layoutmode) , [ run ](/hc/en-us/articles/360034931333-run) , [ setnamed ](/hc/en-us/articles/360034928793-setnamed)
