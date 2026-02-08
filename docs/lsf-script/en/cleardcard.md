# cleardcard

Clears global d-cards. Only global d-cards are cleared. Local d-cards are associated
with the current simulation and can only be cleared by switching from Analysis Mode to
Layout Mode.

| **Syntax**                          | **Description**                                                        |
| ----------------------------------- | ---------------------------------------------------------------------- |
| cleardcard;                         | Clears all the global d-cards. This function does not return any data. |
| cleardcard( "name1", "name2", ...); | Clears any number of specified d-cards.                                |

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ havedata ](./havedata.md) , [ copydcard ](./copydcard.md)
