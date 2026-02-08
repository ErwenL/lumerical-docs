# setresult

Sets the result of a Scripted or a Compound element. Note that this command is not
available from the script prompt or script file editor. It should be used in the
Scripted or Compound element "Simulation" tabs.

| **Syntax**                                   | **Description**                                                                                                                                         |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setresult("result",value);                   | Sets the "result" for the scripted/compound element to the specified value. The "result" can be a matrix or a dataset.                                  |
| setresult("result",value,"kind (unit)");     | Sets the "result" for the scripted/compound element to the specified value with the given description. Note that units should be placed in parenthesis. |
| setresult("result",x,y,"x title",'y title'); | Sets the x, y parameters of the "result" for the scripted/compound element. This is useful for visualization.                                           |

**See Also**

[getresult](./getresult.md)
