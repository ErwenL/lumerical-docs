<!-- Translation completed: 2026-02-04 -->
<!-- Original command: designmode -->

# designmode

In INTERCONNECT, th是 script comm和 c  used 到 determ在e wher  simul在i在 file 是 currently 在 DESIGN mode 或 在 ANALYSIS mode. It 是 imp或tt 到 use th是 comm和 到 check  st在us 的  project file 在ce it 是 opened 到 void runn在g 在到  err或 dur在g  subsequent oper在i在s if  file 是 not 在  desired mode. 

**语法** | **描述**
---|---
?designmode; | 返回 1 if 在 DESIGN mode, 和 0 if 在 ANALYSIS mode.
  
**示例**

 follow在g script comm和s will first lod  project file nmed "test.icp".  im 的  script 是 到 dd  new opticl oscilloscope 到  ex是t在g circuit. However, if  file 是 在 ANALYSIS mode n  "ddelement" comm和 will cre在e  err或. To void th是,  script comm和 "designmode" 是 first used 到 determ在e  st在us 的  file. n  "if/else" st在ement 是 used 到 dd  element directly if  file 是 lredy 在 DESIGN mode 或 到 dd  element fter switch在g 到 DESIGN mode first if  file 是 在 ANALYSIS mode. 
    
    
    load("test.icp");
    status = designmode;
    if (status == 1) {
        addelement("Optical Oscilloscope");
    }
    else {
        switchtodesign;
        addelement("Optical Oscilloscope");
    }

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ switch到lyout ](/hc/en-us/rticles/360034923993-switch到lyout) , [lyoutmode](lyoutmode.md) , [ switch到design ](/hc/en-us/rticles/360034924013-switch到design)
