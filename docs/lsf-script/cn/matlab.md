# matlab

从 Lumerical 脚本提示符运行 MATLAB 命令。这使得可以从 Lumerical 脚本环境中访问扩展的数学和可视化功能。如果未启用 MATLAB 脚本集成，此函数将返回错误。

第一次调用 MATLAB 函数（matlab、matlabget 或 matlabput）时，将启动 MATLAB 会话并与 Lumerical 脚本环境建立连接。建立此连接后，可以使用 matlab 函数运行 MATLAB 命令。重要的是要理解 MATLAB 和 Lumerical 脚本变量工作区是完全独立和独立的。MATLAB 命令无法作用于 Lumerical 工作区中定义的变量，反之亦然。必须使用 matlabget 和 matlabput 函数在工作区之间传递变量。随时可以通过在 MATLAB 脚本提示符下输入命令来检查 MATLAB 工作区或与 MATLAB 环境交互。MATLAB 实例的工作目录始终设置为与 Lumerical 应用程序的工作目录匹配。

MATLAB 命令的输出将打印在 Lumerical 脚本提示符上。matlab 函数的一个限制是既不向 Lumerical 脚本提示符也不向 MATLAB 提示符提供错误报告。MATLAB 命令应在直接从 MATLAB 提示符测试后再从 Lumerical 脚本调用。输出缓冲区长度约为 1e5 个字符，多余的输出将被截断。

当您有一系列较长的 MATLAB 命令时，您可能会发现将它们保存到 MATLAB m 文件中更方便。然后，您可以通过运行单个命令来调用该 m 文件。

有关安装和配置说明，请参阅 MATLAB 集成设置。附加提示（特别是关于在 Matlab 中绘制数据）可在在线帮助的 MATLAB 部分找到。

**语法** | **描述**
---|---
matlab("command"); | command：包含一个或多个有效 MATLAB 命令的字符串。
matlab("  command_1  command_2  "); | 多行字符串可用于脚本文件中包含 MATLAB 命令块。脚本命令提示符不支持多行字符串。

**示例**

此示例将演示如何使用 MATLAB 的 "surf" 命令绘制 Ex 实部的曲面图。假设变量 x、y、Ex 已定义在 Lumerical 工作区中。

```
matlabput(x,y,Ex);
matlab("surf(y,x,real(Ex))");
```

此示例显示如何在单个 matlab 函数调用中包含多个 MATLAB 命令。在 MATLAB 中创建对数间隔向量，然后导入 Lumerical 工作区。

```
matlab("
 % 创建对数间隔向量
 x_min = 1
 x_max = 4
 x = logspace(x_min,x_max,1000)
");
matlabget(x);
```

**另请参阅**

- [命令列表](./命令列表.md)
- [matlabget](./matlabget.md)
- [matlabput](./matlabput.md)
- [MATLAB 集成设置](./MATLAB%20集成设置.md)
- [MATLAB](./MATLAB.md)
