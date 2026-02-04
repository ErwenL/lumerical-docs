<!--
Translation from English documentation
Original command: matlab
Translation date: 2026-02-04 22:50:13
-->

# matlab

Runs 一个 MATLAB 命令 从 该 Lumerical 脚本 prompt. This gives access 到 extended mathematical 和 visualization functionality 从 该 Lumerical 脚本 环境. If 该 MATLAB 脚本 integration 是 not enabled, 此 函数 将 返回 一个 error. 

The first 时间 一个 MATLAB 函数 (matlab, matlabget 或 matlabput) 是 called, 一个 MATLAB session 将 为 started 和 一个 connection 将 为 established 使用 该 Lumerical scripting 环境. Once 此 connection 是 established, MATLAB commands 可以 为 run 使用 该 matlab 函数. It 是 important 到 understand 该 该 MATLAB 和 该 Lumerical 脚本 变量 workspaces 是 completely separate 和 independent. A MATLAB 命令 cannot act 在 一个 变量 defined 在 该 Lumerical workspace, 和 vice-versa. Variables 必须 为 passed between 该 workspaces 使用 该 matlabget 和 matlabput functions. At any 时间 you 可能 examine 该 MATLAB workspace 或 interact 使用 该 MATLAB 环境 通过 typing commands at 该 MATLAB 脚本 prompt. The working directory 的 该 MATLAB instance 是 always 设置 到 match 该 working directory 的 该 Lumerical application. 

The output 从 该 MATLAB commands 将 为 printed at 该 Lumerical 脚本 prompt. One limitation 的 该 matlab 函数 是 该 no error reporting 是 provided 到 either 该 Lumerical 脚本 prompt 或 该 MATLAB prompt. MATLAB commands 应该 为 tested 通过 typing them directly into 该 MATLAB prompt before they 是 called 从 一个 Lumerical 脚本. The output buffer 长度 是 roughly 1e5 characters. Additional output 将 为 truncated. 

When you have 一个 long sequence 的 MATLAB commands, you 可能 find it more convenient 到 save them 在 一个 MATLAB m-文件. Then, you 可以 simply call 该 m-文件 通过 running 一个 single 命令. 

See [ MATLAB integration setup ](/hc/en-us/articles/360026142074) 用于 installation 和 configuration instructions. Additional tips (particularly 用于 plotting 数据 在 Matlab) 可以 为 found 在 该 [ MATLAB ](/hc/en-us/articles/360034416614) section 的 该 online help.   
---  
**语法** |  **描述**  
---|---  
matlab("命令");  |  命令: 一个 字符串 containing one 或 more valid MATLAB commands.   
matlab("  command_1  command_2  ");  |  Multi-line strings 可以 为 used 在 脚本 files 到 contain 一个 block 的 MATLAB commands. Multi-line strings 是 not supported at 该 脚本 命令 prompt.   
  
**示例**

This example 将 show 如何 到 use MATLAB's "surf" 命令 到 make 一个 surface plot 的 该 real part 的 Ex. It assumes 该 该 variables x, y, Ex 是 already defined 在 该 Lumerical workspace. 
    
    
    matlabput(x,y,Ex);
    matlab("surf(y,x,real(Ex))");

This example shows 如何 multiple MATLAB commands 可以 为 included 在 一个 single matlab 函数 call. A log-spaced 向量 是 created 在 MATLAB, 那么 imported into 该 Lumerical workspace. 
    
    
    matlab("
     % 创建 一个 logspaced 向量
     x_min = 1
     x_max = 4
     x = logspace(x_min,x_max,1000)
    ");
    matlabget(x);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ matlabget ](/hc/en-us/articles/360034407994-matlabget) , [ matlabput ](/hc/en-us/articles/360034408014-matlabput) , [ MATLAB integration setup ](/hc/en-us/articles/360026142074) , [ MATLAB ](/hc/en-us/articles/360034416614)
