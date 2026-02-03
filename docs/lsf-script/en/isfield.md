# isfield

The script command checks whether input is a field. 

**Syntax** |  **Description**  
---|---  
value= isfield(input, field);  |  Determine whether ‘input contains filed name ‘field’. It returns logical 1 (true) if ‘input contains ‘field’, and logical 0 (false) otherwise.   
  
###  Example 
    
    
    >x=struct;
    >x.t=10;
    >?isfield(x,'t');
    result: 
    1

###  See Also 

[ issweep ](/hc/en-us/articles/360034411634-issweep) , [ isstruct ](/hc/en-us/articles/360034411654-isstruct) , [ iscell ](/hc/en-us/articles/360034932273-iscell) , [ getfield ](/hc/en-us/articles/360034411674-getfield) , [ setfield ](/hc/en-us/articles/360034932313-setfield)
