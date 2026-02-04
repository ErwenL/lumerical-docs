<!--
Translation from English documentation
Original command: disconnect
Translation date: 2026-02-03 23:10:22
-->

# disconnect

通过指定端口将一个元素与另一个元素断开连接。

**Syntax** |  **Description**  
---|---  
disconnect("element1", "port1", "element2", "port2"); |  删除"element1"的"port1"与"element2"的"port2"之间的连接。  
  
 **示例**

 要断开"Straight Waveguide_1"的port_1与"Waveguide Coupler_1"的port_2之间的连接
    
    
    disconnect("Straight Waveguide_1","port 1","Waveguide Coupler_1","port 2");

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [connect](./connect.md)
