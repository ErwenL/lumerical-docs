# insertsweep

Inserts a sweep/optimization/Monte Carlo item as a parent to an existing analysis item. The existing item becomes a child of the newly inserted sweep.

**Syntax** |  **Description**  
---|---  
insertsweep("name"); |  Inserts a sweep/optimization/Monte Carlo item as a child to a parent analysis item. "name" is the absolute name of the existing analysis item.  
  
**Example**
    
    
    addsweep(0);
    insertsweep("sweep");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ deletesweep ](/hc/en-us/articles/360034930173-deletesweep) , [ copysweep ](/hc/en-us/articles/360034930373-copysweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ addsweep ](/hc/en-us/articles/360034930413-addsweep) , [ getsweep ](/hc/en-us/articles/360034930453-getsweep) , [setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](/hc/en-us/articles/360034927973-setsetting), [ addsweepparameter ](/hc/en-us/articles/360034930493-addsweepparameter) , [ addsweepresult ](/hc/en-us/articles/360034410034-addsweepresult) , [ removesweepparameter ](/hc/en-us/articles/360034930513-removesweepparameter) , [ removesweepresult ](/hc/en-us/articles/360034930533-removesweepresult)
