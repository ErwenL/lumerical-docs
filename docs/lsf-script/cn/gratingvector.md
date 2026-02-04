<!-- Translation completed: 2026-02-04 -->
<!-- Original command: gratingvector -->

# gratingvector

**语法** | **描述**
---|---
out = gratingvector( "mname", f, index, direction); | 返回 the strength of all physical grating orders from monitorname. 输出 is in Cartesian coordinates.
mname | required
f | optional
index | optional
direction | optional

**示例**

This 2D result shows that gratingvector gives the same result as the grating 函数 when we 计算 |Ex|^2+|Ey|^2+ |Ez|^2.
    ?Gv=gratingvector("monitor1");
    result: 
    0.0476203+0.219991i 0.0509014+0.235148i 0+0i 
    0.0794422+0.373053i 0.0173684+0.0815601i 0+0i 
    0.638599+0.42186i -0.203101-0.134169i 0+0i 
    0.0335526+0.172349i -0.0480246-0.246687i 0+0i 
    ?求和(abs(Gv)^2,2);
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

This 2D result shows that gratingvector gives the same result as the grating 函数 when we 计算 |Ex|^2+|Ey|^2+ |Ez|^2.
    ?Gv=gratingvector("monitor1");
    result: 
    0.0476203+0.219991i 0.0509014+0.235148i 0+0i 
    0.0794422+0.373053i 0.0173684+0.0815601i 0+0i 
    0.638599+0.42186i -0.203101-0.134169i 0+0i 
    0.0335526+0.172349i -0.0480246-0.246687i 0+0i 
    ?求和(abs(Gv)^2,2);
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

[ List of commands ](/hc/en-us/articles/360037228834) , [ grating ](/hc/en-us/articles/360034927213-grating) , [ gratingn ](/hc/en-us/articles/360034407014-gratingn) , [ gratingperiod1 ](/hc/en-us/articles/360034927253-gratingperiod1) , [ gratingbloch1 ](/hc/en-us/articles/360034407134-gratingbloch1) , [ gratingu1 ](/hc/en-us/articles/360034407094-gratingu1) , [ gratingangle ](/hc/en-us/articles/360034927273-gratingangle) , [ gratingpolar ](/hc/en-us/articles/360034407034-gratingpolar) , [ Far field projections - Field polarization ](/hc/en-us/articles/360034914753-FFP-Field-polarization)
