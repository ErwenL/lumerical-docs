<!--
Translation from English documentation
Original command: substring
Translation date: 2026-02-04 22:50:15
-->

# substring

Extracts 一个 substring 从 一个 字符串. 

**语法** |  **描述**  
---|---  
s1 = substring(s,pos);  |  返回 一个 substring 的 s, starting at position pos 到 该 end 的 s. The position pos 可以 为 1 到 长度(s).   
s1 = substring(s,pos,len);  |  返回 一个 substring 的 s, starting at position pos, 使用 len characters. If len 是 -1 (或 any 值 less than 0) it 返回 该 substring at position pos 到 该 end 的 s. The default 值 的 len 是 -1.   
  
**示例**

The following example shows 该 different ways 到 extract 一个 substring 从 一个 字符串. 
    
    
    ?substring("hello",3);
    llo
    ?substring("hello",3,2);
    ll  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 长度 ](/hc/en-us/articles/360034925653-长度) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ splitstring ](/hc/en-us/articles/360034926093-splitstring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
