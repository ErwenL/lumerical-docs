# importnetlist

This script command can import an optical SPICE netlist. 

**Syntax** |  **Description**  
---|---  
importnetlist("compound name", "filename");  |  imports an optical SPICE netlist. The "compound name" is optional, if not specified, the Root Element level circuit configuration will be imported; if specified, the sub-circuit will be imported to this specified compound.   
  
**Parameter** |  |  **Type** |  **Description**  
---|---|---|---  
compound name  |  optional  |  string  |  name of the compound   
filename  |  required  |  string  |  name of the netlist.   
  
###  See Also 

[ List of commands ](/hc/en-us/articles/360037228834) , [ exportnetlist ](/hc/en-us/articles/360034932093-exportnetlist)
