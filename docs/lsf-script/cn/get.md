<!--
Translation from English documentation
Original command: get
Translation date: 2026-02-04 22:49:49
-->

# 获取

获取 一个 属性 从 选中的 对象. The 属性 names 用于 该 获取 命令 是 该 same as 该 属性 names 在 该 Edit dialogue box. For example, 如果 you see 一个 属性 called "mesh accuracy", 那么 you 可以 use 该 命令 获取("mesh accuracy"); 到 获取 该 属性. It 是 possible 到 获取 numeric, 字符串, drop down 和 checkbox 属性.

**语法** |  **描述**  
---|---  
?获取; |  返回 一个 list 的 该 属性 的 该 选中的 对象(s).   
out = 获取("属性"); |  获取 该 requested 属性 值 从 该 currently 选中的 对象. It cannot 为 used 到 获取 该 属性 值 的 一个 选中的 对象 在 一个 group. If multiple 对象 是 选中的 获取("属性") 是 该 same as 获取("属性",i), 其中 i 是 该 数字 的 该 first 选中的 对象 使用 该 requested 属性. Out 可以 为 一个 矩阵 或 一个 字符串, depending 在 该 属性 requested. "Property" accepts 结构体 format 该 allows 用户 到 obtain multiple attributes.  
获取("属性",i); |  获取 该 属性 的 该 ith 选中的 对象. Use 此 到 act 在 一个 series 的 对象. It cannot 为 used 到 获取 该 值 的 一个 选中的 对象 在 一个 group. The 对象 是 ordered 通过 their location 在 该 对象 tree. The uppermost 选中的 对象 是 given 该 index 1, 和 该 index numbers increase as you go down 该 tree.  
获取(cell_array_of_properties) |  获取 该 specific 属性 的 该 选中的 对象 as 一个 结构体 (key-值 pairs). The input 是 一个 单元格 数组.  
  
**示例**

See 该 list 的 该 属性 的 一个 rectangle.
    
    
    addrect;
    ?获取;
    alpha
    color opacity
    detail
    enabled
      ⋮
    z
    z最大值
    z最小值
    z跨度

获取 该 x跨度 的 一个 对象 named substrate.
    
    
    select("substrate");
    x_span = 获取("x跨度"); 

添加 2 微米 到 该 radius 的 all 选中的 对象 该 have 一个 radius 属性.
    
    
    select("circle");
    用于 (i=1:getnumber) {
     rad=获取("radius",i);
     设置("radius",rad+2e-6,i);
    }

设置 和 获取 该 vertices 的 一个 pentagon 使用 一个 circumradius 的 1um.
    
    
    addpoly;
    theta=linspace(0,2*pi*4/5,5);
    x=cos(theta)*1e-6;
    y=sin(theta)*1e-6;
    V=[x,y];
    设置("vertices",V);
    ?获取("vertices");
    result: 
    1e-06 0   
    3.09017e-07 9.51057e-07   
    -8.09017e-07 5.87785e-07   
    -8.09017e-07 -5.87785e-07   
    3.09017e-07 -9.51057e-07 

获取 该 属性 的 一个 circle as 一个 结构体
    
    
    addcircle;  
      
    # 获取 specific 属性 的 该 选中的 对象 as 一个 结构体  
    PropStruct = 获取({"x","y","z","radius"});  
    ?PropStruct;  
    Struct 使用 fields:  
    radius  
    x  
    y  
    z  
      
    ?PropStruct.radius;  
    result:   
    1.8e-07   
      
    # 获取 all 该 属性 的 该 选中的 对象 as 一个 结构体  
    AllProps = 获取; # saved as 一个 字符串  
    AllProps = splitstring(AllProps, endl); # 转换 到 一个 单元格 数组  
    PropStruct = 获取(AllProps);  
      
    # Here's 一个 single-line equivalent 的 该 above three-line code   
    PropStruct = 获取(splitstring(获取,endl));

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ getnumber ](/hc/en-us/articles/360034928913-getnumber) , [ getnamed ](/hc/en-us/articles/360034408574-getnamed) , [ getnamednumber ](/hc/en-us/articles/360034408594-getnamednumber) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ haveproperty ](/hc/en-us/articles/360034928973-haveproperty) , [ runsetup ](/hc/en-us/articles/360034928893-runsetup)
