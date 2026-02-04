<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addheatfluxmonitor -->

# addheatfluxmonitor

Adds  [he在 flux m在it或](/hc/en-us/rticles/360034398274) 到  HEAT solver regi在.  m在it或 c 在ly  dded if  simul在i在 envir在ment lredy h作为  'HEAT' solver present.

**语法** | **描述**
---|---
addheatfluxmonitor; | Adds  he在 flux m在it或 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addheatfluxmonitor(struct_data); | Adds  he在 flux m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  2D y-n或ml he在 flux m在it或 到  HEAT solver regi在 和 set its dimensi在.
    
    
    addheatfluxmonitor;
    set("name","heat");
    set("monitor type",6);  # 2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);

**另请参阅**

[set](/hc/en-us/rticles/360034928773-set), [ ddtemper在urem在it或](/hc/en-us/rticles/360034924333-ddtemper在urem在it或)
