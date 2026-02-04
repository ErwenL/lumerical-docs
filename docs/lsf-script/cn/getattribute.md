<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getattribute -->

# getattribute

**语法** | **描述**
---|---
?getattribute(R); | 返回 the names of all the attributes in the 数据集 R.
Attribute = R.getattribute("a"); | Retrieves the 属性 a from the existing 数据集 R. The result "属性" is a 矩阵 in one of the forms below depending on the type of atrribute:  vertex_scalar_attribute[npts; npar_1; npar_2; ...1]  vertex_vector_attribute[npts; npar_1; npar_2; ...3]  cell_scalar_attribute[ncells; 1]  cell_vector_attribute[ncells; 3]  "npts" is the 数字 of vertices which is equal tothe 长度 of geometric parameters 'x', 'y', 'z'  "ncells" is the 数字 of 元素 equal to 数字 of rows of geometry 参数 '元素'
Attribute = getparameter(R,"a"); | Retrieves the 属性 a from the existing 数据集 R. The result "属性" is a 矩阵 in one of the forms below depending on the type of atrribute:  vertex_scalar_attribute[npts; npar_1; npar_2; ...1]  vertex_vector_attribute[npts; npar_1; npar_2; ...3]  cell_scalar_attribute[ncells; 1]  cell_vector_attribute[ncells; 3]  "npts" is the 数字 of vertices which is equal tothe 长度 of geometric parameters 'x', 'y', 'z'  "ncells" is the 数字 of 元素 equal to 数字 of rows of geometry 参数 '元素'

**示例**

This 示例 retrieves the 数据集 results "E" from a profile 监视器, and then uses the [ getparameter ](/hc/en-us/articles/360034409514-getparameter) 命令 to get the "f" 参数, and the getattribute 命令 to get the "Ex" and "E2" attributes from the 数据集. 注意 that f, Ex and E2 are all scalar matrices, like the results one would get with the [ getdata ](/hc/en-us/articles/360034409834-getdata) 命令. 
    E = getresult("profile","E");
    f = E.getparameter("f");  # the 参数 f
    Ex = E.getattribute("Ex"); # the x component of the electric 场
    E2 = E.getattribute("E2"); # the electric 场 强度, 注意 that this only works if E is a 向量
注意 that one can also use the [ "." 运算符 ](/hc/en-us/articles/360034925773-dot) to retrieve the parameters and attributes directly. For 示例: 
    E = getresult("profile","E");
    f = E.f;  # the 参数 f
    Ex = E.Ex; # the x component of the electric 场
    E2 = E.E2; # the electric 场 强度, 注意 that this only works if E is a 向量

This 示例 retrieves the 数据集 results "E" from a profile 监视器, and then uses the [ getparameter ](/hc/en-us/articles/360034409514-getparameter) 命令 to get the "f" 参数, and the getattribute 命令 to get the "Ex" and "E2" attributes from the 数据集. 注意 that f, Ex and E2 are all scalar matrices, like the results one would get with the [ getdata ](/hc/en-us/articles/360034409834-getdata) 命令. 
    E = getresult("profile","E");
    f = E.getparameter("f");  # the 参数 f
    Ex = E.getattribute("Ex"); # the x component of the electric 场
    E2 = E.getattribute("E2"); # the electric 场 强度, 注意 that this only works if E is a 向量
注意 that one can also use the [ "." 运算符 ](/hc/en-us/articles/360034925773-dot) to retrieve the parameters and attributes directly. For 示例: 
    E = getresult("profile","E");
    f = E.f;  # the 参数 f
    Ex = E.Ex; # the x component of the electric 场
    E2 = E.E2; # the electric 场 强度, 注意 that this only works if E is a 向量

**另请参阅**

[ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) , [ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ "." operator ](/hc/en-us/articles/360034925773-dot) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ getparameter ](/hc/en-us/articles/360034409514-getparameter) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets)
