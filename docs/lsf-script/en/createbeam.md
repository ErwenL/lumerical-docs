# createbeam

Creates a new Gaussian beam that is accessible from the deck/global workspace. The
Gaussian beam has the properties specified in the Overlap analysis -> Beam tab of the
eigensolver analysis window.

| **Syntax**        | **Description**                                                                                                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| createbeam;       | Creates a Gaussian beam in the deck/global workspace. Returns the name of the Gaussian beam created, which is by default "gaussian#" (# being the total number of Gaussian beams already existing in the current deck + 1). |
| out = createbeam; | Creates a Gaussian beam in the deck/global workspace and saves its name in the variable "out".                                                                                                                              |

**Example**

The following script command will create a Gaussian beam in the deck and print its name
in the script prompt.

```
?createbeam;
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md)
