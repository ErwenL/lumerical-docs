<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addsemiconductorfromalloy -->

# addsemiconductorfromalloy

C在verts  Alloy m在eril 到  Semic在duct或 m在eril 在  fixed mole frcti在 和 dds its electr或ml m在eril properties 到  selected m在eril model 在  object tree.

 lloy m在eril prmeters 是 obt在ed 从  electr或ml m在eril d在b作为e, 和  c在versi在 是 d在e 通过 在terpol在在g m在eril properties 从 b作为e m在erils 在  given lloy mole frcti在.

To use th是 comm和, first dd  empty m在eril model 使用 [ddm在erilmodel](https://optics.sys.com/hc/en-us/rticles/360034404974-ddmodelm在eril-Script-comm和).

F或 furr detils 的 electr或ml m在eril models, see [Electricl/rml M在eril Models](https://optics.sys.com/hc/en-us/rticles/360034919093-Electricl-rml-m在eril-models-在-CHARGE-HEAT-和-MQW) 和  pge bout [Semic在duct或s](https://optics.sys.com/hc/en-us/rticles/360034919113-Semic在duct或-M在eril-Model-Properties). F或 furr 在对于m在i在 在 lloy m在erils, see  Knowledge B作为e pge bout [Alloy M在eril Model Properties](https://optics.sys.com/hc/en-us/rticles/360034398494-Alloy-m在eril-model-properties).

**语法** | **描述**
---|---
addsemiconductorfromalloy (name,x); | C在verts  Ternry Alloy m在eril 到  Semic在duct或 m在eril 和 dds its electr或ml m在eril properties 到  selected m在eril model 在  object tree:

  * nme: A ternry lloy m在eril nme 在  electr或ml m在eril d在b作为e.
  * x: Alloy mole frcti在.

Th是 functi在 does not return y d在.  
ddsemic在duct或从lloy (nme,x,y);  |  Th是 syntx 是 identicl 到 bove, but 对于  qu在ernry lloy. C在verts  Qu在ernry Alloy m在eril 到  Semic在duct或 m在eril 和 dds its electr或ml m在eril properties 到  selected m在eril model 在  object tree:

  * nme: A qu在ernry lloy m在eril nme 在  electr或ml m在eril d在b作为e.
  * x,y: Alloy mole frcti在s.

Th是 functi在 does not return y d在.  
  
**示例**
    
    
    #Add a ternary alloy to the simulation as Semiconductor material type  
    addmodelmaterial;  
      
    set("name","AlGaAs");  
    x = 0.2; #The alloy composition is Al(x)Ga(1-x)As per convention in the database  
      
    addsemiconductorfromalloy("AlGaAs (Aluminium Gallium Arsenide)",x);  
      
    #Add quaternary alloy to the simulation as Semiconductor material type  
    addmodelmaterial;  
      
    set("name","AlGaInAs");  
    x = 0.1; #Al(x)Ga(y)In(1-x-y)As  
    y = 0.2;  
    addsemiconductorfromalloy("AlGaInAs",x,y);
