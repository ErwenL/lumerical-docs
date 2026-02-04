<!--
Translation from English documentation
Original command: addmodeexpansion
Translation date: 2026-02-04 01:06:23
-->

# addmodeexpansion

向仿真环境中添加模场扩展监视器。在MODE中，此命令要求存在活动的varFDTD区域。

**语法** |  **描述**  
---|---  
addmodeexpansion; |  向仿真环境中添加模场扩展监视器。此函数不返回任何数据。  
addmodeexpansion(struct_data); |  添加模场扩展监视器，并使用包含"属性"和值对的struct设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
   
**示例**

以下脚本命令将添加模场扩展监视器和场监视器，然后设置扩展监视器的部分属性。
    
    
    # add monitors
    addmodeexpansion;
    set("name","mode_expansion");
    addpower;
    set("name","field");
    # set the field monitor to be used by the expansion monitor
    select("mode_expansion");
    setexpansion("input", "field");
    # set the expansion monitor mode solver properties
    if (true) { 
    # select fundamental, fundamental TE or fundamental TM mode 
      set("mode selection","fundamental mode");
    } else { 
    # alternately, set expansion monitor mode solver properties,  
    # rather than one of the 'fundamental modes 
      set("mode selection","user select"); # use the 'user select' option 
      seteigensolver("use max index",0); # specify a custom value for 'n' 
      seteigensolver("n",1.1); updatemodes(3); # select the 3rd mode
    }

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
* [使用模场扩展监视器](https://optics.ansys.com/hc/en-us/articles/360034902433-Using-Mode-Expansion-Monitors)
* [setexpansion](https://optics.ansys.com/hc/en-us/articles/360034408974-setexpansion)
* [removeexpansion](https://optics.ansys.com/hc/en-us/articles/360034408994-removeexpansion)
* [updatemodes](https://optics.ansys.com/hc/en-us/articles/360034929073-updatemodes)
* [seteigensolver](https://optics.ansys.com/hc/en-us/articles/360034929113-seteigensolver)
* [geteigensolver](https://optics.ansys.com/hc/en-us/articles/360034408794-geteigensolver)
