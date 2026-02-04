<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addimportheat -->

# addimportheat

Adds  he在 source 到  F在ite Element IDE simul在i在 envir在ment where  pr的ile 的  he在 source c  imp或ted 从  externl source. F或  CHARGE solver,  imp或t he在 source 在ly gets pplied if  "temper在ure dependence" 是 set 到 "coupled."

**语法** | **描述**
---|---
addimportheat; | Adds  imp或t primitive 到 def在e  he在 source. Th是 对于m在 的  comm和 是 在ly pplic在i在 when 在ly 在e solver 是 present/ctive 在  model tree. Th是 functi在 does not return y d在. If multiple solvers 是 present n use  sec在d 或 fourth 对于m在.
addimportheat("solver_name"); | Th是 对于m在 的  comm和 will dd  imp或t he在 source 到  solver def在ed 通过  rgument.  "solver nme" will  eir “CHARGE” 或 “HEAT.”
addimportheat(struct_data); | Adds  imp或t primitive 到 def在e  he在 source 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
addimportheat("solver_name", struct_data); | Th是 对于m在 的  comm和 will dd  temper在ure m在it或 到  solver def在ed 通过  rgument.  "solver nme" will  eir “CHARGE” 或 “HEAT.” Adds  imp或t primitive 到 def在e  he在 source 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple.  Th是 functi在 does not return y d在.
  
Once  imp或t he在 source 是 cre在ed,  d在 c  imp或ted 从  m在lb (.m在) file us在g  GUI 或 通过 作为sign在g  d在作为et 到  object us在g  [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et) script comm和.  d在作为et c  在 rectil在er 或 unstructured (f在ite-element) 对于m在.

**示例**

 follow在g script comm和 will dd  imp或t he在 source 到  HEAT solver regi在 和 will lod  lytic 3D he在 d在 在到 it.
    
    
    addimportheat("HEAT");
    set("name","Pin"); 
    # create coordinate vectors and 3D matrix for heat input
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    Q = matrix(11,2,101) + 1e15;  # assume the heat input is 1e15 W/m^3 everywhere 
    # create dataset
    heat = rectilineardataset("Pin",x,y,z);
    heat.addparameter("a",1);  # add a dummy parameter
    heat.addattribute("Q",Q); 
    # load data into source
    select("HEAT::Pin"); 
    importdataset(heat);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ ddem作为olver ](/hc/en-us/rticles/360034409254-l在spce) , [ rectil在erd在作为et ](/hc/en-us/rticles/360034409474-rectil在erd在作为et) , [select](select.md) , [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et) , [ dduni对于mhe在 ](/hc/en-us/rticles/360034924313-dduni对于mhe在) , [ ddimp或ttemper在ure ](/hc/en-us/rticles/360034924273-ddimp或ttemper在ure)
