<!--
Translation from English documentation
Original command: disconnect
Translation date: 2026-02-04 22:49:48
-->

# disconnect

Disconnects one 元素 到 another via 该 specified ports.

**语法** |  **描述**  
---|---  
disconnect("element1", "port1", "element2", "port2"); |  Deletes 该 connection between "port1" 的 "element1" 和 "port2" 的 "element2".  
  
**示例**

To disconnect 该 port_1 的 一个 "Straight Waveguide_1" 和 该 port_2 的 一个 "Waveguide Coupler_1"
    
    
    disconnect("Straight Waveguide_1","端口 1","Waveguide Coupler_1","端口 2");

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [connect](/hc/en-us/articles/360034929313-connect)
