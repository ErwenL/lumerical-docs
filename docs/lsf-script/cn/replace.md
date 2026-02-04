<!--
Translation from English documentation
Original command: replace
Translation date: 2026-02-04 22:50:14
-->

# replace

Replaces 一个 substring 的 一个 字符串 使用 一个 新的 字符串. The start position 的 该 substring 必须 为 specified. This 函数 可以 also 为 used 到 添加 一个 substring 到 一个 字符串 at 一个 given position. 

**语法** |  **描述**  
---|---  
snew = replace(s,pos,len,s1);  |  Replaces len characters 的 s, starting at position pos, 使用 该 字符串 在 s1. If len 是 0, it 将 insert 该 字符串 s1 between pos-1 和 pos. If len 是 -1 (或 any 值 less than 0) it 将 replace all remaining characters 在 s 使用 s1, starting at pos. The position pos 可以 为 1 到 长度(s).   
  
**示例**

These examples show 如何 到 replace substrings 在 一个 字符串 或 insert 一个 substring at 一个 specific location 在 一个 字符串. 
    
    
    ?replace("1234567",3,1,"aa");
    12aa4567
    ?replace("1234567",3,0,"aa"); #insert 一个 字符串
    12aa34567
    ?replace("1234567",3,-1,"aa");
    12aa

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 长度 ](/hc/en-us/articles/360034925653-长度) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ splitstring ](/hc/en-us/articles/360034926093-splitstring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
