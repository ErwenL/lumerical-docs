<!-- Translation completed: 2026-02-04 -->
<!-- Original command: gratingpolar -->

# gratingpolar

**语法** | **描述**
---|---
out = gratingpolar( "mname", f, index, direction); | 返回 the strength of all physical grating orders from the 监视器. 输出 is in spherical coordinates.
mname | required
f | optional
index | optional
direction | optional

**示例**

This 2D result shows that gratingpolar gives the same result as the grating 函数 when we 计算 |Er|^2+|Etheta|^2+ |Ephi|^2.
    ?Gp=gratingpolar("monitor1");
    result: 
    -3.06956e-017+0i -0.069704-0.32201i 0+0i 
    -3.66784e-018-1.46714e-017i -0.0813186-0.381864i 0+0i 
    2.97089e-017+1.48545e-017i -0.670119-0.442682i 0+0i 
    -4.78864e-018-3.83091e-017i -0.0585844-0.30093i 0+0i 
    ?求和(abs(Gp)^2,2);
    result: 
    0.108549 
    0.152433 
    0.645027 
    0.093991 
    ?G=grating("monitor1");
    result: 
    0.108549 
    0.152433 
    0.645027 
    0.093991 

This 2D result shows that gratingpolar gives the same result as the grating 函数 when we 计算 |Er|^2+|Etheta|^2+ |Ephi|^2.
    ?Gp=gratingpolar("monitor1");
    result: 
    -3.06956e-017+0i -0.069704-0.32201i 0+0i 
    -3.66784e-018-1.46714e-017i -0.0813186-0.381864i 0+0i 
    2.97089e-017+1.48545e-017i -0.670119-0.442682i 0+0i 
    -4.78864e-018-3.83091e-017i -0.0585844-0.30093i 0+0i 
    ?求和(abs(Gp)^2,2);
    result: 
    0.108549 
    0.152433 
    0.645027 
    0.093991 
    ?G=grating("monitor1");
    result: 
    0.108549 
    0.152433 
    0.645027 
    0.093991 

**另请参阅**

[List of commands ](/hc/en-us/articles/360037228834) , [ grating ](/hc/en-us/articles/360034927213-grating) , [ gratingn ](/hc/en-us/articles/360034407014-gratingn) , [ gratingperiod1 ](/hc/en-us/articles/360034927253-gratingperiod1) , [ gratingbloch1 ](/hc/en-us/articles/360034407134-gratingbloch1) , [ gratingu1 ](/hc/en-us/articles/360034407094-gratingu1) , [ gratingangle ](/hc/en-us/articles/360034927273-gratingangle) , [ gratingvector ](/hc/en-us/articles/360034407054-gratingvector) , [ Far field projections - Field polarization ](/hc/en-us/articles/360034914753-FFP-Field-polarization)
