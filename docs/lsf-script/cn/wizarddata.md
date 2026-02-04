<!--
Translation from English documentation
Original command: wizarddata
Translation date: 2026-02-04 22:50:31
-->

# wizarddata

This 命令 将 cause 该 wizard window 到 wait until 该 用户 selects OK 或 Cancel. It 那么 返回 值 数据 从 该 矩阵 在 一个 N+1 长度 矩阵, 其中 N 是 该 数字 的 wid获取(excluding labels) 在 该 current wizard page。 

**语法** |  **描述**  
---|---  
out = wizarddata;  |  The 值 的 out 是 

  * out(1) = 0, 1 或 -1. 0 means 该 用户 pressed Cancel, 1 means 该 用户 pressed 该 first button (typically "OK" 或 "Next") 和 -1 means 该 用户 pressed 该 second button (typically "Back") 
  * out(2:N+1) gives 该 numeric 值 该 该 用户 entered 用于 each input field **当 out(1) 是 1** . 注意 该 check boxes 返回 1 如果 checked 和 0 如果 unchecked. Menu items 返回 一个 数字 between 1 和 M 其中 M 是 该 数字 的 choices 在 该 menu. If out(1) 是 0 或 -1, all 该 值 out(2:N+1) 是 zero. 

  
  
**示例**

See 该 newwizard page 用于 一个 example. 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ newwizard ](/hc/en-us/articles/360034932353-newwizard)
