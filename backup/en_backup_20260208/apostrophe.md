# '

Is a string operator. Strings can be created with single or double quotes. 

The following escape sequences are recognized when creating strings with single quotes: 

''  |  single quote in string (two single quote characters)   
---|---  
**Syntax** |  **Description**  
---|---  
out='my string';  |  use single quotes to create strings   
  
**Example**

Store a monitor name in a string using single quotes. 
    
    
    m='time_monitor';
    t=getdata(m,'t');
    Ex=getdata(m,'Ex');

Embed backslashes with single quotes. Backslash is not escape characters with single quote strings, so you don't have to do anything special to include them in strings created with single quotes. 
    
    
    ?'This is how you backslash \ in a single quoted string';
    This is how you backslash \ in a single quoted string

Single and double quotes in strings created with single quotes. 
    
    
    ?'This is how you "double quote" a word';
    This is how you "double quote" a word
    ?'This is how you ''single quote'' a word';
    This is how you 'single quote' a word

This is how you create multi-line strings with single quotes. The /n escape character is not recognized with single quote strings. You must create one string per line. Add the endl variable between each line to add a new line character after each line. 
    
    
    ?'This is how you create' + endl + 'multi-line strings';
    This is how you create
    multi-line strings

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ " ](/hc/en-us/articles/360034410394--) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ \+ ](/hc/en-us/articles/360034410254--) , [ endl ](/hc/en-us/articles/360034410414-endl) , [ write ](/hc/en-us/articles/360034411134-write) , [ eval ](/hc/en-us/articles/360034926013-eval) , [ system ](/hc/en-us/articles/360034410894-system)
