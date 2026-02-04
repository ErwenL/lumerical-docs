# exportcsvresults

此脚本命令可将仿真结果导出为逗号分隔值格式的文件，这些文件可由 Microsoft Excel 打开。

**语法** | **描述**
---|---
exportcsvresults("filename") | 将整个仿真的结果导出到多个 .cvs 文件，文件名为 filename_elementname.csv
exportcsvresults("filename", "elementname") | 将指定元素的结果导出到 .cvs 文件，文件名为 filename_elementname.csv

**参数** | **类型** | **描述**
---|---|---
filename | string | .csv 文件名
elementname | string | 元素名称

### 另请参阅

[命令列表](../命令列表.md)