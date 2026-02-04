<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getnamednumber -->

# getnamednumber

**语法** | **描述**
---|---
out = getnamednumber( "name"); | The same as getnumber, but acts on objects with a specific name, instead of selected objects.
out = getnamednumber( "groupname::name"); | The same as getnumber, but acts on all objects named "name" in the group "groupname", instead of selected objects.

**示例**

Add 2 microns to the radius of all selected objects named circle. 
    for (i=1:getnamednumber("circle")) {
     rad=getnamed("circle","radius",i);
     setnamed("circle","radius",rad+2e-6,i);
    }

Add 2 microns to the radius of all selected objects named circle. 
    for (i=1:getnamednumber("circle")) {
     rad=getnamed("circle","radius",i);
     setnamed("circle","radius",rad+2e-6,i);
    }

**另请参阅**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ get ](/hc/en-us/articles/360034928873-get) , [ getnamed ](/hc/en-us/articles/360034408574-getnamed) , [ getnumber ](/hc/en-us/articles/360034928913-getnumber) , [ set ](/hc/en-us/articles/360034928773-set) , [ setnamed ](/hc/en-us/articles/360034928793-setnamed)
