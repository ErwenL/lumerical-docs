# exportnetlist

导出当前电路的网表。

**语法** | **描述**
---|---
exportnetlist;
exportnetlist (filename);
exportnetlist (element,filename,overwrite=true); | 导出当前电路的网表。'filename' 是输出网表名称，'element' 是要导出的复合元素。如果 'overwrite' 为 true，任何与 'filename' 同名的现有网表文件都将被覆盖。如果未提供 'element'，则导出当前选中的复合元素，否则导出根元素。

### 示例

```powershell
exportnetlist;
exportnetlist("circuit.spi");
```

### 另请参阅

[命令列表](../命令列表.md)、[importnetlist](./importnetlist.md)