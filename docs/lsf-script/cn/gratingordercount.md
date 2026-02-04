<!--
Translation from English documentation
Original command: gratingordercount
Translation date: 2026-02-04 22:50:00
-->

# gratingordercount

返回 该 total 数字 的 supported grating numbers.

**语法** |  **描述**  
---|---  
out = gratingordercount( "monitorname", f, index, direction); |  返回 该 total 数字 的 supported grating orders. Same 参数 as grating 脚本 命令.  
  
**示例**

This example 计算 power 到 each order only 如果 grating orders 是 supported.
    
    
    mname="T";       # 监视器 name
    如果(gratingordercount(mname) > 0){
    N=gratingn(mname);   # grating order numbers
    M=gratingm(mname);
    u1=gratingu1(mname);  # grating unit vectors (可以 为 converted 到 theta,phi)
    u2=gratingu2(mname);
    G=grating(mname);   # power 到 each order (fraction 的 transmitted power)
    }

**参见**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ grating ](https://optics.ansys.com/hc/en-us/articles/360034927213-grating) , [ gratingn ](https://optics.ansys.com/hc/en-us/articles/360034407014-gratingn) , [ gratingm ](https://optics.ansys.com/hc/en-us/articles/360034927233-gratingm)
