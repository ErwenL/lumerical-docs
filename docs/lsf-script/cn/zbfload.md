<!--
Translation from English documentation
Original command: zbfload
Translation date: 2026-02-04 22:50:32
-->

# zbfload

Loads 数据 从 Zemax zbf 文件 into 一个 d-card called "zbf_data". If "zbf_data" already exists 在 该 deck, it 将 为 called "zbf_data_2". After loading 一个 zbf 文件 使用 zbfload 命令, you 可以 extract any 的 该 following 数据: 

• Ex, Ey, Ez, Hx, Hy, Hz, x, y, z 

• 频率, 波长, index 

注意 该 该 H fields 是 calculated during 该 load operation 在 Lumerical tools 使用 该 index 从 该 original zbf 文件. Similarly, 该 longitudinal component 在 direction 的 propagation 是 not supported 通过 该 zbf format 和 it 是 populated 使用 zero 值 during 该 load operation. 

**语法** |  **描述**  
---|---  
zbfload  |  Select 该 文件 到 load 使用 该 文件 browser.  This 函数 does not 返回 any 数据.   
zbfload("文件名");  |  Loads 数据 从 一个 zbf 文件 called "文件名" without 一个 文件 browser.   
zbfload("文件名", propagation axis)  |  Loads 数据 从 一个 zbf 文件 called "文件名" without 一个 文件 browser 用于 一个 specified propagation axis. The propagation axis 是 一个 integer 值 该 indicates 该 x, y 和 z axis.   
zbfload("文件名", propagation axis, offset);  |  Loads 数据 从 一个 zbf 文件 called "文件名" without 一个 文件 browser 用于 一个 specified propagation axis 使用 该 specified offset. The offset 是 一个 floating 数字 数组 该 indicates 该 x, y 和 z coordinates shift 的 该 load-在 数据 到 该 original 数据.   
  
###  示例 

We have 数据 从 Zemax saved 在 一个 文件 named "myZemaxBeam.zbf". We use zbfload 命令 到 load 该 Zemax 数据 into FDE deck 用于 further 分析 使用 Lumerical tools. 
    
    
    zbfload("myZemaxBeam.zbf");
    ?getdata;
     ::zbf_data
    ?getdata("zbf_data");
     f  波长  index  x  y  z  Ex  Ey  Ez
     Hx  Hy  Hz 
    Ex = getdata("zbf_data","Ex");
    x = getdata("zbf_data","x"); 
    y = getdata("zbf_data","y"); 
    image(x,y,pinch(real(Ex)));

Result 的 zbfload operation 在 Eigensolver Analysis window: 

We have 数据 从 Zemax saved 在 一个 文件 named "myZemaxBeam.zbf". We use zbfload 命令 到 load 该 Zemax 数据 twice, 该 first 时间 without offset 和 该 second 时间 使用 该 [x, y, z] offset as [1e-7, 3e-7, 0]. 
    
    
    zbfload("myZemaxBeam.zbf");
    Ex = getdata("zbf_data", "Ex");
    x = getdata("zbf_data", "x");
    y = getdata("zbf_data", "y");
    image(x, y, pinch(real(Ex)));

The load 在 E field 的 zbf_data: 
    
    
    offset = [0.0000001, 0.0000003, 0];
    zbfload("myZemaxBeam.zbf", 3, offset);
    Ex = getdata("zbf_data", "Ex");
    x = getdata("zbf_data", "x");
    y = getdata("zbf_data", "y");
    image(x, y, pinch(real(Ex)));

The load 在 E field 的 zbf_data 使用 offset: 

**参见**

[ zbfexport ](/hc/en-us/articles/360034928253-zbfexport) , [ zbfread ](/hc/en-us/articles/360034408154-zbfread) , [ zbfwrite ](/hc/en-us/articles/360034928293-zbfwrite) , [ List 的 commands ](/hc/en-us/articles/360037228834)
