<!-- Translation: updatesourcemode -->
<!-- Date: 2026-02-03 -->
<!-- Original: updatesourcemode -->

# updatesourcemode

更新所选模式源的源模式分布。如果源中没有存储模式分布，则将选择具有最高有效折射率的模式。如果源中已存储模式，则将选择与旧模式重叠最佳的模式。注意，在运行此命令之前必须先选择模式源。

**语法** | **说明**
---|---
?updatesourcemode; | 更新所选模式源的模式分布。返回旧模式和新模式之间的电磁场重叠分数。
?updatesourcemode(mode_number); | 更新模式源并选择所需的模式编号。例如，updatesourcemode(1);将计算基模。请注意，进行此调用将强制重新计算模式，即使之前已计算过相同的模式。此外，进行此调用将强制模式选择方法变为"用户选择"。此可选参数在FDTD 8.6.3和MODE 6.5.3中引入。

注意：在使用updatesourcemode之前保存仿真文件 如果您有一个更新仿真网格的脚本文件，那么应该在更新源模式之前使用[save脚本命令](./save.md)。这将确保在计算新模式之前已更新网格。

注意：重叠 两个模式之间的电磁场重叠分数由下面的表达式给出。它也是mode2的功率可以在mode1中传播的比例。有关更多信息，请参见[overlap脚本命令](./overlap.md)。

**示例**

选择源，然后更新模式分布。一旦更新了模式分布，输出来模式的有效折射率并可视化模式场分布。


    # 更新源模式分布  
    select("source");  
    updatesourcemode;  
    
    # 获取模式分布和有效折射率  
    n=getresult("source","neff");  
    ?"Effective index = " + num2str(n.neff);  
    field=getresult("source","mode profiles");  
      
    visualize(field);

**参见**

[操作对象](./360037228834.md), [addmode](./addmode.md), [clearsourcedata](./clearsourcedata.md), [clearmodedata](./clearmodedata.md), [getresult](./getresult.md), [overlap](./overlap.md), [expand](./expand.md), [seteigensolver](./seteigensolver.md), [geteigensolver](./geteigensolver.md), [updatemodes](./updatemodes.md), [updateportmodes](./updateportmodes.md)
