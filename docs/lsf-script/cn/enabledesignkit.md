<!--
Translation from English documentation
Original command: enabledesignkit
Translation date: 2026-02-03 23:51:24
-->

# enabledesignkit

启用Design Kits文件夹中的设计套件。 

**Syntax** |  **Description**  
---|---  
enabledesignkit("name", ["version"]);  |  启用已安装到Design Kit文件夹中具有版本号"version"的设计套件。"version"是可选参数，默认为空字符串。   
  
**Example**
    
    
    #enables the design kit "LCML" with version v1.1 from the element library ‘Design kits’ folder
    enabledesignkit("LCML", "v1.1");

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [removedesignkit](./removedesignkit.md)
- [reloaddesignkit](./reloaddesignkit.md)
- [loaddesignkit](./loaddesignkit.md)
- [disabledesignkit](./disabledesignkit.md)
- [installdesignkit](./installdesignkit.md)
- [uninstalldesignkit](./uninstalldesignkit.md)
