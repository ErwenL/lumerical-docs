# closesession

An interoperability command that will close an active server session of a specified
Lumerical product previously opened via automation API.

| **Syntax**       | **Description**            |
| ---------------- | -------------------------- |
| closesession(s); | Closes an active session s |

### Example

The following code example opens Device as a server, sends local variable 'x' to Device
workspace followed by a command to manipulate the variable and the retrieves the result
before closing the session:

```
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
```

**See Also**

[ opensession ](./closesession.md) , [ putremotedata ](./putremotedata.md) ,
[ getremotedata ](./getremotedata.md) , [ evalremote ](./evalremote.md)
