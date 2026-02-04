<!-- Translated: 2024-01-XX by AI Assistant -->
<!-- Status: Initial translation -->
<!-- Review needed: Technical terms, consistency check -->

# runanalysis

运行分析对象中的分析脚本。

**注意**：已经有数据的脚本不会重新运行；要重新运行脚本，请先使用 [clearanalysis](clearanalysis.md) 清除数据。

**语法** | **描述**  
---|---  
runanalysis; | 运行仿真文件中所有分析对象的分析脚本。此函数不返回任何数据。  
runanalysis("group name"); | 运行名为 "group name" 的分析对象中的分析脚本。此函数不返回任何数据。  

**另见**

[run](run.md), [getdata](getdata.md), [getresult](getresult.md), [havedata](havedata.md), [clearanalysis](clearanalysis.md), [runsetup](runsetup.md)
