# addsweep

Adds a parameter sweep/optimization/Monte Carlo/S-parameter sweep item as the top-most
analysis item.

| **Syntax**      | **Description**                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addsweep(type); | adds a parameter sweep/optimization/Monte Carlo/S-parameter sweep item as the top-most analysis item. 'type' = 0 for parameter sweep 'type' = 1 for optimization 'type' = 2 for Monte Carlo analysis 'type' = 3 for S-parameter matrix sweep in FDTD and MODE solver 'type' = 4 for Corner sweep analysis in INTERCONNECT If type is not provided, by default type 0 will be applied to add a sweep. |

**Example**

Type = 0, for adding a **parameter sweep** analysis:

```
addsweep(0);
?setsweep("sweep");
> Result:
name
type  
solver
number of points
resave files after analysis
```

Type = 1, for adding an **optimization** analysis:

```
addsweep(1);
?setsweep("optimization");
> Result:
name  
algorithm  
maximum generations  
reset random generator  
type  
generation size  
tolerance  
first generation script  
next generation script  
use figure of merit script  
figure of merit script
```

Type = 2, for adding a **Monte Carlo** analysis:

```
addsweep(2);  
?setsweep("Monte Carlo analysis");
> Result:
name  
number of trials  
variation  
seed  
enable seed  
individual trial  
enable individual trial  
enable spatial correlations
```

Type = 3, for adding an **S-parameter sweep** analysis in FDTD:

```
addsweep(3);  
?setsweep("s-parameter sweep");
> Result:
name  
excite all ports  
calculate group delay  
invert sign  
map from  
active  
port  
mode  
map vector  
auto symmetry  
export setup
```

Type = 3, for adding an **S-parameter sweep** analysis in MODE:

```
addsweep(3);  
?setsweep("s-parameter sweep");
> Result:
name  
number of points  
calculate group delay  
group delay wavelength  
parameter label  
start wavelength  
stop wavelength  
include group delay
```

Type = 4, for adding a **Corner sweep** analysis in INTERCONNECT:

```
addsweep(4);  
?getsweep("Corner sweep");  
> Result:  
name  
resave files after analysis
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ deletesweep ](./deletesweep.md) , [ copysweep ](./copysweep.md) ,
[ pastesweep ](./pastesweep.md) , [ insertsweep ](./insertsweep.md) ,
[ getsweep ](./getsweep.md) ,
[setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](./setsweep.md),
[ addsweepparameter ](./addsweepparameter.md) , [ addsweepresult ](./addsweepresult.md)
, [ removesweepparameter ](./removesweepparameter.md) ,
[ removesweepresult ](./removesweepresult.md)
