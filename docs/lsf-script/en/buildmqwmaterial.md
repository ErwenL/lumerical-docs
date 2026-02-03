# buildmqwmaterial

Creates a struct with material parameters for use with [mqwgain](/hc/en-us/articles/360034926533-mqwgain) and [mqwindex](/hc/en-us/articles/360041072553) commands.

**Syntax** |  **Description**  
---|---  
result = buildmqwmaterial(location, T, matname, x); |  Ternary materials. location: string specifying the path to the database file. Alternatively, if empty struct, the default database will be used. T: temperature. matname: ternary material name. x: material composition. result: struct with material properties.  
result = buildmqwmaterial(location, 300, matname, x, cbValley); |  same as above with the additional parameter cbValley that specifies which conduction band valleys will be included for the interpolation of parameters. Possible values: “Gamma”, “X”, “L”, or “All” (default is “Gamma”; option “All” uses the lowest band gap to select).  
result = buildmqwmaterial(location, 300, matname, x, y); |  Quaternary material with compositions x and y.  
result = buildmqwmaterial(location, 300, matname, x, y, cbValley); |  Quaternary material with compositions x and y and the valley mixing specifier.  
  
The supported materials are listed in the table below:

**III-V semiconductors** |  **Ternary alloys** |  **Quaternary Alloys**  
---|---|---  
AlAs |  AlxGa1-xAs |  InxGa1-xAsyP1-y  
GaAs |  AlxGa1-xP |  AlxGayIn1-x-yAs  
InAs |  AlxIn1-xP |   
AlP |  GaAsxP1-x |   
GaP |  InxAl1-xAs |   
InP |  InAsxP1-x |   
|  InxGa1-xAs |   
|  InxGa1-xP |   
  
When database materials are used, the properties of ternary alloys P(AxB1−xD) are interpolated from the corresponding properties of the base materials (P(AD) and P(BD)) according to the formula

$$ P\left(A_x B_{1-x}D\right)=xP\left(AD\right)+\left(1-x\right)P\left(BD\right)+x\left(1-x\right)C, $$

where x is the composition fraction and C is the bowing parameter (quadratic coefficient).

Quaternary alloys of type AxB1-xCyD1-y (two group III and two group V elements) are composed from the interpolation of ternary alloy constituents [1]:

$$ P\left(A_xB_{1-x}C_yD_{1-y}\right)=\frac{x\left(1-x\right)\left[\left(1-y\right)P\left(A_xB_{1-x}D\right)+yP\left(A_xB_{1-x}C\right)\right]+y\left(1-y\right)\left[xP\left(AC_yD_{1-y}\right)+\left(1-x\right)P\left(BC_yD_{1-y}\right)\right]}{x\left(1-x\right)+y\left(1-y\right)}, $$

for composition fractions x and y. For example, a combination of the properties of InxGa1−xP, InxGa1−xAs, InAsyP1−y, and GaAsyP1−y is used to define the properties of InxGa1−xAsyP1−y.

Quaternary alloys of type AxByC1-x-yD (three group III elements and one group V element) are composed from the interpolation of ternary alloy constituents [1]:

$$ P\left(A_xB_yC_{1-x-y}D\right)=\frac{xyP\left(A_{1-u}B_uD\right)+y(1-x-y)P\left(B_{1-v}C_{v}D\right)+x(1-x-y)P\left(A_{1-w}C_{w}D\right)}{xy+y(1-x-y)+x(1-x-y)}, $$

for composition fractions x and y and u = (1-x+y)/2, v = (2-x-2y)/2, w = (2-2x-y)/2. For example, a combination of the properties of Al1-uGauAs, Ga1-vInvAs, and Al1-wInwAs, is used to define the properties of AlxGayIn1-x-yAs.

**result** is a struct with the following fields:

**Coefficient** |  **Units** |  **Description**  
---|---|---  
eg |  eV |  Band gap  
ep |  eV |  Energy parameter for the optical matrix element  
me |  1/m0 |  Electron effective mass  
gamma1 |  |  Luttinger parameter  
gamma2 |  |  Luttinger parameter  
gamma3 |  |  Luttinger parameter  
ac |  eV |  Conduction band deformation potential  
av |  eV |  Valence band deformation potential  
b |  eV |  Valence band deformation potential  
c11 |  N/m2 |  Elastic stiffness coefficient  
c12 |  N/m2 |  Elastic stiffness coefficient  
lc |  m |  Lattice constant  
vb |  eV |  Valence band absolute energy (all layers should have common reference)  
eps |  |  Relative static permittivity  
  
**References**

[1] Vurgaftman et al., J. Appl. Phys., 89, 5815 (2001)

**Example**
    
    
    mymat = buildmqwmaterial(“/home/auser/myfolder/my_material_db.json”, 300, “InAlAs”, 0.47);

**See Also**

[mqwgain](/hc/en-us/articles/360034926533-mqwgain), [mqwindex](/hc/en-us/articles/360041072553)
