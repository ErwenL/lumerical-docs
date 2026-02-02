# addimportdope

Adds a [doping region](/hc/en-us/articles/360034398054) to the simulation environment that can be used to load a custom doping profile. The custom doping profile can be created analytically using script or it can be imported from other sources such as process simulation. This command requires a CHARGE solver region to be present in the objects tree.

**Syntax** |  **Description**  
---|---  
addimportdope; |  Add an import doping region to the simulation environment. This function does not return any data.  
addimportdope(struct_data); |  Adds an import doping region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
Once the import doping object is created, the doping data can be imported from a matlab (.mat) file using the GUI or by assigning a dataset to the object using the [ importdataset ](/hc/en-us/articles/360034409114-importdataset) script command. The dataset can be a rectilinear or an unstructured dataset. Doping data can be imported into the solver workspace from other tools (e.g. process simulation) using the [ Dataset builder ](/hc/en-us/articles/360034901713-Dataset-builder) .

**Example**

The following script command will add an import doping object to the CHARGE solver region and will load an analytic 3D doping data into it.
    
    
    addimportdope;
    set("name","pepi");
    set("x",0);
    set("y",0);
    set("z",0);
    # create coordinate vectors and 3D matrix for doping profile
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    N = matrix(11,2,101) + 1e21;  # assume uniform doping concentration of 1e15 /cm3 (1e21 /m3)
    # create dataset
    doping = rectilineardataset("dope",x,y,z);
    doping.addparameter("a",1);  # add a dummy parameter
    doping.addattribute("N",N);
    # load data into doping object
    select("CHARGE::pepi");
    importdataset(doping);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ linspace ](/hc/en-us/articles/360034409254-linspace) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ select ](/hc/en-us/articles/360034928593-select) , [ importdataset ](/hc/en-us/articles/360034409114-importdataset) , [ adddope ](/hc/en-us/articles/360034404594-adddope) , [ adddiffusion ](/hc/en-us/articles/360034924513-adddiffusion)
