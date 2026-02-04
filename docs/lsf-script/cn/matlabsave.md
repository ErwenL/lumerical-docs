# matlabsave

## 注释

  * 从 Lumerical 2024 R1 开始，MATLAB Linux 库不再随 Lumerical 应用程序打包
  * 我们仍然支持 7 及更高版本的 MATLAB 文件加载和保存
  * 有关更多信息，请参阅此知识库文章。

将 Lumerical 工作区变量保存到 MATLAB .mat 数据文件。

**语法** | **描述**
---|---
matlabsave(""); | 将所有工作区变量保存到与模拟文件同名的 .mat 文件。此函数不返回任何数据。
matlabsave("filename"); | 将所有工作区变量保存到指定的 .mat 文件。
matlabsave("filename", var1, ..., varN); | 将指定的工作区变量保存到 .mat 文件。

**示例**

简单示例：

```
x=1:10;
y=x^2;
matlabsave("x_squared_data", x, y);
```

保存来自名为 xy_monitor 的监视器的数据。数据首先使用 getdata 和 transmission 等脚本函数获取。然后使用 matlabsave 函数保存这些工作区变量。可以使用 num2str 命令创建复杂的文件名。当执行参数扫描时这很有用，因为扫描中的每个点都需要唯一的文件名。

```
# 从模拟获取原始矩阵数据
mname="xy_monitor";       # 监视器名称
x=getdata(mname,"x");      # 与 Ex 场相关的位置向量
y=getdata(mname,"y");      # 与 Ex 场相关的位置向量
Ex=getdata(mname,"Ex");     # 监视器处的 Ex 场
T=transmission(mname);     # 通过监视器的功率传输

# 将矩阵变量 x、y、Ex、T 和 i 保存到数据文件
i=1;
filename="results_"+num2str(i); # 设置文件名。i 可以是循环计数器变量。
matlabsave(filename, x,y,Ex,T,i);
```

将 Lumerical 数据集（如 Electric field vs x,y,z,f）保存到 .mat 文件。Lumerical 数据集将使用 struct 数据类型导入 Matlab。

```
# 从模拟获取电场数据集
mname="xy_monitor";       # 监视器名称
E=getresult(mname,"E");     # 监视器处的 E 场

# 将数据集保存到 mat 文件
filename="ElectricField";
matlabsave(filename, E);
```

**另请参阅**

- [MATLAB 脚本集成 – Ansys Optics](./MATLAB%20脚本集成.md)
- [matlabput](./matlabput.md)
- [matlabsavelegacy](./matlabsavelegacy.md)
- [matlabload](./matlabload.md)
- [vtksave](./vtksave.md)
