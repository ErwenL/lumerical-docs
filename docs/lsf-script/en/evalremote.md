# evalremote

An interoperability command that will send a script commnad(s) to the server product and executes it there 

**Syntax** |  **Description**  
---|---  
evalremote(s,"y=x^2;");  |  Sends command y=x^2; to the server via an open session  s  and executes it   
  
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

[ opensession ](/hc/en-us/articles/360034407894-evalremote) , [ closesession ](/hc/en-us/articles/360034407854-closesession) , [ putremotedata ](/hc/en-us/articles/360034928053-putremotedata) , [ getremotedata ](/hc/en-us/articles/360034407874-getremotedata)
