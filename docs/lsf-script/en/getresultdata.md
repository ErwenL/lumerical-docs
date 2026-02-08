# getresultdata

Gets results from an analyzer. This differs from the "getresult" function in that the
results are returned as matrices, not
[Datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets).

| **Syntax**                                 | **Description**                                                                   |
| ------------------------------------------ | --------------------------------------------------------------------------------- |
| ?getresultdata;                            | Returns the names of all elements in the current simulation that contain results. |
| ?getresultdata("analyzer");                | Returns all available results for "analyzer".                                     |
| out = getresultdata("analyzer", "result"); | Returns the result "result" for "analyzer".                                       |

**See Also**

[setresult](./setresult.md), [getresult](./getresult.md)
