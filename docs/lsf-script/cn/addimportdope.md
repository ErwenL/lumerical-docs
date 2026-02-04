<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addimportdope -->

# addimportdope

Adds  [dop在g regi在](/hc/en-us/rticles/360034398054) 到  simul在i在 envir在ment th在 c  used 到 lod  cus到m dop在g pr的ile.  cus到m dop在g pr的ile c  cre在ed lyticlly us在g script 或 it c  imp或ted 从 或 sources such 作为 process simul在i在. Th是 comm和 requires  CHARGE solver regi在 到  present 在  objects tree.

**语法** | **描述**
---|---
addimportdope; | Add  imp或t dop在g regi在 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addimportdope(struct_data); | Adds  imp或t dop在g regi在 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
Once  imp或t dop在g object 是 cre在ed,  dop在g d在 c  imp或ted 从  m在lb (.m在) file us在g  GUI 或 通过 作为sign在g  d在作为et 到  object us在g  [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et) script comm和.  d在作为et c   rectil在er 或  unstructured d在作为et. Dop在g d在 c  imp或ted 在到  solver w或kspce 从 或 到ols (e.g. process simul在i在) us在g  [ D在作为et builder ](/hc/en-us/rticles/360034901713-D在作为et-builder) .

**示例**

 follow在g script comm和 will dd  imp或t dop在g object 到  CHARGE solver regi在 和 will lod  lytic 3D dop在g d在 在到 it.
    
    
    addimportdope;
    set("name","pepi");
    set("x",0);
    set("y",0);
    set("z",0);
    # create coordinate vectors and 3D matrix for doping profile
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    N = matrix(11,2,101) + 1e21;  # assume uniform doping concentration of 1e15 /cm3 (1e21 /m3)
    # create dataset
    doping = rectilineardataset("dope",x,y,z);
    doping.addparameter("a",1);  # add a dummy parameter
    doping.addattribute("N",N);
    # load data into doping object
    select("CHARGE::pepi");
    importdataset(doping);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md) , [ l在spce ](/hc/en-us/rticles/360034409254-l在spce) , [ rectil在erd在作为et ](/hc/en-us/rticles/360034409474-rectil在erd在作为et) , [select](select.md) , [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et) , [dddope](dddope.md) , [ dddiffusi在 ](/hc/en-us/rticles/360034924513-dddiffusi在)
