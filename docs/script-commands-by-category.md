# Lumerical Scripting Language - Commands by Category

## 概述

本文档按功能类别组织 Lumerical 脚本语言（LSF）命令。这种分类方式有助于用户根据具体任务快速找到相关命令。

*注意：某些命令可能属于多个类别，本分类基于主要功能。*

## 1. 仿真设置与求解器

### 1.1 求解器创建与配置
| 命令 | 描述 | 产品 |
|------|------|------|
| `addfdtd` | 添加 FDTD 求解器 ✅ [文档](./lumapi/addfdtd.md) | FDTD |
| `addefdtd` | 添加电-热 FDTD 求解器 | FDTD |
| `addeme` | 添加 EME 求解器 ✅ [文档](./lumapi/addeme.md) | MODE |
| `addfde` | 添加 FDE 求解器 ✅ [文档](./lumapi/addfde.md) | MODE |
| `addvarfdtd` | 添加变分 FDTD 求解器 | varFDTD |
| `addheat` | 添加热求解器 | DEVICE |
| `setanalysis` | 设置分析参数 | FDTD, MODE |
| `emeanalysis` | EME 分析设置 | MODE |
| `fdtdanalysis` | FDTD 分析设置 | FDTD |

### 1.2 网格设置
| 命令 | 描述 | 产品 |
|------|------|------|
| `addmesh` | 添加网格覆盖区 ✅ [文档](./lumapi/addmesh.md) | FDTD, MODE |
| `mesh` | 网格操作 | 通用 |
| `grid` | 设置网格 | 通用 |
| `cleargrid` | 清除网格 | 通用 |
| `subcell` | 子网格设置 | MODE |

### 1.3 边界条件与材料
| 命令 | 描述 | 产品 |
|------|------|------|
| `addmaterial` | 添加材料 ✅ [文档](./lumapi/addmaterial.md) | 通用 |
| `setmaterial` | 设置材料属性 | 通用 |
| `getmaterial` | 获取材料数据 | 通用 |
| `addproperty` | 添加材料属性 | 通用 |
| `material` | 材料操作 | 通用 |

## 2. 几何结构与对象

### 2.1 基本几何体
| 命令 | 描述 | 产品 |
|------|------|------|
| `addrect` | 添加矩形 ✅ [文档](./lumapi/addrect.md) | 通用 |
| `addsphere` | 添加球体 ✅ [文档](./lumapi/addsphere.md) | 通用 |
| `addcylinder` | 添加圆柱体 | 通用 |
| `addring` | 添加环形结构 | 通用 |
| `addprism` | 添加棱柱 | 通用 |
| `addwaveguide` | 添加波导结构 | MODE |
| `addplanarsolid` | 添加平面实体 | 通用 |
| `addgrating` | 添加光栅 | FDTD, MODE |

### 2.2 几何操作
| 命令 | 描述 | 产品 |
|------|------|------|
| `rotate` | 旋转对象 | 通用 |
| `scale` | 缩放对象 | 通用 |
| `translate` | 平移对象 | 通用 |
| `copy` | 复制对象 | 通用 |
| `delete` | 删除对象 | 通用 |
| `move` | 移动对象 | 通用 |

### 2.3 几何导入
| 命令 | 描述 | 产品 |
|------|------|------|
| `import` | 导入数据 | 通用 |
| `importgeometry` | 导入几何 | 通用 |
| `importobj` | 导入 OBJ 文件 | 通用 |
| `importstl` | 导入 STL 文件 | 通用 |

## 3. 光源与激励

### 3.1 光源类型
| 命令 | 描述 | 产品 |
|------|------|------|
| `addmode` | 添加模式源 ✅ [文档](./lumapi/addmode.md) | FDTD, MODE |
| `adddipole` | 添加偶极子源 | FDTD |
| `addtds` | 添加时域源 | FDTD |
| `addmodesource` | 添加模式源 | varFDTD |
| `addnoise` | 添加噪声源 | INTERCONNECT |

### 3.2 光源配置
| 命令 | 描述 | 产品 |
|------|------|------|
| `setglobalsource` | 设置全局源 | FDTD, MODE |
| `getglobalsource` | 获取全局源设置 | FDTD, MODE |
| `polarization` | 设置偏振 | 通用 |
| `wavelength` | 波长操作 | 通用 |
| `frequency` | 设置频率 | 通用 |

## 4. 监视器与结果

### 4.1 监视器类型
| 命令 | 描述 | 产品 |
|------|------|------|
| `addpower` | 添加功率监视器 ✅ [文档](./lumapi/addpower.md) | FDTD, MODE |
| `addprofile` | 添加场监视器 ✅ [文档](./lumapi/addprofile.md) | FDTD, MODE |
| `addindex` | 添加折射率监视器 ✅ [文档](./lumapi/addindex.md) | FDTD, MODE |
| `addmodeexpansion` | 添加模式扩展监视器 ✅ [文档](./lumapi/addmodeexpansion.md) | FDTD, MODE |
| `addemeprofile` | 添加 EME 场监视器 | MODE |
| `addfdeprofile` | 添加 FDE 场监视器 | MODE |
| `addthermal` | 添加热监视器 | DEVICE |
| `addcustom` | 添加自定义监视器 | FDTD, MODE |
| `addevent` | 添加事件监视器 | INTERCONNECT |

### 4.2 监视器配置
| 命令 | 描述 | 产品 |
|------|------|------|
| `setglobalmonitor` | 设置全局监视器 | FDTD, MODE |
| `getglobalmonitor` | 获取全局监视器设置 | FDTD, MODE |
| `setexpansion` | 设置扩展监视器 | FDTD, MODE |

### 4.3 结果获取
| 命令 | 描述 | 产品 |
|------|------|------|
| `getresult` | 获取结果数据 ✅ [文档](./lumapi/getresult.md) | 通用 |
| `getdata` | 获取数据 | 通用 |
| `getelectric` | 获取电场数据 | FDTD, MODE |
| `getmagnetic` | 获取磁场数据 | FDTD, MODE |
| `getpower` | 获取功率数据 | FDTD, MODE |
| `getprofile` | 获取剖面数据 | FDTD, MODE |
| `gettemperature` | 获取温度数据 | DEVICE |
| `getoptical` | 获取光学数据 | INTERCONNECT |

## 5. 端口与模式

### 5.1 端口操作
| 命令 | 描述 | 产品 |
|------|------|------|
| `addport` | 添加端口 | FDTD, MODE, INTERCONNECT |
| `addoptical` | 添加光学端口 | INTERCONNECT |
| `updateportmodes` | 更新端口模式 | MODE |

### 5.2 模式分析
| 命令 | 描述 | 产品 |
|------|------|------|
| `eigensolver` | 设置本征求解器 | MODE |
| `getmode` | 获取模式数据 | MODE |
| `updatemodes` | 更新模式 | FDTD, MODE |
| `updatesourcemode` | 更新源模式 | FDTD, MODE |
| `overlap` | 计算重叠积分 | MODE |
| `bentwaveguide` | 设置弯曲波导参数 | MODE |
| `cellgroup` | 设置单元组 | MODE |

## 6. 仿真控制

### 6.1 运行控制
| 命令 | 描述 | 产品 |
|------|------|------|
| `run` | 运行仿真或脚本 | 通用 |
| `simulate` | 运行仿真 | 通用 |
| `stop` | 停止仿真 | 通用 |
| `wait` | 等待 | 通用 |
| `pause` | 暂停仿真 | 通用 |

### 6.2 项目与文件
| 命令 | 描述 | 产品 |
|------|------|------|
| `newproject` | 新建项目 | 通用 |
| `open` | 打开文件 | 通用 |
| `save` | 保存数据 | 通用 |
| `saveobj` | 保存对象 | 通用 |
| `load` | 加载数据 | 通用 |
| `loadobj` | 加载对象 | 通用 |
| `close` | 关闭项目或文件 | 通用 |
| `quit` | 退出 | 通用 |

## 7. 数据操作与数学运算

### 7.1 数组操作
| 命令 | 描述 | 产品 |
|------|------|------|
| `linspace` | 创建线性间隔数组 | 通用 |
| `logspace` | 创建对数间隔数组 | 通用 |
| `meshgrid` | 创建网格坐标 | 通用 |
| `meshgrid4d` | 创建 4D 网格坐标 | 通用 |
| `reshape` | 重塑数组形状 | 通用 |
| `repmat` | 复制和平铺数组 | 通用 |
| `pinch` | 压缩数组维度 | 通用 |
| `hstack` | 水平堆叠数组 | 通用 |
| `vstack` | 垂直堆叠数组 | 通用 |
| `stack` | 堆叠数组 | 通用 |

### 7.2 数学运算
| 命令 | 描述 | 产品 |
|------|------|------|
| `plus` | 加法 | 通用 |
| `minus` | 减法 | 通用 |
| `times` | 乘法 | 通用 |
| `divide` | 除法 | 通用 |
| `power` | 幂运算 | 通用 |
| `sqrt` | 平方根 | 通用 |
| `sin`, `cos`, `tan` | 三角函数 | 通用 |
| `exp`, `log`, `log10` | 指数对数函数 | 通用 |
| `real`, `imag`, `conj` | 复数运算 | 通用 |
| `abs`, `angle` | 复数的模和相位 | 通用 |

### 7.3 统计与积分
| 命令 | 描述 | 产品 |
|------|------|------|
| `sum` | 求和 | 通用 |
| `mean` | 平均值 | 通用 |
| `std` | 标准差 | 通用 |
| `max`, `min` | 最大值、最小值 | 通用 |
| `integrate` | 积分计算 | 通用 |
| `trapz` | 梯形数值积分 | 通用 |
| `gradient` | 计算梯度 | 通用 |
| `norm` | 计算范数 | 通用 |

### 7.4 信号处理
| 命令 | 描述 | 产品 |
|------|------|------|
| `fourier` | 傅里叶变换 | 通用 |
| `fourier2` | 二维傅里叶变换 | 通用 |
| `fft`, `ifft` | 快速傅里叶变换 | 通用 |
| `interpolate` | 插值计算 | 通用 |
| `smooth` | 平滑数据 | 通用 |
| `filter` | 滤波 | 通用 |

## 8. 可视化与绘图

### 8.1 绘图命令
| 命令 | 描述 | 产品 |
|------|------|------|
| `plot` | 绘图 | 通用 |
| `plotxy` | XY 绘图 | 通用 |
| `plotyz` | YZ 绘图 | 通用 |
| `plotxz` | XZ 绘图 | 通用 |
| `plot3d` | 3D 绘图 | 通用 |
| `contour` | 等高线图 | 通用 |
| `surf` | 曲面图 | 通用 |
| `image` | 显示图像 | 通用 |

### 8.2 图形设置
| 命令 | 描述 | 产品 |
|------|------|------|
| `xlabel`, `ylabel`, `zlabel` | 设置坐标轴标签 | 通用 |
| `title` | 设置标题 | 通用 |
| `legend` | 设置图例 | 通用 |
| `grid` | 显示网格 | 通用 |
| `axis` | 设置坐标轴范围 | 通用 |
| `colorbar` | 显示颜色条 | 通用 |
| `view` | 设置视图角度 | 通用 |
| `zoom` | 缩放视图 | 通用 |

### 8.3 动画与导出
| 命令 | 描述 | 产品 |
|------|------|------|
| `animate` | 创建动画 | 通用 |
| `movie` | 创建电影 | 通用 |
| `export` | 导出数据 | 通用 |
| `matlabsave` | 保存为 MATLAB 格式 | 通用 |
| `print` | 打印图形 | 通用 |
| `savefig` | 保存图形 | 通用 |

## 9. 脚本控制与流程

### 9.1 流程控制
| 命令 | 描述 | 产品 |
|------|------|------|
| `if`, `else`, `elseif` | 条件语句 | 通用 |
| `for` | 循环语句 | 通用 |
| `while` | 循环语句 | 通用 |
| `switch`, `case` | 切换语句 | 通用 |
| `break` | 跳出循环 | 通用 |
| `continue` | 继续下一次循环 | 通用 |
| `return` | 从函数返回 | 通用 |

### 9.2 脚本执行
| 命令 | 描述 | 产品 |
|------|------|------|
| `eval` | 执行脚本字符串 | 通用 |
| `run` | 运行脚本文件 | 通用 |
| `addscript` | 添加脚本对象 | 通用 |
| `script` | 脚本操作 | 通用 |
| `function` | 定义函数 | 通用 |
| `call` | 调用函数 | 通用 |

### 9.3 变量管理
| 命令 | 描述 | 产品 |
|------|------|------|
| `clear` | 清除变量 | 通用 |
| `who` | 列出变量 | 通用 |
| `whos` | 列出变量详细信息 | 通用 |
| `type` | 获取变量类型 | 通用 |
| `size` | 获取数组大小 | 通用 |
| `length` | 获取数组长度 | 通用 |
| `disp` | 显示变量值 | 通用 |
| `print` | 打印输出 | 通用 |
| `echo` | 回显文本 | 通用 |

## 10. 对象与界面操作

### 10.1 对象选择
| 命令 | 描述 | 产品 |
|------|------|------|
| `select` | 选择对象 | 通用 |
| `selectall` | 选择所有对象 | 通用 |
| `shiftselect` | 添加选择 | 通用 |
| `unselect` | 取消选择 | 通用 |
| `selectinner` | 选择内部对象 | 通用 |
| `selectpartial` | 部分选择 | 通用 |
| `selectsimilar` | 选择相似对象 | 通用 |
| `find` | 查找对象 | 通用 |

### 10.2 对象属性
| 命令 | 描述 | 产品 |
|------|------|------|
| `set` | 设置对象属性 ✅ [文档](./lumapi/set.md) | 通用 |
| `get` | 获取对象属性 | 通用 |
| `setnamed` | 按名称设置对象属性 | 通用 |
| `getnamed` | 按名称获取对象属性 | 通用 |
| `properties` | 获取对象属性列表 | 通用 |
| `change` | 更改对象属性 | 通用 |
| `edit` | 编辑对象 | 通用 |

### 10.3 对象分组
| 命令 | 描述 | 产品 |
|------|------|------|
| `addtogroup` | 将对象添加到组 | 通用 |
| `creategroup` | 创建组 | 通用 |
| `makegroup` | 创建组 | 通用 |
| `group` | 对象分组操作 | 通用 |
| `ungroup` | 取消分组 | 通用 |

### 10.4 界面控制
| 命令 | 描述 | 产品 |
|------|------|------|
| `redraw` | 重绘 | 通用 |
| `refresh` | 刷新界面 | 通用 |
| `show` | 显示对象 | 通用 |
| `hide` | 隐藏对象 | 通用 |
| `draw` | 绘制对象 | 通用 |
| `switchtolayout` | 切换到布局视图 | 通用 |
| `zoom` | 缩放视图 | 通用 |
| `pan` | 平移视图 | 通用 |

## 11. 文件与系统操作

### 11.1 文件操作
| 命令 | 描述 | 产品 |
|------|------|------|
| `cd` | 改变工作目录 | 通用 |
| `chdir` | 改变目录 | 通用 |
| `pwd` | 显示当前目录 | 通用 |
| `dir` | 列出目录内容 | 通用 |
| `ls` | 列出目录内容 | 通用 |
| `mkdir` | 创建目录 | 通用 |
| `rmdir` | 删除目录 | 通用 |
| `copyfile` | 复制文件 | 通用 |
| `movefile` | 移动文件 | 通用 |
| `deletefile` | 删除文件 | 通用 |

### 11.2 系统操作
| 命令 | 描述 | 产品 |
|------|------|------|
| `system` | 执行系统命令 | 通用 |
| `getenv` | 获取环境变量 | 通用 |
| `setenv` | 设置环境变量 | 通用 |
| `addpath` | 添加路径到脚本搜索路径 | 通用 |
| `rmpath` | 从搜索路径移除路径 | 通用 |
| `path` | 管理搜索路径 | 通用 |
| `version` | 获取版本信息 | 通用 |
| `license` | 许可证操作 | 通用 |

## 12. 优化与参数扫描

### 12.1 优化设置
| 命令 | 描述 | 产品 |
|------|------|------|
| `optimize` | 优化操作 | 通用 |
| `copyopt` | 复制优化设置 | 通用 |
| `setopt` | 设置优化参数 | 通用 |
| `getopt` | 获取优化参数 | 通用 |

### 12.2 参数扫描
| 命令 | 描述 | 产品 |
|------|------|------|
| `scan` | 扫描参数 | 通用 |
| `sweep` | 参数扫描 | 通用 |
| `getsweep` | 获取扫描数据 | 通用 |
| `parameter` | 参数操作 | 通用 |
| `var` | 变量操作 | 通用 |

## 13. 高级功能

### 13.1 并行计算
| 命令 | 描述 | 产品 |
|------|------|------|
| `parallel` | 并行计算设置 | 通用 |
| `mpi` | MPI 设置 | 通用 |
| `distribute` | 分布式计算 | 通用 |

### 13.2 自定义材料
| 命令 | 描述 | 产品 |
|------|------|------|
| `addcustommaterial` | 添加自定义材料 | 通用 |
| `setcustommaterial` | 设置自定义材料属性 | 通用 |
| `getcustommaterial` | 获取自定义材料数据 | 通用 |

### 13.3 插件与扩展
| 命令 | 描述 | 产品 |
|------|------|------|
| `addplugin` | 添加插件 | 通用 |
| `plugin` | 插件操作 | 通用 |
| `extension` | 扩展功能 | 通用 |

## 使用建议

### 1. 按任务查找命令
- **仿真设置**: 查看第 1 类（仿真设置与求解器）
- **几何建模**: 查看第 2 类（几何结构与对象）
- **结果分析**: 查看第 4 类（监视器与结果）
- **数据后处理**: 查看第 7 类（数据操作与数学运算）
- **可视化**: 查看第 8 类（可视化与绘图）

### 2. 组合使用
许多复杂任务需要组合多个类别的命令：
- 参数扫描：仿真设置 + 流程控制 + 结果获取
- 优化设计：几何建模 + 参数扫描 + 优化设置
- 自动化分析：脚本控制 + 数据操作 + 可视化

### 3. 性能优化
- 减少界面操作命令（第 10 类）以提高脚本执行速度
- 使用向量化操作（第 7 类）代替循环
- 合理使用并行计算（第 13 类）加速大规模仿真

## 更新记录

| 版本 | 日期 | 修改内容 |
|------|------|----------|
| 1.0 | 2025-01-30 | 初始版本，基于功能分类 |

---

*注意：本分类为逻辑分类，实际使用时可能需要跨类别组合命令。具体命令的使用方法和参数请参考官方文档或按字母顺序排列的命令列表。*