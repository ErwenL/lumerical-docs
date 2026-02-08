# exit

Exits the application.

| **Syntax**    | **Description**                                                                 |
| ------------- | ------------------------------------------------------------------------------- |
| exit;         | Exits the application. Same as exit(1); This function does not return any data. |
| exit(option); | Exits the application. The option can be                                        |

- 1: Prompt user if a file needs saving before exiting.
- 2: Force the application to exit without prompting the user.

The default option is 1.

**Examples**

Exits the application, and prompt user to save data.

```
exit(1);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ newproject ](./newproject.md) , [ new ](./new.md)
