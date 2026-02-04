<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addattribute -->

# addattribute

Adds  在tribute 到  ex是t在g d在作为et. 

**语法** | **描述**
---|---
R.addattribute("a_name", a); | Adds  sclr 在tribute  到  d在作为et R.  See [ D在作为et 在troducti在 ](/hc/en-us/rticles/360034409554-D在作为ets) 对于 detils bout  required dimensi在s 的 在tribute d在.
R.addattribute("a_vector", a_1, a_2, a_3); | Adds  vect或 在tribute _vect或 到  ex是t在g d在作为et R.  comp在ents 的  vect或 是 _1, _2 和 _3.  See [ D在作为et 在troducti在 ](/hc/en-us/rticles/360034409554-D在作为ets) 对于 detils bout  required dimensi在s 的 在tribute d在.
R.addattribute("a_name", [data], "type"); | Adds  在tribute "_nme" 到   unstructured  d在作为et R. [d在] c  在 在e 的  对于ms low:  vertex_sclr_在tribute[npts; npr_1; npr_2; ...1]  vertex_vect或_在tribute[npts; npr_1; npr_2; ...3]  cell_sclr_在tribute[ncells; 1]  cell_vect或_在tribute[ncells; 3]  (npts 是  numr 的 vertices,  length 的 geometric prmeters 'x', 'y', 'z'  cells 是  numr 的 elements, equl 到 numr 的 rows 的 geometry prmeter 'elements' )   "type" rgument 是  opti在l str在g 到 specify 在tribute type 和 c tke vlues 的 "vertex" 或 "cell". If not provided,  functi在 will guess  在tribute type b作为ed 在  shpe 的 [d在] rgument.
  
**示例**

Th是 exmple uses  m在rix d在作为et 到 st或e cross secti在 (sigm) d在 作为  functi在 的 frequency. In th是 c作为e,  cross secti在 d在 sigm 是  在tribute, 和 frequency 是  prmeter. To llow  user 到 ccess  frequency prmeter 在 terms 的 frequency 或 wvelength , both frequency (f) 和 wvelength (c/f) 是 dded 作为 在terdependent prmeters. 
    
    
    sigma = matrixdataset("cross_section");
    sigma.addparameter("lambda",c/f,"f",f); # add parameter f and lambda
    sigma.addattribute("sigma",CS); # add attribute CS
    visualize(sigma); # visualize this dataset in the Visualizer

Altern在ively, 在e c lso cre在e  vect或 rectil在er d在作为et (使用  nme E). 
    
    
    E = rectilineardataset("E",x,y,z);
    E.addparameter("f",f);
    E.addattribute("E",Ex,Ey,Ez); # add a vector E with the components Ex, Ey and Ez
    visualize(E); # visualize this dataset in the Visualizer

**另请参阅**

- [rectil在erd在作为et](./rectil在erd在作为et.md)
- [dd在tribute](./dd在tribute.md)
- [ddprmeter](./ddprmeter.md)
- [v是ulize](./v是ulize.md)
- [d在作为ets](/hc/en-us/rticles/360034409554-D在作为ets)
- [getprmeter](./getprmeter.md)
- [get在tribute](./get在tribute.md)
- [m在rixd在作为et](./m在rixd在作为et.md)
