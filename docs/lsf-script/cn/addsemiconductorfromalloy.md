<!--
Translation from English documentation
Original command: addsemiconductorfromalloy
Translation date: 2026-02-04 22:49:30
-->

# addsemiconductorfromalloy

转换 一个 Alloy 材料 到 一个 Semiconductor 材料 at 一个 fixed mole fraction 和 添加 its electrothermal 材料 属性 到 该 选中的 材料 model 在 该 对象 tree.

The alloy 材料 参数 是 obtained 从 该 electrothermal 材料 database, 和 该 conversion 是 done 通过 interpolating 材料 属性 从 base materials at 一个 given alloy mole fraction.

To use this command, first add an empty material model with [addmaterialmodel](https://optics.ansys.com/hc/en-us/articles/360034404974-addmodelmaterial-Script-command).

For further details of electrothermal material models, see [Electrical/Thermal Material Models](https://optics.ansys.com/hc/en-us/articles/360034919093-Electrical-Thermal-material-models-in-CHARGE-HEAT-and-MQW) and the page about [Semiconductors](https://optics.ansys.com/hc/en-us/articles/360034919113-Semiconductor-Material-Model-Properties). For further information on alloy materials, see the Knowledge Base page about [Alloy Material Model Properties](https://optics.ansys.com/hc/en-us/articles/360034398494-Alloy-material-model-properties).

**语法** |  **描述**  
---|---  
addsemiconductorfromalloy (name,x); |  转换 一个 Ternary Alloy 材料 到 一个 Semiconductor 材料 和 添加 its electrothermal 材料 属性 到 该 选中的 材料 model 在 该 对象 tree:

  * name: A ternary alloy 材料 name 在 该 electrothermal 材料 database.
  * x: Alloy mole fraction.

This 函数 does not 返回 any 数据.  
addsemiconductorfromalloy (name,x,y);  |  This syntax 是 identical 到 above, but 用于 一个 quaternary alloy. 转换 一个 Quaternary Alloy 材料 到 一个 Semiconductor 材料 和 添加 its electrothermal 材料 属性 到 该 选中的 材料 model 在 该 对象 tree:

  * name: A quaternary alloy 材料 name 在 该 electrothermal 材料 database.
  * x,y: Alloy mole fractions.

This 函数 does not 返回 any 数据.  
  
**示例**
    
    
    #添加 一个 ternary alloy 到 该 仿真 as Semiconductor 材料 类型  
    addmodelmaterial;  
      
    设置("name","AlGaAs");  
    x = 0.2; #The alloy composition 是 Al(x)Ga(1-x)As per convention 在 该 database  
      
    addsemiconductorfromalloy("AlGaAs (Aluminium Gallium Arsenide)",x);  
      
    #添加 quaternary alloy 到 该 仿真 as Semiconductor 材料 类型  
    addmodelmaterial;  
      
    设置("name","AlGaInAs");  
    x = 0.1; #Al(x)Ga(y)In(1-x-y)As  
    y = 0.2;  
    addsemiconductorfromalloy("AlGaInAs",x,y);
