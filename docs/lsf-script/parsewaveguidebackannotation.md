# parsewaveguidebackannotation

Parses the waveguide back annotation at a given temperature in Celsius. 

**Syntax** |  **Description**  
---|---  
parsewaveguidebackannotation(backannotation, temperature)  |  Parses the waveguide back annotation at a given temperature in Celsius. The annotation contains a list of mode labels, and for each mode a list of temperature and wavelength dependent propagation parameters are provided.  The function returns a cell vector containing multiple structures with the parsed data at the given input temperature.   
  
**Example**
    
    
    sIn = "( ( 'TE' ( '26.85' '1.5475u' 0.0501323 2.4485 4.19145 0.000138683 ) ( '26.85' '1.5u' 0.0501323 2.4485 4.19145 0.000138683 ) ) ( 'TM' ( '26.85' '1.5475u' 17.3718 1.785382 3.76608 -0.019477 ) ( '26.85' '1.5u' 17.3718 1.785382 3.76608 -0.019477 ) ) ( 'TX' ( '26.85' '1.5650u' 0.0485085 2.42879 4.19216 0.000133047 ) ( '26.85' '1.5u' 0.0485085 2.42879 4.19216 0.000133047 ) ) ( 'TY' ( '49.85' '1.5475u' 0.0501048 2.45306 4.19667 0.000154927 ) ( '49.85' '1.5u' 0.0501048 2.45306 4.19667 0.000154927 ) ) ) ";
    x= parsewaveguidebackannotation(sIn, 10);
    ?toscript(x);
    x=cell(4);
    x{1}=struct;
    x{1}.label='TE';
    x{1}.orthogonal_identifier=1;
    x{1}.propagation=matrix(2,5);
    x{1}.propagation(1,1)=1.99862e+014;
    x{1}.propagation(2,1)=1.93727e+014;
    x{1}.propagation(1,2)=0.0501323;…

**See Also**

[ parsebackannotation ](/hc/en-us/articles/360034927593-parsebackannotation)
