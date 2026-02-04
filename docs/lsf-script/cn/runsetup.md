<!-- Translated: 2024-01-XX by AI Assistant -->
<!-- Status: Initial translation -->
<!-- Review needed: Technical terms, consistency check -->

# runsetup

Runsetup 强制运行结构组和分析组的设置脚本。

在大多数情况下，不需要使用此函数，因为在脚本结束时，如果对象已被修改，组设置脚本会自动重新运行。只有当你需要在脚本文件结束前强制设置脚本运行时才需要使用此函数。

**语法** | **描述**  
---|---  
runsetup; | 强制运行组的设置脚本。  

**示例**

我们使用 runsetup 命令在脚本完成之前强制组设置脚本运行。这使我们能够获取组的子对象的属性。

```
# 创建结构组。
deleteall;
addstructuregroup;
adduserprop("radius",2,0.5e-6);
myscript =      "addcircle; \n";
myscript = myscript + "copy(1e-6); \n";
myscript = myscript + "selectall; \n";
myscript = myscript + "set(\"radius\",radius);";
set("name","dimer");
set("script",myscript); 
# 尝试获取组内圆对象的半径
# 此命令在没有 runsetup 函数的情况下将失败
# runsetup 函数会强制组设置脚本运行
runsetup;
?getnamed("dimer::circle","radius");
```

**另见**

[操作对象](index.md), [get](get.md), [set](set.md), [runanalysis](runanalysis.md)
