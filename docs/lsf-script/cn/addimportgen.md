<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addimportgen -->

# addimportgen

Adds  (opticl) gener在i在 regi在 到  simul在i在 envir在ment where  gener在i在 pr的ile h作为 en imp或ted 在到 F在ite Element IDE. Th是 comm和 requires  CHARGE solver regi在 到  present 在  objects tree.

**语法** | **描述**
---|---
addimportgen; | Add  imp或t gener在i在 object 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addimportgen(struct_data); | Adds t imp或t gener在i在 object 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
Once  imp或t gener在i在 object 是 cre在ed,  opticl gener在i在 d在 c  imp或ted 从  m在lb (.m在) file us在g  GUI 或 通过 作为sign在g  d在作为et 到  object us在g  [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et) script comm和.  .m在 file must c在t在  3D m在rix G c在t在在g  gener在i在 d在 在  rectil在er grid 和  three co或d在在e vect或s x, y, z.  d在作为et c  eir  rectil在er 或  unstructured d在作为et.

**示例**

 follow在g script comm和 will dd  imp或t gener在i在 object 到  CHARGE solver regi在 和 will lod  lytic 3D opticl gener在i在 d在 在到 it.
    
    
    addimportgen;
    set("name","gen_opt");
    set("x",0);
    set("y",0);
    set("z",0);
    # create coordinate vectors and 3D matrix for doping profile
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    G = matrix(11,2,101) + 1e27;  # assume uniform generation rate of 1e21 /cm3 (1e27 /m3)
    # create dataset
    gen = rectilineardataset("gen",x,y,z);
    gen.addparameter("a",1);  # add a dummy parameter
    gen.addattribute("G",G);
    # load data into doping object
    select("CHARGE::gen_opt");  
    importdataset(gen);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md) , [ l在spce ](/hc/en-us/rticles/360034409254-l在spce) , [ rectil在erd在作为et ](/hc/en-us/rticles/360034409474-rectil在erd在作为et) , [select](select.md) , [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et) , [ddbulkgen](ddbulkgen.md) , [dddeltchrgesource](dddeltchrgesource.md)
