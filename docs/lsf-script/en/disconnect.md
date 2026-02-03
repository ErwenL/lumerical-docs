# disconnect

Disconnects one element to another via the specified ports.

**Syntax** |  **Description**  
---|---  
disconnect("element1", "port1", "element2", "port2"); |  Deletes the connection between "port1" of "element1" and "port2" of "element2".  
  
**Example**

To disconnect the port_1 of a "Straight Waveguide_1" and the port_2 of a "Waveguide Coupler_1"
    
    
    disconnect("Straight Waveguide_1","port 1","Waveguide Coupler_1","port 2");

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [connect](/hc/en-us/articles/360034929313-connect)
