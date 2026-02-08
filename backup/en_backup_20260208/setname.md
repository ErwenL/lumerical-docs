# setname

The script command setname is used to set the name of a datset. 

**Syntax** |  **Description**  
---|---  
setname("test");  |  Returns the name of the dataset of the variable a.   
  
**Example**

The following is a short example in which we create a matrix dataset named tt and assign it to variable named T. Using the setname script command the name of the dataset can be changed. 
    
    
    T = matrixdataset("tt"); 
    T.setname("test");
    ?getname(T);
    test
    ?T.getname;
    test

**See Also**

[ getname ](/hc/en-us/articles/360034929373-getname) , [ Datasets ](/hc/en-us/articles/360034409554-Datasets)
