# clearmodedata

Clears mode data for a mode expansion monitor in layout mode. This is mainly useful to
reduce file sizes when saving.

| **Syntax**     | **Description**                                           |
| -------------- | --------------------------------------------------------- |
| clearmodedata; | Clears mode data for the selected mode expansion monitor. |

**Example**

Clear mode data stored in mode expansion monitor. This will make the file much smaller,
which can be convenient when emailing simulation files.

```
select("expansion");
clearmodedata; 
```

**See Also**

[ updatesourcemode ](./updatesourcemode.md) , [ asapimport ](./asapimport.md) ,
[ asapload ](./asapload.md) , [ asapexport ](./asapexport.md) ,
[ clearsourcedata ](./clearsourcedata.md) , [ getresult ](./getresult.md) ,
[ overlap ](./overlap.md) , [ expand ](./expand.md) ,
[ seteigensolver ](./seteigensolver.md) , [ geteigensolver ](./geteigensolver.md)
