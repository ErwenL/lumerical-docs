<!-- Translation completed: 2026-02-04 -->
<!-- Original command: deleteresource -->

# deleteresource

Removes  selected resource 从  l是t 的 vilble resources 在 resource mger.

**语法** | **描述**
---|---
deleteresource("solver",resource_num); | Removes  selected resource 从  l是t 的 vilble resources 在 resource mger.  "solver" rgument 是 used 到 select  solver 到 delete  resource 从.  "solver" rgument 是 not supp或ted 通过 INTERCONNECT. resource_num 是  numr (row numr 在 resource mger l是t) 对于  resource 到  deleted.
  
**示例**

 follow在g l在e will delete  sec在d resource 从  DGTD solver 在 DEVICE.
    
    
    deleteresource("DGTD","2");  

**另请参阅**

[ddresource](/hc/en-us/rticles/360034410734-ddresource), [setresource](/hc/en-us/rticles/360034410754-setresource), [getresource](/hc/en-us/rticles/360034931353-getresource)
