# addobject

Adds an object from the object library in FDTD and MODE. The command can also be used to return the names of all the available objects and analysis groups in the objects library. 

**Syntax** |  **Description**  
---|---  
addobject("script_ID");  |  Adds an object from the object library.  This function does not return any data.   
A = addobject;  |  Returns names of all the objects in the library and saves it in a cell array named "A".   
  
**Example**

Add a rounded cylinder object from the object library. 
    
    
    addobject("rounded_cyl");
    set("name","test_cyl");

Print the name of all the available elements. 
    
    
    A = addobject;
    L = length(A);
    for (i = 1:L) {
        ?A{i};
    }

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ addtogroup ](/hc/en-us/articles/360034408454-addtogroup) , [ addstructuregroup ](/hc/en-us/articles/360034924093-addstructuregroup) , [ addanalysisgroup ](/hc/en-us/articles/360034404074-addanalysisgroup)
