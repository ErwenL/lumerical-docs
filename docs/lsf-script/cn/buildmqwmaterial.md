<!-- Translation completed: 2026-02-04 -->
<!-- Original command: buildmqwmaterial -->

# buildmqwmaterial

**语法** | **描述**
---|---
result = buildmqwmaterial(location, T, matname, x); | Ternary materials. location: 字符串 specifying the 路径 to the database 文件. Alternatively, if 空 struct, the default database will be used. T: temperature. matname: ternary material name. x: material composition. result: struct with material properties.
result = buildmqwmaterial(location, 300, matname, x, cbValley); | same as above with the additional 参数 cbValley that specifies which conduction band valleys will be included for the interpolation of parameters. Possible 值: “Gamma”, “X”, “L”, or “All” (default is “Gamma”; option “All” uses the lowest band gap to select).
result = buildmqwmaterial(location, 300, matname, x, y); | Quaternary material with compositions x and y.
result = buildmqwmaterial(location, 300, matname, x, y, cbValley); | Quaternary material with compositions x and y and the valley mixing specifier.
**III-V semiconductors** | **Ternary alloys**
AlAs | AlxGa1-xAs
GaAs | AlxGa1-xP
InAs | AlxIn1-xP
AlP | GaAsxP1-x
GaP | InxAl1-xAs
InP | InAsxP1-x
 | InxGa1-xAs
 | InxGa1-xP
eg | eV
ep | eV
me | 1/m0
gamma1 | 
gamma2 | 
gamma3 | 
ac | eV
av | eV
b | eV
c11 | N/m2
c12 | N/m2
lc | m
vb | eV
eps | 

**示例**

    mymat = buildmqwmaterial(“/home/auser/myfolder/my_material_db.json”, 300, “InAlAs”, 0.47);

    mymat = buildmqwmaterial(“/home/auser/myfolder/my_material_db.json”, 300, “InAlAs”, 0.47);

**另请参阅**

[mqwgain](/hc/en-us/articles/360034926533-mqwgain), [mqwindex](/hc/en-us/articles/360041072553)
