<!--
Translation from English documentation
Original command: addmovie
Translation date: 2026-02-04 01:08:24
-->

# addmovie

向仿真环境中添加电影监视器。电影监视器在仿真期间捕获监视器覆盖区域内所需的场分量。

**语法** |  **描述**  
---|---  
addmovie; |  向仿真环境中添加电影监视器。此函数不返回任何数据。  
addmovie(struct_data); |  添加电影监视器，并使用包含"属性"和值对的struct设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
   
**示例**

以下脚本命令将向仿真区域添加一个2D z-normal电影监视器，设置其位置和尺寸，并在保持宽高比锁定的情况下设置其分辨率。锁定宽高比可确保视频保持监视器数据的形状。
    
    
    addmovie;
    set("name","movie_1");
    set("monitor type",3);  # 1 = 2D x-normal,  2 = 2D y-normal,  3 = 2D z-normal
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("lock aspect ratio",1);
    set("horizontal resolution",240);

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
