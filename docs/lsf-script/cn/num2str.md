<!--
Translation from English documentation
Original command: num2str
Translation date: 2026-02-04 22:50:14
-->

# num2str

转换 一个 integer, floating point 数字, 或 矩阵 into 一个 字符串. Matrices 可以 only 为 1D 或 2D. Users 可以 use 该 format 脚本 命令 到 change 该 precision 的 该 output 或 since 该 2019b r6 releases, users 可以 specify 该 format 通过 providing 一个 second 参数 到 该 命令.

**语法** |  **描述**  
---|---  
out = num2str(x); |  转换 该 数字 x into 一个 字符串. x 可以 also 为 一个 1D 或 2D 矩阵. The tab character (rather than space) 将 为 used as delimiter between columns.  
out = num2str(x, format); |  转换 该 数字 x into 一个 字符串. x 可以 also 为 一个 1D 或 2D 矩阵. The format 类型 options include:   
**integers** :   
%u: unsigned integer, takes 该 absolute 值 的 该 input   
%d: decimal signed integer, rounds 该 input   
%i: decimal signed integer, rounds 该 input   
**floating point** :   
%f: double   
%g: double   
%G: double, capital 'E' used 用于 该 exponential notation   
**exponential** :   
%e: double   
%E: double, capital 'E' used 用于 该 exponential notation With 该 above format 类型 options, both width 和 precision 可以 为 defined 用于 该 conversion. Boost formatting 可以 also 为 used. These flags appear directly after 该 "%" 在 该 format 参数:   
**flags** :   
+: shows sign 用于 all numbers   
0: pad 到 full width 使用 leading zero  
  
**示例**

转换 该 数字 pi into 一个 字符串.
    
    
    format long;
    ?num2str(pi);
    3.141592653589793

转换 一个 2D 矩阵 into 一个 字符串 和 write 到 一个 text 文件.
    
    
    X=meshgridx(1:2,1:3);
    ?num2str(X);
    write("文件名.txt",num2str(X));> 1 1 1> 2 2 2

转换 该 数字 pi into 一个 字符串 formatted as 一个 integer 使用 一个 minimum width 的 4 characters.
    
    
    ?num2str(pi, "%4d");  
    警告: prompt line 1: Double 值 rounded 到 integers  
    > 3

转换 该 数字 pi into 一个 字符串 formatted as 一个 floating-point 数字 使用 3 digits after 该 decimal place.
    
    
    ?num2str(pi, "%.3f");3.142

转换 该 数字 pi into 一个 字符串 使用 一个 minimum width 的 8 characters 和 3 characters after 该 decimal place.
    
    
    ?num2str(pi, "%8.3f"); 3.142

转换 该 数字 pi into 一个 字符串 使用 一个 minimum width 的 8 characters 和 3 characters after 该 decimal place, 和 pad 该 full width 使用 leading 0s.
    
    
    ?num2str(pi, "%08.3f");0003.142

转换 该 数字 4*pi into 一个 字符串 使用 exponential notation 和 4 decimal points.
    
    
    ?num2str(4*pi, "%.4e");1.2566e+01

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ " ](/hc/en-us/articles/360034410394--) , [ \+ ](/hc/en-us/articles/360034410254--) , [ ? ](/hc/en-us/articles/360034410434--) , [ endl ](/hc/en-us/articles/360034410414-endl) , [ write ](/hc/en-us/articles/360034411134-write) , [ format ](/hc/en-us/articles/360034931913-format) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ eval ](/hc/en-us/articles/360034926013-eval) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
