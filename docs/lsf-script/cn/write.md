<!-- Translation completed: 2026-02-04 -->
<!-- Original command: write -->

# write

    a=linspace(0,2*pi,9);
    b=sin(a);
    data_to_print=[a,b];
    写入("testfile.txt",num2str(data_to_print));
Generally, more complicated formatting is required. For 示例, suppose you want to have a header section that describes what the variables are. You also want to 使用 comma separated columns (CSV), rather than TAB separated. Finally, you want to 输出 the full double precision numbers, rather than just the first 5 digits.
    a=linspace(0,pi,9);
    b=sin(a);
    rm("testfile.txt");
    写入("testfile.txt","theta, sin(theta)");
    格式 long;
    for (i=1:长度(a) ) {
     str= num2str(a(i))+", "+num2str(b(i));
     写入("testfile.txt",str);
    }
The contents of  testfile.txt  will be:
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

**语法** | **描述**
---|---
write(my_string); | 写入 my_string to the standard 输出 (Linux only).
write("testfile.txt", my_string, option); | Will 写入 the contents of the 字符串 变量 my_string to testfile.txt. The 文件 "testfile.txt" will be created if it does not exist.  option: can be "append" or "overwrite", to append the 变量 my_string to the end of the 文件 or overwrite the 文件, respectively. If option is not provided, "append" will be used by default. This 函数 does not 返回 any data.

**示例**

写入 an 数组 of numbers to a text 文件. If you want to overwrite the 文件, use the "overwrite" option in the 命令.
    a=linspace(0,2*pi,9);
    写入("testfile.txt",num2str(a), "overwrite");
The 写入 命令 can 输出 2D matrices in a single 命令. Each column will be separated with a TAB character.

写入 an 数组 of numbers to a text 文件. If you want to overwrite the 文件, use the "overwrite" option in the 命令.
    a=linspace(0,2*pi,9);
    写入("testfile.txt",num2str(a), "overwrite");
The 写入 命令 can 输出 2D matrices in a single 命令. Each column will be separated with a TAB character.

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ savedata ](/hc/en-us/articles/360034411174-savedata) , [ readdata ](/hc/en-us/articles/360034411234-readdata) , [ read ](/hc/en-us/articles/360034931933-read) , [ rm ](/hc/en-us/articles/360034931533-rm) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ ? ](/hc/en-us/articles/360034410434--) , [ endl ](/hc/en-us/articles/360034410414-endl) , [ format ](/hc/en-us/articles/360034931913-format) , [ fileexists ](/hc/en-us/articles/360034931633-fileexists) , [ matlabsave ](/hc/en-us/articles/360034928113-matlabsave)
