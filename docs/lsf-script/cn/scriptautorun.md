<!--
Translation from English documentation
Original command: scriptautorun
Translation date: 2026-02-04 22:50:14
-->

# scriptautorun

Disable 或 启用 running 脚本 files automatically 通过 typing 该 脚本 name.

**语法** |  **描述**  
---|---  
scriptautorun(option); |  The options 是

  * 0: disables automatic running 的 脚本 files
  * 1: enables automatic running 的 脚本 files

  
  
**示例**

The following examples assume you have created 一个 脚本 文件 called hello_world.lsf 该 prints 该 message "hello". You 将 获取 该 error message "Error: prompt line 3: hello_world 是 not 一个 valid 函数 或 变量 name" 当 running 该 following commands because scriptautorun 是 disabled.
    
    
    clear;
    scriptautorun(0); #disable autorun
    hello_world;

When you 启用 scriptautorun 该 脚本 文件 是 executed 和 该 message "hello" 将 appear 在 该 脚本 prompt.
    
    
    clear;
    scriptautorun(1); #启用 autorun
    hello_world;

If scriptautorun 是 disabled you 可以 still run 脚本 files 使用 该 函数 feval.
    
    
    clear;
    scriptautorun(0); #disable autorun
    feval("hello_world");

**参见**

[ List 的 commands](/hc/en-us/articles/360037228834), [ feval](/hc/en-us/articles/360034405934-feval)
