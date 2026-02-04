<!--
Translation from English documentation
Original command: selectpartial
Translation date: 2026-02-04 22:50:14
-->

# selectpartial

Selects any 对象 使用 一个 given partial name. 

**语法** |  **描述**  
---|---  
selectpartial("partialname");  |  Selects any 对象 其中 "partialname" 可以 为 found 在 该 对象 name provided 该 对象 是 not 在 一个 group. To select 对象 located 在 groups see 该 命令 below.  This 函数 does not 返回 any 数据.   
selectpartial("partialgroupname::partialname");  |  Selects any 对象 其中 "partialgroupname" 可以 为 found 在 该 group name 和 "partialname" 可以 为 found 在 该 对象 name.   
  
**示例**

创建 two 对象 和 put them 在 一个 group. Make 一个 additional copy 的 该 triangle 对象 within 该 group. 
    
    
    #创建 一个 substrate 使用 一个 channel etched 在 该 center. Put 该 对象 在 一个 group
    addrect;
    addtriangle;
    selectpartial("angle"); # select both 该 triANGLE 和 rectANGLE 对象
    addtogroup("结构");# 添加 选中的 到 group
    #select 该 etch 和 copy 到 创建 一个 second channel
    selectpartial("结构::tri"); # select 该 TRIangle
    copy(1e-6);            # copy 该 TRIangle

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ groupscope ](/hc/en-us/articles/360034928553-groupscope)
