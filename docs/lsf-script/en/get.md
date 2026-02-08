# get

Gets a property from selected objects. The property names for the get command are the
same as the property names in the Edit dialogue box. For example, if you see a property
called "mesh accuracy", then you can use the command get("mesh accuracy"); to get that
property. It is possible to get numeric, string, drop down and checkbox properties.

| **Syntax**                    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ?get;                         | Returns a list of the properties of the selected object(s).                                                                                                                                                                                                                                                                                                                                                                                                                    |
| out = get("property");        | Gets the requested property value from the currently selected object. It cannot be used to get the property value of a selected object in a group. If multiple objects are selected get("property") is the same as get("property",i), where i is the number of the first selected objects with the requested property. Out can be a matrix or a string, depending on the property requested. "Property" accepts struct format which allows user to obtain multiple attributes. |
| get("property",i);            | Gets the property of the ith selected object. Use this to act on a series of objects. It cannot be used to get the value of a selected object in a group. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree.                                                                                                                                            |
| get(cell_array_of_properties) | Get the specific properties of the selected object as a struct (key-value pairs). The input is a cell array.                                                                                                                                                                                                                                                                                                                                                                   |

**Examples**

See the list of the properties of a rectangle.

```
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
```

Get the x span of an object named substrate.

```
select("substrate");
x_span = get("x span"); 
```

Add 2 microns to the radius of all selected objects that have a radius property.

```
select("circle");
for (i=1:getnumber) {
 rad=get("radius",i);
 set("radius",rad+2e-6,i);
}
```

Set and get the vertices of a pentagon with a circumradius of 1um.

```
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
```

Get the properties of a circle as a struct

```
addcircle;  
  
# Get specific properties of the selected object as a struct  
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
  
# Get all the properties of the selected object as a struct  
AllProps = get; # saved as a string  
AllProps = splitstring(AllProps, endl); # convert to a cell array  
PropStruct = get(AllProps);  
  
# Here's a single-line equivalent of the above three-line code   
PropStruct = get(splitstring(get,endl));
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ getnumber ](./getnumber.md) , [ getnamed ](./getnamed.md) ,
[ getnamednumber ](./getnamednumber.md) , [ set ](./set.md) ,
[ haveproperty ](./haveproperty.md) , [ runsetup ](./runsetup.md)
