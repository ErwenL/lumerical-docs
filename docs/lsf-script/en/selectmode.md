# selectmode

Selects a mode from the mode list. All modes found in a simulation are numbered based on their effective index and they are displayed in the mode list in the Eigensolver analysis window.

**Syntax** |  **Description**  
---|---  
selectmode(N); |  Select the Nth mode from the mode list.  
selectmode([N]); |  Select mode(s) from a scalar matrix argument; multiple modes can be selected by listing multiple elements in [N], e.g., [1,2,3].  
selectmode(name); |  Selects the desired mode where name is a string containing the name of a mode. Modes are named mode1, mode2, ..modeN. This form of the command is compatible with the [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) function.  
  
**Examples**

Both these commands select the third mode in the list:
    
    
    selectmode(3);selectmode("mode3");

Selects the 3rd, 5th, and 6th modes.
    
    
    selectmode([3,5,6]);
    

Selects the modes 2 through 5, and 8.
    
    
    selectmode([[2:5];8]);
    

This command selects the mode that has the best overlap with the D-card named "reference"
    
    
    selectmode(bestoverlap("reference"));

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ setanalysis ](/hc/en-us/articles/360034925113-setanalysis) , [ mesh ](/hc/en-us/articles/360034410654-mesh) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ frequencysweep](/hc/en-us/articles/360034925153-frequencysweep) , [bestoverlap](/hc/en-us/articles/360034405274)
