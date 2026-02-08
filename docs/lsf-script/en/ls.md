# ls

Lists files in a directory. Files other than Lumerical project files are also listed.

| **Syntax**                                     | **Description**                                                                |
| ---------------------------------------------- | ------------------------------------------------------------------------------ |
| out = dir; out = ls;                           | The output is a string. Use ?dir; to write the value to the screen.            |
| out = dir("directory"); out = ls("directory"); | Lists the files in the specified directory. For example, ?ls("C:\\Downloads"); |

**Example**

Uses the splitstring command to get the contents of a directory in a cell (ie. string)
array. Then loop through the array looking for all FDTD project files (.fsp).

```
files = splitstring(dir,endl);    # directory contents in a cell(string) array
for(i=1:length(files)) {          # loop over all files
 if (findstring(files{i},"fsp") != -1) {  # look for 'fsp' files
  if (fileexists(files{i})) {       # check if the file exists
   ?files{i};               # output file name
   load(files{i});            # load file
  }
 }
}
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ load ](./load.md) ,
[ splitstring ](./splitstring.md)
