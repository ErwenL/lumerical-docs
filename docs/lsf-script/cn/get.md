<!-- Translation completed: 2026-02-04 -->
<!-- Original command: get -->

# get

    PropStruct = get({"x","y","z","radius"});  
    ?PropStruct;  
    Struct with fields:  
    radius  
    x  
    y  
    z  
    ?PropStruct.radius;  
    result:   
    1.8e-07   
    AllProps = get; # saved as a 字符串  
    AllProps = splitstring(AllProps, endl); # convert to a cell 数组  
    PropStruct = get(AllProps);  
    PropStruct = get(splitstring(get,endl));

**语法** | **描述**
---|---
?get; | 返回 a list of the properties of the selected object(s).
out = get("property"); | Gets the requested property 值 from the currently selected object. It cannot be used to get the property 值 of a selected object in a group. If multiple objects are selected get("property") is the same as get("property",i), where i is the 数字 of the first selected objects with the requested property. Out can be a 矩阵 or a 字符串, depending on the property requested. "Property" accepts struct 格式 which allows user to obtain multiple attributes.
get("property",i); | Gets the property of the ith selected object. Use this to act on a series of objects. It cannot be used to get the 值 of a selected object in a group. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree.
get(cell_array_of_properties) | Get the specific properties of the selected object as a struct (key-值 pairs). The 输入 is a cell 数组.

**示例**

See the list of the properties of a rectangle.
    addrect;
    ?get;
    alpha
    color opacity
    detail
    enabled
      ⋮
    z
    z max
    z min
    z span
Get the x span of an object named substrate.
    select("substrate");
    x_span = get("x span"); 
Add 2 microns to the radius of all selected objects that have a radius property.
    select("circle");
    for (i=1:getnumber) {
     rad=get("radius",i);
     set("radius",rad+2e-6,i);
    }
Set and get the vertices of a pentagon with a circumradius of 1um.
    addpoly;
    theta=linspace(0,2*pi*4/5,5);
    x=cos(theta)*1e-6;
    y=sin(theta)*1e-6;
    V=[x,y];
    set("vertices",V);
    ?get("vertices");
    result: 
    1e-06 0   
    3.09017e-07 9.51057e-07   
    -8.09017e-07 5.87785e-07   
    -8.09017e-07 -5.87785e-07   
    3.09017e-07 -9.51057e-07 
Get the properties of a circle as a struct
    addcircle;  

See the list of the properties of a rectangle.
    addrect;
    ?get;
    alpha
    color opacity
    detail
    enabled
      ⋮
    z
    z max
    z min
    z span
Get the x span of an object named substrate.
    select("substrate");
    x_span = get("x span"); 
Add 2 microns to the radius of all selected objects that have a radius property.
    select("circle");
    for (i=1:getnumber) {
     rad=get("radius",i);
     set("radius",rad+2e-6,i);
    }
Set and get the vertices of a pentagon with a circumradius of 1um.
    addpoly;
    theta=linspace(0,2*pi*4/5,5);
    x=cos(theta)*1e-6;
    y=sin(theta)*1e-6;
    V=[x,y];
    set("vertices",V);
    ?get("vertices");
    result: 
    1e-06 0   
    3.09017e-07 9.51057e-07   
    -8.09017e-07 5.87785e-07   
    -8.09017e-07 -5.87785e-07   
    3.09017e-07 -9.51057e-07 
Get the properties of a circle as a struct
    addcircle;  

**另请参阅**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ getnumber ](/hc/en-us/articles/360034928913-getnumber) , [ getnamed ](/hc/en-us/articles/360034408574-getnamed) , [ getnamednumber ](/hc/en-us/articles/360034408594-getnamednumber) , [ set ](/hc/en-us/articles/360034928773-set) , [ haveproperty ](/hc/en-us/articles/360034928973-haveproperty) , [ runsetup ](/hc/en-us/articles/360034928893-runsetup)
