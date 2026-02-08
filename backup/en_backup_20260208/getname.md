# getname

The script command getname is used to get the name of a datset. 

**Syntax** |  **Description**  
---|---  
?getname(a);  |  Returns the name of the dataset of the variable a.   
?a.getname;  |  Returns the name of the dataset of the variable a.   
  
**Example**

The following is a short example in which we create a matrix dataset named tt and assign it to variable named T. Using the getname script command the name of the dataset can be obtained. 
    
    
    T = matrixdataset("tt"); 
    T.setname("test");
    ?getname(T);
    test
    ?T.getname;
    test

**See Also**

[ setname ](/hc/en-us/articles/360034929353-setname) , [ Datasets ](/hc/en-us/articles/360034409554-Datasets)
