# fileopendialog

调用标准的 Windows 文件打开对话框。

**语法** | **描述**
---|---
out = fileopendialog; | 打开文件对话框并返回用户选择的路径。
out = fileopendialog(".ext"); | 打开文件对话框，仅显示扩展名为 .ext 的文件。返回用户选择的文件路径。

**示例**

允许用户从文件打开对话框中选择要加载到 CAD 中的仿真文件。

```powershell
load(fileopendialog("*.fsp"));
```

**另请参阅**

[命令列表](../命令列表.md)、[filesavedialog](./filesavedialog.md)