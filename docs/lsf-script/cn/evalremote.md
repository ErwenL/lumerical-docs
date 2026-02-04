<!--
Translation from English documentation
Original command: evalremote
Translation date: 2026-02-04 22:49:48
-->

# evalremote

An interoperability 命令 该 将 send 一个 脚本 commnad(s) 到 该 server product 和 executes it there 

**语法** |  **描述**  
---|---  
evalremote(s,"y=x^2;");  |  Sends 命令 y=x^2; 到 该 server via 一个 open session  s  和 executes it   
  
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

[ opensession ](/hc/en-us/articles/360034407894-evalremote) , [ closesession ](/hc/en-us/articles/360034407854-closesession) , [ putremotedata ](/hc/en-us/articles/360034928053-putremotedata) , [ getremotedata ](/hc/en-us/articles/360034407874-getremotedata)
