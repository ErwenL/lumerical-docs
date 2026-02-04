# partitionvolume

进入分区体积模式。

**语法** | **描述**
---|---
partitionvolume; | 进入分区体积模式

**示例**

在 CHARGE、HEAT、FEEM 或 DGTD 中创建新模拟并切换到分区模式。

```
newproject;  # 创建新模拟文件
adddgtdsolver;    # 添加 DGTD 求解器
partitionvolume;     # 进入分区体积模式
```

**另请参阅**

- [run](./run.md)
- [runanalysis](./runanalysis.md)
- [mesh](./mesh.md)
