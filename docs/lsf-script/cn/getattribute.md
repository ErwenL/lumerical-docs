<!--
Translation from English documentation
Original command: getattribute
Translation date: 2026-02-04 22:49:59
-->

# getattribute

获取 一个 attribute 从 一个 existing dataset. 

**语法** |  **描述**  
---|---  
?getattribute(R);  |  返回 该 names 的 all 该 attributes 在 该 dataset R.   
Attribute = R.getattribute("一个");  |  Retrieves 该 attribute 一个 从 该 existing dataset R. The result "Attribute" 是 一个 矩阵 在 one 的 该 forms below depending 在 该 类型 的 atrribute:  vertex_scalar_attribute[npts; npar_1; npar_2; ...1]  vertex_vector_attribute[npts; npar_1; npar_2; ...3]  cell_scalar_attribute[ncells; 1]  cell_vector_attribute[ncells; 3]  "npts" 是 该 数字 的 vertices 该 是 equal tothe 长度 的 geometric 参数 'x', 'y', 'z'  "ncells" 是 该 数字 的 elements equal 到 数字 的 rows 的 geometry 参数 'elements'   
Attribute = getparameter(R,"一个");  |  Retrieves 该 attribute 一个 从 该 existing dataset R. The result "Attribute" 是 一个 矩阵 在 one 的 该 forms below depending 在 该 类型 的 atrribute:  vertex_scalar_attribute[npts; npar_1; npar_2; ...1]  vertex_vector_attribute[npts; npar_1; npar_2; ...3]  cell_scalar_attribute[ncells; 1]  cell_vector_attribute[ncells; 3]  "npts" 是 该 数字 的 vertices 该 是 equal tothe 长度 的 geometric 参数 'x', 'y', 'z'  "ncells" 是 该 数字 的 elements equal 到 数字 的 rows 的 geometry 参数 'elements'   
  
**示例**

This example retrieves 该 dataset results "E" 从 一个 profile 监视器, 和 那么 uses 该 [ getparameter ](/hc/en-us/articles/360034409514-getparameter) 命令 到 获取 该 "f" 参数, 和 该 getattribute 命令 到 获取 该 "Ex" 和 "E2" attributes 从 该 dataset. 注意 该 f, Ex 和 E2 是 all scalar matrices, like 该 results one would 获取 使用 该 [ getdata ](/hc/en-us/articles/360034409834-getdata) 命令. 
    
    
    E = getresult("profile","E");
    f = E.getparameter("f");  # 该 参数 f
    Ex = E.getattribute("Ex"); # 该 x component 的 该 electric field
    E2 = E.getattribute("E2"); # 该 electric field intensity, note 该 此 only works 如果 E 是 一个 向量

注意 该 one 可以 also use 该 [ "." operator ](/hc/en-us/articles/360034925773-dot) 到 retrieve 该 参数 和 attributes directly. For example: 
    
    
    E = getresult("profile","E");
    f = E.f;  # 该 参数 f
    Ex = E.Ex; # 该 x component 的 该 electric field
    E2 = E.E2; # 该 electric field intensity, note 该 此 only works 如果 E 是 一个 向量

**参见**

[ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) , [ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ "." operator ](/hc/en-us/articles/360034925773-dot) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ getparameter ](/hc/en-us/articles/360034409514-getparameter) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets)
