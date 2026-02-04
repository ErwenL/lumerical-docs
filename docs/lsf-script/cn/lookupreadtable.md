# lookupreadtable

从包含设计和提取参数查找表的文件中返回插值矩阵。

**语法** | **描述**
---|---
out = lookupreadtable ("filename","table",design,"extracted"); | 从包含设计和提取参数查找表的文件中返回插值矩阵。参数 table 是文件内查找表的名称，design 是包含多个结构的单元数组，用于定义要搜索的设计参数，extracted 是要提取的参数名称。它将返回一个包含多列的矩阵。第一列是自变量，例如频率相关的传输值。

**示例**

以下脚本加载弯曲波导的频率相关传播特性：

```
filename = "waveguide.ixml";
table = "waveguide";
design = cell(1);
# design（输入参数）
design{1} = struct;
design{1}.name = "radius";
design{1}.value = 3e-6;
w_length = 1e-6;
M=lookupreadtable("waveguide.ixml", "waveguide", design, "Filename" );
# 在脚本元素中设置 s 参数
setsparameter("port 2", "port 1", "propagation", M, w_length);
setsparameter("port 1", "port 2", "propagation", M, w_length);
```

其中 "waveguide.ixml" 是包含波导 'radius' 与包含频率相关传播特性的 'Filename' 之间映射的查找表：

```
<?xml version="1.0" encoding="UTF-8"?>
<lumerical_lookup_table version="1.0" name = "waveguide">
  <association>
    <design>
      <value name="radius" type="double">3e-06</value>
    </design>
    <extracted>
      <value name="Filename" type="string">radius_3.txt</value>
    </extracted>
  </association>
</lumerical_lookup_table>
```

例如，"radius_3.txt" 文件包含一个矩阵，其中包含频率相关的传播特性：

```
2.315e+14552.62.787.071e+07
2.30918e+14552.72.717.076e+07
2.30335e+14543.32.737.075e+07
2.29753e+14543.32.767.076e+07
2.2917e+14544.72.787.062e+07
2.28588e+14545.52.727.061e+07
2.28006e+14546.62.717.064e+07
2.27423e+14544.22.737.061e+07
2.26841e+14533.12.747.063e+07
2.26258e+14532.22.757.069e+07
```

**另请参阅**

- [命令列表](./命令列表.md)
- [lookupopen](./lookupopen.md)
- [lookupread](./lookupread.md)
- [lookupwrite](./lookupwrite.md)
- [lookupclose](./lookupclose.md)
- [lookupreadvalue](./lookupreadvalue.md)
- [lookupreadnportsparameter](./lookupreadnportsparameter.md)
- [lookupappend](./lookupappend.md)
- [insert](./insert.md)
