# now

Display the Unix time

**Syntax** |  **Description**  
---|---  
?now; |  Displays the current UNIX time  
  
### Example
    
    
    ?now;
    result:
    1494022382266

Get the simulation job runtime
    
    
    load("simulationfile");  
    switchtolayout;  
    ct1=now;  
    run;  
    ct2=now;  
    ctmin=(ct2-ct1)/1000/60;  
    ctsec=(ct2-ct1)/1000/60*60;  
    ?"CPU runtime: "+ num2str(ctmin) +" min";  
    ?"CPU runtime: "+ num2str(ctsec) +" sec";
