# encryptscript

Save a copy of the specified script file in an encrypted format. The new file will have a .lsfx file extension. Encrypting a script allows a script to be shared with others, without allowing them to see the contents of the script.

**Syntax** |  **Description**  
---|---  
encryptscript("filename.lsf"); |  Recommended: Encrypt a copy of the script, not compatible with earlier versions. The new file will be named "filename.lsfx".  
encryptscript("filename.lsf", 1); |  Legacy: Encrypt a copy of the script, compatible with earlier versions.  
encryptscript("filename.lsf", "new_filename"); |  Specify an alternate file name, not compatible with earlier versions. The new file will be named "filename.lsfx".  
encryptscript("filename.lsf", "new_filename", 1); |  Specify an alternate file name, compatible with earlier versions. The new file will be named "filename.lsfx".  
  
Scripts encrypted with 2020B will not be compatible with 2020A and earlier, unless the additional argument (1) is passed to encryptscript specifying legacy compatibility. Scripts encrypted with 2020A and earlier will continue to be compatible with later versions.

### Example

If the script file is already encrypted, user can run the script file by entering the name of the file in the Script Prompt. However, user will not be able to see the content of the file.
    
    
    filename # it will run the encrypted script file filename.lsfx

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834)
