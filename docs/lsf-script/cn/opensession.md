<!--
Translation from English documentation
Original command: opensession
Translation date: 2026-02-04 22:50:14
-->

# opensession

An interoperability 命令 该 opens 一个 server session 的 选中的 Lumerical product via automation API. Once 该 session 是 opened, client product 可以 call 该 server 到 execute arbitrary Lumerical 脚本 命令(s) 和 execute them. Opened Lumerical session also allows 到 send 和 获取 variables 从/到 workspace. 

**语法** |  **描述**  
---|---  
s2=opensession('device');  |  When executed, 此 命令 将 open 一个 session 的 Device via 该 automation API.  Accepted 参数:  'fdtd'  'mode'  'device'  'interconnect'   
  
###  示例 

The following code example opens Device as 一个 server, sends local 变量 'x' 到 Device workspace followed 通过 一个 命令 到 manipulate 该 变量 和 该 retrieves 该 result before closing 该 session: 
    
    
    #Opend Device session
    s2=opensession('device');
    #Declare local 变量 x
    x=2;
    #Send 该 local 变量 到 Device workspace via API
    putremotedata(s2,'x_device',x);
    #Send 脚本 命令 到 Device via API andsquare 该 变量
    evalremote(s2,"y_device=x_device^2;");
    #获取 该 变量 从 Device worksapace via API 
    ?y=getremotedata(s2,'y_device');
    #Close 该 session
    closesession(s2);

**参见**

[ closesession ](/hc/en-us/articles/360034407854-closesession) , [ putremotedata ](/hc/en-us/articles/360034928053-putremotedata) , [ getremotedata ](/hc/en-us/articles/360034407874-getremotedata) , [ evalremote ](/hc/en-us/articles/360034407894-evalremote)
