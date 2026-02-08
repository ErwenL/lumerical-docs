# getresultdata

Gets results from an analyzer. This differs from the "getresult" function in that the results are returned as matrices, not [Datasets](/hc/en-us/articles/360034409554-Datasets).

**Syntax** |  **Description**  
---|---  
?getresultdata; |  Returns the names of all elements in the current simulation that contain results.  
?getresultdata("analyzer"); |  Returns all available results for "analyzer".   
out = getresultdata("analyzer", "result"); |  Returns the result "result" for "analyzer".  
  
**See Also**

[setresult](/hc/en-us/articles/360034407694-setresult), [getresult](/hc/en-us/articles/360034409854-getresult)
