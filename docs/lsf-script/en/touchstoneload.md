# touchstoneload

Loads passive network data from a file containing Touchstone file formatted
s-parameters. For more information about the Touchstone specification refer to
[this page](https://helpfiles.keysight.com/csg/N1930xB/FilePrint/SnP_File_Format.htm).

| **Syntax**                       | **Description**                                                                                                                                                                    |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = touchstoneload (filename); | It returns a matrix where the first column contains the frequency values in Hz. S-parameters are returned using MA format, where M is the magnitude and A is the angle in radians. |

### Example

In this simple example, an s2p formatted touchstone file is loaded.

```
#filename PA3-110.s2p
out=touchstoneload('PA3-110.s2p');
#display loaded values
?out
result: 
2e+009 0.933287 -0.363001 0.01969 0.641089 0.000111993 1.32332 0.978723 -0.583973 
3e+009 0.930915 -0.519211 0.0985939 0.0471047 0.000391381 -1.06654 0.950211 -0.84896 
4e+009 0.930101 -0.670744 0.246948 -0.680015 0.000315715 1.6003 0.903597 -1.08584 
5e+009 0.926808 -0.840421 0.716968 -2.01287 0.000155772 -0.796779 0.887657 -1.24546 
6e+009 0.899653 -0.98587 0.426378 2.38857 0.00010399 -1.82364 0.914271 -1.43473 
...
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md)
