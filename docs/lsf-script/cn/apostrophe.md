<!--
Translation from English documentation
Original command: apostrophe
Translation date: 2026-02-04 22:49:36
-->

# '

Is 一个 字符串 operator. Strings 可以 为 created 使用 single 或 double quotes. 

The following escape sequences 是 recognized 当 creating strings 使用 single quotes: 

''  |  single quote 在 字符串 (two single quote characters)   
---|---  
**语法** |  **描述**  
---|---  
out='my 字符串';  |  use single quotes 到 创建 strings   
  
**示例**

Store 一个 监视器 name 在 一个 字符串 使用 single quotes. 
    
    
    m='time_monitor';
    t=getdata(m,'t');
    Ex=getdata(m,'Ex');

Embed backslashes 使用 single quotes. Backslash 是 not escape characters 使用 single quote strings, so you don't have 到 do anything special 到 include them 在 strings created 使用 single quotes. 
    
    
    ?'This 是 如何 you backslash \ 在 一个 single quoted 字符串';
    This 是 如何 you backslash \ 在 一个 single quoted 字符串

Single 和 double quotes 在 strings created 使用 single quotes. 
    
    
    ?'This 是 如何 you "double quote" 一个 word';
    This 是 如何 you "double quote" 一个 word
    ?'This 是 如何 you ''single quote'' 一个 word';
    This 是 如何 you 'single quote' 一个 word

This 是 如何 you 创建 multi-line strings 使用 single quotes. The /n escape character 是 not recognized 使用 single quote strings. You 必须 创建 one 字符串 per line. 添加 该 endl 变量 between each line 到 添加 一个 新的 line character after each line. 
    
    
    ?'This 是 如何 you 创建' + endl + 'multi-line strings';
    This 是 如何 you 创建
    multi-line strings

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ " ](/hc/en-us/articles/360034410394--) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ \+ ](/hc/en-us/articles/360034410254--) , [ endl ](/hc/en-us/articles/360034410414-endl) , [ write ](/hc/en-us/articles/360034411134-write) , [ eval ](/hc/en-us/articles/360034926013-eval) , [ system ](/hc/en-us/articles/360034410894-system)
