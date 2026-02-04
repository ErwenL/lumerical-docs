# matlabload

## 注释

  * 从 Lumerical 2024 R1 开始，MATLAB Linux 库不再随 Lumerical 应用程序打包
  * 我们仍然支持 7 及更高版本的 MATLAB 文件加载和保存
  * 有关更多信息，请参阅此知识库文章。

将 Matlab .mat 数据加载到工作区。

**语法** | **描述**
---|---
matlabload("filename"); | 将指定 .mat 文件的数据加载到工作区。

**示例**

这是一个简单的示例，演示如何从 .mat 数据文件加载到工作区。

```
# 此文件有变量 data1、data2、data3
matlabload("myData.mat");
?workspace;
matrices:
 data1 data2 data3
```

**另请参阅**

- [MATLAB 脚本集成 – Ansys Optics](./MATLAB%20脚本集成.md)
- [命令列表](./命令列表.md)
- [matlabput](./matlabput.md)
- [matlabsavelegacy](./matlabsavelegacy.md)
- [matlabsave](./matlabsave.md)
