# for

Starts a for loop to allow some operations to be repeated a number of times. A while loop can be implemented when using the three argument version of a for loop.

**Syntax** |  **Description**  
---|---  
for(x=1:100) { ?x; } |  Single argument for loop. The loop will be sequentially executed for each value of x.  
for(x=1; x<= 100; x=x+1) { ?x; } |  Three argument for loop. x=1 at the start of the loop. The loop continues while x <=100 and sets x=x+1 at each pass.  
x=1; for(0; x<10; 0) { ?x; x=x+1; } |  This is equivalent to a while loop that will execute while x<10.  
  
**Examples**

This example shows a simple for loop where x takes the values 1, 3, 5, 7, 9.
    
    
    a=1:2:10;
    for(x=a) { 
     ?x; 
    } 

Nested loops: This example shows a nested for loop.
    
    
    for(i=1:100) { 
     for(j=1:100) { 
      x = i^2+j; 
      ?x; 
     } 
    } 

The following code will get the electric field data from each monitors in this simulation file, then save that data in a series of Lumerical data files. To test this example, download the associated simulation file, run the simulation, then run the following script.
    
    
    run;
    mNames = splitstring(getresult,endl);
     
    for (i=1:length(mNames)) {
     if (haveresult(mNames{i},"E")) {
      E=getresult(mNames{i},"E");   # get a result from that monitor
     } else {
      E = mNames{i} + " did not contain the specified data.";
     }
     savedata(mNames{i},E);     # save data to file
    }

While loops: There is no "while" command in the scripting language, but the "for" command can be used to implement a "while" command. The command  for(0; conditional_expression; 0) {}  is the same as  while(conditional_expression) {}.  The “0” statements in the “for” loop do nothing and are just placeholders because the scripting language expects an argument there.
    
    
    # implementation of a while loop in languages that support while loops
    x=1;
    while(x<10) {
      ?x;
      x=x+1;
    }
    # equivalent implementation of a while loop in Lumerical script language
    x=1;
    for(0; x<10; 0) {
      ?x;
      x=x+1;
    }

**See Also**

[ List of commands](/hc/en-us/articles/360037228834), [ if ](/hc/en-us/articles/360034408294-if)
