# num2str

Converts an integer, floating point number, or matrix into a string. Matrices can only be 1D or 2D. Users can use the format script command to change the precision of the output or since the 2019b r6 releases, users can specify the format by providing a second argument to the command.

**Syntax** |  **Description**  
---|---  
out = num2str(x); |  Converts the number x into a string. x can also be a 1D or 2D matrix. The tab character (rather than space) will be used as delimiter between columns.  
out = num2str(x, format); |  Converts the number x into a string. x can also be a 1D or 2D matrix. The format type options include:   
**integers** :   
%u: unsigned integer, takes the absolute value of the input   
%d: decimal signed integer, rounds the input   
%i: decimal signed integer, rounds the input   
**floating point** :   
%f: double   
%g: double   
%G: double, capital 'E' used for the exponential notation   
**exponential** :   
%e: double   
%E: double, capital 'E' used for the exponential notation With the above format type options, both width and precision can be defined for the conversion. Boost formatting can also be used. These flags appear directly after the "%" in the format argument:   
**flags** :   
+: shows sign for all numbers   
0: pad to full width with leading zero  
  
**Example**

Convert the number pi into a string.
    
    
    format long;
    ?num2str(pi);
    3.141592653589793

Convert a 2D matrix into a string and write to a text file.
    
    
    X=meshgridx(1:2,1:3);
    ?num2str(X);
    write("filename.txt",num2str(X));> 1 1 1> 2 2 2

Convert the number pi into a string formatted as an integer with a minimum width of 4 characters.
    
    
    ?num2str(pi, "%4d");  
    Warning: prompt line 1: Double values rounded to integers  
    > 3

Convert the number pi into a string formatted as a floating-point number with 3 digits after the decimal place.
    
    
    ?num2str(pi, "%.3f");3.142

Convert the number pi into a string with a minimum width of 8 characters and 3 characters after the decimal place.
    
    
    ?num2str(pi, "%8.3f"); 3.142

Convert the number pi into a string with a minimum width of 8 characters and 3 characters after the decimal place, and pad the full width with leading 0s.
    
    
    ?num2str(pi, "%08.3f");0003.142

Convert the number 4*pi into a string with exponential notation and 4 decimal points.
    
    
    ?num2str(4*pi, "%.4e");1.2566e+01

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ " ](/hc/en-us/articles/360034410394--) , [ \+ ](/hc/en-us/articles/360034410254--) , [ ? ](/hc/en-us/articles/360034410434--) , [ endl ](/hc/en-us/articles/360034410414-endl) , [ write ](/hc/en-us/articles/360034411134-write) , [ format ](/hc/en-us/articles/360034931913-format) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ eval ](/hc/en-us/articles/360034926013-eval) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
