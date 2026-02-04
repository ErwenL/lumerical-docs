# mapfind

从包含值映射的文件中返回最近的值。它返回位于指定最近点的字符串值。

**语法** | **描述**
---|---
out = mapfind (filename,x,y); | 从包含值映射的文件中查找最近的值。它返回位于最近点 (x,y) 的字符串值。
out = mapfind (filename,x,y,z); | 从包含值映射的文件中查找最近的值。它返回位于最近点 (x,y,z) 的字符串值。
out = mapfind (filename,x,y,z,w); | 从包含值映射的文件中查找最近的值。它返回位于最近点 (x,y,z,w) 的字符串值。

**示例**

从当前工作目录中的文本文件加载与给定波导宽度和高度相关联的有效折射率。该文件包含不同宽度和高度值的有效折射率，用 "," 分隔。例如：

```
width, height, neff

4.9e-007,2.1e-007,2.38997

4.9e-007,2.12222e-007,2.39885

4.9e-007,2.14444e-007,2.40796

4.9e-007,2.16667e-007,2.41618
```

第一行包含列标题（可选），接下来的四行包含数据。mapfind 命令的使用方法如下：

```
# 我们要查找的宽度和高度：
waveguide_width = 4.9e-007;
waveguide_height = 2.1e-007;
# 查找最近宽度-高度组合的有效折射率（值作为字符串返回）：
sneff = mapfind( "neff_map.txt", waveguide_width, waveguide_height );
# 将字符串 sneff 转换为数值
?neff = str2num(sneff);
result:
2.38997
```

**另请参阅**

- [read](./read.md)
- [readdata](./readdata.md)
