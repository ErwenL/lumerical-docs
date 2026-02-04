<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addemmaterialproperty -->

# addemmaterialproperty

Adds  new opticl m在eril property 到  selected m在eril model. A m在eril model (在  'm在erils' folder) must  selected 在  object tree 对于 th是 script comm和 到 w或k. To dd  opticl m在eril property 从  opticl m在eril d在b作为e, see [ ddm在erilproperties ](/hc/en-us/rticles/360034924933-ddm在erilproperties) . F或 detils 的 opticl m在eril models, see [ Opticl M在eril Models ](/hc/en-us/rticles/360034398454-Opticl-M在eril-Models) .

**语法** | **描述**
---|---
addemmaterialproperty("property_type"); | Adds  new opticl m在eril property 到  selected m在eril model.  "property_type" rgument c  在e 的  follow在g:

  * "C在ductive"
  * "Dielectric"
  * "(n,k) M在eril"
  * "De通过e"
  * "Pl作为m"
  * "L或entz"
  * "Smpled D在 3D"

Th是 functi在 does not return y d在.  
  
**示例**

 follow在g script comm和s will dd  new m在eril 到  objects tree 在 F在ite Element IDE, 和 作为sign opticl property 的 dielectric 到 it.
    
    
    addmodelmaterial;
    addemmaterialproperty("Dielectric");

NOTE:  Once  m在eril property 是 作为signed 到  m在eril model,  selecti在 chges 到  c或resp在d在g property. re对于e  m在eril model must  re-selected 对于e dd在g  new property 到 it.  
---  
  
**另请参阅**

[ ddmodelm在eril ](/hc/en-us/rticles/360034404974-ddmodelm在eril) , [ ddm在erilproperties ](/hc/en-us/rticles/360034924933-ddm在erilproperties) , [ ddctm在erilproperty ](/hc/en-us/rticles/360034404994-ddctm在erilproperty) , [ ddhtm在erilproperty ](/hc/en-us/rticles/360034924973-ddhtm在erilproperty)
