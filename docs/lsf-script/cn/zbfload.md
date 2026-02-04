<!-- Translation completed: 2026-02-04 -->
<!-- Original command: zbfload -->

# zbfload

**语法** | **描述**
---|---
zbfload | Select the 文件 to 加载 with the 文件 browser.  This 函数 does not 返回 any data.
zbfload("filename"); | Loads data from a zbf 文件 called "文件名" without a 文件 browser.
zbfload("filename", propagation axis) | Loads data from a zbf 文件 called "文件名" without a 文件 browser for a specified 传播 axis. The 传播 axis is an 整数 值 that indicates the x, y and z axis.
zbfload("filename", propagation axis, offset); | Loads data from a zbf 文件 called "文件名" without a 文件 browser for a specified 传播 axis with the specified offset. The offset is a floating 数字 数组 that indicates the x, y and z coordinates shift of the 加载-in data to the original data.

**另请参阅**

[ zbfexport ](/hc/en-us/articles/360034928253-zbfexport) , [ zbfread ](/hc/en-us/articles/360034408154-zbfread) , [ zbfwrite ](/hc/en-us/articles/360034928293-zbfwrite) , [ List of commands ](/hc/en-us/articles/360037228834)
