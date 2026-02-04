<!--
Translation from English documentation
Original command: addparameter
Translation date: 2026-02-04 01:09:56
-->

# addparameter

向现有数据集添加参数。

**语法** |  **描述**  
---|---  
R.addparameter("p_name", p);  |  向现有数据集R添加参数p。  
R.addparameter("p1_name", p1, "p2_name", p2);  |  向数据集R添加相互依赖的参数p1_name、p2_name。最常见的相互依赖参数是频率和波长。非相互依赖的参数必须单独添加。  
   
**示例**

此示例使用矩阵数据集存储作为频率函数的截面（sigma）数据。在这种情况下，截面数据sigma是属性，频率是参数。为了让用户能够以频率或波长访问频率参数，将频率（f）和波长（c/f）都添加为相互依赖的参数。
    
    
    sigma = matrixdataset("cross_section");
    sigma.addparameter("lambda",c/f,"f",f); # 添加参数f和lambda
    sigma.addattribute("sigma",CS); # 添加属性CS
    visualize(sigma); # 在可视化器中可视化此数据集

**参见**

* [rectilineardataset](https://optics.ansys.com/hc/en-us/articles/360034409474-rectilineardataset)
* [addattribute](https://optics.ansys.com/hc/en-us/articles/360034929873-addattribute)
* [addparameter](https://optics.ansys.com/hc/en-us/articles/360034409494-addparameter)
* [visualize](https://optics.ansys.com/hc/en-us/articles/360034410514-visualize)
* [datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
* [getparameter](https://optics.ansys.com/hc/en-us/articles/360034409514-getparameter)
* [getattribute](https://optics.ansys.com/hc/en-us/articles/360034409534-getattribute)
* [matrixdataset](https://optics.ansys.com/hc/en-us/articles/360034409454-matrixdataset)
