<!--
Translation from English documentation
Original command: addtogroup
Translation date: 2026-02-04 22:49:36
-->

# addtogroup

添加 选中的 对象 到 一个 group. 

**语法** |  **描述**  
---|---  
addtogroup("group_name");  |  添加 选中的 对象(s) 到 一个 group. If 一个 group 使用 name "group_name" already exists, 那么 该 对象 是 added 到 该 existing group. Otherwise, 一个 group named "group_name" 是 created.  "group_name" 可以 为 一个 absolute path, such as "::model::G1"   
  
**示例**

添加 一个 substrate 在 到 一个 group "G2", 和 subsequently move 该 substrate back 到 "G1" 
    
    
    addrect;
    设置("name","substrate");
    select("substrate");
    addtogroup("::model::G1::G2"); #此 对象 是 added 到 该 group "G2"
    # moves 该 rectangle back 到 G1
    addtogroup("::model::G1");

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ addgroup ](/hc/en-us/articles/360034924073-addgroup) , [ addstructuregroup ](/hc/en-us/articles/360034924093-addstructuregroup) , [ addanalysisgroup ](/hc/en-us/articles/360034404074-addanalysisgroup) , [ adduserprop ](/hc/en-us/articles/360034928733-adduserprop) , [ runsetup ](/hc/en-us/articles/360034928893-runsetup)
