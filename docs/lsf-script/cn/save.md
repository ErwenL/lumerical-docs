<!--
Translation from English documentation
Original command: save
Translation date: 2026-02-04 22:50:14
-->

# save

Saves 一个 仿真 project 文件. If 该 仿真 has been run, 该 文件 将 also contain 该 仿真 results, such as sweep 和 optimization 数据.

**语法** |  **描述**  
---|---  
save; |  Open 一个 文件 browser 到 save 该 文件. This 函数 does not 返回 any 数据.  
save(文件名); |  Save 使用 该 specified name 到 该 current working directory. A path 可以 为 specified.  
  
**示例**

Saves 该 current profile 文件
    
    
    save("project_name"); # saves 该 文件 在 该 current working directory
    save("C:\Downloads\project_name.fsp") # saves 该 文件 在 一个 path specified

### **参见**

[ load](/hc/en-us/articles/360034410834-load), [ loaddata](/hc/en-us/articles/360034411214-loaddata), [ savedata](/hc/en-us/articles/360034411174-savedata), [ savedcard](/hc/en-us/articles/360034411154-savedcard)
