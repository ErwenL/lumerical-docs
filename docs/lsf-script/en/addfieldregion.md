# addfieldregion

Adds a
[field region object](https://optics.ansys.com/hc/en-us/articles/36967414684947-Field-Region-Simulation-object)
to the simulation environment. The field region object is used with lumopt, see the
Knowledge Base article on
[Getting started with lumopt](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API)
for more information.

| **Syntax**                   | **Description**                                                                                                                                                                                                                                                                   |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addfieldregion;              | Adds a field region object to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addfieldregion(struct_data); | Adds a field region object and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**See Also**

[List of commands ](../lsf-script-commands-alphabetical.md), [set ](./set.md),
[addplane ](./addplane.md), [addgaussian ](./addgaussian.md), [addtfsf](./addtfsf.md),
[adddipole](https://optics.ansys.com/hc/en-us/articles/360034924393-adddipole-Script-command),
[adddftmonitor](https://optics.ansys.com/hc/en-us/articles/36957320687763-adddftmonitor-Script-command)
