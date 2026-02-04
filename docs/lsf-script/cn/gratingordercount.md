<!-- Translation completed: 2026-02-04 -->
<!-- Original command: gratingordercount -->

# gratingordercount

**语法** | **描述**
---|---
out = gratingordercount( "monitorname", f, index, direction); | 返回 the total 数字 of supported grating orders. Same arguments as grating 脚本 命令.

**示例**

This 示例 计算 功率 to each order only if grating orders are supported.
    mname="T";       # 监视器 name
    if(gratingordercount(mname) > 0){
    N=gratingn(mname);   # grating order numbers
    M=gratingm(mname);
    u1=gratingu1(mname);  # grating unit vectors (can be converted to theta,phi)
    u2=gratingu2(mname);
    G=grating(mname);   # 功率 to each order (fraction of transmitted 功率)
    }

This 示例 计算 功率 to each order only if grating orders are supported.
    mname="T";       # 监视器 name
    if(gratingordercount(mname) > 0){
    N=gratingn(mname);   # grating order numbers
    M=gratingm(mname);
    u1=gratingu1(mname);  # grating unit vectors (can be converted to theta,phi)
    u2=gratingu2(mname);
    G=grating(mname);   # 功率 to each order (fraction of transmitted 功率)
    }

**另请参阅**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ grating ](https://optics.ansys.com/hc/en-us/articles/360034927213-grating) , [ gratingn ](https://optics.ansys.com/hc/en-us/articles/360034407014-gratingn) , [ gratingm ](https://optics.ansys.com/hc/en-us/articles/360034927233-gratingm)
