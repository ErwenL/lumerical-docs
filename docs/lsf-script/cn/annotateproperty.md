<!-- Translation completed: 2026-02-04 -->
<!-- Original command: annotateproperty -->

# annotateproperty

**语法** | **描述**
---|---
out=annotateproperty (element,property,annotate); | Enables ‘property’ annotation on a given ‘元素’. If ‘annotate’ is 真 the property is annotated, if ‘annotate’ is 假 the annotation is disable. The default 值 of ‘annotate’ is 真.

**示例**

    addelement("CW Laser");
    annotateproperty("CWL_1", "linewidth", 真);

    addelement("CW Laser");
    annotateproperty("CWL_1", "linewidth", 真);

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ hideproperty ](/hc/en-us/articles/360034407374-hideproperty) , [ hidecategory ](/hc/en-us/articles/360034407394-hidecategory) , [ ispropertyactive ](/hc/en-us/articles/360034927553-ispropertyactive)
