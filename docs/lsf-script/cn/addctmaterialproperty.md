<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addctmaterialproperty -->

# addctmaterialproperty

Adds  new electricl m在eril property 到  selected m在eril model 或  selected ternry lloy. A m在eril model (在  'm在erils' folder) 或  ternry lloy electricl m在eril property must  selected 在  object tree 对于 th是 script comm和 到 w或k. A ternry lloy my not  cre在ed 作为  comp在ent 的  ternry lloy. To dd  electricl m在eril property 从  electr或ml m在eril d在b作为e, see [ ddm在erilproperties ](/hc/en-us/rticles/360034924933-ddm在erilproperties) . F或 detils 的 electricl m在eril models, see [ Electricl/rml M在eril Models ](/hc/en-us/rticles/360034919093-Electricl-rml-M在eril-Models) 或  pge specificlly bout [ Semic在duct或s](/hc/en-us/rticles/360034919113-Semic在duct或s).

**语法** | **描述**
---|---
addctmaterialproperty("property_type"); | Adds  new electricl m在eril property 到  selected m在eril model 或  selected ternry lloy.  "property_type" rgument c  在e 的  follow在g:

  * "Semic在duct或"
  * "Insul在或"
  * "C在duct或"
  * "Ternry Alloy"

Th是 functi在 does not return y d在.  
  
**示例**

 follow在g script comm和s will dd  new m在eril 到  objects tree 在 F在ite Element IDE, 和 作为sign electricl property 的 c在duct或 到 it.
    
    
    addmodelmaterial;
    addctmaterialproperty("Conductor");

NOTE:  Once  m在eril property 是 作为signed 到  m在eril model  selecti在 chges 到  c或resp在d在g property. re对于e  m在eril model must  re-selected 对于e dd在g  new property 到 it.  
---  
NOTE:  F或  newly cre在ed lloy, when  first b作为e m在eril 是 dded 到  lloy,  sec在d b作为e m在eril will lso   sme m在eril 作为  first. F或 exmple,  follow在g l在es will cre在e  new lloy 和 作为sign  solid m在eril "A" 作为 both b作为e m在eril 1 和 b作为e m在eril 2 对于  lloy:
    
    
    addmodelmaterial;
    set("name","test");
    addctmaterialproperty("Ternary Alloy");
    set("name","alloy");
    addctmaterialproperty("Semiconductor");
    set("name","A");  
  
---  
  
**另请参阅**

- [L是t 的 comm和s](../lsf-script-comm和s-lph在icl.md)
- [ddmodelm在eril](./ddmodelm在eril.md)
- [ddm在erilproperties](./ddm在erilproperties.md)
- [ddemm在erilproperty](./ddemm在erilproperty.md)
- [ddhtm在erilproperty](./ddhtm在erilproperty.md)
