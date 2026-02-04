<!--
Translation from English documentation
Original command: designmode
Translation date: 2026-02-03 23:04:26
-->

# designmode

在INTERCONNECT中，此脚本命令可用于确定仿真文件当前处于DESIGN模式还是ANALYSIS模式。打开项目文件后立即使用此命令检查状态非常重要，以避免在后续操作中因文件不在所需模式而导致错误。 

**Syntax** |  **Description**  
---|---  
?designmode;  |  如果处于DESIGN模式返回1，处于ANALYSIS模式返回0。   
  
 **示例**

 以下脚本命令首先加载名为"test.icp"的项目文件。脚本的目的是在现有电路中添加一个新的光学示波器。但是，如果文件处于ANALYSIS模式，则"addelement"命令会产生错误。为避免此情况，首先使用"designmode"脚本命令确定文件状态。然后使用"if/else"语句：如果文件已处于DESIGN模式则直接添加元素；如果文件处于ANALYSIS模式则先切换到DESIGN模式后再添加元素。
    
    
    load("test.icp");
    status = designmode;
    if (status == 1) {
        addelement("Optical Oscilloscope");
    }
    else {
        switchtodesign;
        addelement("Optical Oscilloscope");
    }

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [switchtolayout](./switchtolayout.md)
- [layoutmode](./layoutmode.md)
- [switchtodesign](./switchtodesign.md)
