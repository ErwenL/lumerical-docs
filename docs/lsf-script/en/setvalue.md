# setvalue

Sets an internal value for an element's internal parameter.

| **Syntax**                           | **Description**                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setvalue(element, parameter ,value); | Set an internal value for an ‘element’ internal ‘parameter’. Different from ‘set’ or ‘setnamed’, ‘setvalue’ can have direct access to internal element parameters. Currently only the ‘Optical N Port S-Parameter’ support this function for the internal ‘s parameters’ value. The ‘s parameters’ parameter is a cell that contains a complete description of the element s-parameters. |

**Example**

```
M=cell(3);
M{1}=struct;
M{1}.numberOfNPorts=-1;
M{2}=struct;
M{2}.numberOfMPorts=-1;
M{3}=cell(1);
M{3}{1}=struct;
M{3}{1}.data=matrix(5,3);
M{3}{1}.data(1,1)=2.26258e+014;
M{3}{1}.data(2,1)=2.27569e+014;
M{3}{1}.data(3,1)=2.28879e+014;
M{3}{1}.data(4,1)=2.3019e+014;
M{3}{1}.data(5,1)=2.315e+014;
M{3}{1}.data(1,2)=0.0104993;
M{3}{1}.data(2,2)=0.00926858;
M{3}{1}.data(3,2)=0.00596999;
M{3}{1}.data(4,2)=0.00182042;
M{3}{1}.data(5,2)=0.00429422;
M{3}{1}.data(1,3)=-2.64534;
M{3}{1}.data(2,3)=-2.75636;
M{3}{1}.data(3,3)=-2.89119;
M{3}{1}.data(4,3)=-3.62524;
M{3}{1}.data(5,3)=-5.23423;
M{3}{1}.modeInputLabel='TE';
M{3}{1}.modeInputOID=1;
M{3}{1}.modeInputUID='#1';
M{3}{1}.modeOutputLabel='TE';
M{3}{1}.modeOutputOID=1;
M{3}{1}.modeOutputUID='#1';
M{3}{1}.portInput='port 1';
M{3}{1}.portOutput='port 2';
# sets the s-parameter for the element SPAR_1
setvalue('SPAR_1','s parameters',M);
```

**See Also**

[ getvalue ](./getvalue.md)
