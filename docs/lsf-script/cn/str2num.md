<!--
Translation from English documentation
Original command: str2num
Translation date: 2026-02-04 22:50:15
-->

# str2num

转换 一个 字符串 into 一个 floating point 数字. Use 该 format 脚本 命令 到 change 该 precision 的 该 output. 

**语法** |  **描述**  
---|---  
out = str2num(字符串);  |  转换 字符串 into 一个 数字.   
  
**示例**

转换 一个 字符串 into 一个 数字. 
    
    
    ?str2num("1+2");
    3

Compare 该 output 使用  almostequal  . 
    
    
    ?almostequal(str2num("1.5677"), 1.5677);
    result: 
    1  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ " ](/hc/en-us/articles/360034410394--) , [ \+ ](/hc/en-us/articles/360034410254--) , [ ? ](/hc/en-us/articles/360034410434--) , [ endl ](/hc/en-us/articles/360034410414-endl) , [ write ](/hc/en-us/articles/360034411134-write) , [ format ](/hc/en-us/articles/360034931913-format) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript) , [ almostequal ](/hc/en-us/articles/360034410294-almostequal)
