# ?

# ? (print, display) - Script operator

[FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
[MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
[DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
[CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
[HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
[FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
[INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)

Prints output to the screen. To change the precision of the output, use the format
script command

| **Syntax** | **Description**                                                                          |
| ---------- | ---------------------------------------------------------------------------------------- |
| ?command;  | Displays the output of the command on the screen This function does not return any data. |

**Examples**

This example shows how the "?" command is used to display the result of the calculation
on the screen.

```
?(5+5);
result: 
10 
```

This example shows how the "?" command is used to display strings.

```
?"file_"+"name_"+num2str(1);
file_name_1
```

\[[NOTE:]\] When the output is a matrix, the maximum length that can be displayed is
2000\. This limitation does not apply to a string.

```
?1:2001;  
matrices of length greater than 2000 are not displayed to the output  
  
?num2str(1:2001)  
1  
2  
3  
⋮  
2000  
2001
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ write ](./write.md) ,
[ format ](https://optics.ansys.com/hc/en-us/articles/360034931913-format) ,
[ # ](./minus.md)

### Associated files

### Related articles

- [Lumerical scripting language - By category](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCCIh5NNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCMIfudNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJNL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNzIyODgzNC1MdW1lcmljYWwtc2NyaXB0aW5nLWxhbmd1YWdlLUJ5LWNhdGVnb3J5BjsIVDoJcmFua2kG--72ec6e9b85cb4036d9162e887b75a6ac3ac390cd)
- [print - Script command](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCJUMwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCMIfudNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI5L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkyOTgxMy1wcmludC1TY3JpcHQtY29tbWFuZAY7CFQ6CXJhbmtpBw%3D%3D--a2ed89ae68cdc7fe129ef311d3144defa8935259)
- [format - Script command](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCMkUwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCMIfudNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI6L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkzMTkxMy1mb3JtYXQtU2NyaXB0LWNvbW1hbmQGOwhUOglyYW5raQg%3D--f3b98f7ba9771b8faaf5ae30fffb85acd9397efa)
- [Grating coupler](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCDaXMdRTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCMIfudNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI0L2hjL2VuLXVzL2FydGljbGVzLzM2MDA0MjMwNTMzNC1HcmF0aW5nLWNvdXBsZXIGOwhUOglyYW5raQk%3D--50b4a12264ea19dbfeda3f50031e9a6af1523027)
- [Traveling Wave Mach-Zehnder Modulator](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCMbyMdRTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCMIfudNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJKL2hjL2VuLXVzL2FydGljbGVzLzM2MDA0MjMyODc3NC1UcmF2ZWxpbmctV2F2ZS1NYWNoLVplaG5kZXItTW9kdWxhdG9yBjsIVDoJcmFua2kK--944a07ea954f39eea58f43a09a9197293fc91d62)
