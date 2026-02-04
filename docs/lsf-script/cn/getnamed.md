<!--
Translation from English documentation
Original command: getnamed
Translation date: 2026-02-04 22:50:00
-->

# getnamed

获取 一个 属性 从 对象 使用 一个 given name.

If multiple 对象 是 选中的, 和 该 值 是 different, 该 smallest 值 是 returned. To 为 certain 的 该 results, 为 sure 该 only one 对象 是 选中的, 或 use 该 form 的 getnamed 该 allows 一个 specific 对象 到 为 选中的.

**语法** |  **描述**  
---|---  
?getnamed("name"); |  返回 一个 list 的 该 属性 的 该 对象 called name.  
out = getnamed("name", "属性"); |  返回 该 值 的 该 specific 属性 的 该 named 对象.  
out = getnamed("name", "properties_array"); |  返回 该 值 的 该 属性 的 该 named 对象 as 结构体. The "properties_array" 是 一个 单元格 数组 的 strings.  
out=getnamed("name", "属性", i); |  获取 该 属性 的 该 ith named 对象. Use 此 到 act 在 一个 series 的 对象. The 对象 是 ordered 通过 their location 在 该 对象 tree. The uppermost 选中的 对象 是 given 该 index 1, 和 该 index numbers increase as you go down 该 tree.  
out = getnamed("groupname::name", "属性"); |  The same as 获取, but acts 在 对象 named "name" located 在 该 group "groupname", instead 的 选中的 对象.  
out = getnamed("groupname::name", "属性", i); |  获取 该 属性 的 该 ith 对象 named "name" located 在 该 group "groupname". Use 此 到 act 在 一个 series 的 对象. The 对象 是 ordered 通过 their location 在 该 对象 tree. The uppermost 选中的 对象 是 given 该 index 1, 和 该 index numbers increase as you go down 该 tree.  
  
**示例**

This example uses 该 获取 命令 到 获取 该 x跨度 的 一个 对象 named substrate.
    
    
    addrect;
    设置("name","substrate");
    setnamed("substrate","x跨度",2e-6); 
    x_span = getnamed("substrate","x跨度"); 
    ?x_span;
    result: 
    2e-006  

添加 2 微米 到 该 radius 的 all 选中的 对象 named circle.
    
    
    用于 (i=1:getnamednumber("circle")) {
     rad=getnamed("circle","radius",i);
     setnamed("circle","radius",rad+2e-6,i);
    }

获取 该 x, y, z positions 的 该 named 对象 as 结构体.
    
    
    addrect({"name":"substrate"});  
    A = getnamed("substrate",{"x","y","z"});  
    ?A.x;  
    result:   
    0 

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ 获取 ](/hc/en-us/articles/360034928873-获取) , [ getnumber ](/hc/en-us/articles/360034928913-getnumber) , [ getnamednumber ](/hc/en-us/articles/360034408594-getnamednumber) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ setnamed ](/hc/en-us/articles/360034928793-setnamed)
