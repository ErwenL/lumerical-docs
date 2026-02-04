<!--
Translation from English documentation
Original command: expand
Translation date: 2026-02-04 22:49:48
-->

# expand

返回 该 expansion coefficients between 该 fields recorded at two arbitrary DFT monitors, saved 在 two D-CARDs, 或 saved 在 two rectilinear datasets. The coefficients 是 defined according 到:

$$ \begin{数组}{l}{一个=0.25 *\left(\frac{\int d \mathbf{S} \cdot \mathbf{E}_{1} \times \mathbf{H}_{2}^{*}}{N}+\frac{\int d \mathbf{S} \cdot \mathbf{E}_{2}^{*} \times \mathbf{H}_{1}}{\operatorname{conj}(N)}\right)} \\\ {b=0.25 *\left(\frac{\int d \mathbf{S} \cdot \mathbf{E}_{1} \times \mathbf{H}_{2}^{*}}{N}-\frac{\int d \mathbf{S} \cdot \mathbf{E}_{2}^{*} \times \mathbf{H}_{1}}{\operatorname{con} j(N)}\right)} \\\ {N=0.5^{*} \int d \mathbf{S}\cdot \mathbf{E}_{2} \times \mathbf{H}_{2}^{*}} \\\ {P=0.5 * \int d \mathbf{S} \cdot \mathbf{E}_{1} \times \mathbf{H}_{1}^{*}}\end{数组} $$

For more detail 在 如何 到 use 此 命令, definitions 在 该 参数 和 如何 到 interpret 该 results, please see [ Using Mode Expansion Monitors](/hc/en-us/articles/360034902433-Using-Mode-Expansion-Monitors). 注意 该 real(N) 是 该 power 的 该 waveguide mode. conj(N) 是 equal 到 N 如果 此 是 一个 real 数字. For 该 unconjugated coefficients, see [ expand2](/hc/en-us/articles/360034406414-expand2).

**语法** |  **描述**  
---|---  
expand(mode1,mode_ref,x,y,z); |  Outputs 该 expansion coefficients between 该 fields 的 two modes

  * mode1, mode_ref: field information, 使用 \\(\mathbf{E}_{1}\\),\\(\mathbf{H}_{1}\\) contained 在 mode1, 和 \\(\mathbf{E}_{2}\\),\\(\mathbf{H}_{2}\\) contained 在 mode_ref. Can 为 在 one 的 该 following formats: 
    1.        1. Frequency domain 监视器 names, 字符串 input, e.g. “monitor1”
       2. Mode D-CARDs containing field information, 字符串 input, e.g. “mode1”
       3. Rectilinear datasets, see below 用于 more information
  * x,y,z: spatial displacement 的 该 fields 从 monitor1 使用 respect 到 那些 从 monitor_ref

  
  
## Using Rectilinear Datasets

Starting 在 2024R2.3, rectilinear data设置使用 arbitrary field profiles 是 supported 在 addition 到 监视器 names 和 D-CARDs。

Rectilinear datasets **cannot** be mixed with other input types, however, data can be extracted from modes using the [getresult script command](https://optics.ansys.com/hc/en-us/articles/360034409854-getresult-Script-command), shown in the examples below.

When 使用 rectilinear datasets, they 应该 contain attribute names ‘E’ 和 ‘H’, 该 将 为 used as 该 electric 和 magnetic fields, respectively. If no attribute name ‘E’ 是 found, 该 first attribute 的 该 dataset 是 assumed 到 为 该 electric field. If no attribute ‘H’ 是 found, 该 first attribute 的 该 dataset after 该 electric field attribute 是 assumed 到 为 该 magnetic field.

**示例**

The following 脚本 expands 该 fields 从 监视器 "R" onto 该 reference 监视器 "R_ref":
    
    
    M = expand("R","R_ref",0,0,0);
    f = getdata("R","f");
    一个 = pinch(M,1,1);
    b = pinch(M,1,2);
    n = pinch(M,1,3);
    p = pinch(M,1,4);
    S11 = b;

The following 脚本 expands 该 fields 从 监视器 “R” onto reference 监视器 “R_ref” 通过 first converting them 到 rectilinear data设置使用 getresult。 The result 是 identical 到 above.
    
    
    # example 使用 rectilinear datasets  
    #First, obtain rectilinear dataset 从 monitors 使用 getresult  
    #These datasets could have been imported 从 elsewhere as well  
    EH1 = getresult("R","E");  
    H1 = getresult("R","H");  
    EH1.addattribute("H",H1.H);  
    EH2 = getresult("R_ref","E");  
    H2 = getresult("R_ref","H");  
    EH2.addattribute("R_ref",H2.H);  
      
    M = expand(EH1,EH2,0,0,0);  
    f = EH1.f;  
    一个 = pinch(M,1,1);  
    b = pinch(M,1,2);  
    n = pinch(M,1,3);  
    p = pinch(M,1,4);  
    S11 = b;

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ Using Mode Expansion Monitors ](/hc/en-us/articles/360034902433-Using-Mode-Expansion-Monitors) , [ setexpansion ](/hc/en-us/articles/360034408974-setexpansion) , [ removeexpansion ](/hc/en-us/articles/360034408994-removeexpansion) , [ expand2 ](/hc/en-us/articles/360034406414-expand2)
