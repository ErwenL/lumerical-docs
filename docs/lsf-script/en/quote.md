# "

" and ' are string operators. Strings can be created with single or double quotes.

The following escape sequences are recognized when creating strings with double quotes:

\" |  double quotes in string  
---|---  
\n |  newline (linefeed) character in string  
\\\ |  backslash in string  
**Syntax** |  **Description**  
---|---  
out="my string"; |  use double quotes to create strings  
  
_ NOTE: Literal backslashes and double quotes  _

It is always possible to create a literal backslash in a string with \\\\. However, \ also results in a literal backslash, IF it it will not be interpreted as part of an escape sequence (\n, \", \\\\). This note is important when storing paths in strings.

Suppose we want to create the string  C:\Program Files\Lumerical  . The following three commands are valid and equivalent:
    
    
    mystring = 'C:\Program Files\Lumerical';  # use single quotes
    mystring = "C:\Program Files\Lumerical";  # use double quotes
    mystring = "C:\\Program Files\\Lumerical"; # use double quotes and \\ escape character

However, suppose we want to create the string  C:\Program Files\Lumerical\  . The only difference is the additional backslash at the end of the string. The following two commands are valid and equivalent:
    
    
    mystring = 'C:\Program Files\Lumerical\';   # use single quotes
    mystring = "C:\\Program Files\\Lumerical\\"; # use double quotes and \\ escape character

The other potential command, where we use a single backslash, is not valid syntax and will result in an error.
    
    
    mystring = "C:\Program Files\Lumerical\";  # use double quotes

The problem is that the script interpreter will interpret the final \" as an escape character for a literal double quote, rather than as a single backslash and a closing double quote. When interpreted this way, the command results in a syntax error because there is no double quote character closing the string.

**Examples**

Store a monitor name in a string.
    
    
    m="time_monitor";
    t=getdata(m,"t");
    Ex=getdata(m,'Ex');

Single and Double quotes within strings
    
    
    ?"This is how you \"double quote\" a word";
    This is how you "double quote" a word
    ?"This is how you 'single quote' a word";
    This is how you 'single quote' a word 

This is how you add a backslash to a string. If the backslash is in the middle of a string, you can use \ or \\\ to create a backslash. However, when the backslash is at the end of a string, you MUST use \\\ to create the backslash. A single backslash will cause a syntax error because the backslash and the closing quote (i.e. \") will be interpreted as a literal double quote within the string, rather than as a backslash and a closing quote.
    
    
    ?"Backslash in the middle \ of a string";
    Backslash in the middle \ of a string
    ?"Backslash in the middle \\ of a string";
    Backslash in the middle \ of a string
    ?"Backslash in the end of a string\\";
    Backslash in the end of a string\
     ?"Backslash in the end of a string\";
    syntax error: prompt line: 1

This is how users can create multi-line strings with double quote strings. Users can use the  endl  special character between strings, or the \n escape character within strings.
    
    
    ?"This is how you create" + endl + "multi-line strings";
    This is how you create
    multi-line strings
    ?"This is how you create \nmulti-line strings";
    This is how you create 
    multi-line strings 

**See Also**

[ List of commands](/hc/en-us/articles/360037228834), ['](/hc/en-us/articles/360034931053--), [num2str](/hc/en-us/articles/360034925993-num2str), [+](/hc/en-us/articles/360034410254--), [endl](/hc/en-us/articles/360034410414-endl), [write](/hc/en-us/articles/360034411134-write), [eval](/hc/en-us/articles/360034926013-eval), [system](/hc/en-us/articles/360034410894-system)
