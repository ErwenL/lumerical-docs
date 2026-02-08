# lookupread

Finds the nearest extracted value from a file containing a lookup table of design and extracted parameters. 

**Syntax** |  **Description**  
---|---  
out = lookupread ("filename","table",design,"extracted");  |  Finds the nearest extracted value from a file containing a lookup table of design and extracted parameters. Parameter table is the name of the lookup table located inside the file, design is a cell containing multiple structures that define the design parameters to search, and extracted is the name of the parameter to be extracted. It will return the value located at the nearest design parameters.   
out = lookupread ("filename");  |  Returns a script object, in this case a cell array containing all the contents of the xml file.   
  
**Example**

To load the coupling length index associated to a coupler gap: 
    
    
    #design cell containing design/layout parameters (input parameter to search)#“gap” is the name of the property in the file  
    
    w_gap=3.5e-07;
    design = cell(1);
    design{1} = struct;
    design{1}.name = "gap";
    design{1}.value = w_gap;
    #read coupling length from file (using design as input search “coupling_length”)
    cl=lookupread( "coupler_map.xml", "coupler_extracted", design, "coupling_length" );
    ?c1
    7.18624026618721e-06

where “coupler_map.xml” is a lookup table containing a map between coupler gap and coupling length values: 
    
    
    ?xml version="1.0" encoding="UTF-8"?
    <lumerical_lookup_table version="1.0" name = "coupler_extracted">
      <association>
        <design>
          <value name="gap" type="double">3.5e-07</value>
        </design>
        <extracted>
          <value name="coupling_length" type="double">7.18624026618721e-06</value> 
        </extracted> 
      </association>
    ...
    </lumerical_lookup_table>
    

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ lookupclose ](/hc/en-us/articles/360034408234-lookupclose) , [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) , [ lookupwrite ](/hc/en-us/articles/360034928353-lookupwrite) , [ lookupreadtable ](/hc/en-us/articles/360034928393-lookupreadtable) , [ lookupreadvalue ](/hc/en-us/articles/360034928413-lookupreadvalue) , [ lookupreadnportsparameter ](/hc/en-us/articles/360034408274-lookupreadnportsparameter) , [ lookupappend ](/hc/en-us/articles/360034928433-lookupappend) , [ insert ](/hc/en-us/articles/360034928453-insert)
