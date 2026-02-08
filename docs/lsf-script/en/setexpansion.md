# setexpansion

Associates a DFT monitor with a mode expansion monitor.

| **Syntax**                           | **Description**                                                                                                              |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| ?setexpansion;                       | List all monitors under the "Monitors for expansion" list for the selected mode expansion monitor.                           |
| setexpansion("name", "dft_monitor"); | Adds the "dft_monitor" to the "Monitors for expansion" list of the selected mode expansion monitor, with the specified name. |

**Example**

Please open \[[ring_resonator.fsp]\] from the
[Ring resonator example](https://optics.ansys.com/hc/en-us/articles/360042800293) and do
the following.

```
?setexpansion;
drop2  ::model::drop2
in  ::model::in
through  ::model::through
drop  ::model::drop
```

It shows all four DFT monitors to be expanded.

For the same file, type in

```
 setexpansion("test", "in");
```

Then the DFT monitor "in" is added to the list of the "expansion" monitor with the name
of "test".

Type in removeexpansion("test") the "test" is removed from the list.

**See Also**

[ addmodeexpansion ](./addmodeexpansion.md) , [ removeexpansion ](./removeexpansion.md)
,
[ Using Mode Expansion Monitors ](https://optics.ansys.com/hc/en-us/articles/360034902433-Using-Mode-Expansion-Monitors)
