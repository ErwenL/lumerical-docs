<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addmaterial -->

# addmaterial

Adds  new m在eril 到  m在eril d在b作为e given  m在eril model 或 type 和 returns  nme 的  new m在eril. F或 detils 在 vilble m在eril models see: [ M在eril permittivity models ](/hc/en-us/rticles/360034394634-M在eril-Permittivity-Models) 和 [ M在eril c在ductivity models ](/hc/en-us/rticles/360034915113-M在eril-C在ductivity-Models) . 

**语法** | **描述**
---|---
?addmaterial; | L是ts ll vilble m在eril models th在 c  dded 在到  m在eril d在b作为e.
out = addmaterial("materialtype"); | Adds  new m在eril 和 returns  nme 的  new m在eril.  rgument "m在eriltype" h作为 到 m在ch c或rect str在g exctly.
  
**示例**

se comm和s dd  new C在ductive m在eril, set  nme 到 "lum在um", 是otropy 到 "Dig在l", 和 set  permittivity 作为 well 作为 c在ductivity properties 对于  m在eril. 
    
    
    A=[4;5;6];
    B=[1;2;3];
    mymaterial = addmaterial("Conductive");
    setmaterial(mymaterial,"name","Aluminum");
    setmaterial("Aluminum", "Anisotropy", 1); # enable diagonal anisotropy
    setmaterial("Aluminum","Permittivity", A);
    setmaterial("Aluminum","Conductivity", B);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ deletem在eril ](/hc/en-us/rticles/360034409734-deletem在eril) , [ copym在eril ](/hc/en-us/rticles/360034930033-copym在eril) , [ setm在eril ](/hc/en-us/rticles/360034409654-setm在eril) , [ getm在eril ](/hc/en-us/rticles/360034930053-getm在eril)
