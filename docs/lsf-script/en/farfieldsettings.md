# farfieldsettings

Sets the parameters available in the Far field settings window for far field
calculations. To get the available parameters for far field settings, as is shown below,
right click on a frequency-domain field monitor and visualize the far field. then select
the Far field settings.

______________________________________________________________________

| **Syntax**                           | **Description**                                                                                                                                                                                 |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| farfieldsettings("property", value); | Set the far field filter settings for far field calculations. These settings are applied to all far field projections. Value can be a number or string. This function does not return any data. |

**Example**

```
farfieldsettings("far field filter",0.2);farfieldsettings("override near field mesh",1);
farfieldsettings("near field samples per wavelength",5);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ farfield2d ](./farfield2d.md) , [ farfield3d ](./farfield3d.md) ,
[ farfieldfilter ](./farfieldfilter.md) , [ setanalysis ](./setanalysis.md) (for
farfield settings in FDE)
