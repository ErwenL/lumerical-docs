<!--
Translation from English documentation
Original command: removeport
Translation date: 2026-02-03
-->

# removeport

从复合/脚本元件中删除端口（注意：此命令不适用于原始元件）。

**语法** | **描述**
---|---
removeport("element", "port"); | 从 "element" 中删除 "port"。如果端口成功删除，则返回 1，否则返回 0。

**示例**

打开示例文件 compound_element.icp，并输入以下脚本：

```lsf
disconnect("Optical Network Analyzer","input 1","Compound Element","port 2");
disconnect("Optical Network Analyzer","output","Compound Element","port 1");
removeport("Compound Element","port 1"); #删除端口
addport("Compound Element","port 1","input","optical Signal"); #添加端口
```

**另请参见**

- [操作对象](./command_list.md)
- [addport](./addport.md)
