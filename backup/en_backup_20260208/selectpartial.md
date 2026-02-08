# selectpartial

Selects any objects with a given partial name. 

**Syntax** |  **Description**  
---|---  
selectpartial("partialname");  |  Selects any objects where "partialname" can be found in the object name provided the object is not in a group. To select objects located in groups see the command below.  This function does not return any data.   
selectpartial("partialgroupname::partialname");  |  Selects any objects where "partialgroupname" can be found in the group name and "partialname" can be found in the object name.   
  
**Example**

Create two objects and put them in a group. Make an additional copy of the triangle object within the group. 
    
    
    #create a substrate with a channel etched in the center. Put the objects in a group
    addrect;
    addtriangle;
    selectpartial("angle"); # select both the triANGLE and rectANGLE objects
    addtogroup("structure");# add selected to group
    #select the etch and copy to create a second channel
    selectpartial("structure::tri"); # select the TRIangle
    copy(1e-6);            # copy the TRIangle

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ groupscope ](/hc/en-us/articles/360034928553-groupscope)
