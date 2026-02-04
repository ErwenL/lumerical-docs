<!--
Translation Status: Completed
Source: docs/lsf-script/en/resume.md
Last Updated: 2026-02-03
-->

# resume

从先前创建的[检查点](https://optics.ansys.com/hc/en-us/articles/360034382534-FDTD-solver-Simulation-Object#h_01HQ233EQNZ88X91YBEKF8SQ9R)恢复模拟。当模拟完成时，所有模拟数据将保存到当前模拟文件。然后更新后的模拟文件将被GUI重新加载。

**语法** |  **说明**  
---|---  
resume; |  以资源管理器中定义的并行模式启动模拟。此函数不返回任何数据。  
resume(option1); |  Option1（默认值：3）可以是：

  * 1：以单处理器模式恢复FDTD（传统模式），避免使用MPI。
  * 2：以单处理器模式恢复FDTD（传统模式）。弹出对话框不再获取焦点。
  * 3：以资源管理器中定义的并行模式恢复FDTD。

  
  
**恢复要求**

  * 项目必须完全相同，"auto shutoff min"和"auto shutoff max"除外。
  * 项目可以处于布局或分析模式。切换到布局后仍可以恢复模拟。
  * 多个/分布式/MPI进程中的每一个都必须能够访问其特定的检查点文件。用户可能需要[指定进程等级分配](https://software.intel.com/en-us/mpi-developer-guide-linux-controlling-process-placement)。
  * 处理器布局、MPI技术（mpich或impi等）、平台（linux/mac/windows）、CPU架构和Lumerical构建号必须相同



**内存使用**

  * 创建检查点或从检查点恢复不需要额外内存



**支持的对象**

  * 所有源和监视器类型。
  * 要恢复电影监视器，磁盘上必须仍然存在之前的电影文件。否则电影监视器将被忽略。



**另请参见**

- [run](./run.md)
- [resumejobs](./resumejobs.md)
