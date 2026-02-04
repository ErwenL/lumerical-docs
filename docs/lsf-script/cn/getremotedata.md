<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getremotedata -->

# getremotedata

**语法** | **描述**
---|---
y=getremotedata(s,'x'); | Creates 变量 y in the local client workspace that has 值 of x in the server workspace via an active session s.

**示例**

The following code 示例 opens Device as a server, sends local 变量 'x' to Device workspace followed by a 命令 to manipulate the 变量 and the retrieves the result before closing the session:
    #Opend Device session
    s2=opensession('device');
    #Declare local 变量 x
    x=2;
    #Send the local 变量 to Device workspace via API
    putremotedata(s2,'x_device',x);
    #Send 脚本 命令 to Device via API andsquare the 变量
    evalremote(s2,"y_device=x_device^2;");
    #Get the 变量 from Device worksapace via API 
    ?y=getremotedata(s2,'y_device');
    #Close the session
    closesession(s2);

The following code 示例 opens Device as a server, sends local 变量 'x' to Device workspace followed by a 命令 to manipulate the 变量 and the retrieves the result before closing the session:
    #Opend Device session
    s2=opensession('device');
    #Declare local 变量 x
    x=2;
    #Send the local 变量 to Device workspace via API
    putremotedata(s2,'x_device',x);
    #Send 脚本 命令 to Device via API andsquare the 变量
    evalremote(s2,"y_device=x_device^2;");
    #Get the 变量 from Device worksapace via API 
    ?y=getremotedata(s2,'y_device');
    #Close the session
    closesession(s2);

**另请参阅**

[ opensession ](/hc/en-us/articles/360034407874-getremotedata) , [ closesession ](/hc/en-us/articles/360034407854-closesession) , [ putremotedata ](/hc/en-us/articles/360034928053-putremotedata) , [ evalremote ](/hc/en-us/articles/360034407894-evalremote)
