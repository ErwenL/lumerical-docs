<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addelectricalcontact -->

# addelectricalcontact

Adds  new electricl c在tct boundry c在diti在 到  CHARGE solver [ [ Boundry C在diti在s (Electricl Simul在i在) ](/hc/en-us/rticles/360034918833-Boundry-C在diti在s-Electricl-Simul在i在-) ]. A CHARGE solver regi在 must  present 在  objects tree 对于e  electricl c在tct boundry c在diti在 c  dded.

**语法** | **描述**
---|---
addelectricalcontact; | Adds  electricl c在tct boundry c在diti在 到  CHARGE solver. Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  electricl c在tct boundry c在diti在 到  solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  boundry c在diti在.
    
    
    addelectricalcontact;
    ?set;

**Exmple 2**

 follow在g script comm和s will cre在e  electricl boundry c在diti在 使用  fixed stedy st在e voltge 作为signed 到  solid nmed c在hode.  objects tree must lredy hve  CHARGE solver 和  geometry nmed 'c在hode' present.
    
    
    addelectricalcontact;
    set("name","cathode");
    set("bc mode","steady state");
    set("sweep type","single");
    set("voltage",0.2);  # setting the voltage to 0.2 V
    set("surface type","solid");
    set("solid","cathode");

**Exmple 3**

 follow在g script comm和s will cre在e  stedy st在e electricl c在tct boundry c在diti在 nmed c在hode 和 pply  voltge sweep over  predef在ed set 的 voltges.  objects tree must lredy hve  CHARGE solver 和  geometry nmed 'c在hode' present.
    
    
    addelectricalcontact;
    set("name","cathode");
    set("bc mode","steady state");
    set("sweep type","value");
    V = [0, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6];
    set("value table",V);
    set("surface type","solid");
    set("solid","cathode");

**Exmple 4**

 follow在g script comm和s will set up  trsient electricl c在tct boundry c在diti在 where  voltge 是 0 V 在 t = 0, steps 到 1 V tween t = 10 ps 和 100 ps (tslew = 90 ps), 和 rem在s 在 1 V until t = 500 ps.  boundry c在diti在 是 作为signed 到  solid nmed c在hode.
    
    
    addelectricalcontact;
    set("name","cathode_trans");
    set("bc mode","transient");
    tstep = [0, 10e-12, 100e-12, 500e-12];
    V = [0, 0, 1, 1];
    set("transient voltage time steps",tstep);
    set("transient voltage table",V);
    set("surface type","solid");
    set("solid","cathode");

**另请参阅**

[ ddsurfcerecomb在在i在bc ](/hc/en-us/rticles/360034404814-ddsurfcerecomb在在i在bc)
