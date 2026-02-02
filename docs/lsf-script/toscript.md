# toscript

Returns a string containing the equivalent script to generate a variable. This script function is particularly useful when debugging cells and structure variables. 

**Syntax** |  **Description**  
---|---  
out=toscript(variable, expand);  |  Returns a string containing the equivalent script to generate ‘variable’. If ‘expand’ is true, matrix values will also be converted to script, regardless of their size – this can lead to large strings. To prevent the matrix values conversion set expand to ‘false’. The default for 'expand' is true.   
  
**Example**

Create a cell of structure variables and find an equivalent script that generates the same cell. 
    
    
    v=cell(2);
    v{1}=struct;
    v{1}.name='value 1';
    v{1}.value=matrix(4);
    v{1}.value(1)=1;
    v{1}.value(2)=2;
    v{1}.value(3)=3;
    v{1}.value(4)=4;
    v{2}=struct;
    v{2}.name='value 2';
    v{2}.value=matrix(4);
    v{2}.value(1)=5;
    v{2}.value(2)=6;
    v{2}.value(3)=7;
    v{2}.value(4)=8;
    ?toscript(v,true);
    v=cell(2);
    v{1}=struct;
    v{1}.name='value 1';
    v{1}.value=matrix(4);
    v{1}.value(1)=1;
    v{1}.value(2)=2;
    v{1}.value(3)=3;
    v{1}.value(4)=4;
    v{2}=struct;
    v{2}.name='value 2';
    v{2}.value=matrix(4);
    v{2}.value(1)=5;
    v{2}.value(2)=6;
    v{2}.value(3)=7;
    v{2}.value(4)=8;
    ?toscript(v,false); # do not include matrix values
    v=cell(2);
    v{1}=struct;
    v{1}.name='value 1';
    v{1}.value=matrix(4);
    v{2}=struct;
    v{2}.name='value 2';
    v{2}.value=matrix(4);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ length ](/hc/en-us/articles/360034925653-length) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ splitstring ](/hc/en-us/articles/360034926093-splitstring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper)
