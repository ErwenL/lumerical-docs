<!--
Translation from English documentation
Original command: getelectric
Translation date: 2026-02-04 22:49:59
-->

# getelectric

返回 该 sum 的 该 amplitude squares 用于 all electric field components, i.e. it 返回 |Ex|  2  +|Ey|  2  +|Ez|  2  . 

**语法** |  **描述**  
---|---  
out = getelectric( "monitorname");  |  返回 |Ex|  2  +|Ey|  2  +|Ez|  2  从 该 监视器.   
getelectric( "monitorname", option);  |  The optional 参数, option, 可以 have 一个 值 的 1 或 2. If it 是 2, 该 数据 是 unfolded 其中 possible according 到 该 symmetry 或 anti-symmetric boundaries 如果 it comes 从 一个 监视器 该 intersect such 一个 boundary at x最小值, y最小值 或 z最小值. The default 值 的 option 是 2.   
  
**示例**

This example 创建 一个 image plot 的 |E|^2 用于 一个 z-normal 频率 监视器 在 该 x-y plane. 
    
    
    E2=getelectric("output");
    x=getdata("output","x");
    y=getdata("output","y");
    image(x,y,E2);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ getdata ](/hc/en-us/articles/360034409834-getdata) , [ getmagnetic ](/hc/en-us/articles/360034930293-getmagnetic) , [ cwnorm ](/hc/en-us/articles/360034405454-cwnorm) , [ nonorm ](/hc/en-us/articles/360034405434-nonorm)
