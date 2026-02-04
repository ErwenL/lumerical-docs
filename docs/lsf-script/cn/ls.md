# ls

列出目录中的文件。也会列出 Lumerical 项目文件以外的文件。

**语法** | **描述**
---|---
out = dir; out = ls; | 输出是字符串。使用 ?dir; 将值写入屏幕。
out = dir("directory"); out = ls("directory"); | 列出指定目录中的文件。例如，?ls("C:\Downloads");

**示例**

使用 splitstring 命令获取目录内容到单元数组（即字符串数组）。然后遍历数组查找所有 FDTD 项目文件（.fsp）。

```
files = splitstring(dir,endl);    # 目录内容在单元(字符串)数组中
for(i=1:length(files)) {          # 遍历所有文件
 if (findstring(files{i},"fsp") != -1) {  # 查找 'fsp' 文件
  if (fileexists(files{i})) {       # 检查文件是否存在
   ?files{i};               # 输出文件名
   load(files{i});            # 加载文件
  }
 }
}
```

**另请参阅**

- [命令列表](./命令列表.md)
- [load](./load.md)
- [splitstring](./splitstring.md)
