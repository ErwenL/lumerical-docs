<!-- Translated: 2024-01-XX by AI Assistant -->
<!-- Status: Initial translation -->
<!-- Review needed: Technical terms, consistency check -->

# runoptimization

在指定条件下优化所选元件的属性。

**语法** | **描述**  
---|---  
x=runoptimization(element, property, min, max, analyzer, result, 'target', target, tolerance=1e-9, iterations=2000) | 优化元件属性，直到达到分析器结果的目标值。函数返回一个包含两列的数组，第一列包含属性值，第二列包含结果值。  
x=runoptimization(element, property, min, max, analyzer, result, 'minimize', tolerance=1e-9, iterations=2000) | 优化元件属性，直到达到分析器结果的最小值。函数返回一个包含两列的数组，第一列包含属性值，第二列包含结果值。  
x=runoptimization(element, property, min, max, analyzer, result, 'maximize', tolerance=1e-9, iterations=2000) | 优化元件属性，直到达到分析器结果的最大值。函数返回一个包含两列的数组，第一列包含属性值，第二列包含结果值。  

**示例**

### 以下脚本行优化 PIN 光电探测器的散粒噪声，以达到目标值

```
x=runoptimization("PIN Photodetector","thermal noise",1e-20,1e-17,"Eye Diagram","measurement/Q factor","target",6,1e-2);
```

### 以下脚本行搜索 LP Bessel 滤波器的最小截止频率

```
x=runoptimization("LP Bessel Filter","cutoff frequency",1e+09,1e+10,"Eye Diagram","measurement/log of BER","minimize");
```

### 以下脚本行搜索 LP Bessel 滤波器的最大截止频率

```
x=runoptimization("LP Bessel Filter","cutoff frequency",1e+09,1e+10,"Eye Diagram","measurement/Q factor","maximize");
```
