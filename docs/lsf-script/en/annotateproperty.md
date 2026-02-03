# annotateproperty

Enables ‘property’ annotation on a given ‘element’. 

**Syntax** |  **Description**  
---|---  
out=annotateproperty (element,property,annotate);  |  Enables ‘property’ annotation on a given ‘element’. If ‘annotate’ is true the property is annotated, if ‘annotate’ is false the annotation is disable. The default value of ‘annotate’ is true.   
  
**Example**
    
    
    addelement("CW Laser");
    annotateproperty("CWL_1", "linewidth", true);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ hideproperty ](/hc/en-us/articles/360034407374-hideproperty) , [ hidecategory ](/hc/en-us/articles/360034407394-hidecategory) , [ ispropertyactive ](/hc/en-us/articles/360034927553-ispropertyactive)
