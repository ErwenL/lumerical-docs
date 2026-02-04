<!--
Translation from English documentation
Original command: getmaterial
Translation date: 2026-02-04 22:50:00
-->

# getmaterial

返回 属性 的 一个 材料 在 该 材料 database.

**语法** |  **描述**  
---|---  
?getmaterial( "materialname"); |  Displays 该 属性 names 的 该 specified 材料 该 可以 为 modified.  
out = getmaterial( "materialname", "propertyname"); |  返回 该 属性 named "propertyname" 的 该 材料 使用 该 name "materialname". The returned 变量 是 either 一个 矩阵 或 一个 字符串, depending 在 该 属性 在 该 query.  
out = getmaterial( "materialname", _**cell**_); |  Return multiple properties, by passing a [cell](https://support.lumerical.com/hc/en-us/articles/360034929913-cell) with entries equal to "propertyname". In this case out will be a struct with keys equal to the "propertyname" entries in the cell.  
  
**示例**

These commands 添加 一个 新的 Conductive 材料, 设置 该 name 到 "aluminum", anisotropy 到 "Diagonal", 和 设置 该 permittivity as well as conductivity 属性 用于 该 材料. The 命令 getmaterial() 是 那么 used 到 find 该 permittivity 的 该 材料.
    
    
    A=[4;5;6];
    B=[1;2;3];
    mymaterial = addmaterial("Conductive");
    setmaterial(mymaterial,"name","Aluminium");
    setmaterial("Aluminum", "Anisotropy", 1); # 启用 diagonal anisotropy
    setmaterial("Aluminum","Permittivity", A);
    setmaterial("Aluminum","Conductivity", B);
    ?getmaterial("Aluminum","Permittivity");
    result: 
    4 5 6   
      
    #Using 单元格 数组  
    props = 单元格(2);  
    props{1} = "Permittivity"; props{2} = "Conductivity";  
    Al_vals = getmaterial("Aluminum",props);  
    ?Al_vals.Conductivity;  
    result:   
    1 2 3 

This example shows 如何 到 access raw 数据 从 一个 Sampled 数据 材料.

注意: Sampled 数据 矩阵 format The sampled 数据 矩阵 has 2 或 4 columns, 用于 isotropic 或 anisotropic materials \- The first column 是 该 频率 向量, 在 Hz. \- The next column(s) 是 该 complex valued permittivity. If you want refractive index 数据 (rather than permittivity), remember 该 permittivity 是 simply 该 square 的 该 refractive index.  
---  
      
    
    matName = "Ag (Silver) - CRC";
    ?getmaterial(matName);
    maxCoeff = getmaterial(matName,"max coefficient");
    sampledData = getmaterial(matName,"sampled 数据");
    # 转换 sampledData 矩阵 到 refractive index
    f1  = pinch(sampledData,2,1); # first column
    eps = pinch(sampledData,2,2);  # second column
    nk1 = sqrt(eps);
    # use getindex 命令 用于 comparison
    f2 = linspace(100e12,1000e12,100);
    nk2 = getindex(matName,f2);
    plotxy(c/f1*1e6,real(nk1),
        c/f1*1e6,imag(nk1),
        c/f2*1e6,real(nk2),
        c/f2*1e6,imag(nk2),
        "波长 (um)","refractive index");
    legend("n - getmaterial",
        "k - getmaterial",
        "n - getindex",
        "k - getindex"); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getindex ](/hc/en-us/articles/360034409674-getindex) , [ getfdtdindex ](/hc/en-us/articles/360034409694-getfdtdindex)
