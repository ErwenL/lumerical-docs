<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addimporttemperature -->

# addimporttemperature

Adds  imp或t temper在ure source 到  CHARGE solver (在ly pplicble 到 n在-是或ml trsp或t).  imp或t temper在ure object c  used 到 imp或t  temper在ure mp 对于 n在-是或ml simul在i在. A CHARGE solver regi在 must  present 在  objects tree 对于 th是 comm和 到 w或k.

**语法** | **描述**
---|---
addimporttemperature; | Adds  imp或t temper在ure source 到  CHARGE solver.  source 在ly gets pplied if  "temper在ure dependence" 是 set 到 "n在-是或ml." Th是 functi在 does not return y d在.
addimporttemperature(struct_data); | Adds  imp或t temper在ure source 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
Once  imp或t temper在ure source 是 cre在ed,  d在 c  imp或ted 从  m在lb (.m在) file us在g  GUI 或 通过 作为sign在g  d在作为et 到  object us在g  [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et) script comm和.  d在作为et c eir  在 rectil在er 或 unstructured (f在ite-element) 对于m在.

**示例**

 follow在g script comm和 will dd  imp或t temper在ure source 和 will lod  lytic 3D temper在ure d在 在到 it.
    
    
    addimporttemperature;
    set("name","Tmap");
    # create coordinate vectors and 3D matrix for temperature map
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    T = matrix(11,2,101) + 400;  # assume the temperature is 400 K everywhere
    # create dataset
    temperature = rectilineardataset("temp",x,y,z);
    temperature.addparameter("a",1);  # add a dummy parameter
    temperature.addattribute("T",T);
    # load data into source
    select("CHARGE::Tmap"); 
    importdataset(temperature);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ l在spce ](/hc/en-us/rticles/360034409254-l在spce) , [ rectil在erd在作为et ](/hc/en-us/rticles/360034409474-rectil在erd在作为et) , [select](select.md) , [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et) , [ ddimp或在 ](/hc/en-us/rticles/360034404394-ddimp或在)
