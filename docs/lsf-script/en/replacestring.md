# replacestring

Replaces all the instances of a substring in a string with a new string. 

**Syntax** |  **Description**  
---|---  
snew = replacestring(s,s1,s2);  |  Replaces all instances of s1 in s with s2. If s1 is not found, the original string s is returned.   
  
**Example**

Replace a substring in a string at all the places where it occurs. 
    
    
    ?replacestring("test12test34","test","NEWTEST");
    NEWTEST12NEWTEST34

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ length ](/hc/en-us/articles/360034925653-length) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ splitstring ](/hc/en-us/articles/360034926093-splitstring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
