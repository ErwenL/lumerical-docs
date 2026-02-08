# overlap

Returns the overlap and power coupling between two modes calculated by the FDE solver or
recorded by frequency monitors from an FDTD or varFDTD simulation, or field profiles
recorded in rectilinear datasets.

Overlap measures the fraction of electromagnetic fields that overlap between the two
field profiles (modes). This is also the fraction of power from mode2 that can propagate
in mode1 (for both forward and backward propagating fields). The absolute value of the
entire formula is to ensure it is positive.

$$ {\\text { overlap }=\\left| \\operatorname{Re} \\left\[\\frac{(\\int \\mathbf{E}_{1}
\\times \\mathbf{H}_{2}^{*} \\cdot d \\mathbf{S}) (\\int \\mathbf{E}_{2} \\times
\\mathbf{H}_{1}^{*} \\cdot d \\mathbf{S} ) }{\\int \\mathbf{E}_{1} \\times
\\mathbf{H}_{1}^{*} \\cdot d \\mathbf{S} }\\right\] \\frac{1}{ \\operatorname{Re} (
\\int \\mathbf{E}_{2} \\times \\mathbf{H}_{2}^{*} \\cdot d \\mathbf{S} )} \\right| } $$

| **Syntax**                   | **Description** |
| ---------------------------- | --------------- |
| out = overlap(mode2, mode1); |                 |

- mode2, mode1: modes to calculate overlaps for, inputs can be
  1. Mode D-CARDs in FDE, string input, e.g., ‘mode1’, ‘mode2’
  1. Names of frequency domain monitors in FDTD, string input, e.g., ‘m1’, ‘m2’
  1. Rectilinear datasets, see below for more information
- out(1): the mode overlap
- out(2): the mode power coupling

out = overlap(mode2, mode1, x, y,z); | Mode alignment can be adjusted before overlap is
calculated.

- x offset
- y offset
- z offset

The offset is applied to the second mode listed, i.e. ‘mode1’ in this case. All inputs
(FDE mode names, frequency monitors, rectilinear datasets) are valid also for the syntax
with alignment adjustment.

## Using Rectilinear Datasets

Starting in 2024R2.3, rectilinear datasets with arbitrary field profiles are supported
in addition to monitor names and D-CARDs.

Rectilinear datasets **cannot** be mixed with other input types, however, data can be
extracted from modes using the
[getresult script command](https://optics.ansys.com/hc/en-us/articles/360034409854-getresult-Script-command),
shown in the examples below.

When using rectilinear datasets, they should contain attribute names ‘E’ and ‘H’, which
will be used as the electric and magnetic fields, respectively. If no attribute name ‘E’
is found, the first attribute of the dataset is assumed to be the electric field. If no
attribute ‘H’ is found, the first attribute of the dataset after the electric field
attribute is assumed to be the magnetic field.

**Examples**

This example shows how to use the overlap command to calculate the overlap and power
coupling between two modes.

```
copydcard("mode1","test_mode1");copydcard("mode2","test_mode2");
out = overlap("test_mode1","test_mode2");
?out(1);  # overlap  
?out(2);  # power coupling  
  
#The same result as above, but using rectilinear datasets  
EH1 = getresult("mode1","E"); #getresult used to extract E and H data  
H1 = getresult("mode1","H");  
EH1.addattribute("H",H1.H);  
EH2 = getresult("mode2","E");  
H2 = getresult("mode2","H");  
EH2.addattribute("H",H2.H);  
out2 = overlap(EH1,EH2);  
?out2(1); # overlap  
?out2(2); # power coupling
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ copydcard ](./copydcard.md) , [ findmodes ](./findmodes.md) ,
[ coupling ](./coupling.md) , [ bestoverlap ](./bestoverlap.md) ,
[ propagate ](./propagate.md) , [ expand ](./expand.md) , [ expand2 ](./expand2.md) ,
[ optimizeposition ](./optimizeposition.md)
