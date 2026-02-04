# now

显示 Unix 时间。

**语法** | **描述**
---|---
?now; | 显示当前 UNIX 时间

**示例**

```
?now;
result:
1494022382266
```

获取模拟作业运行时间

```
load("simulationfile");
switchtolayout;
ct1=now;
run;
ct2=now;
ctmin=(ct2-ct1)/1000/60;
ctsec=(ct2-ct1)/1000/60*60;
?"CPU runtime: "+ num2str(ctmin) +" min";
?"CPU runtime: "+ num2str(ctsec) +" sec";
