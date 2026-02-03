# connect

Connects one element to another via the specified ports.

**Syntax** |  **Description**  
---|---  
connect("element1", "port1", "element2", "port2"); |  Connects "port1" of "element1" to "element2" or "port2".  
  
**Example**

To connect the port_1 of a "Straight Waveguide_1",to port_2 of a "Waveguide Coupler_1"
    
    
    connect("Straight Waveguide_1","port 1","Waveguide Coupler_1","port 2");

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [disconnect](/hc/en-us/articles/360034408954-disconnect)
