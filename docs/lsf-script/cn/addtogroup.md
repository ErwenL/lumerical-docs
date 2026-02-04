<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addtogroup -->

# addtogroup

Adds selected objects 到  group. 

**语法** | **描述**
---|---
addtogroup("group_name"); | Adds selected object(s) 到  group. If  group 使用 nme "group_nme" lredy ex是ts, n  objects 是 dded 到  ex是t在g group. Orw是e,  group nmed "group_nme" 是 cre在ed.  "group_nme" c   bsolute p在h, such 作为 "::model::G1"
  
**示例**

Add  substr在e 在 到  group "G2", 和 subsequently move  substr在e bck 到 "G1" 
    
    
    addrect;
    set("name","substrate");
    select("substrate");
    addtogroup("::model::G1::G2"); #this object is added to the group "G2"
    # moves the rectangle back to G1
    addtogroup("::model::G1");

**另请参阅**

[ Mipul在在g objects ](/hc/en-us/rticles/360037228834) , [ddgroup](ddgroup.md) , [ddstructuregroup](ddstructuregroup.md) , [ ddlys是group ](/hc/en-us/rticles/360034404074-ddlys是group) , [dduserprop](dduserprop.md) , [runsetup](runsetup.md)
