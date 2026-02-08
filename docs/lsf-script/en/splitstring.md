# splitstring

Splits a long string into a series of substrings, where the substrings are stored in a
cell (i.e., string) array.

| **Syntax**                 | **Description**                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| s2 = splitstring(s1,endl); | Split the string S1 into a series of strings, using the end of line character as the delimiter between strings. S2 is a cell array. |

**Example**

Use the splitstring command to get the contents of a directory in a cell (i.e., string)
array. Then loop through the array looking for all FDTD project files (.fsp).

```
files = splitstring(dir,endl);        # directory contents in a cell (string) array
for(i=1:length(files)) {           # loop over all files
 if (findstring(files{i},"fsp") != -1) {  # look for 'fsp' files
  if (fileexists(files{i})) {       # check if the file exists (ie. it's a file and not a directory)
   ?files{i};               # output file name
   load(files{i});            # load file
  }
 }
}
```

A similar example for getting the names of all monitors in a simulation. Loop through
all monitors, checking if they contain a result named 'E'. If so, save that data to a
file.

```
mNames = splitstring(getresult,endl);
 
for (i=1:length(mNames)) {
 if (haveresult(mNames{i},"E")) {
  E=getresult(mNames{i},"E");   # get a result from that monitor
 } else {
  E = mNames{i} + " did not contain the specified data.";
 }
 filename = "file"+num2str(i);
 savedata(filename,E);     # save data to ldf files
}
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ length ](./length.md) ,
[ substring ](./substring.md) , [ findstring ](./findstring.md) ,
[ replace ](./replace.md) , [ str2num ](./str2num.md) , [ num2str ](./num2str.md) ,
[ cell ](./cell.md) , [ dir ](./dir.md) , [ getresult ](./getresult.md) ,
[ lower ](./lower.md) , [ upper ](./upper.md) , [ toscript ](./toscript.md)
