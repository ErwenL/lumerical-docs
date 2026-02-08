# lookupreadtable

Returns an interpolated matrix from a file containing a lookup table of design and extracted parameters. 

**Syntax** |  **Description**  
---|---  
out = lookupreadtable ("filename","table",design,"extracted");  |  Returns an interpolated matrix from a file containing a lookup table of design and extracted parameters. Parameter table is the name of the lookup table located inside the file, design is a cell containing multiple structures that define the design parameters to search, and extracted is the name of the parameter to be extracted. It will return a matrix that contains multiple columns. The first column is the independent variable. e.g. frequency dependent transmission values.   
  
**Example**

The script below loads the frequency dependent propagation properties of a bent waveguide: 
    
    
    filename = "waveguide.ixml";
    table = "waveguide";
    design = cell(1);
    #design (input parameters)
    design{1} = struct;
    design{1}.name = "radius";
    design{1}.value = 3e-6;
    w_length = 1e-6;
    M=lookupreadtable("waveguide.ixml", "waveguide", design, "Filename" );
    # set the s-parameter in scripted element
    setsparameter("port 2", "port 1", "propagation", M, w_length);
    setsparameter("port 1", "port 2", "propagation", M, w_length);

where “waveguide.ixml” is a lookup table containing a map between waveguide ‘radius’ and ‘Filename’ containing frequency dependent propagation properties: 
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <lumerical_lookup_table version="1.0" name = "waveguide">
      <association> 
        <design>
          <value name="radius" type="double">3e-06</value>
        </design> 
        <extracted>
          <value name="Filename" type="string">radius_3.txt</value> 
        </extracted>
      </association>
    </lumerical_lookup_table>

For example, “radius_3.txt” file contains a matrix with frequency dependent propagation properties 
    
    
    2.315e+14552.62.787.071e+07
    2.30918e+14552.72.717.076e+07
    2.30335e+14543.32.737.075e+07
    2.29753e+14543.32.767.076e+07
    2.2917e+14544.72.787.062e+07
    2.28588e+14545.52.727.061e+07
    2.28006e+14546.62.717.064e+07
    2.27423e+14544.22.737.061e+07
    2.26841e+14533.12.747.063e+07
    2.26258e+14532.22.757.069e+07 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) , [ lookupread ](/hc/en-us/articles/360034928333-lookupread) , [ lookupwrite ](/hc/en-us/articles/360034928353-lookupwrite) , [ lookupclose ](/hc/en-us/articles/360034408234-lookupclose) , [ lookupreadvalue ](/hc/en-us/articles/360034928413-lookupreadvalue) , [ lookupreadnportsparameter ](/hc/en-us/articles/360034408274-lookupreadnportsparameter) , [ lookupappend ](/hc/en-us/articles/360034928433-lookupappend) , [ insert ](/hc/en-us/articles/360034928453-insert)
