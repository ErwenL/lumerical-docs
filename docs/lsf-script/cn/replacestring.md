<!--
Translation Status: Completed
Source: docs/lsf-script/en/replacestring.md
Last Updated: 2026-02-03
-->

# replacestring

将字符串中所有子字符串的实例替换为新字符串。

**语法** |  **说明**  
---|---  
snew = replacestring(s,s1,s2);  |  将字符串s中所有s1的实例替换为s2。如果未找到s1，则返回原始字符串s。   
  
**示例**

将字符串中所有出现的子字符串替换为新字符串。
    
    
    ?replacestring("test12test34","test","NEWTEST");
    NEWTEST12NEWTEST34

**另请参见**

- [length](./length.md)
- [substring](./substring.md)
- [findstring](./findstring.md)
- [replace](./replace.md)
- [str2num](./str2num.md)
- [num2str](./num2str.md)
- [splitstring](./splitstring.md)
- [lower](./lower.md)
- [upper](./upper.md)
- [toscript](./toscript.md)
