<!-- Translated: 2024-01-XX by AI Assistant -->
<!-- Status: Initial translation -->
<!-- Review needed: Technical terms, consistency check -->

# runparallel

以并行模式启动仿真。等效于 run 和 run(3)。仿真完成后，所有仿真数据将保存到当前文件。此命令已被弃用，请使用 run。

**语法** | **描述**  
---|---  
runparallel; | 按照资源管理器中定义的并行模式启动仿真。此函数不返回任何数据。  

**示例**

```
newproject;
addfdtd; 
adddipole; 
runparallel;      
```

**另见**

[run](run.md), [runanalysis](runanalysis.md)
