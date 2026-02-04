<!--
Translation from English documentation
Original command: cp
Translation date: 2026-02-04 22:49:48
-->

# cp

Copies 一个 文件. The copy 可以 为 created 在 一个 specified path.

**语法** |  **描述**  
---|---  
cp("file1","file2"); |  Makes 一个 copy 的 file1 called file2. This 函数 does not 返回 any 数据.  
cp("path1\file1","path2\file2"); |  Copies file1 在 path1 到 file2 在 path2.  
  
**Note** : This command cannot be used while in [safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**示例**

Makes 一个 copy 的 "myscript.lsf" 在 c:\working called "temp.lsf".
    
    
    cp("c:\myscript.lsf","c:\working\temp.lsf");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ mv ](/hc/en-us/articles/360034931593-mv) , [ pwd ](/hc/en-us/articles/360034931773-pwd) , [ copy (对象) ](/hc/en-us/articles/360034408434-copy)
