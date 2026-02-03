# findstring

Returns the position of a given substring in a string. 

**Syntax** |  **Description**  
---|---  
pos = findstring(s,s1);  |  Returns the position of the first instance substring s1 in s. If s1 is not found in s, it returns -1.   
pos = findstring(s,s1,p0);  |  Returns the position of the first instance substring s1 in s, starting at position p0. If s1 is not found in s, starting from p0, it returns -1.   
  
**Example**

These are some examples of how to find a substring in a string. 
    
    
    ?findstring("test12test34","test34");
    result: 
    7
    ?findstring("test12test34","test");
    result: 
    1
    ?findstring("test12test34","test",4);
    result: 
    7
    ?findstring("test12test34","test",8);
    result: 
    -1

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ length ](/hc/en-us/articles/360034925653-length) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ splitstring ](/hc/en-us/articles/360034926093-splitstring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
