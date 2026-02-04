<!--
Translation from English documentation
Original command: encryptscript
Translation date: 2026-02-04 22:49:48
-->

# encryptscript

Save 一个 copy 的 该 specified 脚本 文件 在 一个 encrypted format. The 新的 文件 将 have 一个 .lsfx 文件 extension. Encrypting 一个 脚本 allows 一个 脚本 到 为 shared 使用 others, without allowing them 到 see 该 contents 的 该 脚本.

**语法** |  **描述**  
---|---  
encryptscript("文件名.lsf"); |  Recommended: Encrypt 一个 copy 的 该 脚本, not compatible 使用 earlier versions. The 新的 文件 将 为 named "文件名.lsfx".  
encryptscript("文件名.lsf", 1); |  Legacy: Encrypt 一个 copy 的 该 脚本, compatible 使用 earlier versions.  
encryptscript("文件名.lsf", "new_filename"); |  Specify 一个 alternate 文件 name, not compatible 使用 earlier versions. The 新的 文件 将 为 named "文件名.lsfx".  
encryptscript("文件名.lsf", "new_filename", 1); |  Specify 一个 alternate 文件 name, compatible 使用 earlier versions. The 新的 文件 将 为 named "文件名.lsfx".  
  
Scripts encrypted 使用 2020B 将 not 为 compatible 使用 2020A 和 earlier, unless 该 additional 参数 (1) 是 passed 到 encryptscript specifying legacy compatibility. Scripts encrypted 使用 2020A 和 earlier 将 continue 到 为 compatible 使用 later versions.

### 示例

If 该 脚本 文件 是 already encrypted, 用户 可以 run 该 脚本 文件 通过 entering 该 name 的 该 文件 在 该 Script Prompt. However, 用户 将 not 为 able 到 see 该 content 的 该 文件.
    
    
    文件名 # it 将 run 该 encrypted 脚本 文件 文件名.lsfx

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834)
