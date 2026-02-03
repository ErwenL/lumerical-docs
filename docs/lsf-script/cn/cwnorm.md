<!--
Translation from English documentation
Original command: cwnorm
Translation date: 2026-02-03 10:55:30
-->

# cwnorm

使用CW归一化。所有仿真数据将归一化到注入的源功率。大多数用户倾向于在CW归一化状态下进行分析，因为它消除了源有限脉冲长度引起的任何影响。它还将所有电磁场的单位转换为与时间域中相同。注意，此命令在布局模式和分析模式下均有效。

此函数控制位于设置 - 归一化状态中的复选框。

**Syntax** |  **Description**  
---|---  
cwnorm; |  使用CW归一化。使用对象树中的第一个活动源；此函数不返回任何数据。  
cwnorm(norm_option) |  norm_option: 1 (第一个源), 2 (所有源的平均值)  
  
**Example**

此示例展示如何切换到cwnorm状态。
    
    
    cwnorm; # normalized to the first active source  
      
    cwnorm(1); # normalized to the first active source  
    cwnorm(2); # normalized to the average of all the sources

**参见**

- [nonorm](../en/nonorm.md)
- [Units and normalization](/hc/en-us/articles/360034397034)
- [Frequency Domain Normalization](/hc/en-us/articles/360034394234-Frequency-domain-normalization)
