<!-- Translation completed: Tue Feb 03 2026 -->
<!-- Original: saveelement -->

# saveelement

将元件保存到当前工作目录中的 .ice 文件。

**语法** |  **描述**  
---|---  
saveelement ("name");  |  将元件保存到文件。元件将以当前元件名称保存在当前工作目录中，扩展名为 ICE。  
  
**示例**
    
    
    #adds an element star coupler and saves it to an .ice file in the current working directory
    addelement("Star Coupler");
    saveelement("STAR_1");

**另请参阅**

- [命令列表](./index.md)
- [library](./library.md)
- [addtolibrary](./addtolibrary.md)
- [probe](./probe.md)
- [loadelement](./loadelement.md)
