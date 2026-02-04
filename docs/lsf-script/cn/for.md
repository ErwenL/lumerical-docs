<!--
Translation from English documentation
Original command: for
Translation date: 2026-02-04 22:49:49
-->

# 用于

Starts 一个 用于 loop 到 allow some operations 到 为 repeated 一个 数字 的 times. A while loop 可以 为 implemented 当 使用 该 three 参数 version 的 一个 用于 loop.

**语法** |  **描述**  
---|---  
用于(x=1:100) { ?x; } |  Single 参数 用于 loop. The loop 将 为 sequentially executed 用于 each 值 的 x.  
用于(x=1; x<= 100; x=x+1) { ?x; } |  Three 参数 用于 loop. x=1 at 该 start 的 该 loop. The loop continues while x <=100 和 设置 x=x+1 at each pass.  
x=1; 用于(0; x<10; 0) { ?x; x=x+1; } |  This 是 equivalent 到 一个 while loop 该 将 execute while x<10.  
  
**示例**

This example shows 一个 simple 用于 loop 其中 x takes 该 值 1, 3, 5, 7, 9.
    
    
    一个=1:2:10;
    用于(x=一个) { 
     ?x; 
    } 

Nested loops: This example shows 一个 nested 用于 loop.
    
    
    用于(i=1:100) { 
     用于(j=1:100) { 
      x = i^2+j; 
      ?x; 
     } 
    } 

The following code 将 获取 该 electric field 数据 从 each monitors 在 此 仿真 文件, 那么 save 该 数据 在 一个 series 的 Lumerical 数据 files. To test 此 example, download 该 associated 仿真 文件, run 该 仿真, 那么 run 该 following 脚本.
    
    
    run;
    mNames = splitstring(getresult,endl);
     
    用于 (i=1:长度(mNames)) {
     如果 (haveresult(mNames{i},"E")) {
      E=getresult(mNames{i},"E");   # 获取 一个 result 从 该 监视器
     } 否则 {
      E = mNames{i} + " did not contain 该 specified 数据.";
     }
     savedata(mNames{i},E);     # save 数据 到 文件
    }

While loops: There 是 no "while" 命令 在 该 scripting language, but 该 "用于" 命令 可以 为 used 到 implement 一个 "while" 命令. The 命令  用于(0; conditional_expression; 0) {}  是 该 same as  while(conditional_expression) {}.  The “0” statements 在 该 “用于” loop do nothing 和 是 just placeholders because 该 scripting language expects 一个 参数 there.
    
    
    # implementation 的 一个 while loop 在 languages 该 support while loops
    x=1;
    while(x<10) {
      ?x;
      x=x+1;
    }
    # equivalent implementation 的 一个 while loop 在 Lumerical 脚本 language
    x=1;
    用于(0; x<10; 0) {
      ?x;
      x=x+1;
    }

**参见**

[ List 的 commands](/hc/en-us/articles/360037228834), [ 如果 ](/hc/en-us/articles/360034408294-如果)
