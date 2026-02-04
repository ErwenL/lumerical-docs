<!--
Translation from English documentation
Original command: quote
Translation date: 2026-02-04 22:50:14
-->

# "

" 和 ' 是 字符串 operators. Strings 可以 为 created 使用 single 或 double quotes.

The following escape sequences 是 recognized 当 creating strings 使用 double quotes:

\" |  double quotes 在 字符串  
---|---  
\n |  newline (linefeed) character 在 字符串  
\\\ |  backslash 在 字符串  
**语法** |  **描述**  
---|---  
out="my 字符串"; |  use double quotes 到 创建 strings  
  
_ NOTE: Literal backslashes 和 double quotes  _

It 是 always possible 到 创建 一个 literal backslash 在 一个 字符串 使用 \\\\. However, \ also results 在 一个 literal backslash, IF it it 将 not 为 interpreted as part 的 一个 escape sequence (\n, \", \\\\). This note 是 important 当 storing paths 在 strings.

Suppose we want 到 创建 该 字符串  C:\Program Files\Lumerical  . The following three commands 是 valid 和 equivalent:
    
    
    mystring = 'C:\Program Files\Lumerical';  # use single quotes
    mystring = "C:\Program Files\Lumerical";  # use double quotes
    mystring = "C:\\Program Files\\Lumerical"; # use double quotes 和 \\ escape character

However, suppose we want 到 创建 该 字符串  C:\Program Files\Lumerical\  . The only difference 是 该 additional backslash at 该 end 的 该 字符串. The following two commands 是 valid 和 equivalent:
    
    
    mystring = 'C:\Program Files\Lumerical\';   # use single quotes
    mystring = "C:\\Program Files\\Lumerical\\"; # use double quotes 和 \\ escape character

The other potential 命令, 其中 we use 一个 single backslash, 是 not valid syntax 和 将 result 在 一个 error.
    
    
    mystring = "C:\Program Files\Lumerical\";  # use double quotes

The problem 是 该 该 脚本 interpreter 将 interpret 该 final \" as 一个 escape character 用于 一个 literal double quote, rather than as 一个 single backslash 和 一个 closing double quote. When interpreted 此 way, 该 命令 results 在 一个 syntax error because there 是 no double quote character closing 该 字符串.

**示例**

Store 一个 监视器 name 在 一个 字符串.
    
    
    m="time_monitor";
    t=getdata(m,"t");
    Ex=getdata(m,'Ex');

Single 和 Double quotes within strings
    
    
    ?"This 是 如何 you \"double quote\" 一个 word";
    This 是 如何 you "double quote" 一个 word
    ?"This 是 如何 you 'single quote' 一个 word";
    This 是 如何 you 'single quote' 一个 word 

This 是 如何 you 添加 一个 backslash 到 一个 字符串. If 该 backslash 是 在 该 middle 的 一个 字符串, you 可以 use \ 或 \\\ 到 创建 一个 backslash. However, 当 该 backslash 是 at 该 end 的 一个 字符串, you MUST use \\\ 到 创建 该 backslash. A single backslash 将 cause 一个 syntax error because 该 backslash 和 该 closing quote (i.e. \") 将 为 interpreted as 一个 literal double quote within 该 字符串, rather than as 一个 backslash 和 一个 closing quote.
    
    
    ?"Backslash 在 该 middle \ 的 一个 字符串";
    Backslash 在 该 middle \ 的 一个 字符串
    ?"Backslash 在 该 middle \\ 的 一个 字符串";
    Backslash 在 该 middle \ 的 一个 字符串
    ?"Backslash 在 该 end 的 一个 字符串\\";
    Backslash 在 该 end 的 一个 字符串\
     ?"Backslash 在 该 end 的 一个 字符串\";
    syntax error: prompt line: 1

This 是 如何 users 可以 创建 multi-line strings 使用 double quote strings. Users 可以 use 该  endl  special character between strings, 或 该 \n escape character within strings.
    
    
    ?"This 是 如何 you 创建" + endl + "multi-line strings";
    This 是 如何 you 创建
    multi-line strings
    ?"This 是 如何 you 创建 \nmulti-line strings";
    This 是 如何 you 创建 
    multi-line strings 

**参见**

[ List 的 commands](/hc/en-us/articles/360037228834), ['](/hc/en-us/articles/360034931053--), [num2str](/hc/en-us/articles/360034925993-num2str), [+](/hc/en-us/articles/360034410254--), [endl](/hc/en-us/articles/360034410414-endl), [write](/hc/en-us/articles/360034411134-write), [eval](/hc/en-us/articles/360034926013-eval), [system](/hc/en-us/articles/360034410894-system)
