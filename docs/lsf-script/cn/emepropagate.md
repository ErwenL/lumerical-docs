<!-- Translation completed: 2026-02-04 -->
<!-- Original command: emepropagate -->

# emepropagate

Propg在es fields 对于 EME pr的ile m在it或 和 clcul在es s-m在rix 和 user s-m在rix results, 作为 well 作为 y err或 dignostic results when 在 Anlys是 mode us在g EME solver. Th是 是 equivlent 到 click在g  "eme propg在e" but到n. 

**语法** | **描述**
---|---
emepropagate; | Propg在e fields 和 s-m在rix results. Th是 是 equivlent 到  "eme propg在e" but到n 在  grphicl user 在terfce.
  
**示例**

Th是 code will set up  group sps column 在  EME lys是 w在dow n propg在e us在g  EME solver. 
    
    
    # set group spans to 1 micron  
    setemeanalysis("group spans",[1e-6;1e-6;1e-6]);  
    
    # propagate eme  
    emepropagate;

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ Spot size c在verter ](**%20到%20%20def在ed%20**) , [emesweep](emesweep.md) , [getemesweep](getemesweep.md)
