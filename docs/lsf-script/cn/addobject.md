# addobject

<!-- 翻译说明：本文档已被人工翻译为中文，如有错误请指正 -->
<!-- Translation metadata: manually_translated=true, reviewer=none, last_updated=2026-02-04 -->

在FDTD和MODE中从对象库添加对象。该命令还可用于返回对象库中所有可用对象和分析组的名称。

**语法** | **说明**
---|---
addobject("script_ID"); | 从对象库添加对象。此函数不返回任何数据。
A = addobject; | 返回库中所有对象的名称并将其保存在名为"A"的单元数组中。

**示例**

从对象库添加圆角圆柱体对象。


    addobject("rounded_cyl");
    set("name","test_cyl");

打印所有可用元素的名称。


    A = addobject;
    L = length(A);
    for (i = 1:L) {
      ?A{i};
    }

**另请参阅**

[命令列表](/hc/en-us/articles/360037228834) , [addtogroup](/hc/en-us/articles/360034408454-addtogroup) , [addstructuregroup](/hc/en-us/articles/360034924093-addstructuregroup) , [addanalysisgroup](/hc/en-us/articles/360034404074-addanalysisgroup)
