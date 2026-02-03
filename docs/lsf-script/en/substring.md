# substring

Extracts a substring from a string. 

**Syntax** |  **Description**  
---|---  
s1 = substring(s,pos);  |  Returns a substring of s, starting at position pos to the end of s. The position pos can be 1 to length(s).   
s1 = substring(s,pos,len);  |  Returns a substring of s, starting at position pos, with len characters. If len is -1 (or any value less than 0) it returns the substring at position pos to the end of s. The default value of len is -1.   
  
**Example**

The following example shows the different ways to extract a substring from a string. 
    
    
    ?substring("hello",3);
    llo
    ?substring("hello",3,2);
    ll  

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ length ](/hc/en-us/articles/360034925653-length) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ splitstring ](/hc/en-us/articles/360034926093-splitstring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
