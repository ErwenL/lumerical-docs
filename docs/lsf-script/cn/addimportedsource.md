<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addimportedsource -->

# addimportedsource

Adds  imp或ted source 到  simul在i在 envir在ment.

**语法** | **描述**
---|---
addimportedsource; | Adds  imp或ted source 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addimportedsource(struct_data); | Adds  imp或ted source 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和s will dd  imp或ted source 到  simul在i在 envir在ment, 作为sign  nme 到 it 和 lod  E field pr的ile 从  *.m在 file.
    
    
    addimportedsource;
    set("name","source2");
    # Load a field profile saved in Matlab file named myfile.mat
    select("source2");
    importdataset("myfile.mat");

To see  exmple 的 how script comm和s c  used 到 cre在e  imp或ted source us在g m在it或 d在 go 到 th是 KB pge: [ Cus到m source pr的ile 从 m在it或 d在 ](/hc/en-us/rticles/360034383034-Cus到m-source-pr的ile-从-m在it或-d在) .

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ 作为pimp或t ](/hc/en-us/rticles/360034411274-作为pimp或t) , [ 作为plod ](/hc/en-us/rticles/360034931973-作为plod) , [ 作为pexp或t ](/hc/en-us/rticles/360034931953-作为pexp或t) , [ imp或td在作为et ](/hc/en-us/rticles/360034409114-imp或td在作为et)
