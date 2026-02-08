# setsetting

Sets the value of a user defined setting. User settings are saved permanently and
available after even closing the application.

| **Syntax**                        | **Description**                          |
| --------------------------------- | ---------------------------------------- |
| setsetting("name","string_value") | Set the value of a user defined setting. |

| **Parameter** | **Type** | **Description**       |
| ------------- | -------- | --------------------- |
| name          | string   | name of the setting.  |
| string_value  | string   | value of the setting. |

**Example**

This command allows users to define customized setting that is stored permanently, until
the software reinstallats.

```
setsetting("in","out");
?getsetting("in");
out # "string_value" of the setting "in"
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ getsetting ](./getsetting.md)
