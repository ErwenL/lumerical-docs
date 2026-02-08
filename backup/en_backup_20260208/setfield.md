# setfield

The script command assigns a value to a structure input field.

**Syntax** |  **Description**  
---|---  
output= setfield(input, field,value); |  Assigns a ‘value’ to a structure ‘input’ ‘field’.  
  
### Example
    
    
    >x=struct;
    >x=setfield(x,'t',10);
    >?x.t;
    result: 
    10

### See Also

[ isfield ](/hc/en-us/articles/360034932293-isfield) , [ getfield ](/hc/en-us/articles/360034411674-getfield)
