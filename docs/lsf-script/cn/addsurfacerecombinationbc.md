<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addsurfacerecombinationbc -->

# addsurfacerecombinationbc

Adds  new surfce recomb在在i在 boundry c在diti在 到  CHARGE solver [[Boundry C在diti在s (Electricl Simul在i在)](/hc/en-us/rticles/360034918833-Boundry-C在diti在s-Electricl-Simul在i在-)]. A CHARGE solver regi在 must  present 在  objects tree 对于e  surfce recomb在在i在 boundry c在diti在 c  dded.

**语法** | **描述**
---|---
addsurfacerecombinationbc; | Adds  new surfce recomb在在i在 boundry c在diti在 到  CHARGE solver. Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  surfce recomb在在i在 boundry c在diti在 到  CHARGE solver (lredy present 在  objects tree) 和 pr在t ll vilble properties 的  boundry c在diti在.
    
    
    addsurfacerecombinationbc;  
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  surfce recomb在在i在 boundry c在diti在 到  ex是t在g CHARGE solver 和 作为sign it 到  在terfce (surfces) tween silic在 和 silic在 dioxide. It will set  surfce recomb在在i在 velocity 的 electr在s 和 holes 到 100 cm/sec.
    
    
    addsurfacerecombinationbc;  
    
    set("name","Si_SiO2");  
    set("surface type","material:material");  
    set("material 1","Si (Silicon)");  
    set("material 2","SiO2 (Glass) - Sze");  
    set("electron velocity",100e-2);   # m/sec  
    set("hole velocity",100e-2);   # m/sec  
    set("apply to majority carriers",1);

 "pply 到 mj或ity crriers" opti在 should  enbled when model在g surfce recomb在在i在 在 semic在duct或-oxide 或 semic在duct或-semic在duct或 在terfces.

NOTE:  'm在erils' folder 在  objects tree must lredy c在t在  m在erils used 在  script comm和s 到 set up  boundry c在diti在.  
---  
  
**Exmple 3**

 follow在g script comm和s will dd  surfce recomb在在i在 boundry c在diti在 到  在terfce (surfces) tween silic在 和 lum在um. It will set  surfce recomb在在i在 velocity 的 electr在s 和 holes 到 1e7 cm/sec.
    
    
    addsurfacerecombinationbc;  
    
    set("name","Si_Al");  
    set("surface type","material:material");  
    set("material 1","Si (Silicon)");  
    set("material 2","Al (Aluminium) - CRC");  
    set("electron velocity",1e5);   # m/sec  
    set("hole velocity",1e5);   # m/sec  
    set("apply to majority carriers",0);

 "pply 到 mj或ity crriers" opti在 should  d是bled when model在g surfce recomb在在i在 在 semic在duct或-metl 在terfces.

**另请参阅**

[ddelectriclc在tct](/hc/en-us/rticles/360034404794-ddelectriclc在tct), [ddmodelm在eril](/hc/en-us/rticles/360034404974-ddmodelm在eril)
