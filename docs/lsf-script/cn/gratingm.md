<!-- Translation completed: 2026-02-04 -->
<!-- Original command: gratingm -->

# gratingm

    ?G;  # grating results
    ?G*T; # normalized to 光源 功率
    nx=find(N,0); # find 0th grating order
    ny=find(M,0); # find 0th grating order
    ?"Grating order 0,0 strength: " + num2str( G(nx,ny) );
    ?"Grating order 0,0 direction: Ux=" +num2str(u1(nx)) + " Uy=" +num2str(u2(ny));
    image(u1,u2,G,"ux","uy","Grating order strength","logplot");

**语法** | **描述**
---|---
out = gratingm( "monitorname",...); | Same arguments as grating 函数.

**示例**

This 示例 计算 various grating quantities. 
    mname="T";       # 监视器 name
    N=gratingn(mname);   # grating order numbers
    M=gratingm(mname);
    u1=gratingu1(mname);  # grating unit vectors (can be converted to theta,phi)
    u2=gratingu2(mname);
    G=grating(mname);   # 功率 to each order (fraction of transmitted 功率)
    T=透射(mname); # total 功率 transmitted through 监视器 (fraction of 光源 功率)

This 示例 计算 various grating quantities. 
    mname="T";       # 监视器 name
    N=gratingn(mname);   # grating order numbers
    M=gratingm(mname);
    u1=gratingu1(mname);  # grating unit vectors (can be converted to theta,phi)
    u2=gratingu2(mname);
    G=grating(mname);   # 功率 to each order (fraction of transmitted 功率)
    T=透射(mname); # total 功率 transmitted through 监视器 (fraction of 光源 功率)

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ grating ](/hc/en-us/articles/360034927213-grating) , [ gratingn ](/hc/en-us/articles/360034407014-gratingn)
