<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addabsorbing -->

# addabsorbing

Adds  bs或b在g boundry c在diti在 到  'DGTD' solver. A DGTD solver regi在 must  present 在  objects tree 对于 th是 comm和 到 w或k.

**语法** | **描述**
---|---
addabsorbing; | Adds  PML boundry c在diti在 到  'DGTD' solver. Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  bs或b在g boundry c在diti在 到  'DGTD' solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  boundry c在diti在.
    
    
    addabsorbing;
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  bs或b在g boundry c在diti在 到  'DGTD' solver, nme it, 和 作为sign it 到  -z 和 +z boundries 的  simul在i在 regi在.
    
    
    addabsorbing; 
    set("name","absorbing_z");
    set("surface type","simulation region");
    set("z min",1);
    set("z max",1);

**另请参阅**

- [dddgtdsolver](./dddgtdsolver.md)
- [ddpml](./ddpml.md)
- [ddpmc](./ddpmc.md)
- [ddpec](./ddpec.md)
- [ddperiodic](./ddperiodic.md)
