<!--
Translation from English documentation
Original command: gdsaddrect
Translation date: 2026-02-04 22:49:49
-->

# gdsaddrect

This 函数 添加 一个 rectangle 元素 到 一个 GDSII 文件 stream. This 是 just 一个 convenient 函数 到 创建 一个 polygon 用于 该 case 的 一个 rectangle. Other 元素 类型 用于 rectangle (such as, box) 是 not supported at 此 moment. Polygons 可以 only 为 added 在 一个 GDSII 单元格, so 此 命令 可以 为 called only 如果 一个 单元格 has been created.

**语法** |  **描述**  
---|---  
gdsaddrect(f, layer, x, y, width, height) |  添加 一个 rectangle 元素 在 一个 layer 使用 x-, y-coordinates, width 和 height.  
  
**Parameter** |  **Type** |  **描述**  
---|---|---  
f |  字符串 |  一个 文件 handle 该 was previously opened 使用 gdsopen.  
layer |  字符串 或 数字 |  字符串: 一个 字符串 的 该 form "layer:datatype" (用于 example "6:2") 可以 为 used 到 define 该 layer 数字 和 datatype 用于 此 结构 从 该 GDSII 文件 到 import. Layer 和 datatype 是 integers. 数字: defines 该 layer 数字 和 设置 该 datatype 到 为 zero.  
x |  数字 |  x-coordinate 的 该 center position 在 米.  
y |  数字 |  y-coordinate 的 该 center position 在 米.  
width |  数字 |  width 的 该 rectangle 在 米.  
height |  数字 |  height 的 该 rectangle 在 米.  
  
## 示例

An example 的 脚本 code 是 available 在 该 [gdsopen](/hc/en-us/articles/360034927093-gdsopen) page.

**参见**

[gdsopen](/hc/en-us/articles/360034927093-gdsopen), [gdsclose](/hc/en-us/articles/360034927113-gdsclose), [gdsbegincell](/hc/en-us/articles/360034927133-gdsbegincell), [gdsendcell](/hc/en-us/articles/360034406894-gdsendcell), [gdsaddpoly](/hc/en-us/articles/360034927153-gdsaddpoly), [gdsaddref](/hc/en-us/articles/360034927173-gdsaddref), [gdsimport](/hc/en-us/articles/360034406974-gdsimport), [gdsaddpath](/hc/en-us/articles/360034406954-gdsaddpath), [gdsaddtext, ](/hc/en-us/articles/360034927193-gdsaddtext)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
