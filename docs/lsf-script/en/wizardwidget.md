# wizardwidget

Adds a new widget to the current wizard window. This command should only be done after creating a new wizard page with the command newwizard. 

**Syntax** |  **Description**  
---|---  
wizardwidget( "type", "name");  |  type can be 

  * "number" for a numeric input field 
  * "string" for a alphanumeric field 
  * "checkbox" for a checkbox 
  * "menu" for a pulldown menu field 
  * "label" to add a string label (wizardgetdata does not return information for labels) 

name is a string used to give the input field, checkbox, menu item or label a name.   
wizardwidget( "type", "label", defaultValue);  |  defaultValue provides a default value for numeric inputs, checkboxes, menu items or strings.   
wizardwidget( "type", "label", "choices", defaultValue);  |  If the "type" of widget is a "menu", then the menu choices must be provided. These choices should be separated by the character "|". For example, to create a pulldown widget with the name "simulation type" and 3 choices "TE","TM","3D", with the default choice "3D", the command is  wizardwidget("menu","simulation type","TE|TM|3D",3);   
  
**Examples**

See the newwizard page for an example. 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ newwizardpage ](/hc/en-us/articles/360034932373-newwizardpage)
