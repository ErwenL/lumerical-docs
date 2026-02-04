<!-- Translation completed: 2026-02-04 -->
<!-- Original command: cleardataset -->

# cleardataset

**语法** | **描述**
---|---
cleardataset; | Clears the 数据集 from the selected grid 属性.

**示例**

This 示例 shows how to 导入 an unstructured 数据集 'charge' to the 'np Density' grid 属性. 
    select("np density");
    importdataset("device_data.mat");
    cleardataset;

This 示例 shows how to 导入 an unstructured 数据集 'charge' to the 'np Density' grid 属性. 
    select("np density");
    importdataset("device_data.mat");
    cleardataset;

**另请参阅**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ importdataset ](/hc/en-us/articles/360034409114-importdataset) , [ addgridattribute ](/hc/en-us/articles/360034404674-addgridattribute)
