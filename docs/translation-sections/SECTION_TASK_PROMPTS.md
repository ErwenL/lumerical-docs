# LSF文档翻译并行任务提示词

## 概述
本文件为4个并行翻译section提供详细的任务提示词。每个section包含177个LSF脚本命令，需要按照标准四步工作流程进行处理。

**重要提醒**：所有section同时进行，互不冲突。每个命令只属于一个section，从根本上避免了重复劳动。

---

## Section 1 任务提示词

### 📋 Section 基本信息
- **Section编号**：1
- **命令数量**：177个
- **命令范围**：`addcustom` 到 `cross`
- **起始命令**：`addcustom`
- **结束命令**：`cross`
- **进度文件**：`docs/translation-sections/section_1.json`

处理以下177个命令的文档翻译工作（按字母- **当前状态**：进行中 (1/177完成，0.6%)

### 🎯 核心任务顺序）：
```
addcustom, adddeltachargesource, adddevice, adddftmonitor, adddgtdmesh, adddgtdsolver, 
adddiffusion, adddipole, adddope, addeffectiveindex, addefieldmonitor, addelectricalcontact, 
addelement, addemabsorptionmonitor, addeme, addemeindex, addemeport, addemeprofile, 
addemfieldmonitor, addemfieldtimemonitor, addemmaterialproperty, addfde, addfdtd, 
addfeemmesh, addfeemsolver, addfieldregion, addgaussian, addgridattribute, addgroup, 
addheatfluxbc, addheatfluxmonitor, addheatmesh, addheatsolver, addhtmaterialproperty, 
addimplant, addimport, addimportdope, addimportedsource, addimportgen, addimportheat, 
addimportnk, addimporttemperature, addindex, addjfluxmonitor, addjob, addlayer, 
addlayerbuilder, addmaterialproperties, addmesh, addmode, addmodeexpansion, 
addmodelmaterial, addmodesource, addmovie, addobject, addparameter, addpath, addpec, 
addperiodic, addplanarsolid, addplane, addpmc, addpml, addpoly, addport_lparenFDTDrparen, 
addport_lparenINTERCONNECTrparen, addproperty, addpyramid, addradiationbc, addrect, 
addresource, addring, addsemiconductorfromalloy, addsimulationregion, addsphere, 
addstructuregroup, addsurface, addsurfacerecombinationbc, addsweep, addsweepparameter, 
addsweepresult, addtemperaturebc, addtemperaturemonitor, addtfsf, addthermalinsulatingbc, 
addthermalpowerbc, addtime, addtogroup, addtolibrary, addtriangle, adduniformheat, 
adduserprop, addvarfdtd, addvoltagebc, addwaveguide, all, almostequal, amax, amin, 
and, angle, ans, applyscript, approx, area, areaof, ascii, ascii2native, asin, atan, 
atan2, attribute, autoshutoff, autoshutoffmin, average, beambetween, beampropagate, 
beampropagation, beamsize, beamsizeat, boundary, boundarycondition, c, cabs, cacos, 
cadd, casin, catan, caxis, cconj, ccos, cd, ceil, cexp, cfloor, char, chdir, clear, 
cleardcard, clearpersistent, clf, close, cmul, cnorm, complex, conj, contour, 
contourf, conv, convert, convertstl, copy, corrcoef, corrtransf, cos, coupling, 
cov, cp, createbeam, createcompound, createsphericalsurface, cross
```

### 🔧 工作流程（四步法）

#### 步骤1：检查英文文档质量
1. **文件位置**：`docs/lsf-script/en/<command>.md`
2. **检查标准**：
   - 格式正确（标题、代码块、表格）
   - 内容完整（描述、语法、示例、参数说明）
   - "See Also"部分存在且相关
   - 链接有效（内部和外部）

#### 步骤2：修改"See Also"部分
**转换规则**：
- 原始格式：`[命令名](https://optics.ansys.com/hc/en-us/articles/...)`
- 目标格式：`- [命令名](./命令名.md)`
- 添加项目符号列表
- 转换为本地相对链接

#### 步骤3：翻译文档
**翻译原则**：
- 准确性优先，技术术语保持一致
- 代码部分保持英文原样
- 命令名称不翻译
- 技术参数名不翻译
- 中文使用全角标点，中英文间加空格

#### 步骤4：应用格式化
**格式要求**：
- 中英文文档统一格式
- 代码块使用正确的语言标识
- 表格对齐一致
- 行长度限制在80字符内

### 🛠️ 工具使用

#### 1. 创建翻译模板
```bash
python scripts/translation_helper.py --prepare <command>
# 示例：python scripts/translation_helper.py --prepare addcustom
```

#### 2. 检查文档质量
手动检查`docs/lsf-script/en/<command>.md`文件

#### 3. 翻译文档
编辑生成的`docs/lsf-script/cn/<command>.md`文件

### 📊 进度更新
**完成每个命令后必须更新进度**：
```bash
python scripts/section_scheduler.py update --section 1 --completed <命令名>
# 示例：python scripts/section_scheduler.py update --section 1 --completed addcustom
```

### ✅ 质量自查清单（每个文件）
- [ ] 英文文档质量检查通过
- [ ] "See Also"部分已转换为项目符号格式和本地链接
- [ ] 翻译准确、完整，技术术语一致
- [ ] 中文文档格式正确
- [ ] 链接指向正确的本地文件
- [ ] 进度已更新

### ⚠️ 注意事项
1. **避免重复**：本section的命令不会出现在其他section
2. **文件冲突**：使用Git管理文件更改，定期拉取最新
3. **进度更新**：完成一个命令立即更新，避免团队内部重复
4. **批次处理**：建议每5-10个命令为一组，便于质量控制和进度管理

---

## Section 2 任务提示词

### 📋 Section 基本信息
- **Section编号**：2
- **命令数量**：177个
- **命令范围**：`ctranspose` 到 `gratingvector`
- **起始命令**：`ctranspose`
- **结束命令**：`gratingvector`
- **进度文件**：`docs/translation-sections/section_2.json`
- **当前状态**：待开始 (0/177完成，0.0%)

### 🎯 核心任务
处理以下177个命令的文档翻译工作（按字母顺序）：
```
ctranspose, currentfilename, currentscriptname, customlibrary, cwnorm, czt, dcht, 
debug, del, delete, deleteall, deletematerial, deleteresource, deletesweep, 
designmode, dipolepower, dir, disabledesignkit, disconnect, dot, dot_cmd, eig, 
emepropagate, emesweep, enabledesignkit, encryptscript, end, enter, eps, eq, 
equal, equivalent, erf, erfc, erfcinv, erfinv, error, etch, eval, evalc, evalscript, 
exit, exp, expand, expandsource, export, exportimage, exportmonitordata, 
exportsweepdata, eye, farfield, farfield3d, farfieldcartesian, farfieldspherical, 
farfieldx, farfieldy, farfieldz, fclose, fdeanalyze, fdematrix, fderefine, fdesolver, 
fdtdanalyze, fdtdbc, fdtdrefresh, fdtdsolver, feemanifold, feemmesh, feemsolver, 
feemsolverbc, feemsolverrefine, feemsolversource, feemsolverstrain, fft, fftshift, 
field, filein, fileparts, filter, find, findpeaks, findstr, fminsearch, fopen, 
for, format, fprintf, fread, frewind, fscanf, fseek, ftell, fullfile, function, 
fwrite, fzero, gaussfit, gausspulse, gc, gcd, get, getdata, getelectric, 
getfield, getgaussianparameter, getmaterial, getnamed, getnextresult, getoptic, 
getpeaks, getprofile, getresult, getscript, getsweepdata, getsweepresult, 
gettemperature, getuniquegroupname, gfpolarplot, gfpolarplotsetup, grid, gridoff, 
gridon, gratingn, gratingordercount, gratingorders, gratingperiod1, gratingperiod2, 
gratingpolar, gratingprojection, gratingu1, gratingu2, gratingvector
```

### 🔧 工作流程（同Section 1）
#### 四步法：
1. 检查英文文档质量
2. 修改"See Also"部分为本地链接
3. 翻译文档内容
4. 应用统一格式化

### 🛠️ 工具使用（同Section 1）
```bash
# 创建翻译模板
python scripts/translation_helper.py --prepare <command>

# 更新进度（重要！）
python scripts/section_scheduler.py update --section 2 --completed <命令名>
```

### 📊 进度管理
- **起始点**：从`ctranspose`开始
- **建议批次**：每批10-20个命令
- **更新频率**：完成每个命令后立即更新

### ✅ 质量自查清单（同Section 1）
- [ ] 英文文档质量检查通过
- [ ] "See Also"链接转换完成
- [ ] 翻译准确且完整
- [ ] 中文格式正确
- [ ] 进度已更新

### ⚠️ Section 2 特定注意事项
1. **命令特点**：包含较多数学和计算函数（如`fft`, `fminsearch`, `gaussfit`等）
2. **技术术语**：注意数学函数和计算相关术语的一致性
3. **代码示例**：数学计算相关命令可能有复杂代码示例，保持原样不翻译

---

## Section 3 任务提示词

### 📋 Section 基本信息
- **Section编号**：3
- **命令数量**：177个
- **命令范围**：`groupscope` 到 `putremotedata`
- **起始命令**：`groupscope`
- **结束命令**：`putremotedata`
- **进度文件**：`docs/translation-sections/section_3.json`
- **当前状态**：待开始 (0/177完成，0.0%)

### 🎯 核心任务
处理以下177个命令的文档翻译工作（按字母顺序）：
```
groupscope, gt, gte, h5info, h5read, h5readattr, h5writeattr, hash, havedata, 
haveproperty, haveresult, havesweepdata, havesweepresult, help, hide, hidecategory, 
hideproperty, histc, histogram, historyoff, historyon, holdoff, holdon, icht, if, 
imag, image, importnk, importstl, impulse, impulsegaussian, impulsegaussiannorm, 
impulsenorm, impulseuniform, inf, info, inlet, inletg, inner, input, inputnumber, 
inputstring, insert, inspector, int, int2str, int8, int16, int32, int64, interp, 
interp1, interp2, interp3, intersect, inv, invert, iq, iscategorical, iscell, 
ischar, isempty, isequal, isfield, isfinite, isfloat, ishandle, isinf, islogical, 
ismember, isnan, isnumeric, isobject, isscalar, isspace, isstruct, isvalidproperty, 
kron, l1, l2, last, ldivide, ldl, length, lengthof, lininterp, linspace, list, 
listbox, listboxvalue, load, loadgds, loadnk, localtime, log, log10, log2, logspace, 
lower, lscov, lt, lte, lu, make, makeabsolute, makering, mat2str, matdb, matdivide, 
material, matmul, matpow, max, mean, median, memory, mesh, meshorder, meshquality, 
mex, min, mkdir, mod, mode, moviesetup, move, movie, msgbox, mtimes, namelengthmax, 
nan, nargin, nargout, native2ascii, nchoosek, ndims, ne, newdirectory, nextpow2, 
nnz, norm, not, now, num2cell, num2str, numel, nzmax, ones, op, open, optparam, 
or, orderfields, otherwise, outofmemory, outer, overflow, overredraw, p, param, 
parent, pause, pbaspect, pcolor, pdeanalyze, pdeboundary, pdesolver, pinv, plot, 
plot3, plotedit, plotyy, plus, poly, polyand, polyarea, polybool, polybuffer, 
polycentroid, polyclip, polyerase, polyintersect, polyor, polyxor, precision, 
print, probe, prod, propagate, protectproperty, putremotedata
```

### 🔧 工作流程（同前）
#### 标准四步法：
1. **质量检查** → 2. **链接转换** → 3. **翻译** → 4. **格式化**

### 🛠️ 工具使用
```bash
# 为单个命令创建翻译模板
python scripts/translation_helper.py --prepare groupscope

# 更新进度（完成每个命令后执行）
python scripts/section_scheduler.py update --section 3 --completed groupscope
```

### 📊 进度策略
- **推荐批次大小**：每批15个命令
- **质量检查点**：每完成一批运行自查
- **团队协作**：如多人处理本section，内部协调分配子集

### ✅ Section 3 质量重点
1. **数据结构命令**：`isstruct`, `isfield`, `orderfields`等需要准确翻译
2. **数学运算命令**：`pinv`, `kron`, `lu`等线性代数术语保持一致
3. **文件操作命令**：`load`, `save`, `open`等通用术语统一
4. **多边形处理命令**：`polyarea`, `polycentroid`, `polybool`等几何相关术语

### ⚠️ 注意事项
1. **命令多样性**：本section包含多种类型命令（数学、文件、数据结构等）
2. **术语一致性**：同一数学概念在不同命令中保持相同翻译
3. **进度协调**：如团队内部分工，明确各自负责的命令范围

---

## Section 4 任务提示词

### 📋 Section 基本信息
- **Section编号**：4
- **命令数量**：177个
- **命令范围**：`pwd` 到 `zeros`
- **起始命令**：`pwd`
- **结束命令**：`zeros`
- **进度文件**：`docs/translation-sections/section_4.json`
- **当前状态**：待开始 (0/177完成，0.0%)

### 🎯 核心任务
处理以下177个命令的文档翻译工作（按字母顺序）：
```
pwd, quadtet, quadtri, question, quote, rand, randmatrix, randn, randnmatrix, 
read, readdata, readnportsparameterat, readstltriangles, real, rectilineardataset, 
redo, redraw, redrawmode, redrawoff, redrawon, refresh, reloaddesignkit, 
removecustom, removedesignkit, removeexpansion, removeport, removesweepparameter, 
removetask, rename, render, repeat, replace, reset, reshape, resid, resolution, 
resize, restoredefaultpath, result, resultnumber, return, revert, revertall, rmdir, 
rdivide, read, readdata, readnportsparameterat, readstltriangles, real, 
rectilineardataset, redo, redraw, redrawmode, redrawoff, redrawon, refresh, 
reloaddesignkit, removecustom, removedesignkit, removeexpansion, removeport, 
removesweepparameter, removetask, rename, render, repeat, replace, reset, reshape, 
resid, resolution, resize, restoredefaultpath, result, resultnumber, return, 
revert, revertall, rmdir, rdivide, rmse, rolloff, rotate, round, row, run, runall, 
runscript, save, saveas, savegds, savenamed, savenxk, scalefactor, scan, script, 
scriptgroup, scriptname, scripttype, search, sec, select, selectall, selected, 
selectend, selectinside, selection, selectoutside, selectpartial, selectstart, 
selecttouch, semilogx, semilogy, set, setappdata, setdiff, setxor, setup, setupfde, 
setupfdtd, setupmovie, shading, shiftdim, show, showcategory, showproperty, 
shuffle, sign, simresultname, simresultnumber, sin, sind, single, size, sizeof, 
slice, smooth, smooth3, solvenonlinear, sort, sortrows, sound, source, sourcegroup, 
spacecharge, sparse, spconvert, spdiags, specular, speedoflight, sphere, sph2cart, 
spin, spline, split, sprintf, sqrt, square, squeeze, sscanf, stack, standard, 
startup, stlclear, stlreduce, stop, str2double, str2func, str2num, strcat, strcmp, 
strcmpi, stream2, stream3, streamline, strfind, strjoin, strjust, strmatch, strncmp, 
strncmpi, strrep, strsplit, strtok, strtrim, struct, struct2cell, strvcat, sub2ind, 
subplot, subsasgn, subsref, substr, sum, summer, surf, surface, surfc, surfl, 
svd, swapbytes, switch, sym, symmd, synchronize, system, tan, tand, taper, taylor, 
tempname, test, text, textread, textscan, tf, tfe, tic, tie, time, timeofday, 
times, timetable, title, toc, toeplitz, tolerance, trace, transpose, trapz, tri, 
tril, trim, triplequad, triu, true, try, type, uigetdir, uigetfile, uiputfile, 
uisetcolor, uiwait, uminus, undo, unicode2native, union, unique, unix, unmap, 
unprotectproperty, unwrap, uplus, upper, usegpu, usegpuarray, var, varargin, 
varargout, vargin, vector, version, vertcat, view, visible, visdiff, vol, wait, 
waitbar, waitfor, warning, waterfall, wblanks, wfclose, wfopen, wfreplace, 
wfselect, while, whitebg, who, whos, why, wizardgetdata, wizardoption, 
wizardwidget, workspace, write, zbfexport, zbfload, zbfread, zbfwrite, zeros
```

### 🔧 工作流程（标准四步法）
1. **文档质量检查**：确保英文文档符合标准格式
2. **链接转换**：将"See Also"中的外部链接转为本地相对链接
3. **内容翻译**：准确翻译文档内容，保持技术术语一致性
4. **格式统一**：应用中英文统一的Markdown格式

### 🛠️ 必备工具
```bash
# 1. 检查当前进度
python scripts/section_scheduler.py progress

# 2. 创建翻译模板
python scripts/translation_helper.py --prepare pwd

# 3. 更新进度（关键步骤！）
python scripts/section_scheduler.py update --section 4 --completed pwd
```

### 📊 进度管理建议
- **起始顺序**：从`pwd`开始按字母顺序处理
- **批次处理**：每批10个命令，便于质量控制
- **定期同步**：每天结束前更新所有完成命令的进度
- **进度检查**：使用`python scripts/section_scheduler.py progress`监控

### ✅ Section 4 质量重点
1. **字符串处理命令**：`strcmp`, `strfind`, `strrep`等字符串函数术语统一
2. **文件操作命令**：`uigetfile`, `uiputfile`等GUI文件操作准确翻译
3. **数学函数命令**：`svd`, `trace`, `toeplitz`等数学术语保持一致
4. **可视化命令**：`surf`, `plot`, `slice`等图形相关术语准确

### ⚠️ 重要提醒
1. **避免范围外工作**：只处理本section的177个命令，不要处理其他section的命令
2. **进度更新及时性**：完成每个命令后立即更新，避免内部重复
3. **术语一致性**：同一技术概念在整个section中保持相同翻译
4. **代码保持原样**：所有代码示例、命令名称、参数名不翻译

---

## 🎯 通用工作指南（所有Section适用）

### 1. 工作优先级
1. **准确性** > 速度：技术文档翻译必须准确
2. **一致性** > 个性化：术语翻译必须保持一致
3. **完整性** > 简洁性：确保所有内容都翻译

### 2. 冲突避免机制
- **预分配防重复**：每个命令只属于一个section
- **进度实时更新**：完成命令后立即标记
- **文件版本控制**：使用Git管理文件更改

### 3. 质量保证流程
1. **个人自查**：每个文件完成后运行自查清单
2. **批次审查**：每完成10个命令进行批量检查
3. **术语验证**：确保技术术语翻译一致

### 4. 进度协调
```bash
# 查看所有section进度
python scripts/section_scheduler.py progress

# 查看详细命令列表
python scripts/translation_helper.py --list --limit 20
```

### 5. 问题处理
- **翻译不确定**：保持英文术语，添加括号说明
- **链接失效**：暂时保持原链接，添加TODO注释
- **格式不一致**：应用统一模板强制格式化

---

## 📈 成功指标
- **Section完成**：177个命令全部处理完成
- **质量达标**：所有文件通过自查清单
- **进度同步**：进度文件准确反映实际完成情况
- **术语一致**：技术术语在整个文档集中保持一致

---

*文档版本：1.0*  
*生成日期：2026-02-03*  
*更新：使用 `python scripts/section_scheduler.py progress` 查看最新进度*