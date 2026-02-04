<!--
Translation from English documentation
Original command: dot
Translation date: 2026-02-04 22:49:48
-->

# .

Retrieves 该 参数 和 attributes 的 datasets. This 是 not 该 math dot product 函数, see 该 [ dot](/hc/en-us/articles/360034925773-dot) 命令.

**语法** |  **描述**  
---|---  
result = A.result; |  Retrieves 该 参数 或 attribute "result" 从 该 existing dataset A. The result 是 一个 scalar 矩阵.  
  
**示例**

This example retrieves 该 dataset results "E" 从 一个 profile 监视器, 和 那么 uses 该 [ getparameter ](/hc/en-us/articles/360034409514-getparameter) 命令 到 获取 该 "f" 参数, 和 该 [ getattribute ](/hc/en-us/articles/360034409534-getattribute) 命令 到 获取 该 "Ex" 和 "E2" attributes 从 该 dataset. 注意 该 f, Ex 和 E2 是 all scalar matrices, like 该 results one would 获取 使用 该 [ getdata ](/hc/en-us/articles/360034409834-getdata) 命令.
    
    
    E = getresult("profile","E");
    f = E.getparameter("f");  # 该 参数 f
    Ex = E.getattribute("Ex"); # 该 x component 的 该 electric field
    E2 = E.getattribute("E2"); # 该 electric field intensity, note 该 此 only works 如果 E 是 一个 向量

注意 该 one 可以 also use 该 "." operator 到 retrieve 该 参数 和 attributes directly. For example:
    
    
    E = getresult("profile","E");
    f = E.f;  # 该 参数 f
    Ex = E.Ex; # 该 x component 的 该 electric field
    E2 = E.E2; # 该 electric field intensity, note 该 此 only works 如果 E 是 一个 向量

**参见**

[ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ getparameter ](/hc/en-us/articles/360034409514-getparameter) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ getelectric ](/hc/en-us/articles/360034409974-getelectric) , [ getmagnetic ](/hc/en-us/articles/360034930293-getmagnetic)
