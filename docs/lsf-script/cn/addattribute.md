<!--
Translation from English documentation
Original command: addattribute
Translation date: 2026-02-04 22:46:39
-->

# addattribute

添加 an attribute to an existing dataset. 

**语法** |  **描述**  
---|---  
R.addattribute("a_name", a);  |  添加 the scalar attribute a to the dataset R.  See [ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) for details about the required dimensions of attribute 数据.   
R.addattribute("a_vector", a_1, a_2, a_3);  |  添加 the 向量 attribute a_vector to the existing dataset R. The components of the 向量 are a_1, a_2 and a_3.  See [ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) for details about the required dimensions of attribute 数据.   
R.addattribute("a_name", [数据], "type");  |  添加 the attribute "a_name" to the  unstructured  dataset R. [数据] can be in one of the forms below:  vertex_scalar_attribute[npts; npar_1; npar_2; ...1]  vertex_vector_attribute[npts; npar_1; npar_2; ...3]  cell_scalar_attribute[ncells; 1]  cell_vector_attribute[ncells; 3]  (npts is the number of vertices, the length of geometric 参数 'x', 'y', 'z'  cells is the number of elements, equal to number of rows of geometry 参数 'elements' )  The "type" 参数 is an optional string to specify attribute type and can take 值 of "vertex" or "cell". If not provided, the 函数 will guess the attribute type based on the shape of [数据] 参数.   
  
**示例**

This example uses a 矩阵 dataset to store cross section (sigma) 数据 as a 函数 of 频率. In this case, the cross section 数据 sigma is the attribute, and 频率 is the 参数. To allow the user to access the 频率 参数 in terms of 频率 or 波长 , both 频率 (f) and 波长 (c/f) are added as interdependent 参数. 
    
    
    sigma = matrixdataset("cross_section");
    sigma.addparameter("lambda",c/f,"f",f); # 添加 参数 f and lambda
    sigma.addattribute("sigma",CS); # 添加 attribute CS
    visualize(sigma); # visualize this dataset in the Visualizer

Alternatively, one can also 创建 a 向量 rectilinear dataset (with the name E). 
    
    
    E = rectilineardataset("E",x,y,z);
    E.addparameter("f",f);
    E.addattribute("E",Ex,Ey,Ez); # 添加 a 向量 E with the components Ex, Ey and Ez
    visualize(E); # visualize this dataset in the Visualizer

**参见**

- [rectilineardataset](./rectilineardataset.md)
- [addattribute](./addattribute.md)
- [addparameter](./addparameter.md)
- [visualize](./visualize.md)
- [datasets](/hc/en-us/articles/360034409554-Datasets)
- [getparameter](./getparameter.md)
- [getattribute](./getattribute.md)
- [matrixdataset](./matrixdataset.md)
