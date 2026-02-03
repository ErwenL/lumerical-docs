# set

Sets a property of currently selected objects.

Note that most objects can not be modified when the solver is in Analysis mode. In such situations, this command will return an error.

**Syntax** |  **Description**  
---|---  
?set; |  Returns a list of the properties of the selected object(s) that can be changed with the set command.  
set("property",value); |  This will set the properties of a currently selected object, including pull-downs and check boxes. It cannot be used to set the value of a selected object in a group. Value can be a number or string. This function does not return any data.  
set(struct); |  A struct can be accepted in place of "property"-value pair of arguments.  
set("property",value,i); |  This form can be used to set the property of the ith selected object when multiple objects are selected. It cannot be used to set the value of a selected object in a group. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree.  
  
**Examples**

Set the radius of any selected objects (sphere, ring, circle) with a property called radius to 1e-6.
    
    
    set("radius",1e-6);

Set the name property of all selected objects to reflection.
    
    
    set("name","reflection");

Set a checkbox to 0 to uncheck. Set to 1 to check.
    
    
    set("check box label name",0);  # unselect checkbox 

To disable an object.
    
    
    set("enabled",0);

Set the x min boundary condition to be the first choice in the pull-down menu.
    
    
    set("x min bc",1);

Set the x min boundary condition to the string "PML".
    
    
    set("x min bc","PML");

Set the PML profile of the FDTD region
    
    
    set("pml profile", 2);

Set the PML profiles for individual boundary
    
    
    set("same settings on all boundaries",0);
    set("pml profile", [1,1,2,1,1,1]); # setting y min bc to "stabilized", and all other bc to "standard"

Add 2 microns to the radius of all objects named "circle".
    
    
    select("circle");
    for (i=1:getnumber) {
     rad=get("radius",i);
     set("radius",rad+2e-6,i);
    } 

Set and get the vertices of a polygon object. We create an octagon with a radius of 1um.
    
    
    addpoly;
    theta=linspace(0,2*pi,9);
    theta=theta(1:8);
    x=cos(theta)*1e-6;
    y=sin(theta)*1e-6;
    V=[x,y];
    set("vertices",V);
    ?get("vertices");
    result: 
    1e-006 0 
    7.07107e-007 7.07107e-007 
    6.12323e-023 1e-006 
    -7.07107e-007 7.07107e-007 
    -1e-006 1.22465e-022 
    -7.07107e-007 -7.07107e-007 
    -1.83697e-022 -1e-006 
    7.07107e-007 -7.07107e-007 

See a list of the properties of a rectangle.
    
    
    addrect;
    ?get;
    alpha
    color opacity
    detail
    enabled
    first axis
    grid attribute name
    index
    index units
    material
    mesh order
    name
    override color opacity from material database
    override mesh order from material database
    render type
    rotation 1
    rotation 2
    rotation 3
    second axis
    set color opacity from material database
    set mesh order from material database
    third axis
    x
    x max
    x min
    x span
    y
    y max
    y min
    y span
    z
    z max
    z min
    z span

Use struct as an input to set the coordinates and dimensions of a currently selected object called "rectangle":
    
    
    coordinates = {"x" : -3e-7,  
                   "x span" : 1e-6,  
                   "y" : 5e-6,  
                   "y span" : 1e-5,  
                   "z" : 1e-7,  
                   "z span" : 2.2e-7};  
      
    set(coordinates);

**Notes**

In INTERCONNECT, the element property value must be entered in the  set  command using the fixed standard unit. In some cases, the standard unit is different from the default unit in the Property View. Following is an example of setting the ONA center frequency. The center frequency default unit is THz, while the standard unit is Hz, and when using the  set  command, the value needs to be in Hz:
    
    
    select("ONA");
    set("center frequency", 193.1e12); 

To find the standard unit for an element property, open the element's help page on the Knowledge Page, and look at the Default unit column. A note is included for cases where the default and standard units differ. For example, see the center frequency of the [ONA](/hc/en-us/articles/360036617973).

**See Also**

[get](/hc/en-us/articles/360034928873-get), [setnamed](/hc/en-us/articles/360034928793-setnamed), [setmaterial](/hc/en-us/articles/360034409654-setmaterial), [addmaterial](/hc/en-us/articles/360034930013-addmaterial), [haveproperty](/hc/en-us/articles/360034928973-haveproperty), [runsetup](/hc/en-us/articles/360034928893-runsetup), [runanalysis](/hc/en-us/articles/360034409874-runanalysis)
