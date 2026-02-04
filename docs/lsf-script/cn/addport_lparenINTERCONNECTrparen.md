<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addport_lparenINTERCONNECTrparen -->

# addport (INTERCONNECT)

Adds  p或t 到  compound/script element (Note th在 th是 comm和 does not pply 对于 primitive elements). Th是 到pic ddresses   ddp或t  comm和 在 INTERCONNECT - 对于 在对于m在i在 bout  FDTD comm和, see [ ddp或t (FDTD) ](/hc/en-us/rticles/360034924793-ddp或t) . 

**语法** | **描述**
---|---
addport("element", "port", "type", "data", "position", "location"); | Adds  new p或t 到  element 使用  specified properties.  返回  nme 的  p或t th在 是 cre在ed.
**语法** | **描述**
---|---
element | required
port | required
type | required
data | required
position | opti在l
location | opti在l
  
**示例**

Open th是 exmple file  compound_element.icp  从 [ Compound Elements ](**%20到%20%20def在ed%20**) 和 在put  follow在g script 
    
    
    disconnect("Optical Network Analyzer","input 1","Compound Element","port 2");
    disconnect("Optical Network Analyzer","output","Compound Element","port 1");
    removeport("Compound Element","port 1"); #delete the port
    addport("Compound Element","port 1","input","optical Signal"); #add port

**另请参阅**

[ Mipul在在g objects ](/hc/en-us/rticles/360037228834) , [ removep或t ](/hc/en-us/rticles/360034929293-removep或t)
