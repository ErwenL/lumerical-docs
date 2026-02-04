<!--
Translation from English documentation
Original command: write
Translation date: 2026-02-04 22:50:32
-->

# write

Writes 字符串 variables 到 text files 或 到 standard output.

Typically 该 write 命令 是 used 到 output 数据 到 一个 text 文件. If 该 specified 文件 does not exist, it 将 为 created. If it does exist, 那么 该 output 字符串 将 either 为 appended 到 该 end 的 该 文件 或 overwrite 该 文件. The write 命令 将 automatically 添加 一个 新的 line character at 该 end 的 该 字符串.

On Linux systems only, 该 write 命令 将 output 到 该 standard output (stdout) 如果 一个 文件名 是 not specified.

**语法** |  **描述**  
---|---  
write(my_string); |  Write my_string 到 该 standard output (Linux only).  
write("testfile.txt", my_string, option); |  Will write 该 contents 的 该 字符串 变量 my_string 到 testfile.txt. The 文件 "testfile.txt" 将 为 created 如果 it does not exist.  option: 可以 为 "append" 或 "overwrite", 到 append 该 变量 my_string 到 该 end 的 该 文件 或 overwrite 该 文件, respectively. If option 是 not provided, "append" 将 为 used 通过 default. This 函数 does not 返回 any 数据.  
  
**Note** : This command cannot be used while in [safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**示例**

Write 一个 数组 的 numbers 到 一个 text 文件. If you want 到 overwrite 该 文件, use 该 "overwrite" option 在 该 命令.
    
    
    一个=linspace(0,2*pi,9);
    write("testfile.txt",num2str(一个), "overwrite");

The write 命令 可以 output 2D matrices 在 一个 single 命令. Each column 将 为 separated 使用 一个 TAB character.
    
    
    # define 该 variables 到 export
    一个=linspace(0,2*pi,9);
    b=sin(一个);
    # combine both vectors into 一个 single 2D 矩阵 到 为 output 到 文件
    data_to_print=[一个,b];
    # write 该 数据 到 该 文件
    write("testfile.txt",num2str(data_to_print));

Generally, more complicated formatting 是 required. For example, suppose you want 到 have 一个 header section 该 describes 什么 该 variables 是. You also want 到 use comma separated columns (CSV), rather than TAB separated. Finally, you want 到 output 该 full double precision numbers, rather than just 该 first 5 digits.
    
    
    # define 该 variables 到 export
    一个=linspace(0,pi,9);
    b=sin(一个);
    # remove 该 文件 如果 it already exists
    rm("testfile.txt");
    # write 该 文件 header
    write("testfile.txt","theta, sin(theta)");
    # 设置 num2str() 到 返回 16 digits 的 precision
    format long;
    # write 该 数据 到 该 文件
    用于 (i=1:长度(一个) ) {
     str= num2str(一个(i))+", "+num2str(b(i));
     write("testfile.txt",str);
    }

The contents 的  testfile.txt  将 为:

theta, sin(theta)

0.0000000000000000, 0.0000000000000000

0.3926990816987241, 0.3826834323650898

0.7853981633974483, 0.7071067811865475

1.178097245096172, 0.9238795325112867

1.570796326794897, 1.000000000000000

1.963495408493621, 0.9238795325112867

2.356194490192345, 0.7071067811865476

2.748893571891069, 0.3826834323650899

3.141592653589793, 1.224646799147353e-016

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ savedata ](/hc/en-us/articles/360034411174-savedata) , [ readdata ](/hc/en-us/articles/360034411234-readdata) , [ read ](/hc/en-us/articles/360034931933-read) , [ rm ](/hc/en-us/articles/360034931533-rm) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ ? ](/hc/en-us/articles/360034410434--) , [ endl ](/hc/en-us/articles/360034410414-endl) , [ format ](/hc/en-us/articles/360034931913-format) , [ fileexists ](/hc/en-us/articles/360034931633-fileexists) , [ matlabsave ](/hc/en-us/articles/360034928113-matlabsave)
