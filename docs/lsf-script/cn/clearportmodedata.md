<!--
Translation from English documentation
Original command: clearportmodedata
Translation date: 2026-02-04 22:49:48
-->

# clearportmodedata

Clears mode 数据 从 选中的 FDTD 端口 和 ports 在 MODE's EME 求解器. For more information about 该 端口 对象 see [ Ports ](/hc/en-us/articles/360034382554-Ports) .

**语法** |  **描述**  
---|---  
clearportmodedata; |  Clears mode 数据 从 选中的 端口. This 函数 does not 返回 any 数据.  
  
**示例** The following 脚本 添加 一个 FDTD 仿真 region 和 端口, 那么 设置 该 name 的 该 端口, 和 selects 该 端口 modes 那么 clears 该 选中的 端口 mode 数据.
    
    
    # 添加 对象  
    addfdtd; # 添加 FDTD 仿真 region
    addport; # 添加 端口
    # 设置 up 端口
    设置("name","input_port"); # 设置 该 name 的 该 端口
    seteigensolver("bent waveguide",true); # 设置 该 求解器 到 look 用于 modes 的 一个 bent waveguide
    seteigensolver("bend radius",10e-6); # 设置 bending radius 到 10 um
    updateportmodes(1:2); # select 该 first 2 modes 的 该 端口
    # clear 该 选中的 mode 数据
    clearportmodedata;

**参见**

[ Ports ](/hc/en-us/articles/360034382554-Ports) , [ addport ](/hc/en-us/articles/360034924793-addport) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ updateportmodes ](/hc/en-us/articles/360034409174-updateportmodes)
