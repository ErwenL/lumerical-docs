<!--
Translation from English documentation
Original command: addparameter
Translation date: 2026-02-04 22:49:29
-->

# addparameter

添加 一个 参数 到 一个 existing dataset. 

**语法** |  **描述**  
---|---  
R.addparameter("p_name", p);  |  添加 该 参数 p 到 该 existing dataset R.   
R.addparameter("p1_name", p1, "p2_name", p2);  |  添加 该 interdependent 参数 p1_name, p2_name 到 该 R dataset.  The most common interdependent 参数 是 频率 和 波长. Parameters 该 是 not interdependent 必须 为 added separately.   
  
**示例**

This example uses 一个 矩阵 dataset 到 store cross section (sigma) 数据 as 一个 函数 的 频率. In 此 case, 该 cross section 数据 sigma 是 该 attribute, 和 频率 是 该 参数. To allow 该 用户 到 access 该 频率 参数 在 terms 的 频率 或 波长 , both 频率 (f) 和 波长 (c/f) 是 added as interdependent 参数. 
    
    
    sigma = matrixdataset("cross_section");
    sigma.addparameter("lambda",c/f,"f",f); # 添加 参数 f 和 lambda
    sigma.addattribute("sigma",CS); # 添加 attribute CS
    visualize(sigma); # visualize 此 dataset 在 该 Visualizer

**参见**

[ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ addattribute ](/hc/en-us/articles/360034929873-addattribute) , [ addparameter ](/hc/en-us/articles/360034409494-addparameter) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets) , [ getparameter ](/hc/en-us/articles/360034409514-getparameter) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset)
