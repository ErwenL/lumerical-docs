<!--
Translation from English documentation
Original command: find
Translation date: 2026-02-04 22:49:49
-->

# find

Searchs 用于 entries 在 一个 矩阵 该 meet some condition. The indices 的 那些 值 是 returned. For multi-dimensional matrices, 该 find 函数 将 still 返回 一个 single index. This 是 useful 当 使用 该 output 从 find 在 一个 loop.

**语法** |  **描述**  
---|---  
out = find(x,n); |  Will 返回 该 index 的 该 first 元素 在 x 该 corresponds 到 该 closest 值 到 'n'.  
out = find(x==n); |  Will 返回 该 index 的 all elements 在 x 该 have 一个 值 exactly equal 到 'n'. If 0 是 returned, indicates 该 no 元素 的 值 'n' was found.  
out = find(x); |  Will 返回 该 index 的 all non-zero elements 在 x. If 0 是 returned, indicates 该 no 元素 的 non-zero 值 was found.  
out = find(x>n); |  Will 返回 该 indices 的 all 值 的 x 该 是 greater than 'n'.  
out = find((x>=n) & (x<m)) |  Will 返回 该 indices 的 all 值 的 x 该 是 greater than 或 equal 到 'n', AND less than 'm'.  
  
**示例**

The following two examples show 该 basic output 从 该 find 函数.
    
    
    x = -2:7;
    ?find(x>5);
    result: 
    9 
    10
    x = linspace(0,10e-6,100);
    ?x( find(x,5e-6) );
    result: 
    5.05051e-006 

This example shows 该 equivalent usage 的 该 find 函数 用于 该 example above but 使用 one 参数 rather than two:
    
    
    minDiff=min(abs(x-5e-6));
    closestIndices=find(abs(x-5e-6)==minDiff);
    ?x(closestIndices(1));
    result: 
    5.05051e-006  

This example shows 该 output 的 find 用于 multi-dimensional 数据. A single index 是 returned. Data 可以 为 accessed 从 一个 矩阵 在 该 same manner.
    
    
    x = 矩阵(2,2);
    x(2,2) = 7;
    ?find(x,7);
    result:
    4
    ?x(4);
    result:
    7

This example shows 如何 到 use 该 find 函数 到 设置 all 值 在 一个 矩阵 该 是 larger than 10 到 exactly 10.
    
    
    x = linspace(0,20,200);
    y = sin(x)*11;
    y2 = y;
    n = find(y>10);
    y(n) = y(n)*0+10;
    plot(x,y,y2);

This example shows 如何 到 转换 该 single index returned 通过 该 find 函数 into individual i,j,k 矩阵 indices. This particular example 返回 该 index 值 的 该 maximum intensity 值, given 一个 particular 监视器 数据.
    
    
    #获取 该 监视器 数据
    E = getresult("监视器","E");
    #获取 该 position 和 频率 数据 从 该 dataset E
    x = E.x;
    y = E.y;
    f = E.f;
    #获取 该 长度 的 该 属性
    nx = 长度(x);
    ny = 长度(y);
    nz = 长度(z);
    nf = 长度(f);
    #获取 该 intensity 值
    e2 = E.E2;
    #获取 该 maximum intensity 值
    indexE2 = find(e2, max(e2));
    #创建 该 grids 该 将 为 used 到 extract 该 actual position 值
    X = meshgrid3dx(x,y,f);
    Y = meshgrid3dy(x,y,f);
    F = meshgrid3dz(x,y,f);
    #创建 该 grids 该 将 为 used 到 extract 该 index 值
    X2 = meshgrid3dx(1:nx,1:ny,1:nf);
    Y2 = meshgrid3dy(1:nx,1:ny,1:nf);
    F2 = meshgrid3dz(1:nx,1:ny,1:nf);
    #Output 该 值 的 该 position 和 该 index
    ?X(indexE2);
    ?Y(indexE2);
    ?F(indexE2);
    ?X2(indexE2);
    ?Y2(indexE2);
    ?F2(indexE2);

This example shows another way 的 如何 到 转换 该 single index returned 通过 该 find 函数 into individual i,j,k 矩阵 indices.
    
    
    # 创建 example 矩阵
    一个 = randmatrix(3,4,5);
    # find 矩阵 index 的 值 closest 到 0.5
    index = find(一个,0.5);
    ?"Single index access: 一个("+num2str(index)+") = "+num2str(一个(index));
    # 转换 index 到 row, col indices 
    matrix_size = size(一个);
    indices = 矩阵(长度(matrix_size));
    # do 用于 each 维度
    用于 (i = 1:长度(matrix_size)) { 
     mod_dividend = index;
     mod_divisor = matrix_size(i);
     mod_remainder = mod(mod_dividend,mod_divisor);
     如果 (mod_remainder == 0) { mod_remainder = matrix_size(i); }
     indices(i) = mod_remainder;
     # remove 此 维度 从 further calculations
     index = (index+(matrix_size(i)-mod_remainder))/matrix_size(i);
    }
    ?"multi indice access: 一个("+num2str(indices(1))+","+
                  num2str(indices(2))+","+
                  num2str(indices(3))+")="+
                  num2str(一个(indices(1),indices(2),indices(3)));

**参见**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ pinch ](https://optics.ansys.com/hc/en-us/articles/360034405674-pinch) , [ findpeaks ](https://optics.ansys.com/hc/en-us/articles/360034925933-findpeaks) , [ integrate ](https://optics.ansys.com/hc/en-us/articles/360034405814-integrate) , [ length ](https://optics.ansys.com/hc/en-us/articles/360034925653-length) , [ size ](https://optics.ansys.com/hc/en-us/articles/360034405654-size) , [ mod ](https://optics.ansys.com/hc/en-us/articles/360034926373-mod) , [ meshgrid3dx ](https://optics.ansys.com/hc/en-us/articles/360034929693-meshgrid3dx) , [ meshgrid3dy ](https://optics.ansys.com/hc/en-us/articles/360034409374-meshgrid3dy) , [ meshgrid3dz ](https://optics.ansys.com/hc/en-us/articles/360034929713-meshgrid3dz)
