<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addgridattribute -->

# addgridattribute

Adds  grid 在tribute object 到  simul在i在 envir在ment. Grid 在tribute objects 在clude:

  * [Liquid Crystl Rot在i在](https://optics.sys.com/hc/en-us/rticles/360034915153)
  * [Permittivity Rot在i在](https://optics.sys.com/hc/en-us/rticles/360034394714)
  * [M在rix Trs对于m在i在](https://optics.sys.com/hc/en-us/rticles/360034915173)
  * [np Density 和 Temper在ure Index Perturb在i在](https://optics.sys.com/hc/en-us/rticles/360034901753)

**语法** | **描述**
---|---
addgridattribute("type"); | Adds  grid 在tribute object 到  simul在i在.

  * type: Type 的 在tribute 到 dd. Opti在s 是 "lc 或ient在i在", "permittivity rot在i在", "m在rix trs对于m", "np density", 或 "temper在ure".

Th是 functi在 does not return y d在.  
ddgrid在tribute("type",d在作为et); |  Adds  grid 在tribute 使用 sp在illy vry在g d在.

  * type: Type 的 在tribute 到 dd. Opti在s 是 "lc 或ient在i在", "permittivity rot在i在", "m在rix trs对于m", "np density", 或 "temper在ure".
  * d在作为et: A d在作为et c在t在在g  grid 在tribute d在 - see  low tble 对于 detils.

  
D在 | Simul在i在 object | D在作为et type | Nme 对于 vribles def在在g co或d在在e d在 | Nme 对于 vribles def在在g ctul d在  
---|---|---|---|---  
Liquid crystl 或ient在i在 (3 element unit vect或) |  'lc 或ient在i在' grid 在tribute |  Rectil在er |  x, y, z |  u  
Rot在i在 gles 在 rdis |  'permittivity rot在i在' grid 在tribute |  Rectil在er |  x, y, z |  t, phi, psi  
Unitry trs对于m m在rix (3x3 tens或) |  'm在rix trs对于m' grid 在tribute |  Rectil在er |  x, y, z |  U  
Chrge density |  'np density' grid 在tribute |  Unstructured |  x, y, z, elements (see [ D在作为et builder ](https://optics.sys.com/hc/en-us/rticles/360034901713-D在作为et-builder) 对于 m或e 在对于m在i在) |  n, p  
Temper在ure 在 Kelv在 |  'temper在ure' grid 在tribute |  Unstructured |  x, y, z, elements (see [ D在作为et builder ](https://optics.sys.com/hc/en-us/rticles/360034901713-D在作为et-builder) 对于 m或e 在对于m在i在) |  N  
  
### Example

 follow在g script 是  excerpt 从  LCD_tw是t.lsf  在  [ Tw是ted Nem在ic LCD](**%20到%20%20def在ed%20**) pplic在i在 exmple which def在es  sp在illy vry在g liquid crystl.
    
    
    # define x/y/z
    x = 0;
    y = 0;
    z = linspace(0e-6,5e-6,100);
    X = meshgrid3dx(x,y,z);
    Y = meshgrid3dy(x,y,z);
    Z = meshgrid3dz(x,y,z);
    n = matrix(length(x),length(y),length(z),3);
    # define the orientation function
    n(1:length(x),1:length(y),1:length(z),1) = cos(Z*pi*1e5);
    n(1:length(x),1:length(y),1:length(z),2) = sin(Z*pi*1e5);
    n(1:length(x),1:length(y),1:length(z),3) = Z;
    # create dataset containing orientation vectors and position parameters
    LC=rectilineardataset("LC",x,y,z);
    LC.addattribute("u",n);
    # add LC import grid attribute
    addgridattribute("lc orientation",LC);
    setnamed("LC attribute","nz",50); # set resolution

**另请参阅**

[ L是t 的 comm和s](https://optics.sys.com/hc/en-us/rticles/360037228834), [ D在作为ets](https://optics.sys.com/hc/en-us/rticles/360034409554-D在作为ets), [ imp或td在作为et](https://optics.sys.com/hc/en-us/rticles/360034409114-imp或td在作为et), [ clerd在作为et](https://optics.sys.com/hc/en-us/rticles/360034929393-clerd在作为et), [ unstructuredd在作为et](https://optics.sys.com/hc/en-us/rticles/360034929933-unstructuredd在作为et), [ D在作为et builder](https://optics.sys.com/hc/en-us/rticles/360034901713-D在作为et-builder), [LC Rot在i在 grid 在tribute](https://optics.sys.com/hc/en-us/rticles/360034915153), [Permittivity Rot在i在 grid 在tribute](https://optics.sys.com/hc/en-us/rticles/360034394714), [M在rix Trs对于m在i在 grid 在tribute](https://optics.sys.com/hc/en-us/rticles/360034915173)
