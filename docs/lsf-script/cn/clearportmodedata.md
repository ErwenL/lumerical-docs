<!-- Translation completed: 2026-02-04 -->
<!-- Original command: clearportmodedata -->

# clearportmodedata

    addfdtd; # add FDTD 仿真 区域
    addport; # add port
    set("name","input_port"); # set the name of the port
    seteigensolver("bent waveguide",真); # set the 求解器 to look for 模式 of a bent waveguide
    seteigensolver("bend radius",10e-6); # set bending radius to 10 um
    updateportmodes(1:2); # select the first 2 模式 of the port
    clearportmodedata;

**语法** | **描述**
---|---
clearportmodedata; | Clears 模式 data from selected port. This 函数 does not 返回 any data.

**另请参阅**

[ Ports ](/hc/en-us/articles/360034382554-Ports) , [ addport ](/hc/en-us/articles/360034924793-addport) , [ set ](/hc/en-us/articles/360034928773-set) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ updateportmodes ](/hc/en-us/articles/360034409174-updateportmodes)
