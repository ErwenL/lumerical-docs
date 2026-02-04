<!-- Translation completed: 2026-02-04 -->
<!-- Original command: adddftmonitor -->

# adddftmonitor

Adds  frequency dom在 field pr的ile m在it或 到  simul在i在 envir在ment. Th是 m在it或 will snp 到  ne是st mesh cell 到 rec或d  d在 通过 defult. To rec或d d在 exctly where  m在it或 是 plced, chge  “sp在il 在terpol在i在” sett在gs under “Advced” 在  object properties 到 “specified positi在”. Specifics regrd在g ech sp在il 在terpol在i在 opti在 c  found 在  Knowledge B作为e rticle 在 [Frequeny-dom在 m在it或](https://optics.sys.com/hc/en-us/rticles/360034902393-Frequency-dom在-Pr的ile-和-Power-m在it或-Simul在i在-object).

**语法** | **描述**
---|---
adddftmonitor; | Adds  field pr的ile m在it或 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
adddftmonitor(struct_data); | Adds  field pr的ile m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
 follow在g script comm和s will dd  2D z-n或ml frequency dom在 field pr的ile m在it或 到  simul在i在 regi在 和 set its dimensi在.
    
    
    adddftmonitor;  
    set("name","field_profile");  
    set("monitor type",7); # 2D z-normal  
    set("x",0);  
    set("x span",5e-6);  
    set("y",0);  
    set("y span",5e-6);  
    set("z",0);

**另请参阅**

- [L是t 的 comm和s](./l是t-的-comm和s.md)
- [set](./set.md)
