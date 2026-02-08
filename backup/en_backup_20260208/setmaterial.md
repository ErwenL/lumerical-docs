# setmaterial

Sets properties of a material in the material database. This command can only edit the properties of the materials that are NOT write protected.

**Syntax** |  **Description**  
---|---  
?setmaterial("materialname"); |  Displays the property names of the specified material that can be modified.  
setmaterial( "materialname", "propertyname", newvalue); |  Sets the property named "propertyname" of the material with the name "materialname" to newvalue. The argument newvalue can be a number or a string. The arguments "propertyname" and "materialname" have to match correct string exactly. For example, setmaterial("Si","Mesh order",4); will set the property "mesh order" of the materials "Si" to 4.  
setmaterial( "materialname", **_struct_**); |  Update multiple material properties at the same time using a [struct](https://support.lumerical.com/hc/en-us/articles/360034409574-struct-Script-command) of associated properties. Keys are given the respective "propertyname", and values assigned to the new value.  
  
**Example using struct**
    
    
    # create a material
    setmaterial(addmaterial("(n,k) Material"), "name", "myMaterial");  
    
    # set the material properties
    setmaterial("myMaterial", {"Refractive Index": 1.3, "Imaginary Refractive Index": 1.5});

**Conductive material example**

This example adds a new Conductive material, sets the name to "myMaterial", anisotropy to "Diagonal", and sets the permittivity and conductivity properties for the material.
    
    
    A=[4;5;6];
    B=[1;2;3];
    temp = addmaterial("Conductive");
    setmaterial(temp,"name","myMaterial");
    setmaterial("myMaterial", "Anisotropy", 1); # enable diagonal anisotropy
    setmaterial("myMaterial","Permittivity", A);
    setmaterial("myMaterial","Conductivity", B);

**Sampled data material example**

This example shows how to create a new Sampled data material.

The sampled data matrix must have 2 or 4 columns, for isotropic or anisotropic materials. The first column is the frequency vector, in Hz. The next column(s) are the complex valued permittivity.

If you have refractive index data (rather than permittivity), remember that permittivity is simply the square of the refractive index.
    
    
    f = linspace(1000e12,300e12,30);   # frequency vector
    eps = 2 + 1i*(1e6 / (2*pi*f*eps0)); # create example permittivity vector
    sampledData = [f,eps];        # collect f and eps in one matrix
    matName = "My material";
    temp = addmaterial("Sampled data");
    setmaterial(temp,"name",matName);        # rename material
    setmaterial(matName,"max coefficients",2);    # set the number of coefficients
    setmaterial(matName,"sampled data",sampledData); # load the sampled data matrix

**Index perturbation material example**

This example shows how to create a new Index perturbation material.

The Index perturbation material can define index perturbation for "np Density" and/or "Temperature". For a "np Density" index perturbation:

  * "np density model": takes an integer or string values of [0, 1, 2], 'Drude', 'Soref and Bennet' or 'Custom'
  * for model type "Custom": "n sensitivity table" and "p sensitivity table" take a matrix argument



For a "Temperature" index perturbation:

  * for model type "Linear sensitivity": users need to set individual values for 'Tref', 'dn/dt' and 'dk/dt'
  * for model type "Table of values": "temperature sensitivity table" takes a matrix argument


    
    
    nSensitivity = [1.5, 1.5e-3, 1.5e-3;  1.6, 1.6e-3, 1.6e-3; 1.7, 1.7e-3, 1.7e-3];
    pSensitivity = [1, 1e-3, 1e-3;  1.2, 1.2e-3, 1.2e-3; 1.4, 1.4e-3, 1.4e-3];
    matName = "May material";
    temp = addmaterial("Index perturbation");
    setmaterial(temp, "name", matName);
    setmaterial(matName, "np density model", "Custom"); # use "Custom" model type
    setmaterial(matName, "n sensitivity table", nSensitivity); # set n sensitivity table
    setmaterial(matName, "p sensitivity table", pSensitivity); # set p sensitivity table

It is possible to define the color of the material using command lines. An example is shown below. These script commands will create a material, define the material color, and assign that material to a rectangle to show the color change.

The 4 elements in the matrix for the new color value are for the red, green, blue, and alpha channels of the color, respectively. These elements can be set between 0 to 1, which represents a minimum of 0 and maximum of 255. Alpha defines the opacity, setting to to 0 means transparent, 1 means a solid color. For example, [1;0;0;1] would be solid red, [0;1;0;1] would be solid green, and [0;0;1;1] would be solid blue. More color channel values can be found using an online color picker tool.

Note that the color opacity can be also defined in the structure object by overriding the material properties.
    
    
    mymaterial = addmaterial("PEC");
    setmaterial(mymaterial,"name", "test_material");
    setmaterial("test_material", "color", [1; 0.6; 0.4; 0.3] ); # R, G, B, alpha channel
    addrect;
    set("material", "test_material");
    set("override color opacity from material database", 0);

**See Also**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ addmaterial ](https://optics.ansys.com/hc/en-us/articles/360034930013-addmaterial) , [ deletematerial ](https://optics.ansys.com/hc/en-us/articles/360034409734-deletematerial) , [ getmaterial ](https://optics.ansys.com/hc/en-us/articles/360034930053-getmaterial) , [ getindex ](https://optics.ansys.com/hc/en-us/articles/360034409674-getindex) , [ getfdtdindex ](https://optics.ansys.com/hc/en-us/articles/360034409694-getfdtdindex) , [ importing arbitrary dispersive material ](**%20to%20be%20defined%20**)
