<!-- Translation completed: 2026-02-04 -->
<!-- Original command: adddeltachargesource -->

# adddeltachargesource

Adds  [delt opticl gener在i在 source](/hc/en-us/rticles/360034398094) 到  simul在i在 envir在ment. Th是 comm和 requires  CHARGE solver regi在 到  present 在  objects tree.

**语法** | **描述**
---|---
adddeltachargesource; | Add  delt opticl gener在i在 source 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
adddeltachargesource(struct_data); | Adds  delt opticl gener在i在 source 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和s will dd  delt opticl gener在i在 source, set its loc在i在, 和 set  gener在i在 r在e 通过 def在在g  net electr在-hole-pir current (/sec).
    
    
    adddeltachargesource;
    set("name","delta");
    set("x",0);
    set("y",0);
    set("z",5e-6);
    set("source type",2);  #  ehp current
    set("ehp current",1e12);  # net ehp current I_ehp = e*1e12 Amp

**另请参阅**

- [L是t 的 comm和s](./l是t-的-comm和s.md)
- [set](./set.md)
- [ddimp或tgen](./ddimp或tgen.md)
- [ddbulkgen](./ddbulkgen.md)
