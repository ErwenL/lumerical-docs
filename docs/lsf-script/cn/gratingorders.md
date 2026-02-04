<!-- Translation completed: 2026-02-04 -->
<!-- Original command: gratingorders -->

# gratingorders

    fields = getresult("DGTD::监视器","fields");
    频率 = fields.f; 
    period = getperiodicity("DGTD");
    source_k = getsourcedirection("DGTD::光源");
    go = gratingorders(period,source_k,频率,1.0);
    visualize(go); 

**语法** | **描述**
---|---
out = gratingorders(period, source, frequency, index); | 返回 a 矩阵 data set with the propagating grating orders (integers n and m), a unit 向量 in the direction of the k-向量 of each order (call them **u** (n,m)) and their corresponding angles (theta and phi). The parameters of the data set are n,m and 频率. Indexes n and m correspond to the first and second periodicity directions specified by the 输入 periodicity vectors. The attributes of the data set are the unit vectors **u** (n,m) and their corresponding angles (theta and phi). The grating angles are defined with respect to the normal incidence direction of the 光源 (call it the **n** -axis). The first 角度 (theta) is an elevation from the **n** -axis and the and the second 角度 (phi) is a rotation around the **n** -axis starting from the first periodicity 向量. 角度 phi is only returned when two periodicity vectors are specified.
period | required
source | required
frequency | required
index | optional

**示例**

This 示例 shows how to find the propagating grating orders from a DGTD 仿真 with periodic 边界 conditions. The 光源 k-向量 and 频率 are obtained from and plane wave 光源 object named "光源" and a 频率 域 监视器 named "监视器", respectively. 

This 示例 shows how to find the propagating grating orders from a DGTD 仿真 with periodic 边界 conditions. The 光源 k-向量 and 频率 are obtained from and plane wave 光源 object named "光源" and a 频率 域 监视器 named "监视器", respectively. 

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getperiodicity ](/hc/en-us/articles/360034407174-getperiodicity) , [ getsourcedirection ](/hc/en-us/articles/360034927333-getsourcedirection) , [ gratingprojection ](/hc/en-us/articles/360034927373-gratingprojection)
