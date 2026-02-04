<!--
---
**Translation metadata**
- English title: spline
- Chinese title: spline - 三次样条插值
- Status: Completed
- Translator: AI
- Last updated: 2026-02-03
- Difficulty: Intermediate
- Priority: Standard
---
-->

# spline

对数据集进行三次样条插值。

| **语法** | **描述** |
|---|---|
| out = spline(Ex,xold,xnew); | 一维函数的"非节点"三次样条插值。 |
| | * Ex 是现有数据集<br>* xold 指定 Ex 的采样点<br>* xnew 指定用于插值数据的新点 |
| | xnew 中的点不必在 xold 的范围内。 |
| spline(Ex,xold,xnew,[derivMin; derivMax]); | 一维函数的"夹紧三次样条"插值。 |
| | * Ex 是现有数据集<br>* xold 指定 Ex 的采样点<br>* xnew 指定用于插值数据的新点<br>* derivMin 指定起始点的一阶导数<br>* derivMax 指定终点的一阶导数 |

[[注意:]] [[spline]] 脚本在 2020R2 或更高版本中已修改。要恢复以前版本的结果，请使用"夹紧三次样条"选项并按如下方式定义"derivMin"和"derivMax"：

```
derivMin = (Ex(2)-Ex(1))/(xold(2)-xold(1));
derivMax = (Ex(end)-Ex(end-1))/(xold(end)-xold(end-1));
```

---

**示例**

使用三次样条和线性插值方法在 xnew 处对 Ex 进行重采样。注意 xnew 超出了 xold 的范围。

```
xold=linspace(0,10,7);
Ex=sin(xold);
xnew=linspace(-1,9,25); # 定义新的 x 向量
Exnew=interp(Ex,xold,xnew); # 对新数据集进行插值
Exnew2=spline(Ex,xold,xnew); # 平滑处理
plotxy(xold,Ex,xnew,Exnew,xnew,Exnew2,"x","y","");
legend("old data", "interp", "Spline");
```

示例代码将生成以下图表，显示线性和三次样条插值技术之间的差异。

**另请参见**

[ 命令列表 ](./command_list.md) , [ interp ](./interp.md) , [ plotxy ](./plotxy.md)
