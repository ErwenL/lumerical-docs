<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getmaterial -->

# getmaterial

    f1  = 压缩(sampledData,2,1); # first column
    eps = 压缩(sampledData,2,2);  # second column
    nk1 = sqrt(eps);
    f2 = linspace(100e12,1000e12,100);
    nk2 = getindex(matName,f2);
    plotxy(c/f1*1e6,实部(nk1),
        c/f1*1e6,imag(nk1),
        c/f2*1e6,实部(nk2),
        c/f2*1e6,imag(nk2),
        "波长 (um)","折射率");
    legend("n - getmaterial",
        "k - getmaterial",
        "n - getindex",
        "k - getindex"); 

**语法** | **描述**
---|---
?getmaterial( "materialname"); | Displays the property names of the specified material that can be modified.
out = getmaterial( "materialname", "propertyname"); | 返回 the property named "propertyname" of the material with the name "materialname". The returned 变量 is either a 矩阵 or a 字符串, depending on the property in the query.
out = getmaterial( "materialname", _**cell**_); | 返回 multiple properties, by passing a [cell](https://support.lumerical.com/hc/en-us/articles/360034929913-cell) with entries equal to "propertyname". In this case out will be a struct with keys equal to the "propertyname" entries in the cell.

**示例**

These commands add a new Conductive material, set the name to "aluminum", anisotropy to "对角线", and set the 介电常数 as well as conductivity properties for the material. The 命令 getmaterial() is then used to find the 介电常数 of the material.
    A=[4;5;6];
    B=[1;2;3];
    mymaterial = addmaterial("Conductive");
    setmaterial(mymaterial,"name","Aluminium");
    setmaterial("Aluminum", "Anisotropy", 1); # enable 对角线 anisotropy
    setmaterial("Aluminum","介电常数", A);
    setmaterial("Aluminum","Conductivity", B);
    ?getmaterial("Aluminum","介电常数");
    result: 
    4 5 6   
    #Using cell 数组  
    props = cell(2);  
    props{1} = "介电常数"; props{2} = "Conductivity";  
    Al_vals = getmaterial("Aluminum",props);  
    ?Al_vals.Conductivity;  
    result:   
    1 2 3 
This 示例 shows how to access raw data from a Sampled data material.
注意: Sampled data 矩阵 格式 The sampled data 矩阵 has 2 or 4 columns, for isotropic or anisotropic materials \- The first column is the 频率 向量, in Hz. \- The next column(s) are the 复数 valued 介电常数. If you want 折射率 data (rather than 介电常数), remember that 介电常数 is simply the square of the 折射率.  
---  
    matName = "Ag (Silver) - CRC";
    ?getmaterial(matName);
    maxCoeff = getmaterial(matName,"max coefficient");
    sampledData = getmaterial(matName,"sampled data");

These commands add a new Conductive material, set the name to "aluminum", anisotropy to "对角线", and set the 介电常数 as well as conductivity properties for the material. The 命令 getmaterial() is then used to find the 介电常数 of the material.
    A=[4;5;6];
    B=[1;2;3];
    mymaterial = addmaterial("Conductive");
    setmaterial(mymaterial,"name","Aluminium");
    setmaterial("Aluminum", "Anisotropy", 1); # enable 对角线 anisotropy
    setmaterial("Aluminum","介电常数", A);
    setmaterial("Aluminum","Conductivity", B);
    ?getmaterial("Aluminum","介电常数");
    result: 
    4 5 6   
    #Using cell 数组  
    props = cell(2);  
    props{1} = "介电常数"; props{2} = "Conductivity";  
    Al_vals = getmaterial("Aluminum",props);  
    ?Al_vals.Conductivity;  
    result:   
    1 2 3 
This 示例 shows how to access raw data from a Sampled data material.
注意: Sampled data 矩阵 格式 The sampled data 矩阵 has 2 or 4 columns, for isotropic or anisotropic materials \- The first column is the 频率 向量, in Hz. \- The next column(s) are the 复数 valued 介电常数. If you want 折射率 data (rather than 介电常数), remember that 介电常数 is simply the square of the 折射率.  
---  
    matName = "Ag (Silver) - CRC";
    ?getmaterial(matName);
    maxCoeff = getmaterial(matName,"max coefficient");
    sampledData = getmaterial(matName,"sampled data");

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getindex ](/hc/en-us/articles/360034409674-getindex) , [ getfdtdindex ](/hc/en-us/articles/360034409694-getfdtdindex)
