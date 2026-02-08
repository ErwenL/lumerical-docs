# lookupclose

Closes a lookup table file previously created with a [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) command. 

**Syntax** |  **Description**  
---|---  
lookupclose ("filename");  |  Closes a file previously created with a lookupopen command. This command is required in order to close any file open by  lookupopen  .   
  
**Example**

In order to create the lookup table “new.xml” with table named “new_extracted”: 
    
    
    #open file to write lookup table
    lookupopen("new.xml", "new_extracted" );
    ...
    #write design/extracted pair
    lookupwrite( "new.xml", design, extracted );
    ...
    #close file
    lookupclose("new.xml");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) , [ lookupread ](/hc/en-us/articles/360034928333-lookupread) , [ lookupwrite ](/hc/en-us/articles/360034928353-lookupwrite) , [ lookupreadtable ](/hc/en-us/articles/360034928393-lookupreadtable) , [ lookupreadvalue ](/hc/en-us/articles/360034928413-lookupreadvalue) , [ lookupreadnportsparameter ](/hc/en-us/articles/360034408274-lookupreadnportsparameter) , [ lookupappend ](/hc/en-us/articles/360034928433-lookupappend) , [ insert ](/hc/en-us/articles/360034928453-insert)
