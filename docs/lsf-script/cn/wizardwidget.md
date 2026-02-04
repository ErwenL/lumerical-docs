<!--
Translation from English documentation
Original command: wizardwidget
Translation date: 2026-02-04 22:50:31
-->

# wizardwidget

添加 一个 新的 widget 到 该 current wizard window. This 命令 应该 only 为 done after creating 一个 新的 wizard page 使用 该 命令 newwizard. 

**语法** |  **描述**  
---|---  
wizardwidget( "类型", "name");  |  类型 可以 为 

  * "数字" 用于 一个 numeric input field 
  * "字符串" 用于 一个 alphanumeric field 
  * "checkbox" 用于 一个 checkbox 
  * "menu" 用于 一个 pulldown menu field 
  * "label" 到 添加 一个 字符串 label (wizardgetdata does not 返回 information 用于 labels) 

name 是 一个 字符串 used 到 give 该 input field, checkbox, menu item 或 label 一个 name.   
wizardwidget( "类型", "label", defaultValue);  |  defaultValue provides 一个 default 值 用于 numeric inputs, checkboxes, menu items 或 strings.   
wizardwidget( "类型", "label", "choices", defaultValue);  |  If 该 "类型" 的 widget 是 一个 "menu", 那么 该 menu choices 必须 为 provided. These choices 应该 为 separated 通过 该 character "|". For example, 到 创建 一个 pulldown widget 使用 该 name "仿真 类型" 和 3 choices "TE","TM","3D", 使用 该 default choice "3D", 该 命令 是  wizardwidget("menu","仿真 类型","TE|TM|3D",3);   
  
**示例**

See 该 newwizard page 用于 一个 example. 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ newwizardpage ](/hc/en-us/articles/360034932373-newwizardpage)
