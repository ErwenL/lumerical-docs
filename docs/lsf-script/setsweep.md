# setsweep

Sets a property in a parameter sweep/optimization/Monte Carlo/S-parameter sweep item.

**Syntax** |  **Description**  
---|---  
setsweep("name", "property_name", property_value); |  Sets a property in a sweep/optimization/Monte Carlo/S-parameter item. "name" is the absolute name of an analysis item. "property_name" is the property showed in the edit window.  
?setsweep(“name”); |  View the editable properties of the analysis item.  
“name” is the absolute name of the analysis item.  
  
For a [**parameter sweep**](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweep-utility)analysis:

**Argument** |  **Description**  
---|---  
property_name = "name" |  Sets the name of the sweep.  
property_name = "solver" |  Sets the solver used for sweep.  
property_name = "type" |  Sets the type of the sweep. The value of "type" could be "Ranges" or "Values"  
property_name = "number of points" |  Sets the number of points of the sweep. The default number of points is 10.  
property_name = "resave files after analysis" |  Defines whether or not to re-save the file after analysis.  
  
For an **[optimization](https://optics.ansys.com/hc/en-us/articles/360034922953-Optimization-utility) ** analysis:

**Argument** |  **Description**  
---|---  
property_name = "name" |  Sets the name of the optimization.  
property_name = "algorithm" |  "algorithm" = "Particle Swarm", "User Defined"  
property_name = "maximum generations" |  Sets the maximum generation number.  
property_name = "reset random generator" |  Checks the box of "Reset random generation".  
property_name = "type" |  "Type" = "Maximum", "Minimum"  
property_name = "generation size" |  The number of simulations per generation.  
property_name = "tolerance" |  Sets the tolerance value.  
property_name = "first generation script" |  Sets the "first generation script" in the "Advanced" tab.  
property_name = "next generation script" |  Sets the "next generation script" in the "Advanced" tab.  
property_name = "use figure of merit script" |  Checks the box of "use figure of merit" in the "Figure of merit script" tab.  
property_name = "figure of merit script" |  Sets the "figure of merit script" in the "Figure of merit script" tab.  
  
For a [**Monte Carlo**](https://optics.ansys.com/hc/en-us/articles/360034403194-Monte-Carlo-analysis-utility) analysis:

**Argument** |  **Description**  
---|---  
property_name = "name" |  Sets the name of the Monte Carlo.  
property_name = "number of trials" |  Sets the number of trials for the Monte Carlo. The default number of trials is 10.  
property_name = "variation" |  Sets the variation for "Process" or "Mismatch" or "Both". The default variation is "Both".  
property_name = "seed" |  Sets the seed.  
property_name = "enable seed" |  Sets whether or not to enable the seed.  
property_name = "individual trial" |  Sets the individual trial number.  
property_name = "enable individual trail" |  Sets whether or not to enable individual trials.  
property_name = “enable spatial correlations” |  Sets whether spatial correlation is enabled.  
  
For an [**S-parameter matrix sweep**](https://optics.ansys.com/hc/en-us/articles/360034403214-S-parameter-matrix-sweep-utility) analysis:

**Argument** |  **Description**  
---|---  
property_name = "name" |  Sets the name of the S-parameter matrix sweep.  
property_name = "excite all ports" |  If property_value = "true", the sweep will run as many simulations as there are defined rows in the S-Matrix Setup table. If property_value = "false", simulations will be run only for the selected rows in the S-Matrix Setup table. The default is "true".  
property_name = "calculate group delay" |  When enabled, the group delay of the device is calculated numerically using a finite difference approximation, using the derivative of phase with respect to frequency.  
property_name = "invert sign" property_name = "map from" property_name = "active" property_name = "port" property_name = "mode" property_name = "map vector" |  These properties are set for each row of the S-Matrix Setup table tab. To set them manually, the command [addsweepparameter](https://optics.ansys.com/hc/en-us/articles/360034930493-addsweepparameter-Script-command) should be used. The meaning of each parameter can be found in the Knowledge Base Article on S-parameter sweeps. Once added, the rows cannot be changed and must be removed using [removesweepparameter](https://optics.ansys.com/hc/en-us/articles/360034930513-removesweepparameter-Script-command) first.  
property_name = "auto symmetry" |  If property_value = "true", auto symmetry is calculated and applied when possible (see [ S-parameter matrix sweep ](/hc/en-us/articles/360034403214-S-parameter-matrix-sweep) ). If property_value = "false", no changes are applied to the S-parameter sweep. The default is "false". **Note:** The changes made to the S-parameter sweep cannot be undone by setting property_value = "false". When property_value = "false", no settings change in the current sweep.  
property_name = "export setup" |  This property sets up the layout of the export file for export of data in either Lumerical or Touchstone format. There are two possible arguments:

  * “auto”: Uses automatic definition for the export table.
  * A custom structure defining each port, see the example below on how the structure should be formatted.

  
  
For an [S-parameter matrix sweep](https://optics.ansys.com/hc/en-us/articles/360034403214-S-parameter-matrix-sweep-utility) analysis in MODE:

**Argument** |  **Description**  
---|---  
property_name = "name" |  Sets the name of the S-parameter matrix sweep.  
property_name = "number of points" |  Set the number of points in the sweep.  
property_name = "calculated group delay" |  Set whether the group delay is calculated.  
property_name = "group delay wavelength" |  Set the wavelength to calculate group delay. This option has no effect unless “calculated group delay” is enabled. But if set prior to enabling the calculation, the set value will be automatically applied when the option is enabled.  
property_name = "parameter label" |  Set the name of the parameter of the sweep.  
property_name = "start wavelength" |  Set the start wavelength of the sweep.  
property_name = "stop wavelength" |  Set the stop wavelength of the sweep.  
property_name = "include group delay" |  This property sets up the layout of the export file for export of data in either Lumerical or Touchstone format. There are two possible arguments:

  * “auto”: Uses automatic definition for the export table.
  * A custom structure defining each port, see the example below on how the structure should be formatted.

  
Editing added sweep parameters:  In addition to the listed default properties of the sweep/optimization/Monte Carlo/S-parameter, any added sweep parameters can be edited by the setsweep command by setting the "property_name" to the parameter name.  
---  
  
**Examples**

This examples show how to set a sweep/optimization/Monte Carlo/S-parameter's properties respectively. Please refer to the application example page [ Sweep scripting commands ](/hc/en-us/articles/360034922893-Sweep-scripting-commands) for detailed information.

Sweep:
    
    
    addsweep(0);
    setsweep("sweep", "name", "thickness_sweep_script");
    setsweep("thickness_sweep_script", "type", "Ranges");
    setsweep("thickness_sweep_script", "number of points", 10); 

Optimization:
    
    
    addsweep(1);
    setsweep("optimization", "name", "thickness_optimization_script");
    setsweep("thickness_optimization_script", "Type", "Minimize");
    setsweep("thickness_optimization_script", "algorithm", "Particle Swarm");
    setsweep("thickness_optimization_script", "maximum generations", 20);
    setsweep("thickness_optimization_script", "generation size", 10);
    setsweep("thickness_optimization_script", "tolerance", 0);

Monte Carlo:
    
    
    addsweep(2);
    MC_name = "MC_script";
    setsweep("Monte Carlo analysis", "name", MC_name);
    setsweep(MC_name, "number of trials", 50);
    setsweep(MC_name, "enable seed", 1);
    setsweep(MC_name, "seed", 1);
    setsweep(MC_name, "Variation", "Both");

S-parameter sweep:
    
    
    addsweep(3);
    setsweep("s-parameter sweep", "name", "S sweep");
    setsweep("s-parameter sweep", "Excite all ports", 0);
    setsweep("S sweep", "auto symmetry", true);

This example defines and sets the export setup in FDTD for the setting shown in the figure below. Columns other than “Mode label” , “Mode ID”, and “Port location” cannot be changed.
    
    
    modestruct = {"label": "mode 1", "id" : 1};  
    rowstruct = {"mode 1": modestruct, "location": "LEFT"};  
    portstruct = {"port 2": rowstruct};   
    setsweep("s-parameter sweep", "export setup", portstruct);

This example sets the export setup in MODE for the **second** row in the figure below. Other rows in the table are automatically filled based on the placement of Port objects in the simulation domain. Columns other than “Mode label” and “Mode ID” cannot be changed.

****
    
    
    modestruct = {"label": "my mode 2", "id" : 2};  
    rowstruct = {"mode 1": modestruct};  
    portstruct = {"port 2": rowstruct};   
    setsweep("s-parameter sweep", "export setup", portstruct);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ deletesweep ](/hc/en-us/articles/360034930173-deletesweep) , [ copysweep ](/hc/en-us/articles/360034930373-copysweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ addsweep ](/hc/en-us/articles/360034930413-addsweep) , [ insertsweep ](/hc/en-us/articles/360034930433-insertsweep) , [ getsweep ](/hc/en-us/articles/360034930453-getsweep) , [ addsweepparameter ](/hc/en-us/articles/360034930493-addsweepparameter) , [ addsweepresult ](/hc/en-us/articles/360034410034-addsweepresult) , [ removesweepparameter ](/hc/en-us/articles/360034930513-removesweepparameter) , [ removesweepresult ](/hc/en-us/articles/360034930533-removesweepresult) , [ Sweep scripting commands ](/hc/en-us/articles/360034922893-Sweep-scripting-commands) , [ Optimization scripting commands ](/hc/en-us/articles/360034922973-Optimization-scripting-commands) , [ Monte Carlo scripting commands ](/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)
