# clearsourcedata

Clears source data for an imported source, or the selected mode for a mode source.

| **Syntax**       | **Description**                             |
| ---------------- | ------------------------------------------- |
| clearsourcedata; | Clears source data for the selected source. |

**Example**

Clear source data from an imported source. This will make the file much smaller, which
can be convenient when emailing simulation files.

```
select("source3");
clearsourcedata; 
```

**See Also**

[ updatesourcemode ](./updatesourcemode.md) , [ asapimport ](./asapimport.md) ,
[ asapload ](./asapload.md) , [ asapexport ](./asapexport.md) ,
[ clearmodedata ](./clearmodedata.md) , [ getresult ](./getresult.md) ,
[ overlap ](./overlap.md) , [ expand ](./expand.md) ,
[ seteigensolver ](./seteigensolver.md) , [ geteigensolver ](./geteigensolver.md)
