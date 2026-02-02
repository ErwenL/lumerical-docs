# protectproperty

Protects the ‘property’ of a given ‘element’. 

**Syntax** |  **Description**  
---|---  
protectproperty (element,property,protect);  |  Protects the ‘property’ of a given ‘element’. The argument 'protect' is a boolean value. If ‘protect’ is true the property is protected, if 'protect' is false the property is unprotected. The default value of ‘protect' is true.   
  
**Example**
    
    
    createcompound;
    addproperty("COMPOUND_1", "test_property");
    protectproperty("COMPOUND_1", "test_property", 1);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ hidecategory ](/hc/en-us/articles/360034407394-hidecategory) , [ annotateproperty ](/hc/en-us/articles/360034927533-annotateproperty) , [ ispropertyactive ](/hc/en-us/articles/360034927553-ispropertyactive) , [ hideproperty ](/hc/en-us/articles/360034407374-hideproperty)
