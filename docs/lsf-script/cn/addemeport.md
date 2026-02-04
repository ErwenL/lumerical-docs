<!--
Translation from English documentation
Original command: addemeport
Translation date: 2026-02-03 22:54:08
-->

# addemeport

向EME求解器区域/对象添加一个[port](/hc/en-us/articles/360034396374)（端口）。此命令要求EME求解器对象设置为活动求解器才能工作。

**Syntax** |  **Description**  
---|---  
addemeport; |  向活动EME求解器区域添加一个端口。此函数不返回任何数据。  
addemeport(struct_data); |  向活动EME求解器区域添加一个端口，并使用包含"属性"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将向EME求解器区域添加一个端口。首先使用`setactivesolver`命令将EME求解器区域设置为活动求解器。
    
    
    setactivesolver("EME");
    addemeport;

**参见**

- [setactivesolver](./setactivesolver.md)
