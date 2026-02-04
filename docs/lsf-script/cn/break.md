<!--
Translation from English documentation
Original command: break
Translation date: 2026-02-04 22:49:36
-->

# break

Stops 一个 脚本 从 executing.

**语法** |  **描述**  
---|---  
break; |  Will stop 一个 脚本 文件 从 executing at 该 line. A warning 将 为 generated. This 函数 does not 返回 any 数据.  
  
**示例**

The 脚本 将 stop at 此 line.
    
    
    用于 (i=1:100) {
     pause(1);
     break;
    }
    警告: prompt line 3: break 命令

**参见**

[ List 的 commands](/hc/en-us/articles/360037228834), [ESCAPE key](/hc/en-us/articles/360034931893-Escape-key), [pause](/hc/en-us/articles/360034411114-pause)
