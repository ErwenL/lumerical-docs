# mcfit

脚本命令对包含多个频率相关传输值的文件运行多系数拟合。

**语法** | **描述**
---|---
mcfit(filenamein,filenameout,npoles,tolerance,automatic) ; | 对包含多个频率相关传输值的文件（filenamein）运行多系数拟合，每个传输依赖于工作点，并生成包含拟合数据的文件（filenameout）。极点数和拟合容差分别由参数 npoles 和 tolerance 定义。参数 'automatic' 定义拟合是使用用户定义的 npoles 还是自动估计极点数。

**另请参阅**

- [命令列表](./命令列表.md)
- [mczfit](./mczfit.md)
