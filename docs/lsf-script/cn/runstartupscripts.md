<!-- Translated: 2024-01-XX by AI Assistant -->
<!-- Status: Initial translation -->
<!-- Review needed: Technical terms, consistency check -->

# runstartupscripts

运行启动脚本。

**语法** | **描述**  
---|---  
runstartupscripts; | 按以下顺序运行启动脚本：

1. 全局共享启动脚本
2. 全局 $(PRODUCT) 启动脚本
3. 本地共享启动脚本
4. 本地 $(PRODUCT) 启动脚本

**示例**

以下示例在 INTERCONNECT 中运行 "runstartupscripts"，使用的脚本分别如下：

```
# Shared Startup.lsf
clear;
?a = 1;
# INTERCONNECT Startup.lsf
clear;
?b = 2;
```

输出结果：

```
runstartupscripts;
Shared Startup;
result: 
1  
Running script: /Users/$(Username)/.config/Lumerical/INTERCONNECT Startup.lsf
INTERCONNECT Startup;
result: 
2  
```

**另见**

[命令列表](index.md), [feval](feval.md)
