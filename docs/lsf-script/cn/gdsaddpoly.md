<!--
Translation from English documentation
Original command: gdsaddpoly
Translation date: 2026-02-04 22:49:49
-->

# gdsaddpoly

This function adds a polygon element to a GDSII file stream. Polygons are also known as boundary elements in GDS terminology. This command can be called only if a cell has been created.The maximum number of vertices that can be added in a single polygon is 8190 due to [limitations](https://www.artwork.com/gdsii/max_vertex.htm) in the maximum number of vertices in a gdsii boundary. You can only use this command if a gds cell has already been created, for example, using [gdsbegincell](https://optics.ansys.com/hc/en-us/articles/360034927133-gdsbegincell-Script-command).

For complex geometries requiring more vertices, use [gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command).

**语法** |  **描述**  
---|---  
gdsaddpoly(f, layer, [vertices]) |  添加 一个 polygon 元素 在 一个 layer 使用 vertices.  
  
**Parameter** |  **Type** |  **描述**  
---|---|---  
f |  string |  A file handle that was previously opened with [gdsopen](https://optics.ansys.com/hc/en-us/articles/360034927093-gdsopen-Script-command).  
layer |  字符串 或 数字 |  String: 一个 字符串 的 该 form "layer:datatype" (用于 example "6:2") 可以 为 used 到 define 该 layer 数字 和 datatype 用于 此 结构 从 该 GDSII 文件 到 import. Layer 和 datatype 是 integers. Number: defines 该 layer 数字 和 设置 该 datatype 到 为 zero.  
vertices |  矩阵 |  Vertices 的 该 polygon, 在 一个 Nx2 矩阵 其中 该 first column represents x 和 该 second column represents y, e.g., [x1,y1; x2,y2;...xn,yn]. The 值 是 在 米. The first 和 last 值 应该 not 为 该 same, 该 polygon 将 为 automatically closed.  
  
## 示例

An example 的 脚本 code 是 available 在 该 [gdsopen](/hc/en-us/articles/360034927093-gdsopen) page.

**参见**

[gdsopen](/hc/en-us/articles/360034927093-gdsopen), [gdsclose](/hc/en-us/articles/360034927113-gdsclose), [gdsbegincell](/hc/en-us/articles/360034927133-gdsbegincell), [gdsendcell](/hc/en-us/articles/360034406894-gdsendcell), [gdsaddcircle](/hc/en-us/articles/360034406914-gdsaddcircle), [gdsaddref](/hc/en-us/articles/360034927173-gdsaddref), [gdsimport](/hc/en-us/articles/360034406974-gdsimport), [gdsaddpath](/hc/en-us/articles/360034406954-gdsaddpath), [gdsaddtext,](/hc/en-us/articles/360034927193-gdsaddtext) [gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
