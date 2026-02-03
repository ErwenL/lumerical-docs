# getparameter

Gets a parameter from an existing dataset. 

**Syntax** |  **Description**  
---|---  
?getparameter(R);  |  Returns the names of all the parameters in the dataset R.   
Parameter = R.getparameter("p");  |  Retrieves the parameter p from the existing dataset R. The result "Parameter" is a scalar matrix.  See [ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) for details about dimensions of attribute data.   
Parameter = getparameter(R,"p");  |  Retrieves the parameter p from the existing dataset R. The result "Parameter" is a scalar matrix.  See [ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) for details about dimensions of attribute data.   
  
**Examples**

This example retrieves the dataset results "E" from a profile monitor, and then uses the getparameter command to get the "f" parameter, and the [ getattribute ](/hc/en-us/articles/360034409534-getattribute) command to get the "Ex" and "E2" attributes from the dataset. Note that f, Ex and E2 are all scalar matrices, like the results one would get with the [ getdata ](/hc/en-us/articles/360034409834-getdata) command. 
    
    
    E = getresult("profile","E");
    f = E.getparameter("f");  # the parameter f
    Ex = E.getattribute("Ex"); # the x component of the electric field
    E2 = E.getattribute("E2"); # the electric field intensity, note that this only works if E is a vector

Note that one can also use the [ "." operator ](/hc/en-us/articles/360034925773-dot) to retrieve the parameters and attributes directly. For example: 
    
    
    E = getresult("profile","E");
    f = E.f;  # the parameter f
    Ex = E.Ex; # the x component of the electric field
    E2 = E.E2; # the electric field intensity, note that this only works if E is a vector
    

**See Also**

[ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ "." operator ](/hc/en-us/articles/360034925773-dot) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets)
