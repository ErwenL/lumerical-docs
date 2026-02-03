# jsonsave

Saves data to a JSON file.

**Syntax** |  **Description**  
---|---  
jsonsave("filename"); |  Saves all data in workspace to a JSON file using the explicit Lumerical Cell and Matrix Option 1 notation. For detailed information on the notations, please see the page [ JSON files ](/hc/en-us/articles/360034936933-JSON-files) .  
jsonsave("filename", var1, var2, ...); |  Saves the specified data variables to a JSON file using the explicit Lumerical Cell and Matrix Option 1 notation. For detailed information on the notations, please see the page [ JSON files ](/hc/en-us/articles/360034936933-JSON-files) .  
  
### Example

The following code example shows how to save the data in Lumerical workspace to a JSON file.
    
    
    # Create variables a and b
    a = 1;
    b = [1+2i, 3+4i];
    jsonsave("test_json.json");

Data in the "test_json.json" file:

{ "a" : 1, "b" : { "_complex" : true, "_data" : [ 1, 2, 3, 4 ], "_size" : [ 1, 2 ], "_type" : "matrix" } }  
  
Specify the variables you would like to save in your workspace.
    
    
    a = 1;  
    b = [1+2i, 3+4i];  
    string = "string";  
    jsonsave("test_json.json",a,string);

Creates the following json file.
    
    
    {  
     "a" : 1,  
     "string" : "string"  
    }

**See Also**

[ jsonload ](/hc/en-us/articles/360034408194-jsonload) , [ jsonloads ](/hc/en-us/articles/360038741854) , [ jsonsaves ](/hc/en-us/articles/360039235453) , [ JSON files ](/hc/en-us/articles/360034936933-JSON-files)
