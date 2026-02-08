# write

Writes string variables to text files or to standard output.

Typically the write command is used to output data to a text file. If the specified file
does not exist, it will be created. If it does exist, then the output string will either
be appended to the end of the file or overwrite the file. The write command will
automatically add a new line character at the end of the string.

On Linux systems only, the write command will output to the standard output (stdout) if
a filename is not specified.

| **Syntax**                                | **Description**                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| write(my_string);                         | Write my_string to the standard output (Linux only).                                                                                                                                                                                                                                                                                                                              |
| write("testfile.txt", my_string, option); | Will write the contents of the string variable my_string to testfile.txt. The file "testfile.txt" will be created if it does not exist. option: can be "append" or "overwrite", to append the variable my_string to the end of the file or overwrite the file, respectively. If option is not provided, "append" will be used by default. This function does not return any data. |

**Note** : This command cannot be used while in
[safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**Examples**

Write an array of numbers to a text file. If you want to overwrite the file, use the
"overwrite" option in the command.

```
a=linspace(0,2*pi,9);
write("testfile.txt",num2str(a), "overwrite");
```

The write command can output 2D matrices in a single command. Each column will be
separated with a TAB character.

```
# define the variables to export
a=linspace(0,2*pi,9);
b=sin(a);
# combine both vectors into a single 2D matrix to be output to file
data_to_print=[a,b];
# write the data to the file
write("testfile.txt",num2str(data_to_print));
```

Generally, more complicated formatting is required. For example, suppose you want to
have a header section that describes what the variables are. You also want to use comma
separated columns (CSV), rather than TAB separated. Finally, you want to output the full
double precision numbers, rather than just the first 5 digits.

```
# define the variables to export
a=linspace(0,pi,9);
b=sin(a);
# remove the file if it already exists
rm("testfile.txt");
# write the file header
write("testfile.txt","theta, sin(theta)");
# set num2str() to return 16 digits of precision
format long;
# write the data to the file
for (i=1:length(a) ) {
 str= num2str(a(i))+", "+num2str(b(i));
 write("testfile.txt",str);
}
```

The contents of testfile.txt will be:

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

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ savedata ](./savedata.md) , [ readdata ](./readdata.md) , [ read ](./read.md) ,
[ rm ](./rm.md) , [ num2str ](./num2str.md) , [ ? ](./minus.md) , [ endl ](./endl.md) ,
[ format ](https://optics.ansys.com/hc/en-us/articles/360034931913-format) ,
[ fileexists ](./fileexists.md) , [ matlabsave ](./matlabsave.md)
