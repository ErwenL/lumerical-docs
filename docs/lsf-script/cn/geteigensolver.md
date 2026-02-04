<!--
Translation from English documentation
Original command: geteigensolver
Translation date: 2026-02-04 22:49:59
-->

# geteigensolver

Mode sources, mode expansion monitors, 和 ports 在 FDTD 和 MODE, 和 each individual 单元格 在 EME have embedded eigensolvers. This 脚本 命令 makes it possible 到 获取 该 属性 的 该 eigensolver without 使用 该 GUI. 

**语法** |  **描述**  
---|---  
?geteigensolver;  |  返回 一个 list 的 该 属性 的 该 embedded eigensolver   
geteigensolver("属性");  |  This 将 获取 该 eigensolver 属性 的 该 currently 选中的 对象. The returned 值 可能 为 一个 数字 或 一个 字符串, depending 在 该 属性.   
  
**示例**

Please open  ring_resonator2.lms  从 该 [ ring resonator example ](**%20to%20be%20defined%20**) 和 类型 在 此 命令 
    
    
    select("expansion");
    ?geteigensolver;

It 将 give 一个 list 的 该 参数 的 该 eigensolver. Any 参数 可以 为 obtained, 用于 example, 类型 在 
    
    
    ?geteigensolver("bend radius");
    result: 
    1e-005  

Will give 该 bend radius 的 10e-6 meter. 

Also see 该 examples 在 该 [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) 和 [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) 脚本 functions. 

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ addmode ](/hc/en-us/articles/360034924353-addmode) , [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) , [ addport ](/hc/en-us/articles/360034924793-addport) , [ clearsourcedata ](/hc/en-us/articles/360034929093-clearsourcedata) , [ clearmodedata ](/hc/en-us/articles/360034408774-clearmodedata) , [ clearportmodedata ](/hc/en-us/articles/360034409194-clearportmodedata) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver) , [ updatemodes ](/hc/en-us/articles/360034929073-updatemodes) , [ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ updateportmodes ](/hc/en-us/articles/360034409174-updateportmodes)
