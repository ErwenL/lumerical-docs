<!--
Translation from English documentation
Original command: setnamed
Translation date: 2026-02-04 22:50:14
-->

# setnamed

Likes 该  设置  命令, except 该 该 对象 name 必须 为 specified. This 命令 将 返回 一个 error 在 分析 mode.

**语法** |  **描述**  
---|---  
?setnamed("name"); |  返回 一个 list 的 该 属性 的 该 对象 called name.  
setnamed("name", "属性", 值); |  The same as 设置, but acts 在 对象 使用 一个 specific name, instead 的 选中的 对象.  
setnamed("name", 结构体); |  A 结构体 可以 为 accepted 在 place 的 "属性"-值 pair 的 参数.  
setnamed("name", "属性", 值,i); |  This form 可以 为 used 到 设置 该 属性 的 该 ith named 对象 当 multiple 对象 have 该 same name. The 对象 是 ordered 通过 their location 在 该 对象 tree. The uppermost 选中的 对象 是 given 该 index 1, 和 该 index numbers increase as you go down 该 tree.  
setnamed("groupname::name", "属性", 值); |  The same as 设置, but acts 在 对象 within 该 group named "groupname" 该 是 named "name", instead 的 选中的 对象.  
setnamed("groupname::name", "属性", 值,i); |  This form 可以 为 used 到 设置 该 属性 的 该 ith 对象 使用 该 name "name" 在 该 group "groupname" 当 multiple 对象 have 该 same name. The 对象 是 ordered 通过 their location 在 该 对象 tree. The uppermost 选中的 对象 是 given 该 index 1, 和 该 index numbers increase as you go down 该 tree.  
  
**示例**

设置 该 radius 的 该 对象 called "circle" 到 10nm:
    
    
    setnamed("circle","radius",10e-9); 

添加 2 微米 到 该 radius 的 all 选中的 对象 named circle:
    
    
    用于 (i=1:getnamednumber("circle")) {
     rad=getnamed("circle","radius",i);
     setnamed("circle","radius",rad+2e-6,i);
    }

Use 结构体 as 一个 input 到 设置 该 coordinates 和 dimensions 的 一个 对象 called "rectangle":
    
    
    coordinates = {"x" : -3e-7,  
                   "x跨度" : 1e-6,  
                   "y" : 5e-6,  
                   "y跨度" : 1e-5,  
                   "z" : 1e-7,  
                   "z跨度" : 2.2e-7};  
      
    setnamed("rectangle", coordinates);

**注意**

In INTERCONNECT, 该 元素 属性 值 必须 为 entered 在 该  setnamed  命令 使用 该 fixed standard unit. In some cases, 该 standard unit 是 different 从 该 default unit 在 该 Property View. Following 是 一个 example 的 setting 该 ONA center 频率. The center 频率 default unit 是 THz, while 该 standard unit 是 Hz, 和 当 使用 该  setnamed  命令, 该 值 needs 到 为 在 Hz:
    
    
    setnamed("ONA", "center 频率", 193.1e12); 

To find 该 standard unit 用于 一个 元素 属性, open 该 元素's help page 在 该 Knowledge Page, 和 look at 该 Default unit column. A note 是 included 用于 cases 其中 该 default 和 standard units differ. For example, see 该 center 频率 的 该 [ ONA ](**%20to%20be%20defined%20**) .

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ 获取 ](/hc/en-us/articles/360034928873-获取) , [ getnamed ](/hc/en-us/articles/360034408574-getnamed) , [ getnamednumber ](/hc/en-us/articles/360034408594-getnamednumber)
