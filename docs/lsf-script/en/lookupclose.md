# lookupclose

Closes a lookup table file previously created with a [ lookupopen ](./lookupopen.md)
command.

| **Syntax**                | **Description**                                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| lookupclose ("filename"); | Closes a file previously created with a lookupopen command. This command is required in order to close any file open by lookupopen . |

**Example**

In order to create the lookup table “new.xml” with table named “new_extracted”:

```
#open file to write lookup table
lookupopen("new.xml", "new_extracted" );
...
#write design/extracted pair
lookupwrite( "new.xml", design, extracted );
...
#close file
lookupclose("new.xml");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ lookupopen ](./lookupopen.md) , [ lookupread ](./lookupread.md) ,
[ lookupwrite ](./lookupwrite.md) , [ lookupreadtable ](./lookupreadtable.md) ,
[ lookupreadvalue ](./lookupreadvalue.md) ,
[ lookupreadnportsparameter ](./lookupreadnportsparameter.md) ,
[ lookupappend ](./lookupappend.md) , [ insert ](./insert.md)
