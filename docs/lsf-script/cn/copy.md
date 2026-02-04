<!--
Translation from English documentation
Original command: copy
Translation date: 2026-02-04 22:49:48
-->

# copy

创建 一个 copy 的 该 选中的 对象. The copied 对象 将 typically 为 identical (same name, position, etc). For some 对象 该 必须 have 一个 unique name, '_1' 将 为 appended 到 该 name.

**语法** |  **描述**  
---|---  
copy; |  Copy 该 选中的 对象.  
copy(dx); |  Same as copy; but 使用 一个 specified move 的 dx.  
copy(dx,dy); |  Same as copy; but 使用 一个 specified move 的 dx, dy.  
copy(dx,dy,dz); |  Same as copy; but 使用 一个 specified move 的 dx, dy, dz.  
  
**示例**

创建 一个 copy 的 该 对象 named substrate. The copy 将 为 located 1um 在 该 y direction 从 该 original 对象.
    
    
    addrect;
    设置("name","substrate");
    select("substrate");
    copy(0, 1e-6,0); 

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ move ](/hc/en-us/articles/360034928713-move) , [ select ](/hc/en-us/articles/360034928593-select) , [ cp (copy files) ](/hc/en-us/articles/360034931573-cp) , [ copytoclipboard ](/hc/en-us/articles/360034931993-copytoclipboard)
