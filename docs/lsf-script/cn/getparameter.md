<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getparameter -->

# getparameter

**语法** | **描述**
---|---
?getparameter(R); | 返回 the names of all the parameters in the 数据集 R.
Parameter = R.getparameter("p"); | Retrieves the 参数 p from the existing 数据集 R. The result "参数" is a scalar 矩阵.  See [ 数据集 introduction ](/hc/en-us/articles/360034409554-Datasets) for details about 维度 of 属性 data.
Parameter = getparameter(R,"p"); | Retrieves the 参数 p from the existing 数据集 R. The result "参数" is a scalar 矩阵.  See [ 数据集 introduction ](/hc/en-us/articles/360034409554-Datasets) for details about 维度 of 属性 data.

**示例**

This 示例 retrieves the 数据集 results "E" from a profile 监视器, and then uses the getparameter 命令 to get the "f" 参数, and the [ getattribute ](/hc/en-us/articles/360034409534-getattribute) 命令 to get the "Ex" and "E2" attributes from the 数据集. 注意 that f, Ex and E2 are all scalar matrices, like the results one would get with the [ getdata ](/hc/en-us/articles/360034409834-getdata) 命令. 
    E = getresult("profile","E");
    f = E.getparameter("f");  # the 参数 f
    Ex = E.getattribute("Ex"); # the x component of the electric 场
    E2 = E.getattribute("E2"); # the electric 场 强度, 注意 that this only works if E is a 向量
注意 that one can also use the [ "." 运算符 ](/hc/en-us/articles/360034925773-dot) to retrieve the parameters and attributes directly. For 示例: 
    E = getresult("profile","E");
    f = E.f;  # the 参数 f
    Ex = E.Ex; # the x component of the electric 场
    E2 = E.E2; # the electric 场 强度, 注意 that this only works if E is a 向量

This 示例 retrieves the 数据集 results "E" from a profile 监视器, and then uses the getparameter 命令 to get the "f" 参数, and the [ getattribute ](/hc/en-us/articles/360034409534-getattribute) 命令 to get the "Ex" and "E2" attributes from the 数据集. 注意 that f, Ex and E2 are all scalar matrices, like the results one would get with the [ getdata ](/hc/en-us/articles/360034409834-getdata) 命令. 
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

[ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ "." operator ](/hc/en-us/articles/360034925773-dot) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets)
