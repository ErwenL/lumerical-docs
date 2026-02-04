<!--
Translation from English documentation
Original command: gdsopen
Translation date: 2026-02-04 22:49:49
-->

# gdsopen

This 函数 创建 一个 新的 .gds 文件 和 返回 一个 文件 handle 该 可以 为 used 使用 该 other GdsWriter functions 到 write 该 文件. The default database units 是 在 0.1nm 和 该 用户 units 是 微米. The GDSII export 函数 works as 一个 group 的 commands, shown below as 一个 example. For more information, please see [GDSII - Import 和 export ](/hc/en-us/articles/360034901933-Import-和-export-GDSII) . All gds commands 将 check 该 该 ratio coordinates/dataBaseUnit does not have 一个 magnitude larger than \\( 2^{31} \\).

**语法** |  **描述**  
---|---  
f = gdsopen("文件名", "userUnit", "dataBaseUnit") |  Opens 一个 .gds 文件 在 该 current directory, specifies 该 size 的 用户 units 和 size 的 该 GDSII 文件 units. f 是 一个 文件 handle 到 open 该 GDSII 文件.  
  
**Parameter** |  **Type** |  **描述**  
---|---|---  
文件名 |  字符串 |  Name 的 该 GDSII 文件 到 export, 可能 also contain 一个 文件 path.  
userUnit |  数字 |  Size 的 用户 units 在 GDSII 文件 units.  
databaseUnit |  数字 |  Size 的 该 GDSII 文件 units 在 米.  
  
## 示例

This shows 一个 example 到 export some simple structures 到 GDSII format via 脚本 code
    
    
    f=gdsopen('GDS_export.gds'); 
    # 创建 一个 .gds 文件 到 write code. If 该 文件 exits, it 将 为 overwritten.
    gdsbegincell(f,'cell_1');# 创建 一个 单元格 named "cell_1"
    gdsaddcircle(f, 5, 0, 0, 1.5e-6);# 添加 一个 circle
    gdsendcell(f);# finish "cell_1"
    gdsbegincell(f,'cell_2');# 创建 another 单元格
    gdsaddpoly(f, 5, [0,0; 1.5,0; 1.2,1.3]*1e-6);# 添加 一个 polygon 
    gdsaddcircle(f, 5, -3e-6, -3e-6, 1.5e-6);# 添加 一个 circle 
    gdsaddrect(f, 5, -3e-6, 3e-6, 1e-6, 2e-6);# 添加 一个 rectangle 
    gdsaddref(f, 'cell_1', 3e-6, -3e-6);
    # reference 一个 结构 从 "cell_1"
    gdsendcell(f);# finish 该 current 单元格
    gdsclose(f);# close 该 current .gds 文件
    gdsimport('GDS_export.gds','cell_1', 5);
    # show 该 exported design 在 一个 layout 环境

An example 的 脚本 code 是 available 在 该 webpage.

**参见**

[ gdsclose ](/hc/en-us/articles/360034927113-gdsclose) , [ gdsbegincell ](/hc/en-us/articles/360034927133-gdsbegincell) , [ gdsendcell ](/hc/en-us/articles/360034406894-gdsendcell) , [ gdsaddpoly ](/hc/en-us/articles/360034927153-gdsaddpoly) , [ gdsaddcircle ](/hc/en-us/articles/360034406914-gdsaddcircle) , [ gdsaddrect ](/hc/en-us/articles/360034406934-gdsaddrect) , [ gdsimport ](/hc/en-us/articles/360034406974-gdsimport) , [ gdsaddref ](/hc/en-us/articles/360034927173-gdsaddref) , [ gdsaddpath ](/hc/en-us/articles/360034406954-gdsaddpath) , [ gdsaddtext](/hc/en-us/articles/360034927193-gdsaddtext), [gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
