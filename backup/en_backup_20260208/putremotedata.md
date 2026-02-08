# putremotedata

An interoperability command that will send a variable from the client workspace into the server workspace via an active session. This works for matrices and strings (and not for structs and cell arrays).

**Syntax** |  **Description**  
---|---  
putremotedata(s,'y',x); |  Creates variable y in the server workspace that has value of x in the client workspace via an active session s.  
  
### Example

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

[ opensession ](/hc/en-us/articles/360034928053-putremotedata) , [ closesession ](/hc/en-us/articles/360034407854-closesession) , [ getremotedata ](/hc/en-us/articles/360034407874-getremotedata) , [ evalremote ](/hc/en-us/articles/360034407894-evalremote)
