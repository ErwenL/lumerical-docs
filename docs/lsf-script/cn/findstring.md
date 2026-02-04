<!--
Translation from English documentation
Original command: findstring
Translation date: 2026-02-04 22:49:49
-->

# findstring

返回 该 position 的 一个 given substring 在 一个 字符串. 

**语法** |  **描述**  
---|---  
pos = findstring(s,s1);  |  返回 该 position 的 该 first instance substring s1 在 s. If s1 是 not found 在 s, it 返回 -1.   
pos = findstring(s,s1,p0);  |  返回 该 position 的 该 first instance substring s1 在 s, starting at position p0. If s1 是 not found 在 s, starting 从 p0, it 返回 -1.   
  
**示例**

These 是 some examples 的 如何 到 find 一个 substring 在 一个 字符串. 
    
    
    ?findstring("test12test34","test34");
    result: 
    7
    ?findstring("test12test34","test");
    result: 
    1
    ?findstring("test12test34","test",4);
    result: 
    7
    ?findstring("test12test34","test",8);
    result: 
    -1

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 长度 ](/hc/en-us/articles/360034925653-长度) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ replacestring ](/hc/en-us/articles/360034926073-replacestring) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ splitstring ](/hc/en-us/articles/360034926093-splitstring) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
