# cell

Creates a cell array variable with specified number of elements. The cell array element can be any data type, such as matrix, string, and dataset.

Since Lumerical 2019b R4 version, users can also declare a cell by using the braces and square brackets declaration method.

**Syntax** |  **Description**  
---|---  
a = {"a", "b", 1, 2.3} |  Creates and initializes a cell array.  
a = cell(n); |  Creates a cell array with n elements.  
a{n} = "string"; |  Adds a string to the specified element of the cell array.  
a{n} = matrix(5,5); |  Adds a field of matrix of 5x5 to the specified element of the cell array.  
a.append(value); |  Appends a value to the end of the cell array.  
a.insert(value,index); |  Inserts a value at index, pushing all elements after the index back, and extending the cell array length by 1. The index must be less than or equal to the current array length, else an error will be thrown.  
a.remove(index); |  Removes a value at the specified index, pulling all elements after the index forward, and shortening the array length by 1. The index must be less than or equal to the current array length, else an error will be thrown.  
a.pop; |  Removes and returns the last value from the cell array.  
a.clear; |  Removes all items from the cell array.  
  
**Examples**

A cell can be created and initialized quickly as follows:
    
    
    myCell = {"a", "b", 1, 2.3};   
      
    # cell with struct  
    myCellWithStruct = {"a", {"b" : 2, "c" : 3}};

The above cell can also be declared more pedantically:
    
    
    myCell = cell(4);  
    myCell{1} = "a";  
    myCell{2} = "b";  
    myCell{3} = 1;  
    myCell{4} = 2.3;  
    
    # cell with struct  
    myCellWithStruct = cell(2);  
    myCellWithStruct{1} = "a";  
    myCellWithStruct{2} = struct;  
    myCellWithStruct{2}.b = 2;  
    myCellWithStruct{2}.c = 3;

The above declaration methods are equivalent and will produce the same output:
    
    
    ?myCell;  
    Cell array with 4 elements  
    
    ?myCell{1};  
    a  
    
    ?myCellWithStruct;  
    Cell array with 2 elements  
    
    ?myCellWithStruct{1};  
    a  
    
    ?myCellWithStruct{2};  
    Struct with fields:  
    b  
    c  
    
    ?myCellWithStruct{2}.b;  
    result:   
    2  

Items can be added, removed, and appended from the cell array with array functions:
    
    
    myCell.append(“c”); #Append “c” to the end of the cell array  
    ?myCell{5}; #The array will be {“a”,”b”,1,2.3,”c”} after append  
    result:  
    c  
    ?myCell;  
    Cell array with 5 elements  
      
    myCell.insert(2,matrix(2,2)); #Add a 2x2 matrix filled with zeroes at index 2  
      
    ?myCell{2}; #The array will be {“a”, matrix(2,2), ”b” ,1,2.3,”c”} after insertion  
    0 0   
    0 0   
      
    myCell.remove(2); #Remove the newly added matrix at index 2  
    ?myCell(2); #The array will be {“a”,”b”,1,2.3,”c”} after removal  
    b  
      
    ?myCell;  
    Cell array with 5 elements  
      
    popped = myCell.pop; #Remove the last element (“c”) and assign it to new variable “popped”  
    ?myCell;  
    Cell array with 4 elements  
    ?popped;  
    c  
      
    myCell.clear; #Clear all elements of cell array  
    ?myCell;  
    Cell array with 0 elements

When two or more objects have similar properties, such as spatial location of "x" and "y", one can define a "cell" with "x" and "y", and get their values:
    
    
        propxy = {"x","y"};  
        out1 = getnamed("rectangle",propxy);  
        out2 = getnamed("monitor",propxy);  
        ?out1.x;  
        ?out2.y; 

In the above example, geometry "rectangle" and monitor "monitor" both have "x" and "y" properties.

**See Also**

[Datasets](/hc/en-us/articles/360034409554-Datasets), [matrixdataset](/hc/en-us/articles/360034409454-matrixdataset), [rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset), [struct](/hc/en-us/articles/360034409574-struct), [splitstring](/hc/en-us/articles/360034926093-splitstring)
