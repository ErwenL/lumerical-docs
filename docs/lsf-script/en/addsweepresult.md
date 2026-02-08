# addsweepresult

Adds a result to a sweep/optimization/Monte Carlo item.

| **Syntax**                        | **Description**                                                                                                                                                                                                                                                 |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addsweepresult("name", "result"); | Adds a result to a sweep/optimization/Monte Carlo item. "name" is the absolute name of an analysis item. "result" could be a string (i.e. create a result with default values) or a struct which could contain results and operations. Returns the result name. |

**Example**

This example shows how to add a result to an existing optimization. This piece of script
command is taken from the example file sweep_AR_coating_example_script.lsf in the
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
# define results
result_1 = struct;
result_1.Name = "R";
result_1.Result = "::model::R::T";
result_2 = struct;
result_2.Name = "T";
result_2.Result = "::model::T::T";
# add the results R & T to the sweep
addsweepresult("thickness_sweep_script", result_1);
addsweepresult("thickness_sweep_script", result_2);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ copysweep ](./copysweep.md) , [ pastesweep ](./pastesweep.md) ,
[ addsweep ](./addsphere.md) , [ insertsweep ](./insertsweep.md) ,
[ getsweep ](./getsweep.md) ,
[setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](./setsetting.md),
[ addsweepparameter ](./addsweepparameter.md) ,
[ removesweepparameter ](./removesweepparameter.md) ,
[ removesweepresult ](./removesweepresult.md) ,
[ Sweep scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922893-Sweep-scripting-commands)
,
[ Optimization scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922973-Optimization-scripting-commands)
,
[ Monte Carlo scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)
