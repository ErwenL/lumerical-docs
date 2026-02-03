# groupscope

Changes the group scope. Script commands that add or modify simulation object use the groupscope property to know where to act within the object tree. For example, if you want to delete everything within a particular group, set the groupscope to that group (i.e. ::model::my_group). If you want to delete all objects in the simulation, set the group scope the root level (i.e. ::model). 

**Syntax** |  **Description**  
---|---  
?groupscope;  |  returns the current group scope   
groupscope("group_name");  |  changes the group scope   
  
**Example**

Create an analysis group with a Field and Index monitor. 
    
    
    #create a new FDTD simulation
    newproject;
    addanalysisgroup;
    set("name","Field_Index");
    #change the group scope and add monitors to the group
    groupscope("Field_Index"); # same as groupscope("::model::Field_Index");
    addpower; set("name","field");
    addindex; set("name","index");
    selectall;
    set("monitor type","3D");
    set("spatial interpolation","nearest mesh cell");
    set("x",0); set("y",0); set("z",0);
    set("x span",1e-6); set("y span",1e-6); set("z span",1e-6);
    # change the group scope back the the model
    groupscope("::model");
    # make a copy of the box
    select("Field_Index");
    copy(2e-6,0,0);

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ delete ](/hc/en-us/articles/360034928573-delete) , [ selectall ](/hc/en-us/articles/360034408354-selectall) , [ select ](/hc/en-us/articles/360034928593-select)
