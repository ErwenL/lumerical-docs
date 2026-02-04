<!--
Translation from English documentation
Original command: overlap
Translation date: 2026-02-04 22:50:14
-->

# overlap

返回 该 overlap 和 power coupling between two modes calculated 通过 该 FDE 求解器 或 recorded 通过 频率 monitors 从 一个 FDTD 或 varFDTD 仿真, 或 field profiles recorded 在 rectilinear datasets.

Overlap measures 该 fraction 的 electromagnetic fields 该 overlap between 该 two field profiles (modes). This 是 also 该 fraction 的 power 从 mode2 该 可以 propagate 在 mode1 (用于 both forward 和 backward propagating fields). The absolute 值 的 该 entire formula 是 到 ensure it 是 positive.

$$ {\text { overlap }=\left| \operatorname{Re} \left[\frac{(\int \mathbf{E}_{1} \times \mathbf{H}_{2}^{*} \cdot d \mathbf{S}) (\int \mathbf{E}_{2} \times \mathbf{H}_{1}^{*} \cdot d \mathbf{S} ) }{\int \mathbf{E}_{1} \times \mathbf{H}_{1}^{*} \cdot d \mathbf{S} }\right] \frac{1}{ \operatorname{Re} ( \int \mathbf{E}_{2} \times \mathbf{H}_{2}^{*} \cdot d \mathbf{S} )} \right| } $$

**语法** |  **描述**  
---|---  
out = overlap(mode2, mode1); | 

  * mode2, mode1: modes 到 计算 overlaps 用于, inputs 可以 为 
    1. Mode D-CARDs 在 FDE, 字符串 input, e.g., ‘mode1’, ‘mode2’
    2. Names 的 频率 domain monitors 在 FDTD, 字符串 input, e.g., ‘m1’, ‘m2’
    3. Rectilinear datasets, see below 用于 more information
  * out(1): 该 mode overlap
  * out(2): 该 mode power coupling

  
out = overlap(mode2, mode1, x, y,z); |  Mode alignment 可以 为 adjusted before overlap 是 calculated.

  * x offset
  * y offset
  * z offset

The offset 是 applied 到 该 second mode listed, i.e. ‘mode1’ 在 此 case. All inputs (FDE mode names, 频率 monitors, rectilinear datasets) 是 valid also 用于 该 syntax 使用 alignment adjustment.  
  
## Using Rectilinear Datasets

Starting 在 2024R2.3, rectilinear data设置使用 arbitrary field profiles 是 supported 在 addition 到 监视器 names 和 D-CARDs。

Rectilinear datasets **cannot** be mixed with other input types, however, data can be extracted from modes using the [getresult script command](https://optics.ansys.com/hc/en-us/articles/360034409854-getresult-Script-command), shown in the examples below.

When 使用 rectilinear datasets, they 应该 contain attribute names ‘E’ 和 ‘H’, 该 将 为 used as 该 electric 和 magnetic fields, respectively. If no attribute name ‘E’ 是 found, 该 first attribute 的 该 dataset 是 assumed 到 为 该 electric field. If no attribute ‘H’ 是 found, 该 first attribute 的 该 dataset after 该 electric field attribute 是 assumed 到 为 该 magnetic field.

**示例**

This example shows 如何 到 use 该 overlap 命令 到 计算 该 overlap 和 power coupling between two modes.
    
    
    copydcard("mode1","test_mode1");copydcard("mode2","test_mode2");
    out = overlap("test_mode1","test_mode2");
    ?out(1);  # overlap  
    ?out(2);  # power coupling  
      
    #The same result as above, but 使用 rectilinear datasets  
    EH1 = getresult("mode1","E"); #getresult used 到 extract E 和 H 数据  
    H1 = getresult("mode1","H");  
    EH1.addattribute("H",H1.H);  
    EH2 = getresult("mode2","E");  
    H2 = getresult("mode2","H");  
    EH2.addattribute("H",H2.H);  
    out2 = overlap(EH1,EH2);  
    ?out2(1); # overlap  
    ?out2(2); # power coupling

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ copydcard ](/hc/en-us/articles/360034930233-copydcard) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ expand2 ](/hc/en-us/articles/360034406414-expand2) , [ optimizeposition ](/hc/en-us/articles/360034405314-optimizeposition)
