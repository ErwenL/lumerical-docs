<!--
Translation from English documentation
Original command: asapload
Translation date: 2026-02-04 22:49:36
-->

# asapload

Loads 数据 从 一个 fld 文件 从 BRO's ASAP. asapload 创建 一个 d-card 结构 called "fld_data" 该 contains all 该 数据 在 该 文件. If "fld_data" exists, it 将 为 called "fld_data_2". After loading 一个 asapfile 使用 asapload, you 可以 extract any desired 数据., 该 可以 为 

  * Ex, Ey, Ez, Hx, Hy, Hz, x, y, z 
  * power, 频率, 波长, index 

**语法** |  **描述**  
---|---  
asapload;  |  Select 该 文件 到 load 使用 该 文件 browser.  This 函数 does not 返回 any 数据.   
asapload( "文件名");  |  Loads 数据 从 一个 fld 文件 called "文件名" without 一个 文件 browser.   
  
**示例**

After loading 该 文件, you 可以 use ?getdata 到 see 一个 list 的 all d-cards, 或 该 variables 在 该 d-card. Data 可以 为 extracted 使用 该 getdata 函数. For example, 该 real part 的 Ex 可以 为 imaged 使用 该 following code. 
    
    
    asapload("asap.ldf");
    ?getdata;
    global monitors:
     fld_data 
    ?getdata("fld_data");
    f 波长 index power x y z Ex Ey
    Ez Hx Hy Hz 
    Ex = getdata("fld_data","Ex");
    x = getdata("fld_data","x"); 
    y = getdata("fld_data","y"); 
    image(x,y,pinch(real(Ex)));

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ asapexport ](/hc/en-us/articles/360034931953-asapexport) , [ asapimport ](/hc/en-us/articles/360034411274-asapimport) , [ addimportedsource ](/hc/en-us/articles/360034924433-addimportedsource) , [ fileexists ](/hc/en-us/articles/360034931633-fileexists)
