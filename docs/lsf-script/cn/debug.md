<!--
Translation from English documentation
Original command: debug
Translation date: 2026-02-03 22:32:18
-->

# debug

打开调试工具窗口。此命令用于调试目的。使用此命令时，脚本将运行到debug命令之前的行。然后用户可以开始调用其他命令来测试已运行的命令。一旦工具窗口关闭，脚本行将继续运行。允许使用多个debug命令。 

**Syntax** |  **Description**  
---|---  
debug;  |  打开调试工具窗口。此命令也可用于分析脚本中。   
  
 **示例**

此示例展示如何使用debug命令。以下示例显示第3行有一个错误。 
    
    
    x=linspace(1,10,10);
    y=linspace(1,10,5);
    ?x*y;
    Error: prompt line 3: matrix arguments of * are not the same size
    x=linspace(1,10,10);
    y=linspace(1,10,5);
    debug; # opens the debug utility window.
    ?x*y;

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
