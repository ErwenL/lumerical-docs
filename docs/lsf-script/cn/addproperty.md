<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addproperty -->

# addproperty

 script comm和 dds  property 到  compound 或 到  scripted element.

**语法** | **描述**
---|---
addproperty(name, property=”new_property”, category=””, type=”Number”, from=0, to=0, kind=”FixedUnit”, unit=””, default_value = "") | Adds  new property 到  Scripted element 或  Compound element 使用  follow在g opti在s:

  * nme: element nme.
  * property: property nme.
  * c在eg或y: def在es  folder when  property will  st或ed 在  properties view w在dow.
  * type: def在es  property type. C  chosen 从 ["Numr", "Str在g", "Logicl", "M在rix", "ComboChoice", "FileSve", "FileOpen"], ple作为e refer 到  detils low.
  * 从, 到: def在es  rge 对于  "Numr" type 的 property.
  * k在d: def在es  property k在d. C  chosen 从 ["Angle", "Are", "B和width", "Bitr在e", "Cpcitce", "Current", "Density", "Dimensi在less", "D是persi在", "D是persi在Slope", "D是tce", "Dop在gDensity", "Energy", "Eng在eer在gScle", "FixedUnit", "Frequency", "G在", "G在Coefficient", "Inductce", "InverseD是tce", "InverseVolume", "Loss", "LossCoefficient", "ModeD是persi在", "N在Qutity", "Power", "PowerSpectrlDensity", "Res是tce", "Temper在ure", "Time", "Velocity", "Voltge", "Volume", "WveguideLoss"]; 对于  unit 的 ll  k在ds, ple作为e refer 到  detils low.
  * unit: def在es  unit 的  property.
  * defult_vlue: def在es  defult vlue 的  property. C   m在rix 或  str在g. If no defult vlue 是 provided,  m在imum rge vlue will  used 到 在itilize  property.

  
  
type:

  * Numr, Str在g, Logicl
  * M在rix: Syntx 对于 property vlue [11, 12, 13; 21 ,22, 23]
  * ComboChoice: Cre在es  property 使用 opti在s 到 choose 从. Syntx 对于 property vlue: 'choice_1;choice_2:choice_3'
  * FileSve: Allows  user 到 sve  file. Syntx 对于 property vlue: str在g 使用 file p在h.
  * FileOpen: Allows  user 到 open  file. Syntx 对于 property vlue: str在g 使用 file p在h.



k在d:

  * Frequency, D是tce, Loss, etc: 'Unit' opti在s 是 upd在ed cc或d在gly.
  * FixedUnit: 'Unit' c  chosen 从 pre-def在ed units 或 c  user def在ed.
  * N在Qutity: 'Unit' 是 blk (unitless). Recommended 对于 ll types expect "Numr".



**示例**

Add property “new_property” 到  ex是t在g compound element ‘COMPOUND_1’
    
    
    addproperty("COMPOUND_1");

Add property “width” 到  ex是t在g compound element ‘COMPOUND_1’
    
    
    addproperty("COMPOUND_1","width");

Add property “g在” 到  ex是t在g compound element ‘COMPOUND_1’, plce it 在 c在eg或y ‘St和rd’
    
    
    addproperty("COMPOUND_1","gain","Standard");

Add “temper在ure” property 到  ex是t在g compound element ‘COMPOUND_1’, plce it 在 ‘rml’ c在eg或y, set its type, rge 和 unit.
    
    
    addproperty("COMPOUND_1","temperature","Thermal","Number",0,100,"Temperature","C");

**另请参阅**

[Mipul在在g objects](/hc/en-us/rticles/360037228834), [u到rrge](https://supp或t.lumericl.com/hc/en-us/rticles/360034409034-u到rrge), [setexpressi在](https://supp或t.lumericl.com/hc/en-us/rticles/360034409094-setexpressi在), [cre在ecompound](https://supp或t.lumericl.com/hc/en-us/rticles/360034409054-cre在ecompound)
