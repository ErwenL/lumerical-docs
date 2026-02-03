# read

Reads data from a text file as a string. The supported file format is ASCII.

**Syntax** |  **Description**  
---|---  
read(filename, size); |  Read a text file as a string for the user defined size 'size'. The default value for size is 1e+6, if not specified. Note: This function will check for the file in the current working directory. If the file to read from is in a different directory, either specify the full path or change the current working directory.  
  
**Note** : This command cannot be used while in [safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**Examples**

If you have a text file called  testfile.txt  with the following strings:

String saved in text file 
    
    
    M=read("testfile.txt");
    
    
    ?M;
    String saved in text file

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ readdata ](/hc/en-us/articles/360034411234-readdata) , [ struct ](/hc/en-us/articles/360034409574-struct) , [ cell ](/hc/en-us/articles/360034929913-cell)
