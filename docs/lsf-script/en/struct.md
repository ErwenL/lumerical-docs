# struct

Creates a structure array. Any data type (such as matrix, string, dataset) can be added to structure arrays.

Since Lumerical 2019b R4 version, users can also declare a structure array by using the braces declaration method.

**Syntax** |  **Description**  
---|---  
a = {"one" : "fish", "two" : "fish", "red" : "fish", "blue" : "fish"} |  Creates and initializes a structure array.  
a = struct; |  Creates an structure array.  
a.a = "string"; |  Adds a string field to the structure array.  
a.b = matrix(5,5); |  Adds a field of matrix of 5x5 to the structure array.  
  
**Examples**

A structure can be created and initialized quickly as follows:
    
    
    C = {"a" : [1, 4, 9],  
         "b" : "a string",  
         "d" : matrix(5, 5),  
         "e" : getresult("monitor", "T")};

The above structure array can also be declared more pedantically:
    
    
    C = struct;  
    C.a = [1, 4, 9];   
    C.b = "a string";  
    C.d = matrix(5,5);   
    C.e = getresult("monitor","T");

Both structure arrays are equivalent and will produce the same output:
    
    
    ?C;  
    Struct with fields:  
    a  
    b  
    d  
    e  
    
    ?C.a;  
    result:   
    1 4 9   
      
    ?C.a(2);  
    result:   
    4  
    
    ?C.b;  
    a string  
    
    ?C.d;  
    result:   
    0 0 0 0 0   
    0 0 0 0 0   
    0 0 0 0 0   
    0 0 0 0 0   
    0 0 0 0 0   
    
    ?C.e;  
    T vs lambda/f
    

When two or more objects share the same parameters, a "struct" can be used for all of them:
    
    
        addrect;  
        props = struct;  
        props.x = 1e-6;  
        props.y = 2e-6;  
        setnamed("rectangle",props);  
        addprofile;  
        set(props);

In the above example, both the geometry "rectangle" and the profile monitor have the same x and y values, so the "struct" with given "x,y" can be applied to them in setnamed and/or set.

"struct" can also be used to set the properties directly
    
    
     addcircle( {"name":"c1","x": 1e-6,"y": 2e-6,"radius":0.5e-6});  
     mystruct = {"name":"c2","x":-1e-6,"y":-2e-6,"radius":0.5e-6};  
     addcircle(mystruct);

The above scripts will create two circles "c1" and "c2" located in quadrants I and III with the same radius.

**See Also**

[Datasets](/hc/en-us/articles/360034409554-Datasets), [matrixdataset](/hc/en-us/articles/360034409454-matrixdataset), [rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset), [cell](/hc/en-us/articles/360034929913-cell), [isfield](/hc/en-us/articles/360034932293), [getfield](/hc/en-us/articles/360034411674), [setfield](/hc/en-us/articles/360034932313), [isstruct](/hc/en-us/articles/360034411654)
