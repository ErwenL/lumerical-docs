<!--
Translation from English documentation
Original command: encryptscript
Translation date: 2026-02-03 23:52:55
-->

# encryptscript

将指定脚本文件的副本保存为加密格式。新文件将具有.lsfx文件扩展名。对脚本进行加密允许与他人共享脚本，但不允许他们查看脚本内容。

**Syntax** |  **Description**  
---|---  
encryptscript("filename.lsf"); |  推荐：加密脚本副本，与早期版本不兼容。新文件将命名为"filename.lsfx"。  
encryptscript("filename.lsf", 1); |  传统方式：加密脚本副本，与早期版本兼容。  
encryptscript("filename.lsf", "new_filename"); |  指定备用文件名，与早期版本不兼容。新文件将命名为"filename.lsfx"。  
encryptscript("filename.lsf", "new_filename", 1); |  指定备用文件名，与早期版本兼容。新文件将命名为"filename.lsfx"。  
  
2020B版本加密的脚本将与2020A及更早版本不兼容，除非向encryptscript传递额外参数(1)以指定传统兼容性。2020A及更早版本加密的脚本将继续与后续版本兼容。

### 示例

如果脚本文件已加密，用户可以通过在脚本提示中输入文件名来运行脚本文件。但是，用户将无法看到文件的内容。
    
    
     filename #它将运行加密的脚本文件filename.lsfx

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
