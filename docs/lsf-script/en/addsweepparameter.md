# addsweepparameter

Adds a parameter to a parameter sweep/optimization/Monte Carlo/S-parameter sweep item.

| **Syntax**                              | **Description**                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addsweepparameter("name", "parameter"); | Adds a parameter to a parameter sweep/optimization/Monte Carlo/S-parameter sweep item. "name" is the absolute name of an analysis item. "parameter" could be a string (i.e. create a parameter with default values. eg. ::model::rectangle::index) or a struct which counld contain parameter, type, start, stop, unit, etc. Returns the parameter name. |

**Example**

This example shows how to add a parameter to an existing optimization. This piece of
script command is taken from the example file sweep_AR_coating_example_script.lsf in the
example page
[ Optimization scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922973-Optimization-scripting-commands)
.

```
# add a sweep
addsweep(0);
setsweep("sweep", "name", "thickness_sweep_script");
setsweep("thickness_sweep_script", "type", "Ranges");
setsweep("thickness_sweep_script", "number of points", 10); 
# define the parameter thickness
para = struct;
para.Name = "thickness";
para.Parameter = "::model::AR structure::thickness";
para.Type = "Length";
para.Start = 0.05e-6;
para.Stop = 0.15e-6;
para.Units = "microns";
# add the parameter thickness to the sweep
addsweepparameter("thickness_sweep_script", para);
```

This example shows how to add a parameter sweep which sweeps 5 values of a thickness
parameter.

```
addsweep(0);setsweep("sweep","name","thickness_sweep");
setsweep("thickness_sweep","type","Values");
setsweep("thickness_sweep","number of points",5);
# define the parameter thickness
para = struct;
para.Parameter = "::model::AR structure::thickness";
para.Type = "Length";
para.Value_1 = 0.05e-6;
para.Value_2 = 0.07e-6;
para.Value_3 = 0.09e-6;
para.Value_4 = 0.11e-6;
para.Value_5 = 0.15e-6;
# add the parameter thickness to the sweep
addsweepparameter("thickness_sweep", para);
```

This example shows how to add an S-parameter sweep and set up the rows of the S-matrix
mapping table manually. This script can be used with the example in
[ S-parameter matrix sweep ](https://optics.ansys.com/hc/en-us/articles/360034403214-S-parameter-matrix-sweep)
and it generates the same table without using the "auto symmetry" option for mapping
between rows. This manual mapping is not necessary in this case because the "auto
symmetry" tool will configure the table correctly with minimal effort (compare the
script below with the one under "Scripted setup and analysis" in
[ S-parameter matrix sweep ](https://optics.ansys.com/hc/en-us/articles/360034403214-S-parameter-matrix-sweep)
). Therefore, the manual setup shown here should only be used in particular cases where
the "auto symmetry" tool does not apply the correct mapping.

```
##ADD SWEEP##deletesweep("s-parameter sweep"); # if a sweep task named s-parameter sweep already exists, remove it
addsweep(3); # add s-parameter sweep task
##SWEEP SETUP##
setsweep("s-parameter sweep", "Excite all ports", 0); # un-check "Excite all ports" to define active ports manually
#    Define index entries for s-matrix mapping table as a struct with fields:
#    Port, Mode : Define the port and mode numbers.
#    Active (0 or 1): When a entry is defined as active, a simulation will be run with the source set to the corresponding port and mode combination.
#    Map from: For non-active entries this defines the entry from where the mapping is done.
#    Invert sign (0 or 1): This is only used in cases where additional inversion of the modal fields is required.  
#    Map vector: Array with the permutation of the output indices for the input index given by "Map from".   
# Active entries:
index1 = struct; # Corresponds to S11,S21,...,S61
index1.Port = "port 1";
index1.Mode = "mode 1";
index1.Active = 1;
index2 = struct; # Corresponds to S12,S22,...,S62
index2.Port = "port 1";
index2.Mode = "mode 2";
index2.Active = 1;
index3 = struct; # Corresponds to S13,S23,...,S63
index3.Port = "port 2";
index3.Mode = "mode 1";
index3.Active = 1;
index4 = struct; # Corresponds to S14,S24,...,S64
index4.Port = "port 2";
index4.Mode = "mode 2";
index4.Active = 1;
# Mapped entries:
index5 = struct; # Corresponds to S15,S25,...,S65
index5.Port = "port 3";
index5.Mode = "mode 1";
index5.Active = 0;
index5.%Map from% = 3;
index5.%Invert sign% = 0;
index5.%Map vector% = [1,2,5,6,3,4]; # S15=S13, S25=S23, S35=S53, S45=S63, S55=S33, S65=S43 
index6 = struct; # Corresponds to S16,S26,...,S66
index6.Port = "port 3";
index6.Mode = "mode 2";
index6.Active = 0;
index6.%Map from% = 4;
index6.%Invert sign% = 0;
index6.%Map vector% = [1,2,5,6,3,4]; # S16=S14, S26=S24, S36=S54, S46=S64, S56=S34, S66=S44 
######
# Add index entries to s-matrix mapping table
addsweepparameter("s-parameter sweep",index1);
addsweepparameter("s-parameter sweep",index2);
addsweepparameter("s-parameter sweep",index3);
addsweepparameter("s-parameter sweep",index4);
addsweepparameter("s-parameter sweep",index5);
addsweepparameter("s-parameter sweep",index6);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ copysweep ](./copysweep.md) , [ pastesweep ](./pastesweep.md) ,
[ addsweep ](./addsphere.md) , [ insertsweep ](./insertsweep.md) ,
[ getsweep ](./getsweep.md) ,
[setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](./setsetting.md),
[ addsweepresult ](./addsweepresult.md) ,
[ removesweepparameter ](./removesweepparameter.md) ,
[ removesweepresult ](./removesweepresult.md) ,
[ Sweep scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922893-Sweep-scripting-commands)
,
[ Optimization scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922973-Optimization-scripting-commands)
,
[ Monte Carlo scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)
