# lookupwrite

Writes to a lookup table file with a design and an extracted parameter pair. This function must be called after [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) and before [ lookupclose ](/hc/en-us/articles/360034408234-lookupclose) . 

**Syntax** |  **Description**  
---|---  
out = lookupwrite ("filename","table",design, "extracted");  |  Writes to a lookup table with a design and an extracted parameter pair. The design and extracted parameters are cells that contain multiple structures, allowing for mapping between multiple design and extracted parameters. This function can be called multiple times, for each call the design and extracted parameters will be appended to the current file. This function must be called after  lookupopen  and before  lookupclose  .   
out = lookupwrite ("filename");  |  Takes a script object, in this case a cell array containing all the contents of the xml file, and save it to a file.   
  
**Example**

The script below maps two values of waveguide width and height to the effective index and group index. 
    
    
    design = cell(2);
    #extracted contains neff and ng
    extracted = cell(2);
    #design (input parameters)
    design{1} = struct;
    design{1}.name = "width";
    design{1}.value = 5.03333e-07;
    design{2} = struct;
    design{2}.name = "heigth";
    design{2}.value = 2.18889e-07;
    #extracted (output results)
    extracted{1} = struct;
    extracted{1}.name = "neff";
    extracted{1}.value = 2.1;
    extracted{2} = struct;
    extracted{2}.name = "ng";
    extracted{2}.value = 4.42;
    #open file to write table
    lookupopen( "new.xml", "new_extracted" );
    #write first design/extracted pair
    lookupwrite( "new.xml", design, extracted );
    #second design/extracted pair
    design{1}.value = 6.03333e-07;
    design{2}.value = 1.18889e-07;
    extracted{1}.value = 2.2;
    extracted{2}.value = 4.45;
    #write second design/extracted pair
    lookupwrite( "new.xml", design, extracted );
    #close file
    lookupclose( "new.xml" );

where “new.xml” is a lookup table containing the table “new_extracted” 
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <lumerical_lookup_table version="1.0" name = "new_extracted">
    <association>
      <design>
        <value name="width" type="double">5.03333e-07</value>
        <value name="heigth" type="double">2.18889e-07</value>
      <design>
      <extracted>
        <value name="neff" type="double">2.1</value>
        <value name="ng" type="double">4.42</value>
      </extracted>
    </association>
    <association>  
      <design>
        <value name="width" type="double">6.03333e-07</value>
        <value name="heigth" type="double">1.18889e-07</value>
      <design>
      <extracted>
        <value name="neff" type="double">2.2</value>
        <value name="ng" type="double">4.45</value>
      </extracted>
    </association>
    </lumerical_lookup_table>

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ lookupclose ](/hc/en-us/articles/360034408234-lookupclose) , [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) , [ lookupread ](/hc/en-us/articles/360034928333-lookupread) , [ lookupreadtable ](/hc/en-us/articles/360034928393-lookupreadtable) , [ lookupreadvalue ](/hc/en-us/articles/360034928413-lookupreadvalue) , [ lookupreadnportsparameter ](/hc/en-us/articles/360034408274-lookupreadnportsparameter) , [ lookupappend ](/hc/en-us/articles/360034928433-lookupappend) , [ insert ](/hc/en-us/articles/360034928453-insert)
