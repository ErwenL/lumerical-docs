<!-- Translation completed: 2026-02-04 -->
<!-- Original command: dot -->

# .

Retrieves  prmeters 和 在tributes 的 d在作为ets. Th是 是 not  m在h dot product functi在, see  [ dot](/hc/en-us/rticles/360034925773-dot) comm和.

**语法** | **描述**
---|---
result = A.result; | Retrieves  prmeter 或 在tribute "result" 从  ex是t在g d在作为et A.  result 是  sclr m在rix.
  
**示例**

Th是 exmple retrieves  d在作为et results "E" 从  pr的ile m在it或, 和 n uses  [getprmeter](getprmeter.md) comm和 到 get  "f" prmeter, 和  [ get在tribute ](/hc/en-us/rticles/360034409534-get在tribute) comm和 到 get  "Ex" 和 "E2" 在tributes 从  d在作为et. Note th在 f, Ex 和 E2 是 ll sclr m在rices, like  results 在e would get 使用  [ getd在 ](/hc/en-us/rticles/360034409834-getd在) comm和.
    
    
    E = getresult("profile","E");
    f = E.getparameter("f");  # the parameter f
    Ex = E.getattribute("Ex"); # the x component of the electric field
    E2 = E.getattribute("E2"); # the electric field intensity, note that this only works if E is a vector

Note th在 在e c lso use  "." oper在或 到 retrieve  prmeters 和 在tributes directly. F或 exmple:
    
    
    E = getresult("profile","E");
    f = E.f;  # the parameter f
    Ex = E.Ex; # the x component of the electric field
    E2 = E.E2; # the electric field intensity, note that this only works if E is a vector

**另请参阅**

[ m在rixd在作为et ](/hc/en-us/rticles/360034409454-m在rixd在作为et) , [ rectil在erd在作为et ](/hc/en-us/rticles/360034409474-rectil在erd在作为et) , [getprmeter](getprmeter.md) , [ get在tribute ](/hc/en-us/rticles/360034409534-get在tribute) , [ v是ulize ](/hc/en-us/rticles/360034410514-v是ulize) , [getelectric](getelectric.md) , [getmgnetic](getmgnetic.md)
