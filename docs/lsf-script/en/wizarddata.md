# wizarddata

This command will cause the wizard window to wait until the user selects OK or Cancel.
It then returns value data from the matrix in a N+1 length matrix, where N is the number
of widgets (excluding labels) in the current wizard page.

| **Syntax**        | **Description**       |
| ----------------- | --------------------- |
| out = wizarddata; | The values of out are |

- out(1) = 0, 1 or -1. 0 means the user pressed Cancel, 1 means the user pressed the
  first button (typically "OK" or "Next") and -1 means the user pressed the second
  button (typically "Back")
- out(2:N+1) gives the numeric values that the user entered for each input field **when
  out(1) is 1** . Note that check boxes return 1 if checked and 0 if unchecked. Menu
  items return a number between 1 and M where M is the number of choices in the menu. If
  out(1) is 0 or -1, all the values out(2:N+1) are zero.

**Examples**

See the newwizard page for an example.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ newwizard ](./newwizard.md)
