<!-- Translation completed: 2026-02-04 -->
<!-- Original command: gratingangle -->

# gratingangle

**语法** | **描述**
---|---
out = gratingangle( "monitorname", ...); | Same arguments as grating 函数.

**示例**

This 示例 plots the relative strength of the grating orders.
    mname="T";          # 监视器 name
    theta=gratingangle(mname);  # 角度 of each grating order
    G=grating(mname);      # 功率 to each order (fraction of transmitted 功率)
    plot(theta,G,"theta (deg)","relative 功率","grating orders","plot points");

This 示例 plots the relative strength of the grating orders.
    mname="T";          # 监视器 name
    theta=gratingangle(mname);  # 角度 of each grating order
    G=grating(mname);      # 功率 to each order (fraction of transmitted 功率)
    plot(theta,G,"theta (deg)","relative 功率","grating orders","plot points");

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ grating ](/hc/en-us/articles/360034927213-grating) , [ gratingu1 ](/hc/en-us/articles/360034407094-gratingu1) , [ gratingu2 ](/hc/en-us/articles/360034407114-gratingu2)
