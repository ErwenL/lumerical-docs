# asapexport

Exports the desired monitor to a file for interfacing with BRO's ASAP. These files have
the .fld extension. The monitor must be a frequency power or a frequency profile
monitor.

| **Syntax**                                 | **Description**                                                                                                          |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| asapexport( "monitorname");                | Export data from monitorname. By default, the first frequency point is exported. This function does not return any data. |
| asapexport( "monitorname", f);             | Exports the frequency point specified by the index f.                                                                    |
| asapexport( "monitorname", f, "filename"); | Exports to the specified "filename" without opening a file browser window.                                               |

**Examples**

Export data from monitor transmission to a .fld file for ASAP. The monitor had more than
one frequency point, so the first point was exported by default.

```
asapexport("transmission");
Warning: prompt line 1: in asapexport: no frequency point was specified and the d-card has more than one. The first is used by default.
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ asapload ](./asapload.md) , [ asapimport ](./asapimport.md) ,
[ addimportedsource ](./addimportedsource.md)
