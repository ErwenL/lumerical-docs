<!-- Translation completed: 2026-02-04 -->
<!-- Original command: vtksave -->

# vtksave

**语法** | **描述**
---|---
vtksave(“filename”, dataset); | 保存 the 数据集 in vtk 文件 of the name specified.

**示例**

The following simple 示例 gets the result E, a rectilinear 数据集 and saves into the VTK 格式. 
    E = getresult("monitor2", "E");
    vtksave("beam.vtr", E);

The following simple 示例 gets the result E, a rectilinear 数据集 and saves into the VTK 格式. 
    E = getresult("monitor2", "E");
    vtksave("beam.vtr", E);

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ datasets ](/hc/en-us/articles/360034409554-Datasets) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ matlabsave ](/hc/en-us/articles/360034928113-matlabsave) , [ Advanced visualizations with ParaView ](/hc/en-us/articles/360034416774-Paraview)
