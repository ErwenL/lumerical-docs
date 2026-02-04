<!--
Translation from English documentation
Original command: connect
Translation date: 2026-02-04 22:49:48
-->

# connect

Connects one 元素 到 another via 该 specified ports.

**语法** |  **描述**  
---|---  
connect("element1", "port1", "element2", "port2"); |  Connects "port1" 的 "element1" 到 "element2" 或 "port2".  
  
**示例**

To connect 该 port_1 的 一个 "Straight Waveguide_1",到 port_2 的 一个 "Waveguide Coupler_1"
    
    
    connect("Straight Waveguide_1","端口 1","Waveguide Coupler_1","端口 2");

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [disconnect](/hc/en-us/articles/360034408954-disconnect)
