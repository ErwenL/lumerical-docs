<!-- Translation completed: 2026-02-04 -->
<!-- Original command: geteigensolver -->

# geteigensolver

**语法** | **描述**
---|---
?geteigensolver; | 返回 a list of the properties of the embedded eigensolver
geteigensolver("property"); | This will get the eigensolver properties of the currently selected objects. The returned 值 may be a 数字 or a 字符串, depending on the property.

**示例**

Please open  ring_resonator2.lms  from the [ ring resonator 示例 ](**%20to%20be%20defined%20**) and type in this 命令 
    select("expansion");
    ?geteigensolver;
It will give a list of the parameters of the eigensolver. Any parameters can be obtained, for 示例, type in 
    ?geteigensolver("bend radius");
    result: 
    1e-005  
Will give the bend radius of 10e-6 meter. 
Also see the 示例 in the [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) and [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) 脚本 functions. 

Please open  ring_resonator2.lms  from the [ ring resonator 示例 ](**%20to%20be%20defined%20**) and type in this 命令 
    select("expansion");
    ?geteigensolver;
It will give a list of the parameters of the eigensolver. Any parameters can be obtained, for 示例, type in 
    ?geteigensolver("bend radius");
    result: 
    1e-005  
Will give the bend radius of 10e-6 meter. 
Also see the 示例 in the [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) and [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) 脚本 functions. 

**另请参阅**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ addmode ](/hc/en-us/articles/360034924353-addmode) , [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) , [ addport ](/hc/en-us/articles/360034924793-addport) , [ clearsourcedata ](/hc/en-us/articles/360034929093-clearsourcedata) , [ clearmodedata ](/hc/en-us/articles/360034408774-clearmodedata) , [ clearportmodedata ](/hc/en-us/articles/360034409194-clearportmodedata) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver) , [ updatemodes ](/hc/en-us/articles/360034929073-updatemodes) , [ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ updateportmodes ](/hc/en-us/articles/360034409174-updateportmodes)
