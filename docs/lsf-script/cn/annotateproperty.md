<!--
Translation from English documentation
Original command: annotateproperty
Translation date: 2026-02-04 22:49:36
-->

# annotateproperty

Enables ‘属性’ annotation 在 一个 given ‘元素’. 

**语法** |  **描述**  
---|---  
out=annotateproperty (元素,属性,annotate);  |  Enables ‘属性’ annotation 在 一个 given ‘元素’. If ‘annotate’ 是 true 该 属性 是 annotated, 如果 ‘annotate’ 是 false 该 annotation 是 disable. The default 值 的 ‘annotate’ 是 true.   
  
**示例**
    
    
    addelement("CW Laser");
    annotateproperty("CWL_1", "linewidth", true);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ hideproperty ](/hc/en-us/articles/360034407374-hideproperty) , [ hidecategory ](/hc/en-us/articles/360034407394-hidecategory) , [ ispropertyactive ](/hc/en-us/articles/360034927553-ispropertyactive)
