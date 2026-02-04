<!--
Translation from English documentation
Original command: copydcard
Translation date: 2026-02-04 22:49:48
-->

# copydcard

Will 创建 一个 global copy 的 any d-card currently 在 memory. 

**语法** |  **描述**  
---|---  
copydcard( "name");  |  Will 创建 一个 global copy 的 any d-card currently 在 memory called "name". By default, 该 新的 name 将 为 "::global_name". For example, copydcard("mode1"); sends mode1 到 该 deck, named global_mode1.  This 函数 does not 返回 any 数据.   
copydcard( "name", "newname");  |  Will 创建 一个 global copy 的 any d-card currently 在 memory called "name". The 新的 name 将 为 "::newname".   
  
**示例**

Sending modes 到 该 d-card 和 run overlap 分析, eg, 在 该 FDE 求解器 
    
    
    copydcard("mode1","test_mode1");
    copydcard("mode2","test_mode2");
    ?overlap("test_mode1","test_mode2");

Sending field profiles 到 该 d-card 和 run overlap 分析, eg, 在 该 FDTD 求解器 
    
    
    copydcard("::model::R","test_mode1"); # 用于 该 fields recorded 通过 R, 其中 R 是 该 监视器 name
    copydcard("::model::T","test_mode2"); # 用于 该 fields recorded 通过 T, 其中 T 是 该 监视器 name
    ?overlap("test_mode1","test_mode2");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ havedata ](/hc/en-us/articles/360034930213-havedata) , [ cleardcard ](/hc/en-us/articles/360034930273-cleardcard) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ savedcard ](/hc/en-us/articles/360034411154-savedcard)
