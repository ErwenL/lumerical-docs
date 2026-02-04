<!--
Translation from English documentation
Original command: cleardataset
Translation date: 2026-02-04 22:49:48
-->

# cleardataset

This 命令 clears 该 dataset 从 any current 'np Density' grid attribute. This 是 only useful 用于 keeping 文件 size small. 

**语法** |  **描述**  
---|---  
cleardataset;  |  Clears 该 dataset 从 该 选中的 grid attribute.   
  
**示例**

This example shows 如何 到 import 一个 unstructured dataset '电荷' 到 该 'np Density' grid attribute. 
    
    
    select("np density");
    importdataset("device_data.mat");
    cleardataset;

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ importdataset ](/hc/en-us/articles/360034409114-importdataset) , [ addgridattribute ](/hc/en-us/articles/360034404674-addgridattribute)
