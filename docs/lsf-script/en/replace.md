# replace

Replaces a substring of a string with a new string. The start position of the substring must be specified. This function can also be used to add a substring to a string at a given position. 

**Syntax** |  **Description**  
---|---  
snew = replace(s,pos,len,s1);  |  Replaces len characters of s, starting at position pos, with the string in s1. If len is 0, it will insert the string s1 between pos-1 and pos. If len is -1 (or any values less than 0) it will replace all remaining characters in s with s1, starting at pos. The position pos can be 1 to length(s).   
  
**Example**

These examples show how to replace substrings in a string or insert a substring at a specific location in a string. 
    
    
    ?replace("1234567",3,1,"aa");
    12aa4567
    ?replace("1234567",3,0,"aa"); #insert a string
    12aa34567
    ?replace("1234567",3,-1,"aa");
    12aa

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ length ](/hc/en-us/articles/360034925653-length) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ splitstring ](/hc/en-us/articles/360034926093-splitstring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
