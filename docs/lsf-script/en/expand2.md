# expand2

Returns the expansion coefficients in the unconjugated form between the fields recorded at two arbitrary DFT monitors or saved in D-CARDs, or saved in two rectilinear datasets. The coefficients in the unconjugated form are defined according to:

$$ \begin{array}{l}{a=0.25^{*}\left(\frac{\int d \mathbf{S} \cdot \mathbf{E}_{1} \times \mathbf{H}_{2}}{N}+\frac{\int d \mathbf{S} \cdot \mathbf{E}_{2} \times \mathbf{H}_{1}}{N}\right)} \\\ {b=0.25^{*}\left(\frac{\int d \mathbf{S} \cdot \mathbf{E}_{1} \times \mathbf{H}_{2}}{N}-\frac{\int d \mathbf{S} \cdot \mathbf{E}_{2} \times \mathbf{H}_{1}}{N}\right)} \\\ {N=0.5 * \int d \mathbf{S}\cdot \mathbf{E}_{2} \times \mathbf{H}_{2}} \\\ {P=0.5^{*} \int d \mathbf{S} \cdot \mathbf{E}_{1} \times \mathbf{H}_{1}}\end{array} $$

For more detail on how to use this command, definitions on the parameters and how to interpret the results, please see [ Using Mode Expansion Monitors ](/hc/en-us/articles/360034902433-Using-Mode-Expansion-Monitors) .

**Syntax** |  **Description**  
---|---  
expand2(mode1,mode_ref,x,y,z); |  Outputs the expansion coefficients between the fields of two modes in the unconjugated form

  * mode1, mode_ref: field information, with \\(\mathbf{E}_{1},\mathbf{H}_{1}\\) contained in mode1, and \\(\mathbf{E}_{2},\mathbf{H}_{2}\\) contained in mode_ref. Can be in one of the following formats: 
    *       1. Frequency domain monitor names, string input, e.g. “monitor1”
      2. Mode D-CARDs containing field information, string input, e.g. “mode1”
      3. Rectilinear datasets, see below for more info
  * x,y,z: spatial displacement of the fields from monitor1 with respect to those from monitor_ref

  
  
## Using Rectilinear Datasets

Starting in 2024R2.3, rectilinear datasets with arbitrary field profiles are supported in addition to monitor names and D-CARDs.

Rectilinear datasets **cannot** be mixed with other input types, however, data can be extracted from modes using the [getresult script command](https://optics.ansys.com/hc/en-us/articles/360034409854-getresult-Script-command), shown in the examples below.

When using rectilinear datasets, they should contain attribute names ‘E’ and ‘H’, which will be used as the electric and magnetic fields, respectively. If no attribute name ‘E’ is found, the first attribute of the dataset is assumed to be the electric field. If no attribute ‘H’ is found, the first attribute of the dataset after the electric field attribute is assumed to be the magnetic field.

**Example**

The following script expands the fields from monitor "R" onto the reference monitor "R_ref" in the unconjugated form:
    
    
    M = expand2("R","R_ref",0,0,0);  
    f = getdata("R","f");
    a = pinch(M,1,1);
    b = pinch(M,1,2);
    n = pinch(M,1,3);
    p = pinch(M,1,4);
    S11 = b;

The following script expands the fields from monitor “R” onto reference monitor “R_ref” by first converting them to rectilinear datasets using getresult. The result is identical to above.
    
    
    # example using rectilinear datasets  
    #First, obtain rectilinear dataset from monitors using getresult  
    #These datasets could have been imported from elsewhere as well  
    EH1 = getresult("R","E");  
    H1 = getresult("R","H");  
    EH1.addattribute("H",H1.H);  
    EH2 = getresult("R_ref","E");  
    H2 = getresult("R_ref","H");  
    EH2.addattribute("R_ref",H2.H);  
      
    M = expand2(EH1,EH2,0,0,0);  
    f = EH1.f;  
    a = pinch(M,1,1);  
    b = pinch(M,1,2);  
    n = pinch(M,1,3);  
    p = pinch(M,1,4);  
    S11 = b;

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ Using Mode Expansion Monitors ](/hc/en-us/articles/360034902433-Using-Mode-Expansion-Monitors) , [ setexpansion ](/hc/en-us/articles/360034408974-setexpansion) , [ removeexpansion ](/hc/en-us/articles/360034408994-removeexpansion) , [ expand ](/hc/en-us/articles/360034926653-expand)
