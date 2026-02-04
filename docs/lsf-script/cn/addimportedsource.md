<!--
Translation from English documentation
Original command: addimportedsource
Translation date: 2026-02-04 22:49:29
-->

# addimportedsource

添加 一个 imported 源 到 该 仿真 环境.

**语法** |  **描述**  
---|---  
addimportedsource; |  添加 一个 imported 源 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addimportedsource(struct_data); |  Adds an imported source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 commands 将 添加 一个 imported 源 到 该 仿真 环境, assign 一个 name 到 it 和 load 一个 E field profile 从 一个 *.mat 文件.
    
    
    addimportedsource;
    设置("name","source2");
    # Load 一个 field profile saved 在 Matlab 文件 named myfile.mat
    select("source2");
    importdataset("myfile.mat");

To see 一个 example 的 如何 脚本 commands 可以 为 used 到 创建 一个 imported 源 使用 监视器 数据 go 到 此 KB page: [ Custom 源 profile 从 监视器 数据 ](/hc/en-us/articles/360034383034-Custom-源-profile-从-监视器-数据) .

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ asapimport ](/hc/en-us/articles/360034411274-asapimport) , [ asapload ](/hc/en-us/articles/360034931973-asapload) , [ asapexport ](/hc/en-us/articles/360034931953-asapexport) , [ importdataset ](/hc/en-us/articles/360034409114-importdataset)
