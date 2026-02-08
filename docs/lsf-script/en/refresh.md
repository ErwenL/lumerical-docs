# refresh

This command reloads the current project.

| **Syntax** | **Description**                                                                                                                                                                                                                                                                               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| refresh;   | Reloads the current project. This is particularly useful when changing the ‘library’ property of a reference element. Reference elements must be manually ‘refreshed’ or reloaded if the ‘library’ property is modified – otherwise the use will have to save and reload the current project. |

### Example

```
>setnamed("WG_1","library","::design kits::pdaflow");
>refresh;
```

### See Also

[ List of commands ](../lsf-script-commands-alphabetical.md)
