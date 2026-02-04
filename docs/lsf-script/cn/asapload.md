<!-- Translation completed: 2026-02-04 -->
<!-- Original command: asapload -->

# asapload

**语法** | **描述**
---|---
asapload; | Select the 文件 to 加载 with the 文件 browser.  This 函数 does not 返回 any data.
asapload( "filename"); | Loads data from an fld 文件 called "文件名" without a 文件 browser.

**示例**

After loading the 文件, you can use ?getdata to see a list of all d-cards, or the variables in the d-card. Data can be extracted using the getdata 函数. For 示例, the 实部 part of Ex can be imaged using the following code. 
    asapload("asap.ldf");
    ?getdata;
    global monitors:
     fld_data 
    ?getdata("fld_data");
    f 波长 index 功率 x y z Ex Ey
    Ez Hx Hy Hz 
    Ex = getdata("fld_data","Ex");
    x = getdata("fld_data","x"); 
    y = getdata("fld_data","y"); 
    image(x,y,压缩(实部(Ex)));

After loading the 文件, you can use ?getdata to see a list of all d-cards, or the variables in the d-card. Data can be extracted using the getdata 函数. For 示例, the 实部 part of Ex can be imaged using the following code. 
    asapload("asap.ldf");
    ?getdata;
    global monitors:
     fld_data 
    ?getdata("fld_data");
    f 波长 index 功率 x y z Ex Ey
    Ez Hx Hy Hz 
    Ex = getdata("fld_data","Ex");
    x = getdata("fld_data","x"); 
    y = getdata("fld_data","y"); 
    image(x,y,压缩(实部(Ex)));

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ asapexport ](/hc/en-us/articles/360034931953-asapexport) , [ asapimport ](/hc/en-us/articles/360034411274-asapimport) , [ addimportedsource ](/hc/en-us/articles/360034924433-addimportedsource) , [ fileexists ](/hc/en-us/articles/360034931633-fileexists)
