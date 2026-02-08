# switchtodesign

Switches INTERCONNECT to DESIGN mode. The DESIGN mode allows you to add and modify
circuit elements for a new simulation. Once a simulation is run, the solver goes into
ANALYSIS mode and no elements can be added or modified. While in ANALYSIS mode, any
command to modify or add elements will return error. You must switch to DESIGN mode for
that. Note that any available results will be lost once the solver is switched back to
DESIGN mode.

| **Syntax**      | **Description**                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| switchtodesign; | Switches INTERCONNECT from ANALYSIS to DESIGN mode. This function does not return any data. |

**Example**

The following script commands will first run an INTERCONNECT simulation. The solver will
go to ANALYSIS mode. The "switchtodesign" command is then used to go to DESIGN mode so
that the simulation "bitrate" can be changed in the next line.

```
run;
switchtodesign;
setnamed('::Root Element','bitrate',2e10);  # bit rate set to 20 Gbit/sec
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ switchtolayout ](./switchtolayout.md) , [ layoutmode ](./layoutmode.md) ,
[ designmode ](./designmode.md)
