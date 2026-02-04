<!--
Translation from English documentation
Original command: addlayerbuilder
Translation date: 2026-02-04 01:01:52
-->

# addlayerbuilder

向仿真环境中添加层构建器对象。

**语法** |  **描述**  
---|---  
addlayerbuilder; |  向仿真环境中添加层构建器对象。此函数不返回任何数据。  
addlayerbuilder(struct_data); |  使用包含"属性"和值对的struct添加层构建器对象并设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
   
**示例**

以下脚本命令将创建一个层构建器对象并向其添加两个层。
    
    
    addlayerbuilder;
    # Layer 1: 100 nm layer of silver
    addlayer("layer_1");
    setlayer("layer_1","thickness",100e-9);
    setlayer("layer_1","pattern material","Ag (Silver) - CRC");
    # Layer 2: 500 nm layer of silicon
    addlayer("layer_2");
    setlayer("layer_2","thickness",500e-9);
    setlayer("layer_2","pattern material","Si ("Si (Silicon) - Palik");

**参见**

* [addlayer](https://optics.ansys.com/hc/en-us/articles/360034924693-addlayer)
* [getlayerlist](https://optics.ansys.com/hc/en-us/articles/360034409134-getlayerlist)
* [setlayer](https://optics.ansys.com/hc/en-us/articles/360034929453-setlayer)
* [loadgdsfile](https://optics.ansys.com/hc/en-us/articles/360034929473-loadgdsfile)
* [getcelllist](https://optics.ansys.com/hc/en-us/articles/360034929413-getcelllist)
* [getlayerlist](https://optics.ansys.com/hc/en-us/articles/360034409134-getlayerlist)
* [setlayer](https://optics.ansys.com/hc/en-us/articles/360034929453-setlayer)
* [loadprocessfile](https://support.lumerical.com/hc/en-us/articles/360058330814)
* [saveprocessfile](https://support.lumerical.com/hc/en-us/articles/360060152573)
