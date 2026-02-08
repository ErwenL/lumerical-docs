# hidecategory

Hides all properties of a given ‘category' of a given ‘element’. 

**Syntax** |  **Description**  
---|---  
hidecategory(element,category,hide);  |  Hides all properties of a given ‘category' of a given ‘element’. The argument 'hide' is a boolean value. If ‘hide’ is true the category is invisible, if 'hide' is false the category is visible. The default value of ‘hide’ is true.   
  
**Example**
    
    
    addelement("CW Laser");
    hidecategory("CWL_1","Polarization", true);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ hideproperty ](/hc/en-us/articles/360034407374-hideproperty) , [ protectproperty ](/hc/en-us/articles/360034927513-protectproperty) , [ annotateproperty ](/hc/en-us/articles/360034927533-annotateproperty) , [ ispropertyactive ](/hc/en-us/articles/360034927553-ispropertyactive)
