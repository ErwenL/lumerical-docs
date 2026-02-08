# readdata

Reads a file with data in a row/column format. User can import numerical values stored
in text files with the readdata command. The data must be correctly formatted so each
row has the same number of columns. Readdata will ignore any line that begins with a
letter. The supported file format is ASCII.

| **Syntax**                  | **Description**                                                                                                                                                                                                                                                                                                  |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| M=readdata("filename.txt"); | Will load the text file filename into matrix variable M. Any lines starting with a letter are ignored. Note: This function will check for the file in the current working directory. If the file to read from is in a different directory, either specify the full path or change the current working directory. |

**Examples**

If you have a text file called testfile.txt with the following data:

Time Value

0.0 3.2e-6

1.0 2.8e10

2.0 4.1e5

3.0 3.3

The first rows contains the column headers, and the next four rows contain data. In this
case, readdata will ignore the first line, and import the data as a 4x2 matrix.

```
M=readdata("testfile.txt");
?M;
result: 
0 3.2e-006 
1 2.8e+010 
2 4.1e+005 
3 3.3 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ rm ](./rm.md) ,
[ write ](./write.md) , [ read ](./read.md) , [ str2num ](./str2num.md) ,
[ findstring ](./findstring.md) , [ replace ](./replace.md) ,
[ replacestring ](./replacestring.md) , [ substring ](./substring.md) ,
[ fileexists ](./fileexists.md)
