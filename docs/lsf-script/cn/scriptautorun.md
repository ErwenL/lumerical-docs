<!-- Translation completed: Tue Feb 03 2026 -->
<!-- Original: scriptautorun -->

# scriptautorun

禁用或启用通过输入脚本名称自动运行脚本文件。

**语法** |  **描述**  
---|---  
scriptautorun(option); |  选项包括：

  * 0：禁用脚本文件的自动运行
  * 1：启用脚本文件的自动运行

  
  
**示例**

以下示例假设您创建了一个名为 hello_world.lsf 的脚本文件，该文件打印消息"hello"。当运行以下命令时，您将收到错误消息"Error: prompt line 3: hello_world is not a valid function or variable name"，因为 scriptautorun 被禁用。
    
    
    clear;
    scriptautorun(0); #disable autorun
    hello_world;

当您启用 scriptautorun 时，脚本文件将被执行，消息"hello"将出现在脚本提示符中。
    
    
    clear;
    scriptautorun(1); #enable autorun
    hello_world;

如果 scriptautorun 被禁用，您仍然可以使用 feval 函数运行脚本文件。
    
    
    clear;
    scriptautorun(0); #disable autorun
    feval("hello_world");

**另请参阅**

- [命令列表](./index.md)
- [feval](./feval.md)
