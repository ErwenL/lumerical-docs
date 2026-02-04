<!--
Translation from English documentation
Original command: addlayer
Translation date: 2026-02-04 01:01:01
-->

# addlayer

向层构建器对象添加一个层。此命令仅在存在层构建器对象且被选中时有效。

**语法** |  **描述**  
---|---  
addlayer; |  向选中的层构建器对象添加一个层。层的名称设置为"default name"。此函数不返回任何数据。  
addlayer("name"); |  添加一个名为"name"的层  
   
**示例**

以下脚本命令将创建一个层构建器对象并向其添加两个层。
    
    
    addlayerbuilder;
    # Layer 1 = 100 nm layer of silver
    addlayer("layer_1");
    setlayer("layer_1","thickness",100e-9);
    setlayer("layer_1","material","Ag (Silver) - CRC");
    # Layer 2 = 500 nm layer of silicon
    addlayer("layer_2");
    setlayer("layer_2","thickness",500e-9);
    setlayer("layer_2","material","Si (Silicon)");

**参见**

* [addlayerbuilder](https://optics.ansys.com/hc/en-us/articles/360034404714-addlayerbuilder)
* [getlayerlist](https://optics.ansys.com/hc/en-us/articles/360034409134-getlayerlist)
* [setlayer](https://optics.ansys.com/hc/en-us/articles/360034929453-setlayer)
* [loadgdsfile](https://optics.ansys.com/hc/en-us/articles/360034929473-loadgdsfile)
* [getcelllist](https://optics.ansys.com/hc/en-us/articles/360034929413-getcelllist)
* [getlayerlist](https://optics.ansys.com/hc/en-us/articles/360034409134-getlayerlist)
* [setlayer](https://optics.ansys.com/hc/en-us/articles/360034929453-setlayer)
