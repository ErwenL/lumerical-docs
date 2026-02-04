<!-- Translation completed: Tue Feb 03 2026 -->
<!-- Original: save -->

# save

保存仿真项目文件。如果仿真已运行，文件还将包含仿真结果，如扫描和优化数据。

**语法** |  **描述**  
---|---  
save; |  打开文件浏览器保存文件。此函数不返回任何数据。  
save(filename); |  以指定名称保存到当前工作目录。可以指定路径。  
  
**示例**

保存当前配置文件
    
    
    save("project_name"); # saves the file in the current working directory
    save("C:\Downloads\project_name.fsp") # saves the file in a path specified

### **另请参阅**

- [load](./load.md)
- [loaddata](./loaddata.md)
- [savedata](./savedata.md)
- [savedcard](./savedcard.md)
