<!-- Translation completed: 2026-02-04 -->
<!-- Original command: grating -->

# grating

    ?G;  # grating results
    ?G*T; # normalized to 光源 功率
    nx=find(N,0); # find 0th grating order
    ny=find(M,0); # find 0th grating order
    ?"Grating order 0,0 strength: " + num2str( G(nx,ny) );
    ?"Grating order 0,0 direction: Ux=" +num2str(u1(nx)) + " Uy=" +num2str(u2(ny));
    image(u1,u2,G,"ux","uy","Grating order strength","logplot");
计算 the zeroth grating order 透射 from a 监视器 that recorded multiple 频率 points. The grating 函数 operates on one 频率 point at a time, so a for 循环 is required. 
    mname="T";       # 监视器 name
    f=getdata(mname,"f");  # get 频率 向量
    T=透射(mname); # get total 透射
    G00 = 矩阵(长度(f)); # initialize 矩阵
    for (i=1:长度(T)) {
     N=gratingn(mname,i);  # grating order numbers
     M=gratingm(mname,i); 
     temp=grating("T2",i);
     G00(i) = temp(find(N,0),find(M,0)); # select 0,0 grating order
    }
    plot(c/f*1e6,T,G00*T,"波长 (um)","功率");
    legend("total 透射","0,0 grating 透射"); 

**语法** | **描述**
---|---
out = grating("monitorname",f, index, direction ); | 返回 the strength of all physical grating orders from monitorname.
monitorname | required
f | optional
index | optional
direction | optional
**Monitor orientation** | **监视器 surface normal**
XY plane | Z
XZ plane | Y
YZ plane | X

**示例**

This 2D 示例 plots the relative strength of the grating orders. 
    mname="T";          # 监视器 name
    theta=gratingangle(mname);  # 角度 of each grating order
    G=grating(mname);      # 功率 to each order (fraction of transmitted 功率)
    plot(theta,G,"theta (deg)","relative 功率","grating orders","plot points");
This 3D 示例 计算 various grating quantities. 
    mname="T";       # 监视器 name
    N=gratingn(mname);   # grating order numbers
    M=gratingm(mname);
    u1=gratingu1(mname);  # grating unit vectors (can be converted to theta,phi)
    u2=gratingu2(mname);
    G=grating(mname);   # 功率 to each order (fraction of transmitted 功率)
    T=透射(mname); # total 功率 transmitted through 监视器 (fraction of 光源 功率)

This 2D 示例 plots the relative strength of the grating orders. 
    mname="T";          # 监视器 name
    theta=gratingangle(mname);  # 角度 of each grating order
    G=grating(mname);      # 功率 to each order (fraction of transmitted 功率)
    plot(theta,G,"theta (deg)","relative 功率","grating orders","plot points");
This 3D 示例 计算 various grating quantities. 
    mname="T";       # 监视器 name
    N=gratingn(mname);   # grating order numbers
    M=gratingm(mname);
    u1=gratingu1(mname);  # grating unit vectors (can be converted to theta,phi)
    u2=gratingu2(mname);
    G=grating(mname);   # 功率 to each order (fraction of transmitted 功率)
    T=透射(mname); # total 功率 transmitted through 监视器 (fraction of 光源 功率)

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ gratingn ](/hc/en-us/articles/360034407014-gratingn) , [ gratingperiod1 ](/hc/en-us/articles/360034927253-gratingperiod1) , [ gratingbloch1 ](/hc/en-us/articles/360034407134-gratingbloch1) , [ gratingu1 ](/hc/en-us/articles/360034407094-gratingu1) , [ gratingangle ](/hc/en-us/articles/360034927273-gratingangle) , [ gratingpolar ](/hc/en-us/articles/360034407034-gratingpolar) , [ gratingvector ](/hc/en-us/articles/360034407054-gratingvector)
