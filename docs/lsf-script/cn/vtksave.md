<!--
Translation from English documentation
Original command: vtksave
Translation date: 2026-02-04 22:50:15
-->

# vtksave

Saves 一个 Lumerical dataset into 该 VTK format. The 命令 only saves rectilinear 和 unstructured datasets. The “文件名” 将 have .vtr appended 用于 rectilinear dataset, .vtu appended 用于 unstructured dataset. The freely available 数据 visualization program Paraview 可以 那么 为 used 到 创建 sophisticated plots 的 your 数据. 

**语法** |  **描述**  
---|---  
vtksave(“文件名”, dataset);  |  Save 该 dataset 在 vtk 文件 的 该 name specified.   
  
**示例**

The following simple example 获取 该 result E, 一个 rectilinear dataset 和 saves into 该 VTK format. 
    
    
    E = getresult("monitor2", "E");
    vtksave("beam.vtr", E);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ datasets ](/hc/en-us/articles/360034409554-Datasets) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ matlabsave ](/hc/en-us/articles/360034928113-matlabsave) , [ Advanced visualizations 使用 ParaView ](/hc/en-us/articles/360034416774-Paraview)
