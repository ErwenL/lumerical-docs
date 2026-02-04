<!--
---
**Translation metadata**
- English title: stepimport
- Chinese title: stepimport - STEP 文件导入
- Status: Completed
- Translator: AI
- Last updated: 2026-02-03
- Difficulty: Intermediate
- Priority: Standard
---
-->

# stepimport

将结构添加到模拟环境中，结构几何从指定的 [STEP 或 CAD 文件](https://optics.ansys.com/hc/en-us/articles/360034398374) 加载。此命令与 [cadimport](./cadimport.md) 相同。

| **语法** | **描述** |
|---|---|
| stepimport("filename",scale_factor); | 从指定的 CAD 文件添加新结构。支持的文件格式列表可在关于 [CAD 导入](https://optics.ansys.com/hc/en-us/articles/360034398374) 的知识库文章中找到。SCALE_FACTOR（可选）：<br><br>* 允许值为 3、0、-3、-6、-9，对应于 Ansys Lumerical Multiphysics™ 中 STEP 导入对话框的选项。例如，值 -9 表示以米保存的 STEP 文件将被视为以纳米为单位读取。结构将导入为实际大小的 \(10^{-9}\) 倍。<br><br>* 当省略 'scale_factor' 时，应用'无缩放' |

此函数不返回任何数据。
注意：如何处理 "Model size exceeds valid box" 错误
有限元 IDE 中的几何不能超过最大尺寸，即固定的长度单位数。可以通过更改求解器以使用更大的长度单位，或提供较小的 'scale_factor' 参数来避免此错误。

---

**示例**

以下脚本命令用于根据关于 [CAD 导入](https://optics.ansys.com/hc/en-us/articles/360034398374) 的知识库文章中提供的 STEP 文件创建 3D 几何。

```
filename = "stepimport.step";  
stepimport(filename);
```

以下脚本命令用于根据关于 CAD 导入的知识库文章中提供的 SolidWork 文件创建 3D 几何，使用 \(10^{-6}\) 的缩放因子。

```
filename = "Caliper.SLDPRT";  
stepimport(filename, -6);
```

**另请参见**

[ 命令列表 ](./command_list.md) , [ stlimport](./stlimport.md) , [cadimport](./cadimport.md)
