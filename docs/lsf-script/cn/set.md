<!--
Translation from English documentation
Original command: set
Translation date: 2026-02-04 22:50:14
-->

# 设置

设置 一个 属性 的 currently 选中的 对象.

注意 该 most 对象 可以 not 为 modified 当 该 求解器 是 在 Analysis mode. In such situations, 此 命令 将 返回 一个 error.

**语法** |  **描述**  
---|---  
?设置; |  返回 一个 list 的 该 属性 的 该 选中的 对象(s) 该 可以 为 changed 使用 该 设置 命令.  
设置("属性",值); |  This 将 设置 该 属性 的 一个 currently 选中的 对象, including pull-downs 和 check boxes. It cannot 为 used 到 设置 该 值 的 一个 选中的 对象 在 一个 group. Value 可以 为 一个 数字 或 字符串. This 函数 does not 返回 any 数据.  
设置(结构体); |  A 结构体 可以 为 accepted 在 place 的 "属性"-值 pair 的 参数.  
设置("属性",值,i); |  This form 可以 为 used 到 设置 该 属性 的 该 ith 选中的 对象 当 multiple 对象 是 选中的. It cannot 为 used 到 设置 该 值 的 一个 选中的 对象 在 一个 group. The 对象 是 ordered 通过 their location 在 该 对象 tree. The uppermost 选中的 对象 是 given 该 index 1, 和 该 index numbers increase as you go down 该 tree.  
  
**示例**

设置 该 radius 的 any 选中的 对象 (sphere, ring, circle) 使用 一个 属性 called radius 到 1e-6.
    
    
    设置("radius",1e-6);

设置 该 name 属性 的 all 选中的 对象 到 reflection.
    
    
    设置("name","reflection");

设置 一个 checkbox 到 0 到 uncheck. 设置 到 1 到 check.
    
    
    设置("check box label name",0);  # unselect checkbox 

To disable 一个 对象.
    
    
    设置("enabled",0);

设置 该 x最小值 边界条件 到 为 该 first choice 在 该 pull-down menu.
    
    
    设置("x最小值 bc",1);

设置 该 x最小值 边界条件 到 该 字符串 "PML".
    
    
    设置("x最小值 bc","PML");

设置 该 PML profile 的 该 FDTD region
    
    
    设置("pml profile", 2);

设置 该 PML profiles 用于 individual boundary
    
    
    设置("same settings 在 all boundaries",0);
    设置("pml profile", [1,1,2,1,1,1]); # setting y最小值 bc 到 "stabilized", 和 all other bc 到 "standard"

添加 2 微米 到 该 radius 的 all 对象 named "circle".
    
    
    select("circle");
    用于 (i=1:getnumber) {
     rad=获取("radius",i);
     设置("radius",rad+2e-6,i);
    } 

设置 和 获取 该 vertices 的 一个 polygon 对象. We 创建 一个 octagon 使用 一个 radius 的 1um.
    
    
    addpoly;
    theta=linspace(0,2*pi,9);
    theta=theta(1:8);
    x=cos(theta)*1e-6;
    y=sin(theta)*1e-6;
    V=[x,y];
    设置("vertices",V);
    ?获取("vertices");
    result: 
    1e-006 0 
    7.07107e-007 7.07107e-007 
    6.12323e-023 1e-006 
    -7.07107e-007 7.07107e-007 
    -1e-006 1.22465e-022 
    -7.07107e-007 -7.07107e-007 
    -1.83697e-022 -1e-006 
    7.07107e-007 -7.07107e-007 

See 一个 list 的 该 属性 的 一个 rectangle.
    
    
    addrect;
    ?获取;
    alpha
    color opacity
    detail
    enabled
    first axis
    grid attribute name
    index
    index units
    材料
    mesh order
    name
    override color opacity 从 材料 database
    override mesh order 从 材料 database
    render 类型
    rotation 1
    rotation 2
    rotation 3
    second axis
    设置 color opacity 从 材料 database
    设置 mesh order 从 材料 database
    third axis
    x
    x最大值
    x最小值
    x跨度
    y
    y最大值
    y最小值
    y跨度
    z
    z最大值
    z最小值
    z跨度

Use 结构体 as 一个 input 到 设置 该 coordinates 和 dimensions 的 一个 currently 选中的 对象 called "rectangle":
    
    
    coordinates = {"x" : -3e-7,  
                   "x跨度" : 1e-6,  
                   "y" : 5e-6,  
                   "y跨度" : 1e-5,  
                   "z" : 1e-7,  
                   "z跨度" : 2.2e-7};  
      
    设置(coordinates);

**注意**

In INTERCONNECT, 该 元素 属性 值 必须 为 entered 在 该  设置  命令 使用 该 fixed standard unit. In some cases, 该 standard unit 是 different 从 该 default unit 在 该 Property View. Following 是 一个 example 的 setting 该 ONA center 频率. The center 频率 default unit 是 THz, while 该 standard unit 是 Hz, 和 当 使用 该  设置  命令, 该 值 needs 到 为 在 Hz:
    
    
    select("ONA");
    设置("center 频率", 193.1e12); 

To find 该 standard unit 用于 一个 元素 属性, open 该 元素's help page 在 该 Knowledge Page, 和 look at 该 Default unit column. A note 是 included 用于 cases 其中 该 default 和 standard units differ. For example, see 该 center 频率 的 该 [ONA](/hc/en-us/articles/360036617973).

**参见**

[获取](/hc/en-us/articles/360034928873-获取), [setnamed](/hc/en-us/articles/360034928793-setnamed), [setmaterial](/hc/en-us/articles/360034409654-setmaterial), [addmaterial](/hc/en-us/articles/360034930013-addmaterial), [haveproperty](/hc/en-us/articles/360034928973-haveproperty), [runsetup](/hc/en-us/articles/360034928893-runsetup), [runanalysis](/hc/en-us/articles/360034409874-runanalysis)
