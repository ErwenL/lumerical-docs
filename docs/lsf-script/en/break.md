# break

Stops a script from executing.

| **Syntax** | **Description**                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- |
| break;     | Will stop a script file from executing at that line. A warning will be generated. This function does not return any data. |

**Examples**

The script will stop at this line.

```
for (i=1:100) {
 pause(1);
 break;
}
Warning: prompt line 3: break command
```

**See Also**

[ List of commands](../lsf-script-commands-alphabetical.md),
[ESCAPE key](https://optics.ansys.com/hc/en-us/articles/360034931893-Escape-key),
[pause](./pause.md)
