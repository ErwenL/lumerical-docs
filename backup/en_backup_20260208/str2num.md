# str2num

Converts a string into a floating point number. Use the format script command to change the precision of the output. 

**Syntax** |  **Description**  
---|---  
out = str2num(string);  |  Converts string into a number.   
  
**Example**

Convert a string into a number. 
    
    
    ?str2num("1+2");
    3

Compare the output using  almostequal  . 
    
    
    ?almostequal(str2num("1.5677"), 1.5677);
    result: 
    1  

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ " ](/hc/en-us/articles/360034410394--) , [ \+ ](/hc/en-us/articles/360034410254--) , [ ? ](/hc/en-us/articles/360034410434--) , [ endl ](/hc/en-us/articles/360034410414-endl) , [ write ](/hc/en-us/articles/360034411134-write) , [ format ](/hc/en-us/articles/360034931913-format) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript) , [ almostequal ](/hc/en-us/articles/360034410294-almostequal)
