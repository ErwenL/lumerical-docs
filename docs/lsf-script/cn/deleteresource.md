<!--
Translation from English documentation
Original command: deleteresource
Translation date: 2026-02-04 22:49:48
-->

# deleteresource

Removes 该 选中的 resource 从 该 list 的 available resources 在 resource manager.

**语法** |  **描述**  
---|---  
deleteresource("求解器",resource_num); |  Removes 该 选中的 resource 从 该 list 的 available resources 在 resource manager. The "求解器" 参数 是 used 到 select 该 求解器 到 delete 该 resource 从. The "求解器" 参数 是 not supported 通过 INTERCONNECT. resource_num 是 该 数字 (row 数字 在 resource manager list) 用于 该 resource 到 为 deleted.  
  
**示例**

The following line 将 delete 该 second resource 从 该 DGTD 求解器 在 DEVICE.
    
    
    deleteresource("DGTD","2");  

**参见**

[addresource](/hc/en-us/articles/360034410734-addresource), [setresource](/hc/en-us/articles/360034410754-setresource), [getresource](/hc/en-us/articles/360034931353-getresource)
