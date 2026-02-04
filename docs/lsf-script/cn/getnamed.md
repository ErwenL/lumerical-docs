<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getnamed -->

# getnamed

**语法** | **描述**
---|---
?getnamed("name"); | 返回 a list of the properties of the objects called name.
out = getnamed("name", "property"); | 返回 the 值 of the specific property of the named object.
out = getnamed("name", "properties_array"); | 返回 the 值 of the properties of the named object as struct. The "properties_array" is a cell 数组 of strings.
out=getnamed("name", "property", i); | Gets the property of the ith named object. Use this to act on a series of objects. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree.
out = getnamed("groupname::name", "property"); | The same as get, but acts on objects named "name" located in the group "groupname", instead of selected objects.
out = getnamed("groupname::name", "property", i); | Gets the property of the ith object named "name" located in the group "groupname". Use this to act on a series of objects. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree.

**示例**

This 示例 uses the get 命令 to get the x span of an object named substrate.
    addrect;
    set("name","substrate");
    setnamed("substrate","x span",2e-6); 
    x_span = getnamed("substrate","x span"); 
    ?x_span;
    result: 
    2e-006  
Add 2 microns to the radius of all selected objects named circle.
    for (i=1:getnamednumber("circle")) {
     rad=getnamed("circle","radius",i);
     setnamed("circle","radius",rad+2e-6,i);
    }
Get the x, y, z positions of the named object as struct.
    addrect({"name":"substrate"});  
    A = getnamed("substrate",{"x","y","z"});  
    ?A.x;  
    result:   
    0 

This 示例 uses the get 命令 to get the x span of an object named substrate.
    addrect;
    set("name","substrate");
    setnamed("substrate","x span",2e-6); 
    x_span = getnamed("substrate","x span"); 
    ?x_span;
    result: 
    2e-006  
Add 2 microns to the radius of all selected objects named circle.
    for (i=1:getnamednumber("circle")) {
     rad=getnamed("circle","radius",i);
     setnamed("circle","radius",rad+2e-6,i);
    }
Get the x, y, z positions of the named object as struct.
    addrect({"name":"substrate"});  
    A = getnamed("substrate",{"x","y","z"});  
    ?A.x;  
    result:   
    0 

**另请参阅**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ get ](/hc/en-us/articles/360034928873-get) , [ getnumber ](/hc/en-us/articles/360034928913-getnumber) , [ getnamednumber ](/hc/en-us/articles/360034408594-getnamednumber) , [ set ](/hc/en-us/articles/360034928773-set) , [ setnamed ](/hc/en-us/articles/360034928793-setnamed)
