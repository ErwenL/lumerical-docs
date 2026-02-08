# pause

Pauses program for a time.

| **Syntax**   | **Description**                                                                                                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pause(time); | Pauses script for time, measured in seconds. Hit the space bar to force the script to continue. Hit the ESCAPE key to break the script at this point. This function does not return any data. |

**Examples**

Pauses for 5 seconds.

```
pause(5);
```

Pauses until user clicks space bar.

```
?"Part 1 complete. Hit space bar to proceed with part 2.";
pause(10000);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ break ](./break.md) ,
[ ESCAPE key ](https://optics.ansys.com/hc/en-us/articles/360034931893-Escape-key)
