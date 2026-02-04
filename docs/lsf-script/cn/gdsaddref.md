<!--
Translation from English documentation
Original command: gdsaddref
Translation date: 2026-02-04 22:49:49
-->

# gdsaddref

This function adds a reference to another cell to the current cell in the GDSII file stream. This function replicates the referenced cell (has to be previously opened and finished) to the current cell and creates a nested hierarchy. The layer numbers of the replicated structures follow the referenced cell. References can only be added in a GDSII cell, so this command can be called only if a current cell has been created, for example, using [gdsbegincell](https://optics.ansys.com/hc/en-us/articles/360034927133-gdsbegincell-Script-command). In addition, the cell to be replicated has to exist before it is referenced.

**语法** |  **描述**  
---|---  
gdsaddref(f, "cellname", dx, dy, angle_in_deg) |  添加 一个 reference 到 another 单元格 ("cellname") 到 该 current 单元格, 使用 一个 specified move 的 dx 和 dy.  
  
**Parameter** |  **Type** |  **描述**  
---|---|---  
f |  字符串 |  A 文件 handle 该 was previously opened 使用 gdsopen.  
cellname |  字符串 |  Name 的 该 referenced 单元格.  
dx |  数字 |  X-movement 的 该 replicated 单元格 在 该 current 单元格.  
dy |  数字 |  Y-movement 的 该 replicated 单元格 在 该 current 单元格.  
angle_in_deg |  数字 |  Optional, angle 的 rotation 在 degrees 的 该 replicated 单元格. For 此 operation, 该 **replicated** 单元格 是 rotated 使用 respect 到 **its** **own** origin, 和 该 单元格 是 placed at 该 coordinates specified 通过 参数 dx 和 dy.  
  
## 示例

An example 的 脚本 code 是 available 在 该 [gdsopen](/hc/en-us/articles/360034927093-gdsopen) page.

**参见**

[gdsopen](/hc/en-us/articles/360034927093-gdsopen), [gdsclose](/hc/en-us/articles/360034927113-gdsclose), [gdsbegincell](/hc/en-us/articles/360034927133-gdsbegincell), [gdsendcell](/hc/en-us/articles/360034406894-gdsendcell), [gdsaddpoly](/hc/en-us/articles/360034927153-gdsaddpoly), [gdsaddcircle](/hc/en-us/articles/360034406914-gdsaddcircle), [gdsaddrect](/hc/en-us/articles/360034406934-gdsaddrect), [gdsimport](/hc/en-us/articles/360034406974-gdsimport), [gdsaddpath](/hc/en-us/articles/360034406954-gdsaddpath), [gdsaddtext, ](/hc/en-us/articles/360034927193-gdsaddtext)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
