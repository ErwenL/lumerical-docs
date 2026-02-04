<!--
---
title: setpersistcheckouts
command_type: property
---
-->

# setpersistcheckouts

设置是否启用[持久性许可证签出](persistent-license-checkout.md)功能。

**语法** | **描述**
---|---
`setpersistcheckouts("state");` | 设置是否启用预签许可证签出功能。唯一接受的状态是逻辑真值和假值状态或逻辑0和1。

**示例**

```
# 启用持久性许可证签出功能

setpersistcheckouts(true);

# 禁用持久性许可证签出功能
# 这里使用逻辑0代替false

setpersistcheckouts(0);
```
