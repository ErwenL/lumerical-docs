# deleteresource

Removes the selected resource from the list of available resources in resource manager.

**Syntax** |  **Description**  
---|---  
deleteresource("solver",resource_num); |  Removes the selected resource from the list of available resources in resource manager. The "solver" argument is used to select the solver to delete the resource from. The "solver" argument is not supported by INTERCONNECT. resource_num is the number (row number in resource manager list) for the resource to be deleted.  
  
**Example**

The following line will delete the second resource from the DGTD solver in DEVICE.
    
    
    deleteresource("DGTD","2");  

**See Also**

[addresource](/hc/en-us/articles/360034410734-addresource), [setresource](/hc/en-us/articles/360034410754-setresource), [getresource](/hc/en-us/articles/360034931353-getresource)
