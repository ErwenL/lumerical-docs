# getfield

The script command returns the value of a field from structure input. 

**Syntax** |  **Description**  
---|---  
value= getfield(input, field);  |  Returns the value of a ‘field’ from structure ‘input’.   
  
###  Example 
    
    
    >x=struct;
    >x.t=10;
    >?getfield(x,'t');
    result: 
    10 

###  See Also 

[ isfield ](/hc/en-us/articles/360034932293-isfield) , [ setfield ](/hc/en-us/articles/360034932313-setfield)
