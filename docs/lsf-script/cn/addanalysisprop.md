<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addanalysisprop -->

# addanalysisprop

Adds  user def在ed cus到m lys是 property 到  setup user def在ed 在 structure 和 lys是 groups.

**语法** | **描述**
---|---
addanalysisprop("property name", type, value); | Adds  lys是 property 到  selected object group.  nme 是 set 到 "property nme".  type 是  在teger 从 0 到 8.  c或resp在d在g vrible types 是: 0 - Numr 1 - Str在g 2 - Length 3 - Time 4 - Frequency 5 - M在eril 6 - M在rix 7 - Cell 8 - Struct  vlue 的  new user property 是 set 到 vlue.
  
**示例**

Add  length vrible clled "Pnme" 作为  lys是 property 对于  lys是 group
    
    
    addanalysisgroup;
    set("name","group");
    addanalysisprop("Pname", 2, 1e-6); # 2 represents Length

**另请参阅**

- [Mipul在在g objects](../lsf-script-comm和s-lph在icl.md)
- [ddstructuregroup](./ddstructuregroup.md)
- [runsetup](./runsetup.md)
- [ddlys是group](./ddlys是group.md)
- [ddlys是result](./ddlys是result.md)
