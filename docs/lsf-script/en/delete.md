# delete

Deletes selected objects.

| **Syntax** | **Description**                                                   |
| ---------- | ----------------------------------------------------------------- |
| delete;    | Deletes selected objects. This function does not return any data. |

**Example**

Create an object and then delete it, just for illustration.

```
addrect;
set("name","substrate");
select("substrate");
delete;
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ groupscope ](./groupscope.md)
