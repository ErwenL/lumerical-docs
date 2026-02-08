# select

Selects objects with a given name in the current group scope. A failed select command
will have the same result as the unselectall command.

| **Syntax**                  | **Description**                                                                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| select("name");             | Selects objects with the name "name" in the current group scope. This function does not return any data.                                           |
| select("group name::name"); | Selects all objects with the name "name" located in the group named "group name". The group named "group name" must be in the current group scope. |

**Example**

Add two objects and select the first object for other settings.

```
addrect;
set("name","substrate");
addring;
select("substrate");
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ groupscope ](./groupscope.md) , [ unselectall ](./unselectall.md)
