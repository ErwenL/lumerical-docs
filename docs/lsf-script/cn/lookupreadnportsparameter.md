# lookupreadnportsparameter

从包含设计查找表的 xml 文件中返回特定设计参数的插值 s 参数单元。

xml 文件应具有将 s 参数数据文件与设计参数关联的查找表。表关联的每个 s 参数文件应与 Optical N Port S-Parameter 元素兼容，格式完全相同，且不应包含任何标头。

**语法** | **描述**
---|---
out = lookupreadnportsparameter ("filename","table",design,"extracted"); | 从包含设计查找表的 xml 文件返回插值 s 参数单元：

  * filename：xml 文件的名称。
  * table：xml 文件内查找表的名称。
  * design：包含多个结构的单元，定义要提取的目标设计。
  * extracted：查找表内参数的名称，该参数保存每个设计对应的 s 参数数据文件名。

out = lookupreadnportsparameter ("filename","table",design,"extracted", opt); | 从包含设计查找表的 xml 文件返回插值 s 参数单元，并在结构 opt 中提供插值选项：

  * filename：xml 文件的名称。
  * table：xml 文件内查找表的名称。
  * design：包含多个结构的单元，定义要提取的目标设计。
  * extracted：查找表内参数的名称，该参数保存每个设计对应的 s 参数数据文件名。
  * opt：设置插值选项的结构。下表描述了结构字段。

选项结构具有以下字段，每个字段的拼写区分大小写。

**字段** | **描述**
---|---
method | 用于插值的方法。支持以下选项：

  * spline：样条插值方法，这是默认方法。
  * Geodesic：测地线插值方法，确保平滑过渡。选择测地线插值时，会对用于插值的原始数据点附近的点进行相似性检查，如果这些点不够相似，则数据粗糙，并显示警告。此方法不能用于外推。

passivity | 是否在插值前对 s 参数数据强制执行无源性。此字段仅在选择 "geodesic" 作为插值方法时影响结果。当数据为有源性时，测地线插值始终显示警告消息。支持以下选项：

  * enforce：确保 S 矩阵无源性，确保 s 参数的诱导 2 范数小于 1。这是默认方法。
  * ignore：忽略 s 参数的无源性并按原样进行插值。

**注意**：有关如何强制执行无源性的更多信息，请参阅此知识库文章。

**示例**

根据用户定义的设计参数加载耦合器的 s 参数，设置插值目标：

```
filename = "coupler.ixml";
table = "coupler";
radius = 3e-06;
gap = 3e-07;
design = cell(2);
# design（输入参数）
design{1} = struct;
design{1}.name = "radius";
design{1}.value = radius;
design{2} = struct;
design{2}.name = "gap";
design{2}.value = gap;
```

使用样条插值插值参数并加载到 S 参数单元数组：

```
?M = lookupreadnportsparameter( filename, table, design, "out_filename" );
```

使用测地线插值插值参数并加载到 S 参数单元数组，忽略元素的无源性：

```
?M = lookupreadnportsparameter( filename, table, design, "out_filename", {"method":"geodesic","passivity":"ignore" );
```

设置参数到元素：

```
addelement("Optical N Port S-Parameter");
setvalue('SPAR_1','s parameters',M);
```

"coupler.ixml" 是包含耦合器参数与不同 s 参数之间映射的查找表：

```
<?xml version="1.0" encoding="UTF-8"?>
<lumerical_lookup_table version="1.0" name = "coupler">
  <association>
    <design>
      <value name="radius" type="double">3e-06</value>
      <value name="gap" type="double">3e-07</value>
    </design>
    <extracted>
      <value name="out_filename" type="string">radius_3_gap_3.txt</value>
    </extracted>
  </association>
</lumerical_lookup_table>
```

例如 "radius_3_gap_3.txt" 文件包含 'Optical N Port S-Parameter' 元素的 s 参数：

```
("port 1","TE",1,"port 1",1,"transmission")
(3,3)
 2.262580000000e+014 1.034036580296e-002 -2.629253819969e+000
 2.275690000000e+014 9.716591457652e-003 -2.734774978072e+000
 2.288790000000e+014 6.884340821788e-003 -2.838683842048e+000
("port 1","TE",1,"port 2",1,"transmission")
(3,3)
 2.262580000000e+014 9.847090174703e-001 1.376105202083e-001
 2.275690000000e+014 9.959778891317e-001 1.450376288706e-001
 2.288790000000e+014 1.002869828593e+000 1.483183421805e-001
```

**另请参阅**

- [命令列表](./命令列表.md)
- [lookupopen](./lookupopen.md)
- [lookupread](./lookupread.md)
- [lookupwrite](./lookupwrite.md)
- [lookupclose](./lookupclose.md)
- [lookupreadtable](./lookupreadtable.md)
- [lookupreadvalue](./lookupreadvalue.md)
- [lookupappend](./lookupappend.md)
- [insert](./insert.md)
