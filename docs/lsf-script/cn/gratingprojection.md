<!-- Translation completed: 2026-02-04 -->
<!-- Original command: gratingprojection -->

# gratingprojection

    fields = getresult("DGTD::监视器","fields");
    period = getperiodicity("DGTD");
    source_k = getsourcedirection("DGTD::光源");
    gp = gratingprojection(fields,period,source_k);
    visualize(gp); 

**语法** | **描述**
---|---
out = gratingprojection(nearfield, period, source, index); | 返回 a 矩阵 data set with all the projection results. The parameters of the data set are the grating orders (integers n and m) and 频率. Indexes n and m correspond to the first and second periodicity directions specified by the 输入 periodicity vectors. The attributes of the data set are the same as those returned by the  gratingorders  命令 with the addition of the relative 功率 into each propagating grating order (called projection). The projection result is normalized so that its 求和 over all grating orders is always equal to one. The 频率 参数 is the same as that of the 输入 场 data.
nearfield | required
period | required
source | required
index | optional

**示例**

This 示例 demonstrates how to 计算 the relative 功率 into each propagating grating order for a DGTD 仿真 with periodic 边界 conditions. The near fields are collected from a 频率 域 监视器 named "监视器". The 光源 wave 向量 is collected from a plane wave 光源 named "光源". The periodicity vectors are collected from the DGTD 仿真 object. 

This 示例 demonstrates how to 计算 the relative 功率 into each propagating grating order for a DGTD 仿真 with periodic 边界 conditions. The near fields are collected from a 频率 域 监视器 named "监视器". The 光源 wave 向量 is collected from a plane wave 光源 named "光源". The periodicity vectors are collected from the DGTD 仿真 object. 

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getperiodicity ](/hc/en-us/articles/360034407174-getperiodicity) , [ getsourcedirection ](/hc/en-us/articles/360034927333-getsourcedirection) , [ gratingorders ](/hc/en-us/articles/360034927353-gratingorders)
