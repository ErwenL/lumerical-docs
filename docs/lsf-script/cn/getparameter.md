<!--
Translation from English documentation
Original command: getparameter
Translation date: 2026-02-04 22:50:00
-->

# getparameter

获取 一个 参数 从 一个 existing dataset. 

**语法** |  **描述**  
---|---  
?getparameter(R);  |  返回 该 names 的 all 该 参数 在 该 dataset R.   
Parameter = R.getparameter("p");  |  Retrieves 该 参数 p 从 该 existing dataset R. The result "Parameter" 是 一个 scalar 矩阵.  See [ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) 用于 details about dimensions 的 attribute 数据.   
Parameter = getparameter(R,"p");  |  Retrieves 该 参数 p 从 该 existing dataset R. The result "Parameter" 是 一个 scalar 矩阵.  See [ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) 用于 details about dimensions 的 attribute 数据.   
  
**示例**

This example retrieves 该 dataset results "E" 从 一个 profile 监视器, 和 那么 uses 该 getparameter 命令 到 获取 该 "f" 参数, 和 该 [ getattribute ](/hc/en-us/articles/360034409534-getattribute) 命令 到 获取 该 "Ex" 和 "E2" attributes 从 该 dataset. 注意 该 f, Ex 和 E2 是 all scalar matrices, like 该 results one would 获取 使用 该 [ getdata ](/hc/en-us/articles/360034409834-getdata) 命令. 
    
    
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

[ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ "." operator ](/hc/en-us/articles/360034925773-dot) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets)
