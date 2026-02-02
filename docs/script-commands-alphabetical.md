# Lumerical Scripting Language - Alphabetical List

## 概述

本文档按字母顺序列出了 Lumerical 脚本语言（LSF）的所有可用命令。这些命令可以通过 Lumapi Python 接口直接调用，每个 LSF 命令对应一个 Python 方法。

*注意：本列表为通用参考，具体命令和可用性可能因 Lumerical 版本和产品（FDTD Solutions, MODE Solutions, DEVICE, INTERCONNECT）而异。*

## 命令列表

### A

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `add` | 添加对象到仿真 | `session.add()` | 通用 |
| `addcustom` | 添加自定义监视器 ✅ [文档](./lumapi/addcustom.md) | `session.addcustom()` | FDTD, MODE |
| `addcylinder` | 添加圆柱体 ✅ [文档](./lumapi/addcylinder.md) | `session.addcylinder()` | 通用 |
| `adddipole` | 添加偶极子源 ✅ [文档](./lumapi/adddipole.md) | `session.adddipole()` | FDTD |
| `addfdtd` | 添加 FDTD 求解器 ✅ [文档](./lumapi/addfdtd.md) | `session.addfdtd()` | FDTD |
| `addefdtd` | 添加电-热 FDTD 求解器 ✅ [文档](./lumapi/addefdtd.md) | `session.addefdtd()` | FDTD |
| `addeme` | 添加 EME 求解器 ✅ [文档](./lumapi/addeme.md) | `session.addeme()` | MODE |
| `addemeprofile` | 添加 EME 场监视器 ✅ [文档](./lumapi/addemeprofile.md) | `session.addemeprofile()` | MODE |
| `addevent` | 添加事件监视器 ✅ [文档](./lumapi/addevent.md) | `session.addevent()` | INTERCONNECT |
| `addfde` | 添加 FDE 求解器 ✅ [文档](./lumapi/addfde.md) | `session.addfde()` | MODE |
| `addfdeprofile` | 添加 FDE 场监视器 ✅ [文档](./lumapi/addfdeprofile.md) | `session.addfdeprofile()` | MODE |
| `addgrating` | 添加光栅 ✅ [文档](./lumapi/addgrating.md) | `session.addgrating()` | FDTD, MODE |
| `addheat` | 添加热求解器 ✅ [文档](./lumapi/addheat.md) | `session.addheat()` | DEVICE |
| `addindex` | 添加折射率监视器 ✅ [文档](./lumapi/addindex.md) | `session.addindex()` | FDTD, MODE |
| `addimport` | 添加导入对象 ✅ [文档](./lumapi/addimport.md) | `session.addimport()` | 通用 |
| `addmaterial` | 添加材料 ✅ [文档](./lumapi/addmaterial.md) | `session.addmaterial()` | 通用 |
| `addmesh` | 添加网格覆盖区 ✅ [文档](./lumapi/addmesh.md) | `session.addmesh()` | FDTD, MODE |
| `addmode` | 添加模式源 ✅ [文档](./lumapi/addmode.md) | `session.addmode()` | FDTD, MODE |
| `addmodeexpansion` | 添加模式扩展监视器 ✅ [文档](./lumapi/addmodeexpansion.md) | `session.addmodeexpansion()` | FDTD, MODE |
| `addmodesource` | 添加模式源 ✅ [文档](./lumapi/addmodesource.md) | `session.addmodesource()` | varFDTD |
| `addnoise` | 添加噪声源 ✅ [文档](./lumapi/addnoise.md) | `session.addnoise()` | INTERCONNECT |
| `addoptical` | 添加光学端口 ✅ [文档](./lumapi/addoptical.md) | `session.addoptical()` | INTERCONNECT |
| `addpath` | 添加路径到脚本搜索路径 | `session.addpath()` | 通用 |
| `addplanarsolid` | 添加平面实体 ✅ [文档](./lumapi/addplanarsolid.md) | `session.addplanarsolid()` | 通用 |
| `addport` | 添加端口 ✅ [文档](./lumapi/addport.md) | `session.addport()` | FDTD, MODE, INTERCONNECT |
| `addpower` | 添加功率监视器 ✅ [文档](./lumapi/addpower.md) | `session.addpower()` | FDTD, MODE |
| `addprism` | 添加棱柱 ✅ [文档](./lumapi/addprism.md) | `session.addprism()` | 通用 |
| `addprofile` | 添加场监视器 ✅ [文档](./lumapi/addprofile.md) | `session.addprofile()` | FDTD, MODE |
| `addproperty` | 添加材料属性 ✅ [文档](./lumapi/addproperty.md) | `session.addproperty()` | 通用 |
| `addrect` | 添加矩形 ✅ [文档](./lumapi/addrect.md) | `session.addrect()` | 通用 |
| `addring` | 添加环形结构 ✅ [文档](./lumapi/addring.md) | `session.addring()` | 通用 |
| `addscript` | 添加脚本对象 ✅ [文档](./lumapi/addscript.md) | `session.addscript()` | 通用 |
| `addsphere` | 添加球体 ✅ [文档](./lumapi/addsphere.md) | `session.addsphere()` | 通用 |
| `addtds` | 添加时域监视器 ✅ [文档](./lumapi/addtds.md) | `session.addtds()` | FDTD |
| `addthermal` | 添加热监视器 ✅ [文档](./lumapi/addthermal.md) | `session.addthermal()` | DEVICE |
| `addtogroup` | 将对象添加到组 ✅ [文档](./lumapi/addtogroup.md) | `session.addtogroup()` | 通用 |
| `addvarfdtd` | 添加变分 FDTD 求解器 ✅ [文档](./lumapi/addvarfdtd.md) | `session.addvarfdtd()` | varFDTD |
| `addwaveguide` | 添加波导结构 ✅ [文档](./lumapi/addwaveguide.md) | `session.addwaveguide()` | MODE |
| `animate` | 创建动画 ✅ [文档](./lumapi/animate.md) | `session.animate()` | 通用 |
| `append` | 追加数据到数组 ✅ [文档](./lumapi/append.md) | `session.append()` | 通用 |
| `apply` | 应用变换 ✅ [文档](./lumapi/apply.md) | `session.apply()` | 通用 |

### B

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `bentwaveguide` | 设置弯曲波导参数 ✅ [文档](./lumapi/bentwaveguide.md) | `session.bentwaveguide()` | MODE |

### C

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `calculate` | 执行计算 ✅ [文档](./lumapi/calculate.md) | `session.calculate()` | 通用 |
| `call` | 调用函数 ✅ [文档](./lumapi/call.md) | `session.call()` | 通用 |
| `callsplitter` | 调用分路器模型 ✅ [文档](./lumapi/callsplitter.md) | `session.callsplitter()` | INTERCONNECT |
| `cascadedsmatrix` | 计算级联 S 矩阵 ✅ [文档](./lumapi/cascadedsmatrix.md) | `session.cascadedsmatrix()` | INTERCONNECT |
| `cd` | 改变工作目录 ✅ [文档](./lumapi/cd.md) | `session.cd()` | 通用 |
| `cellgroup` | 设置单元组 ✅ [文档](./lumapi/cellgroup.md) | `session.cellgroup()` | MODE |
| `change` | 更改对象属性 ✅ [文档](./lumapi/change.md) | `session.change()` | 通用 |
| `chdir` | 改变目录 ✅ [文档](./lumapi/chdir.md) | `session.chdir()` | 通用 |
| `clear` | 清除变量 ✅ [文档](./lumapi/clear.md) | `session.clear()` | 通用 |
| `cleargrid` | 清除网格 ✅ [文档](./lumapi/cleargrid.md) | `session.cleargrid()` | 通用 |
| `close` | 关闭项目或文件 ✅ [文档](./lumapi/close.md) | `session.close()` | 通用 |
| `conj` | 复数共轭 ✅ [文档](./lumapi/conj.md) | `session.conj()` | 通用 |
| `copy` | 复制对象 ✅ [文档](./lumapi/copy.md) | `session.copy()` | 通用 |
| `copyopt` | 复制优化设置 ✅ [文档](./lumapi/copyopt.md) | `session.copyopt()` | 通用 |
| `createcircle` | 创建圆形 ✅ [文档](./lumapi/createcircle.md) | `session.createcircle()` | 通用 |
| `createdisk` | 创建磁盘 ✅ [文档](./lumapi/createdisk.md) | `session.createdisk()` | 通用 |
| `creategroup` | 创建组 ✅ [文档](./lumapi/creategroup.md) | `session.creategroup()` | 通用 |
| `createline` | 创建线 ✅ [文档](./lumapi/createline.md) | `session.createline()` | 通用 |
| `createpoly` | 创建多边形 ✅ [文档](./lumapi/createpoly.md) | `session.createpoly()` | 通用 |
| `createrect` | 创建矩形 ✅ [文档](./lumapi/createrect.md) | `session.createrect()` | 通用 |
| `cross` | 向量叉积 ✅ [文档](./lumapi/cross.md) | `session.cross()` | 通用 |
| `crosssection` | 计算横截面 ✅ [文档](./lumapi/crosssection.md) | `session.crosssection()` | 通用 |

### D

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `delete` | 删除对象 ✅ [文档](./lumapi/delete.md) | `session.delete()` | 通用 |
| `dipole` | 设置偶极子源 ✅ [文档](./lumapi/dipole.md) | `session.dipole()` | FDTD |
| `dipolepower` | 计算偶极子功率 ✅ [文档](./lumapi/dipolepower.md) | `session.dipolepower()` | FDTD |
| `disp` | 显示变量值 ✅ [文档](./lumapi/disp.md) | `session.disp()` | 通用 |
| `divide` | 数组除法 ✅ [文档](./lumapi/divide.md) | `session.divide()` | 通用 |
| `dot` | 向量点积 ✅ [文档](./lumapi/dot.md) | `session.dot()` | 通用 |
| `draw` | 绘制对象 ✅ [文档](./lumapi/draw.md) | `session.draw()` | 通用 |

### E

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `echo` | 回显文本 ✅ [文档](./lumapi/echo.md) | `session.echo()` | 通用 |
| `edit` | 编辑对象 ✅ [文档](./lumapi/edit.md) | `session.edit()` | 通用 |
| `eigensolver` | 设置本征求解器 ✅ [文档](./lumapi/eigensolver.md) | `session.eigensolver()` | MODE |
| `else` | 条件语句 ✅ [文档](./lumapi/else.md) | `session.else()` | 通用 |
| `elseif` | 条件语句 ✅ [文档](./lumapi/elseif.md) | `session.elseif()` | 通用 |
| `emeanalysis` | EME 分析设置 ✅ [文档](./lumapi/emeanalysis.md) | `session.emeanalysis()` | MODE |
| `end` | 结束代码块 ✅ [文档](./lumapi/end.md) | `session.end()` | 通用 |
| `epsilon` | 计算介电常数 ✅ [文档](./lumapi/epsilon.md) | `session.epsilon()` | 通用 |
| `eval` | 执行脚本字符串 ✅ [文档](./lumapi/eval.md) | `session.eval()` | 通用 |
| `export` | 导出数据 ✅ [文档](./lumapi/export.md) | `session.export()` | 通用 |
| `eye` | 创建单位矩阵 ✅ [文档](./lumapi/eye.md) | `session.eye()` | 通用 |

### F

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `farfield` | 计算远场 ✅ [文档](./lumapi/farfield.md) | `session.farfield()` | FDTD |
| `farfieldprojection` | 远场投影 ✅ [文档](./lumapi/farfieldprojection.md) | `session.farfieldprojection()` | FDTD |
| `fdtdanalysis` | FDTD 分析设置 | `session.fdtdanalysis()` | FDTD |
| `field` | 获取场数据 | `session.field()` | FDTD, MODE |
| `fieldsummary` | 场数据摘要 | `session.fieldsummary()` | FDTD, MODE |
| `find` | 查找对象 | `session.find()` | 通用 |
| `for` | 循环语句 | `session.for()` | 通用 |
| `fourier` | 傅里叶变换 | `session.fourier()` | 通用 |
| `fourier2` | 二维傅里叶变换 | `session.fourier2()` | 通用 |
| `frequency` | 设置频率 | `session.frequency()` | 通用 |
| `function` | 定义函数 | `session.function()` | 通用 |

### G

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `get` | 获取对象属性 | `session.get()` | 通用 |
| `getdata` | 获取数据 | `session.getdata()` | 通用 |
| `getelectric` | 获取电场数据 | `session.getelectric()` | FDTD, MODE |
| `getepsw` | 获取频域介电常数 | `session.getepsw()` | FDTD |
| `getfield` | 获取场数据 | `session.getfield()` | FDTD, MODE |
| `getglobalmonitor` | 获取全局监视器设置 | `session.getglobalmonitor()` | FDTD, MODE |
| `getglobalsource` | 获取全局源设置 | `session.getglobalsource()` | FDTD, MODE |
| `getmaterial` | 获取材料数据 | `session.getmaterial()` | 通用 |
| `getmagnetic` | 获取磁场数据 | `session.getmagnetic()` | FDTD, MODE |
| `getmode` | 获取模式数据 | `session.getmode()` | MODE |
| `getnamed` | 按名称获取对象属性 | `session.getnamed()` | 通用 |
| `getobject` | 获取对象 | `session.getobject()` | 通用 |
| `getoptical` | 获取光学数据 | `session.getoptical()` | INTERCONNECT |
| `getpattern` | 获取辐射模式 | `session.getpattern()` | FDTD |
| `getpower` | 获取功率数据 | `session.getpower()` | FDTD, MODE |
| `getprofile` | 获取剖面数据 | `session.getprofile()` | FDTD, MODE |
| `getresult` | 获取结果数据 ✅ [文档](./lumapi/getresult.md) | `session.getresult()` | 通用 |
| `getsweep` | 获取扫描数据 | `session.getsweep()` | 通用 |
| `gettemperature` | 获取温度数据 | `session.gettemperature()` | DEVICE |
| `gradient` | 计算梯度 | `session.gradient()` | 通用 |
| `grid` | 设置网格 | `session.grid()` | 通用 |
| `group` | 对象分组操作 | `session.group()` | 通用 |

### H

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `help` | 显示帮助 | `session.help()` | 通用 |
| `hstack` | 水平堆叠数组 | `session.hstack()` | 通用 |

### I

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `if` | 条件语句 | `session.if()` | 通用 |
| `import` | 导入数据 | `session.import()` | 通用 |
| `importdataset` | 导入数据集 | `session.importdataset()` | 通用 |
| `importgeometry` | 导入几何 | `session.importgeometry()` | 通用 |
| `importobj` | 导入 OBJ 文件 | `session.importobj()` | 通用 |
| `importstl` | 导入 STL 文件 | `session.importstl()` | 通用 |
| `index` | 获取折射率数据 | `session.index()` | 通用 |
| `integrate` | 积分计算 | `session.integrate()` | 通用 |
| `interpolate` | 插值计算 | `session.interpolate()` | 通用 |
| `intersect` | 计算交集 | `session.intersect()` | 通用 |

### J

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `join` | 连接字符串 | `session.join()` | 通用 |

### L

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `length` | 获取数组长度 | `session.length()` | 通用 |
| `linspace` | 创建线性间隔数组 | `session.linspace()` | 通用 |
| `load` | 加载数据 | `session.load()` | 通用 |
| `loadobj` | 加载对象 | `session.loadobj()` | 通用 |
| `log` | 自然对数 | `session.log()` | 通用 |
| `log10` | 以 10 为底的对数 | `session.log10()` | 通用 |
| `logspace` | 创建对数间隔数组 | `session.logspace()` | 通用 |
| `lookup` | 查找表操作 | `session.lookup()` | 通用 |

### M

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `makecircle` | 创建圆形 | `session.makecircle()` | 通用 |
| `makedisk` | 创建磁盘 | `session.makedisk()` | 通用 |
| `makegroup` | 创建组 | `session.makegroup()` | 通用 |
| `makeline` | 创建线 | `session.makeline()` | 通用 |
| `makepoly` | 创建多边形 | `session.makepoly()` | 通用 |
| `makerect` | 创建矩形 | `session.makerect()` | 通用 |
| `material` | 材料操作 | `session.material()` | 通用 |
| `matlabsave` | 保存为 MATLAB 格式 | `session.matlabsave()` | 通用 |
| `max` | 最大值 | `session.max()` | 通用 |
| `mesh` | 网格操作 | `session.mesh()` | 通用 |
| `meshgrid` | 创建网格坐标 | `session.meshgrid()` | 通用 |
| `meshgrid4d` | 创建 4D 网格坐标 | `session.meshgrid4d()` | 通用 |
| `min` | 最小值 | `session.min()` | 通用 |
| `minus` | 减法 | `session.minus()` | 通用 |
| `mkdir` | 创建目录 | `session.mkdir()` | 通用 |

### N

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `named` | 按名称操作对象 | `session.named()` | 通用 |
| `newproject` | 新建项目 | `session.newproject()` | 通用 |
| `norm` | 计算范数 | `session.norm()` | 通用 |
| `normalize` | 归一化 | `session.normalize()` | 通用 |
| `num2str` | 数字转字符串 | `session.num2str()` | 通用 |

### O

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `ones` | 创建全 1 数组 | `session.ones()` | 通用 |
| `open` | 打开文件 | `session.open()` | 通用 |
| `optimize` | 优化操作 | `session.optimize()` | 通用 |
| `overlap` | 计算重叠积分 | `session.overlap()` | MODE |

### P

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `padarray` | 填充数组 | `session.padarray()` | 通用 |
| `parallel` | 并行计算设置 | `session.parallel()` | 通用 |
| `paste` | 粘贴对象 | `session.paste()` | 通用 |
| `patch` | 创建面片 | `session.patch()` | 通用 |
| `pinch` | 压缩数组维度 | `session.pinch()` | 通用 |
| `plot` | 绘图 | `session.plot()` | 通用 |
| `plus` | 加法 | `session.plus()` | 通用 |
| `polarization` | 设置偏振 | `session.polarization()` | 通用 |
| `polyarea` | 计算多边形面积 | `session.polyarea()` | 通用 |
| `polyfit` | 多项式拟合 | `session.polyfit()` | 通用 |
| `polyval` | 多项式求值 | `session.polyval()` | 通用 |
| `power` | 功率计算 | `session.power()` | 通用 |
| `print` | 打印输出 | `session.print()` | 通用 |
| `printtomatlab` | 打印到 MATLAB | `session.printtomatlab()` | 通用 |
| `product` | 数组乘积 | `session.product()` | 通用 |
| `properties` | 获取对象属性列表 | `session.properties()` | 通用 |

### Q

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `quit` | 退出 | `session.quit()` | 通用 |

### R

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `random` | 生成随机数 | `session.random()` | 通用 |
| `range` | 创建范围数组 | `session.range()` | 通用 |
| `read` | 读取数据 | `session.read()` | 通用 |
| `real` | 取实部 | `session.real()` | 通用 |
| `rect` | 矩形操作 | `session.rect()` | 通用 |
| `redraw` | 重绘 | `session.redraw()` | 通用 |
| `remove` | 移除对象 | `session.remove()` | 通用 |
| `rename` | 重命名对象 | `session.rename()` | 通用 |
| `repmat` | 复制和平铺数组 | `session.repmat()` | 通用 |
| `reshape` | 重塑数组形状 | `session.reshape()` | 通用 |
| `resize` | 调整数组大小 | `session.resize()` | 通用 |
| `restore` | 恢复对象 | `session.restore()` | 通用 |
| `result` | 结果操作 | `session.result()` | 通用 |
| `return` | 从函数返回 | `session.return()` | 通用 |
| `reverse` | 反转数组 | `session.reverse()` | 通用 |
| `rmdir` | 删除目录 | `session.rmdir()` | 通用 |
| `rotate` | 旋转对象 | `session.rotate()` | 通用 |
| `round` | 四舍五入 | `session.round()` | 通用 |
| `run` | 运行仿真或脚本 | `session.run()` | 通用 |

### S

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `save` | 保存数据 | `session.save()` | 通用 |
| `saveobj` | 保存对象 | `session.saveobj()` | 通用 |
| `scale` | 缩放对象 | `session.scale()` | 通用 |
| `scan` | 扫描参数 | `session.scan()` | 通用 |
| `script` | 脚本操作 | `session.script()` | 通用 |
| `select` | 选择对象 | `session.select()` | 通用 |
| `selectall` | 选择所有对象 | `session.selectall()` | 通用 |
| `selectinner` | 选择内部对象 | `session.selectinner()` | 通用 |
| `selectpartial` | 部分选择 | `session.selectpartial()` | 通用 |
| `selectsimilar` | 选择相似对象 | `session.selectsimilar()` | 通用 |
| `set` | 设置对象属性 ✅ [文档](./lumapi/set.md) | `session.set()` | 通用 |
| `setanalysis` | 设置分析参数 | `session.setanalysis()` | FDTD, MODE |
| `setexpansion` | 设置扩展监视器 | `session.setexpansion()` | FDTD, MODE |
| `setglobalmonitor` | 设置全局监视器 | `session.setglobalmonitor()` | FDTD, MODE |
| `setglobalsource` | 设置全局源 | `session.setglobalsource()` | FDTD, MODE |
| `setmaterial` | 设置材料属性 | `session.setmaterial()` | 通用 |
| `setnamed` | 按名称设置对象属性 | `session.setnamed()` | 通用 |
| `setposition` | 设置位置 | `session.setposition()` | 通用 |
| `setrotation` | 设置旋转 | `session.setrotation()` | 通用 |
| `setscale` | 设置比例 | `session.setscale()` | 通用 |
| `setup` | 设置仿真 | `session.setup()` | 通用 |
| `shiftselect` | 添加选择 | `session.shiftselect()` | 通用 |
| `show` | 显示对象 | `session.show()` | 通用 |
| `simulate` | 运行仿真 | `session.simulate()` | 通用 |
| `sin` | 正弦函数 | `session.sin()` | 通用 |
| `size` | 获取数组大小 | `session.size()` | 通用 |
| `smooth` | 平滑数据 | `session.smooth()` | 通用 |
| `sort` | 排序 | `session.sort()` | 通用 |
| `source` | 源操作 | `session.source()` | 通用 |
| `sphere` | 球体操作 | `session.sphere()` | 通用 |
| `sqrt` | 平方根 | `session.sqrt()` | 通用 |
| `stack` | 堆叠数组 | `session.stack()` | 通用 |
| `std` | 标准差 | `session.std()` | 通用 |
| `stop` | 停止仿真 | `session.stop()` | 通用 |
| `str2num` | 字符串转数字 | `session.str2num()` | 通用 |
| `struct` | 创建结构体 | `session.struct()` | 通用 |
| `subcell` | 子网格设置 | `session.subcell()` | MODE |
| `substitute` | 替换字符串 | `session.substitute()` | 通用 |
| `sum` | 求和 | `session.sum()` | 通用 |
| `surface` | 表面操作 | `session.surface()` | 通用 |
| `switch` | 切换语句 | `session.switch()` | 通用 |
| `switchtolayout` | 切换到布局视图 | `session.switchtolayout()` | 通用 |

### T

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `tan` | 正切函数 | `session.tan()` | 通用 |
| `temperature` | 温度操作 | `session.temperature()` | DEVICE |
| `test` | 测试功能 | `session.test()` | 通用 |
| `time` | 时间操作 | `session.time()` | 通用 |
| `times` | 乘法 | `session.times()` | 通用 |
| `toc` | 停止计时器 | `session.toc()` | 通用 |
| `trace` | 矩阵迹 | `session.trace()` | 通用 |
| `transpose` | 转置 | `session.transpose()` | 通用 |
| `trapz` | 梯形数值积分 | `session.trapz()` | 通用 |
| `type` | 获取变量类型 | `session.type()` | 通用 |

### U

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `unselect` | 取消选择 | `session.unselect()` | 通用 |
| `update` | 更新对象 | `session.update()` | 通用 |
| `updatemodes` | 更新模式 | `session.updatemodes()` | FDTD, MODE |
| `updateportmodes` | 更新端口模式 | `session.updateportmodes()` | MODE |
| `updatesourcemode` | 更新源模式 | `session.updatesourcemode()` | FDTD, MODE |
| `upgrade` | 升级项目 | `session.upgrade()` | 通用 |
| `use` | 使用对象 | `session.use()` | 通用 |

### V

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `var` | 变量操作 | `session.var()` | 通用 |
| `vector` | 向量操作 | `session.vector()` | 通用 |
| `view` | 视图设置 | `session.view()` | 通用 |
| `vstack` | 垂直堆叠数组 | `session.vstack()` | 通用 |

### W

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `wait` | 等待 | `session.wait()` | 通用 |
| `wavelength` | 波长操作 | `session.wavelength()` | 通用 |
| `while` | 循环语句 | `session.while()` | 通用 |
| `who` | 列出变量 | `session.who()` | 通用 |
| `whos` | 列出变量详细信息 | `session.whos()` | 通用 |
| `write` | 写入数据 | `session.write()` | 通用 |

### X

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `xlabel` | 设置 X 轴标签 | `session.xlabel()` | 通用 |

### Y

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `ylabel` | 设置 Y 轴标签 | `session.ylabel()` | 通用 |

### Z

| 命令 | 描述 | Python API | 产品 |
|------|------|------------|------|
| `zeros` | 创建全 0 数组 | `session.zeros()` | 通用 |
| `zlabel` | 设置 Z 轴标签 | `session.zlabel()` | 通用 |
| `zoom` | 缩放视图 | `session.zoom()` | 通用 |

## 使用说明

### 1. 命令格式
每个 LSF 命令在 Python 中都有对应的方法：
```python
# LSF: commandname(parameter1, parameter2, ...);
# Python: session.commandname(parameter1, parameter2, ...)
```

### 2. 返回值
大多数命令返回操作结果或状态码。某些命令返回特定数据结构（如场数据、模式数据等）。

### 3. 错误处理
命令执行失败会抛出异常，建议使用 try-except 块捕获异常。

### 4. 版本差异
不同 Lumerical 版本可能支持不同的命令集，建议查阅对应版本的官方文档。

## 更新记录

| 版本 | 日期 | 修改内容 |
|------|------|----------|
| 1.0 | 2025-01-30 | 初始版本，基于通用 Lumerical 脚本命令 |

---

*注意：本列表为不完全列表，实际命令可能更多。具体命令的使用方法和参数请参考官方文档。建议使用 `help("commandname")` 或 `session.help("commandname")` 查看具体命令的帮助信息。*