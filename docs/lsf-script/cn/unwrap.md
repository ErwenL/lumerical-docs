<!--
Translation from English documentation
Original command: unwrap
Translation date: 2026-02-04 22:50:15
-->

# unwrap

Removes changes 的 more than 2  π  从 一个 1D 数组. It 可以 为 useful after angle(x) 到 see phase without discontinuities. 

The unwrap 函数 是 primarily intended 用于 1D arrays. Care 必须 为 taken 当 applying it 到 matrices 使用 more than one 维度. 

**语法** |  **描述**  
---|---  
out = unwrap(x);  |  返回 该 值 的 x without discontinuities.   
  
**示例**

Apply 该 unwrap 函数 到 一个 1D 数组. 
    
    
    vec=linspace(0,10,100);
    A=cos(vec) + sin(vec)*1i;
    B=angle(A);
    C=unwrap(B);
    plot(vec,real(A),B,C);
    legend("cos(x)","angle", "unwrap");

The following figure 将 为 generated: 

Apply 该 unwrap 函数 到 一个 2D 矩阵. The unwrap 函数 将 treat 该 2D 矩阵 as 一个 1D 向量 (i.e. concatenate each row), meaning 该 该 unwrapped phase 的 该 2nd row 将 start at 该 phase 的 该 end 的 该 first row. Notice 该 该 值 在 all 5 rows 的 矩阵 D 是 identical, but after 该 unwrap 函数 是 applied, 该 lines 是 'stacked' 在 top 的 each other. This 是 because 该 unwrap treated 该 矩阵 as 一个 large 1D 数组, rather than treating each row independently. 
    
    
    vec=linspace(0,10,100);
    A=cos(vec) + sin(vec)*1i; # 创建 complex sinusoid
    B=1:5;           # 向量 从 1:5
    C=meshgridx(A,B);     # 2D 矩阵 使用 5 copies 的 sinusoid
    D=angle(C);        # 获取 angle 的 矩阵 
    image(vec,B,D,"vec","5 copies","angle");  # image plot 的 矩阵
    plot(vec,D,"vec","angle");         # line plot (all 5 lines 是 identical)
    legend("row 1","row 2","row 3","row 4","row 5");
    plot(vec,unwrap(D),"vec","unwrap angle"); # unwrap. Now lines 是 stacked
    legend("row 1","row 2","row 3","row 4","row 5");

To apply 该 unwrap 函数 到 2D phase 数据 在 2D fashion (rather than treating it as 一个 single large 1D 向量), see 该 following example. The unwrap 函数 必须 为 applied 到 one row at 一个 时间, 那么 one column at 一个 时间. 

注意: A 2D unwrap operation 是 non-trivial. This example code works 在 some cases, but not always. Please do some testing 到 determine 如果 it works 用于 your application. 
    
    
    x=linspace(-5,5,100); y=x;
    nx=长度(x); ny=长度(y);
    数据 = exp( 1i* (meshgridx(x,y)+meshgridy(x,y)) );
    phase = angle(数据); 
    image(x,y,phase,"x","y","raw phase (rad)");
    # unwrap over both dimensions 
    用于 (i=1:nx) {
     phase(i,1:ny) = unwrap( pinch(phase,1,i) );
    }
    用于 (j=1:ny) {
     phase(1:nx,j) = unwrap( pinch(phase,2,j) );
    }
    image(x,y,phase,"x","y","unwrapped phase (rad)"); 

|   
---|---  
  
**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ real ](/hc/en-us/articles/360034925493-real) , [ imag ](/hc/en-us/articles/360034925513-imag) , [ angle ](/hc/en-us/articles/360034405614-angle)
