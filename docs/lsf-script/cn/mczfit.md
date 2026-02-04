# mczfit

将可变增益滤波器拟合到一组增益曲线数据，其中曲线组中的每条曲线对应一个载流子密度值，生成增益滤波器系数文件以供 TWLM 元素使用。

**语法** | **描述**
---|---
out=mczfit(inputfilename, outputfilebase, centrefrequency, samplerate, maxnumcoef, tol, maxiter, rectangular, rolloff); | 将可变增益滤波器拟合到一组增益曲线数据，其中曲线组中的每条曲线对应一个载流子密度值，生成增益滤波器系数文件以供 TWLM 元素使用。" **inputfilename** " 是包含输入数据文件名称的字符串（包括后缀）。输入数据的格式如下所述。" **outputfilename** " 是包含增益滤波器系数文件名称（不包括后缀）的字符串。" **centrefrequency** " 是执行增益拟合的频率带的中心频率。" **samplerate** " 是执行增益拟合的频率带的带宽。" **maxnumcoef** " 是用于拟合数据的最大滤波器系数数量。" **tol** " 是容差 " **rectangular** " 是布尔值，它定义数据格式。"true" 表示 'real' 和 'imaginary' 格式；"false" 表示带有 'amplitude' 和 'phase' 的极坐标格式 " **maxiter** " 是用于拟合数据的最大迭代次数。" **rolloff** " 是输入频率数据滚降到带边缘两个值的平均值的带宽分数。

**实现细节**

数据文件的格式如下：

```
(1, Nc)
carrierdensity_1, carrierdenisty_2, …, carrierdensity_Nc
(Ns, Nc+1)
freq_1gain_1_1gain_1_2…gain_1_Nc
freq_2gain_2_1gain_2_2…gain_2_Nc
……………
freq_Nsgain_Ns_1gain_Ns_2…gain_Ns_Nc
```

参数定义如下表：

Nc | 增益曲线的数量
---|---
Ns | 频率样本的数量
carrierdensity_j | 对应第 j 条增益曲线的载流子密度
freq_i | 第 i 个频率样本
gain_i_j | 第 j 条曲线中第 i 个频率样本的增益值

注释：

  1. 频率必须按升序排列，frequency_1 最低，frequency_Ns 最高
  2. 增益曲线和载流子密度必须按载流子密度降序排列。也就是说，carrierdensity_1 是最大的载流子密度，carrierdensity_Nc 是最低的载流子密度，gain_i_1 是最大载流子密度和第 i 个频率样本的增益，gain_i_Nc 是最低载流子密度和第 i 个频率样本的增益

返回值如下表：

fit_out | 包含字段的结构体
---|---
frequency | 频率样本点的列向量
input | 矩阵，包含每列向量，用于每个工作点的输入频率响应以进行拟合
operatingPoint | 行向量，包含与输入矩阵各列中输入频率响应相对应的输入工作点
operatingPointInterpolated | 行向量，包含工作点输入值之间的线性插值
output | 矩阵，包含每列向量，用于每个输入工作点的拟合频率响应
outputInterpolated | 矩阵，包含每列向量，用于行向量 'operatingPointInterpolated' 中包含的每个线性插值工作点的拟合频率响应

注意：

此脚本函数还生成增益滤波器系数以供 TWLM 元素使用。文件名将是 outputfilename.mcfdb。

**示例**

有关此命令的详细用法，请参阅应用程序示例页面增益拟合。

**另请参阅**

- [命令列表](./命令列表.md)
- [mcfit](./mcfit.md)
