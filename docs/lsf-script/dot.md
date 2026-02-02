# .

Retrieves the parameters and attributes of datasets. This is not the math dot product function, see the [ dot](/hc/en-us/articles/360034925773-dot) command.

**Syntax** |  **Description**  
---|---  
result = A.result; |  Retrieves the parameter or attribute "result" from the existing dataset A. The result is a scalar matrix.  
  
**Examples**

This example retrieves the dataset results "E" from a profile monitor, and then uses the [ getparameter ](/hc/en-us/articles/360034409514-getparameter) command to get the "f" parameter, and the [ getattribute ](/hc/en-us/articles/360034409534-getattribute) command to get the "Ex" and "E2" attributes from the dataset. Note that f, Ex and E2 are all scalar matrices, like the results one would get with the [ getdata ](/hc/en-us/articles/360034409834-getdata) command.
    
    
    E = getresult("profile","E");
    f = E.getparameter("f");  # the parameter f
    Ex = E.getattribute("Ex"); # the x component of the electric field
    E2 = E.getattribute("E2"); # the electric field intensity, note that this only works if E is a vector

Note that one can also use the "." operator to retrieve the parameters and attributes directly. For example:
    
    
    E = getresult("profile","E");
    f = E.f;  # the parameter f
    Ex = E.Ex; # the x component of the electric field
    E2 = E.E2; # the electric field intensity, note that this only works if E is a vector

**See Also**

[ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ getparameter ](/hc/en-us/articles/360034409514-getparameter) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ getelectric ](/hc/en-us/articles/360034409974-getelectric) , [ getmagnetic ](/hc/en-us/articles/360034930293-getmagnetic)
