# addtogroup

Adds selected objects to a group. 

**Syntax** |  **Description**  
---|---  
addtogroup("group_name");  |  Adds selected object(s) to a group. If a group with name "group_name" already exists, then the objects are added to the existing group. Otherwise, a group named "group_name" is created.  "group_name" can be an absolute path, such as "::model::G1"   
  
**Example**

Add a substrate in to a group "G2", and subsequently move the substrate back to "G1" 
    
    
    addrect;
    set("name","substrate");
    select("substrate");
    addtogroup("::model::G1::G2"); #this object is added to the group "G2"
    # moves the rectangle back to G1
    addtogroup("::model::G1");

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ addgroup ](/hc/en-us/articles/360034924073-addgroup) , [ addstructuregroup ](/hc/en-us/articles/360034924093-addstructuregroup) , [ addanalysisgroup ](/hc/en-us/articles/360034404074-addanalysisgroup) , [ adduserprop ](/hc/en-us/articles/360034928733-adduserprop) , [ runsetup ](/hc/en-us/articles/360034928893-runsetup)
