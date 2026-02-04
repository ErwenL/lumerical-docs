<!-- Translation completed: 2026-02-04 -->
<!-- Original command: copydcard -->

# copydcard

**语法** | **描述**
---|---
copydcard( "name"); | Will create a global copy of any d-card currently in memory called "name". By default, the new name will be "::global_name". For 示例, copydcard("mode1"); sends mode1 to the deck, named global_mode1.  This 函数 does not 返回 any data.
copydcard( "name", "newname"); | Will create a global copy of any d-card currently in memory called "name". The new name will be "::newname".

**示例**

Sending 模式 to the d-card and run overlap analysis, eg, in the FDE 求解器 
    copydcard("mode1","test_mode1");
    copydcard("mode2","test_mode2");
    ?overlap("test_mode1","test_mode2");
Sending 场 profiles to the d-card and run overlap analysis, eg, in the FDTD 求解器 
    copydcard("::model::R","test_mode1"); # for the fields recorded by R, where R is the 监视器 name
    copydcard("::model::T","test_mode2"); # for the fields recorded by T, where T is the 监视器 name
    ?overlap("test_mode1","test_mode2");

Sending 模式 to the d-card and run overlap analysis, eg, in the FDE 求解器 
    copydcard("mode1","test_mode1");
    copydcard("mode2","test_mode2");
    ?overlap("test_mode1","test_mode2");
Sending 场 profiles to the d-card and run overlap analysis, eg, in the FDTD 求解器 
    copydcard("::model::R","test_mode1"); # for the fields recorded by R, where R is the 监视器 name
    copydcard("::model::T","test_mode2"); # for the fields recorded by T, where T is the 监视器 name
    ?overlap("test_mode1","test_mode2");

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ havedata ](/hc/en-us/articles/360034930213-havedata) , [ cleardcard ](/hc/en-us/articles/360034930273-cleardcard) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ savedcard ](/hc/en-us/articles/360034411154-savedcard)
