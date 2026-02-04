# exporthtml

生成描述元素的 html 文件。

**语法** | **描述**
---|---
exporthtml (element_name) | 生成描述自定义元素的 html 文件。文件列出元素类型、符号和属性列表。此命令仅适用于 Custom 文件夹或其子文件夹中的元素。

**示例**

```powershell
addelement("CW Laser");
# 将元素添加到 Custom 文件夹
addtolibrary;
# 将元素添加到 Custom 文件夹的子文件夹 "test_folder"
addtolibrary("test_folder");
# 导出 Custom 中 CW Laser 元素的 html 页面
exporthtml("CWL_1");
# 导出 "test_folder" 中 CW Laser 元素的 html 页面
exporthtml("test_folder::CWL_1");
# 导出 "test_folder" 中所有元素的 html 页面
exporthtml("test_folder");
```

**另请参阅**

[命令列表](../命令列表.md)、[newproject](./newproject.md)