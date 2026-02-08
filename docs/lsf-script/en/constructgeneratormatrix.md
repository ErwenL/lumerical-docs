# constructgeneratormatrix

Constructs a symmetric coding generator matrix. This command is especially useful
together with the FEC block.

| **Syntax**                                                   | **Description**                                                                                                                                                                                                               |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| constructgeneratormatrix(parityin, generatorout, parityout); | Constructs a symmetric coding generator matrix ‘generatorout’ and the correspondent parity check matrix ‘parityout’ from a input parity check matrix ‘parityin’. The input and the generated files are AList formatted files. |
| **Example**                                                  |                                                                                                                                                                                                                               |

```
constructgeneratormatrix("hamming_7_4_1_h.alist", "hamming_7_4_1_g.alist", "hamming_7_4_1_h.alist");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md)
