# addimportgen

Adds an (optical) generation region to the simulation environment where the generation profile has been imported into Finite Element IDE. This command requires a CHARGE solver region to be present in the objects tree.

**Syntax** |  **Description**  
---|---  
addimportgen; |  Add an import generation object to the simulation environment. This function does not return any data.  
addimportgen(struct_data); |  Adds tan import generation object and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
Once the import generation object is created, the optical generation data can be imported from a matlab (.mat) file using the GUI or by assigning a dataset to the object using the [ importdataset ](/hc/en-us/articles/360034409114-importdataset) script command. The .mat file must contain a 3D matrix G containing the generation data on a rectilinear grid and the three coordinate vectors x, y, z. The dataset can be either a rectilinear or an unstructured dataset.

**Example**

The following script command will add an import generation object to the CHARGE solver region and will load an analytic 3D optical generation data into it.
    
    
    addimportgen;
    set("name","gen_opt");
    set("x",0);
    set("y",0);
    set("z",0);
    # create coordinate vectors and 3D matrix for doping profile
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    G = matrix(11,2,101) + 1e27;  # assume uniform generation rate of 1e21 /cm3 (1e27 /m3)
    # create dataset
    gen = rectilineardataset("gen",x,y,z);
    gen.addparameter("a",1);  # add a dummy parameter
    gen.addattribute("G",G);
    # load data into doping object
    select("CHARGE::gen_opt");  
    importdataset(gen);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ linspace ](/hc/en-us/articles/360034409254-linspace) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ select ](/hc/en-us/articles/360034928593-select) , [ importdataset ](/hc/en-us/articles/360034409114-importdataset) , [ addbulkgen ](/hc/en-us/articles/360034404634-addbulkgen) , [ adddeltachargesource ](/hc/en-us/articles/360034404654-adddeltachargesource)
