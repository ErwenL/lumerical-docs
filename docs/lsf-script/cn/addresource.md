<!--
Translation from English documentation
Original command: addresource
Translation date: 2026-02-04 22:49:30
-->

# addresource

添加 一个 resource 到 该 list 的 available resources 在 resource manager.

**语法** |  **描述**  
---|---  
addresource("求解器"); |  添加 一个 resource 到 该 list 的 available resources 在 resource manager. The "求解器" 参数 是 used 到 select 该 求解器 到 添加 该 resource 到. The "求解器" 参数 是 not supported 通过 INTERCONNECT. It also 返回 该 resource 数字 as 一个 integer.  
  
**示例**

The following line 将 添加 一个 resource 到 该 DGTD 求解器 在 Finite Element IDE.
    
    
    addresource("DGTD");  

**参见**

[deleteresource](/hc/en-us/articles/360034410794-deleteresource), [setresource](/hc/en-us/articles/360034410754-setresource), [getresource](/hc/en-us/articles/360034931353-getresource)
