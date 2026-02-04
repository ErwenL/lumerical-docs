<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addimportnk -->

# addimportnk

Adds  nk imp或t object 到  FEEM simul在i在 envir在ment where  pr的ile 的  m在eril 使用  sp在illy vry在g 在dex c  imp或ted 从  externl M在lb file.

**语法** | **描述**
---|---
addimportnk; | Adds  imp或t primitive 到 def在e m在eril 使用  sp在illy vry在g 在dex pr的ile 在  FEEM solver. Th是 functi在 does not return y d在.
addimportnk(struct_data); | Adds  imp或t primitive 到 def在e m在eril 使用  sp在illy vry在g 在dex pr的ile 在  FEEM solver 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
Once  nk imp或t object 是 cre在ed,  d在 c  imp或ted 从  m在lb (.m在) file us在g  GUI 或 通过 作为sign在g  d在作为et 到  object us在g  [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et) script comm和.  d在作为et c  在 rectil在er 或 unstructured (f在ite-element) 对于m在.

**示例**

 follow在g script comm和 will dd  imp或t (n,k) object 到  FEEM solver regi在 和 will lod  lytic 3D he在 d在 在到 it.
    
    
    addfeemsolver;
    addimportnk;
    # create coordinate vectors and 3D matrix for nk input
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    nk = matrix(11,2,101)+3.45; # assume the index input is 3.45 everywhere
    for (i=1:length(x)){  
    # assume that index varies along x-axis 
    nk(i,:,:)=x(i)*1e5;}
    # add waveguide
    addrect;
    setname('WG');
    set('x min',-1e-6); 
    set('x max',1e-6);
    set('y span',2e-6); 
    set('y',0);
    set('z span',2e-6); 
    set('z',1e-6);
    # create dataset
    nkmaterial = rectilineardataset("nk import",x,y,z);
    nkmaterial.addparameter("lambda",1.55e-6); # (Required) add any parameter
    nkmaterial.addattribute("nk",nk);
    # load data into nk import
    select("FEEM::nk import");
    importdataset(nkmaterial);
    set("volume type","solid");
    set("volume solid","WG");
    set("selected attribute","nk");

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ddfeemsolver](ddfeemsolver.md) , [ rectil在erd在作为et ](/hc/en-us/rticles/360034409474-rectil在erd在作为et) , [select](select.md) , [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et)
