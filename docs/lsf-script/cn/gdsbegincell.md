<!--
Translation from English documentation
Original command: gdsbegincell
Translation date: 2026-02-04 22:49:49
-->

# gdsbegincell

This 函数 创建 一个 单元格 在 一个 GDSII 文件. All GDS elements (polygons, boxes, references, 数组 references, etc) 必须 为 placed inside 一个 单元格, so 此 函数 必须 为 called before adding any elements. When finished adding elements, gdsendcell 可以 为 called 到 finish 该 单元格. Cells cannot 为 nested, so after calling gdsbegincell, 一个 新的 单元格 cannot 为 called again until 该 first called 单元格 has been closed. Although 该 GDSII 文件 是 一个 flat list 的 cells, cells 可以 reference other cells, thus creating 一个 nested hierarchy. See [gdsaddref](/hc/en-us/articles/360034927173-gdsaddref) 用于 more details. A GDS "单元格" exists as 一个 "结构 group" 当 imported 到 FDTD, see [gdsimport](/hc/en-us/articles/360034406974-gdsimport) 用于 more details.

**语法** |  **描述**  
---|---  
gdsbegincell(f, "cellname") |  创建 一个 新的 单元格 在 一个 GDSII 文件.  
**Parameter** |  **Type** |  **描述**  
---|---|---  
f |  字符串 |  一个 文件 handle 该 was previously opened 使用 gdsopen.  
cellname |  字符串 |  name 的 该 单元格.  
  
## 示例

An example 的 脚本 code 是 available 在 该 [gdsopen](/hc/en-us/articles/360034927093-gdsopen) page.

注意: Just 到 clarify, 一个 GDS 单元格 是 different 从 一个 [Cell Array](/hc/en-us/articles/360034929913-单元格) 在 FDTD.

**参见**

[gdsopen](/hc/en-us/articles/360034927093-gdsopen), [gdsclose](/hc/en-us/articles/360034927113-gdsclose), [gdsendcell](/hc/en-us/articles/360034406894-gdsendcell), [gdsaddpoly](/hc/en-us/articles/360034927153-gdsaddpoly), [gdsaddcircle](/hc/en-us/articles/360034406914-gdsaddcircle), [gdsaddrect](/hc/en-us/articles/360034406934-gdsaddrect), [gdsimport](/hc/en-us/articles/360034406974-gdsimport), [gdsaddref](/hc/en-us/articles/360034927173-gdsaddref), [gdsaddpath](/hc/en-us/articles/360034406954-gdsaddpath), [gdsaddtext, ](/hc/en-us/articles/360034927193-gdsaddtext)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
