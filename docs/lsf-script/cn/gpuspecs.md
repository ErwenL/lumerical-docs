<!--
Translation from English documentation
Original command: gpuspecs
Translation date: 2026-02-04 22:50:00
-->

# gpuspecs

Obtains specifications 的 all GPUs 在 该 system 和 返回 as 一个 单元格 数组. Each 元素 的 该 单元格 数组 represents 一个 physical GPU installed 在 该 system, 和 contains 一个 结构 使用 fields showing its specifications.

**语法** |  **描述**  
---|---  
gpuspecs; |  返回 一个 单元格 数组 representing all installed GPUs 在 该 system, elements 到 each 单元格 是 structs 该 show individual specifications. Details 的 each 结构体 是 shown below.  
  
Each 结构 在 该 单元格 数组 将 have 该 following fields

**Field** |  **描述**  
---|---  
availableDeviceMemoryKb | Available Video RAM (VRAM) 的 该 GPU 在 Kilobytes (KB).  
bus | Index 用于 该 bus 的 该 device  
deviceSMCount | Number 的 streaming microprocessors 在 该 GPU.  
deviceTotalMemoryKb | Total VRAM 的 该 GPU 在 KB.  
deviceUUID | Unique Identifier 用于 该 GPU.  
domain | The Peripheral Component Interconnect (PCI) domain 的 该 device.  
maxLinkSpeedMBPS | Maximum link speed 的 该 GPU’s PCI express (PCIe) interface 在 MPBS.  
maxlinkWidth | Maximum link width 的 该 GPU 和 its PCIe interface.  
memoryBusWidth | Memory bus width 的 该 GPU 在 Megabytes-per-second (MBPS).  
nvmlDeviceIndex | Index 的 GPU 用于 Resource Configuration.  
userReadableDeviceName | Human-readable name 用于 该 GPU.  
  
**示例**

Obtain 该 device index 的 该 first detected GPU 在 该 system
    
    
    gpus_cell = gpuspecs; #save 单元格 数组 的 all GPU specs 在 gpus_cell  
      
    ?gpus_cell{1}.deviceIndex;  
      
    result:  
      
    0

Obtain streaming processor count 用于 该 first detected GPU 在 该 system.
    
    
    ?gpus_cell{1}.deviceSMCount;  
      
    result:  
      
    16

**参见**

[List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834-Lumerical-scripting-language-By-category), [FDTD on GPU](https://optics.ansys.com/hc/en-us/articles/17518942465811-Getting-started-with-running-FDTD-on-GPU)
