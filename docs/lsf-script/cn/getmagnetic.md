<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getmagnetic -->

# getmagnetic

**语法** | **描述**
---|---
out = getmagnetic( "monitorname"); | 返回
getmagnetic( "monitorname", option); | The optional 参数, option, can have a 值 of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a 监视器 that intersect such a 边界 at x min, y min or z min. The default 值 of option is 2.

**示例**

This 示例 creates an image plot of |H|^2 for a z-normal 频率 监视器 in the x-y plane. 
    H2=getmagnetic("输出");
    x=getdata("输出","x");
    y=getdata("输出","y");
    image(x,y,H2);

This 示例 creates an image plot of |H|^2 for a z-normal 频率 监视器 in the x-y plane. 
    H2=getmagnetic("输出");
    x=getdata("输出","x");
    y=getdata("输出","y");
    image(x,y,H2);

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getdata ](/hc/en-us/articles/360034409834-getdata) , [ getelectric ](/hc/en-us/articles/360034409974-getelectric) , [ cwnorm ](/hc/en-us/articles/360034405454-cwnorm) , [ nonorm ](/hc/en-us/articles/360034405434-nonorm)
