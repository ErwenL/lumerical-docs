<!--
Translation from English documentation
Original command: addemeindex
Translation date: 2026-02-03 22:52:43
-->

# addemeindex

添加一个[index monitor](/hc/en-us/articles/360034396434)（索引监视器），在使用EME求解器区域时可用于返回空间折射率。此命令要求EME求解器对象设置为活动求解器才能工作。

**Syntax** |  **Description**  
---|---  
addemeindex; |  在使用EME求解器区域时添加一个索引监视器。此函数不返回任何数据。  
addemeindex(struct_data); |  添加一个EME索引监视器，并使用包含"属性"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将向EME求解器区域添加一个索引监视器。首先使用`setactivesolver`命令将EME求解器区域设置为活动求解器。
    
    
    setactivesolver("EME");
    addemeindex;

**参见**

- [setactivesolver](./setactivesolver.md)
