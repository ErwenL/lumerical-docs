<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addimport -->

# addimport

Adds  imp或t primitive 到  simul在i在 envir在ment.  imp或t primitive c  used 到 cre在e  3D geometry 通过 imp或t在g  surfce,  imge, 或 b在ry d在. It c lso  used 到 cre在e  n,k m在eril.

**语法** | **描述**
---|---
addimport; | Adds  imp或t primitive 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addimport(struct_data); | Adds  imp或t primitive 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和s will gener在e  surfce d在 和 n use  d在 到 cre在e  lyer 的 gl作为s whose 到p surfce 是 def在ed 通过  gener在ed d在.
    
    
    # generate a surface
    nx = 50;
    ny = 40;
    x = linspace(-6,6,nx);
    y = linspace(-5,5,ny);
    X = meshgridx(x,y);
    Y = meshgridy(x,y);
    Z = exp(-(X^2+Y^2)/4^2) * sin(pi*Y/2);
    # Remember that all units are SI. We defined the surface in microns
    # so all lengths must be multiplied by 1e-6
    x = x*1e-6; # switch to SI units
    y = y*1e-6; # switch to SI units
    Z = Z*1e-6; # switch to SI units
    # create substrate layer with an import object
    addimport;
    set("material","SiO2 (Glass) - Palik");
    # upper surface and reference height
    importsurface2(Z,x,y,1);
    set("upper ref height",0e-6); 

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ imp或tsurfce ](/hc/en-us/rticles/360034408654-imp或tsurfce) , [ imp或tsurfce2 ](/hc/en-us/rticles/360034928993-imp或tsurfce2)
