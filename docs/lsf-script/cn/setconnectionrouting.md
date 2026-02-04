<!--
Translation from English documentation
Original command: setconnectionrouting
Translation date: 2026-02-03
-->

# setconnectionrouting

此命令设置给定连接的连接路由。

**语法** | **描述**
---|----
setconnectionrouting(element, port, type);<br>setconnectionrouting(element, type); | 此命令设置给定连接的连接路由。如果只提供元件和类型，则元件端口的所有连接将具有相同的路由类型。如果提供元件名称、端口和类型，则只有特定的元件端口连接会受到影响。type = "direct" 或 "manhattan"。

**另请参见**
