# opensession

An interoperability command that opens a server session of selected Lumerical product via automation API. Once the session is opened, client product can call the server to execute arbitrary Lumerical script command(s) and execute them. Opened Lumerical session also allows to send and get variables from/to workspace. 

**Syntax** |  **Description**  
---|---  
s2=opensession('device');  |  When executed, this command will open a session of Device via the automation API.  Accepted parameters:  'fdtd'  'mode'  'device'  'interconnect'   
  
###  Example 

The following code example opens Device as a server, sends local variable 'x' to Device workspace followed by a command to manipulate the variable and the retrieves the result before closing the session: 
    
    
    #Opend Device session
    s2=opensession('device');
    #Declare local variable x
    x=2;
    #Send the local variable to Device workspace via API
    putremotedata(s2,'x_device',x);
    #Send script command to Device via API andsquare the variable
    evalremote(s2,"y_device=x_device^2;");
    #Get the variable from Device worksapace via API 
    ?y=getremotedata(s2,'y_device');
    #Close the session
    closesession(s2);

**See Also**

[ closesession ](/hc/en-us/articles/360034407854-closesession) , [ putremotedata ](/hc/en-us/articles/360034928053-putremotedata) , [ getremotedata ](/hc/en-us/articles/360034407874-getremotedata) , [ evalremote ](/hc/en-us/articles/360034407894-evalremote)
