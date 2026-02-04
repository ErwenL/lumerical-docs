# filesavedialog

调用标准的 Windows 文件保存对话框。

**语法** | **描述**
---|---
out = filesavedialog; | 打开保存文件对话框并返回用户选择的路径。
out = filesavedialog(".ext"); | 打开保存文件对话框，仅显示扩展名为 .ext 的文件。返回用户选择的文件路径。

**示例**

将当前仿真保存到用户选择的路径。

```powershell
save(filesavedialog("*.fsp"));
```

**另请参阅**

[命令列表](../命令列表.md)、[fileopendialog](./fileopendialog.md)