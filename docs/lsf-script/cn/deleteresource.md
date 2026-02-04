<!--
Translation from English documentation
Original command: deleteresource
Translation date: 2026-02-03 23:02:30
-->

# deleteresource

从资源管理器中可用资源列表中删除所选资源。

**Syntax** |  **Description**  
---|---  
deleteresource("solver",resource_num); |  从资源管理器中可用资源列表中删除所选资源。"solver"参数用于选择要删除资源的求解器。INTERCONNECT不支持"solver"参数。resource_num是要删除的资源编号（资源管理器列表中的行号）。  
  
 **示例**

 以下代码将删除DEVICE中DGTD求解器的第二个资源。
    
    
    deleteresource("DGTD","2");  

 **参见**

- [addresource](./addresource.md)
- [setresource](./setresource.md)
- [getresource](./getresource.md)
