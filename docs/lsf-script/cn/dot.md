<!--
Translation from English documentation
Original command: dot
Translation date: 2026-02-03 23:11:24
-->

# .

检索数据集的参数和属性。这不是数学点积函数，请参阅[ dot](/hc/en-us/articles/360034925773-dot)命令。

**Syntax** |  **Description**  
---|---  
result = A.result; |  从现有数据集A中检索参数或属性"result"。结果为标量矩阵。  
  
 **示例**

 此示例从profile监视器检索数据集结果"E"，然后使用[ getparameter](/hc/en-us/articles/360034409514-getparameter)命令获取"f"参数，并使用[ getattribute](/hc/en-us/articles/360034409534-getattribute)命令从数据集中获取"Ex"和"E2"属性。请注意，f、Ex和E2都是标量矩阵，类似于使用[ getdata](/hc/en-us/articles/360034409834-getdata)命令获得的结果。
    
    
    E = getresult("profile","E");
     f = E.getparameter("f");  # 参数f
     Ex = E.getattribute("Ex"); # 电场的x分量
     E2 = E.getattribute("E2"); # 电场强度，注意这仅在E为向量时有效

 注意，也可以使用"."运算符直接检索参数和属性。例如：
    
    
    E = getresult("profile","E");
     f = E.f;  # 参数f
     Ex = E.Ex; # 电场的x分量
     E2 = E.E2; # 电场强度，注意这仅在E为向量时有效

 **参见**

- [matrixdataset](./matrixdataset.md)
- [rectilineardataset](./rectilineardataset.md)
- [getparameter](./getparameter.md)
- [getattribute](./getattribute.md)
- [visualize](./visualize.md)
- [getelectric](./getelectric.md)
- [getmagnetic](./getmagnetic.md)
