<!-- Translation completed: 2026-02-04 -->
<!-- Original command: gpuspecs -->

# gpuspecs

**语法** | **描述**
---|---
gpuspecs; | 返回 a cell 数组 representing all installed GPUs in the system, 元素 to each cell are structs that show individual specifications. Details of each struct are shown below.
availableDeviceMemoryKb | Available Video RAM (VRAM) of the GPU in Kilobytes (KB).
bus | Index for the bus of the device
deviceSMCount | 数字 of streaming microprocessors in the GPU.
deviceTotalMemoryKb | Total VRAM of the GPU in KB.
deviceUUID | Unique Identifier for the GPU.
domain | The Peripheral Component Interconnect (PCI) 域 of the device.
maxLinkSpeedMBPS | 最大值 link speed of the GPU’s PCI express (PCIe) interface in MPBS.
maxlinkWidth | 最大值 link width of the GPU and its PCIe interface.
memoryBusWidth | Memory bus width of the GPU in Megabytes-per-second (MBPS).
nvmlDeviceIndex | Index of GPU for Resource Configuration.
userReadableDeviceName | Human-readable name for the GPU.

**示例**

Obtain the device index of the first detected GPU in the system
    gpus_cell = gpuspecs; #保存 cell 数组 of all GPU specs in gpus_cell  
    ?gpus_cell{1}.deviceIndex;  
    result:  
    0
Obtain streaming processor count for the first detected GPU in the system.
    ?gpus_cell{1}.deviceSMCount;  
    result:  
    16

Obtain the device index of the first detected GPU in the system
    gpus_cell = gpuspecs; #保存 cell 数组 of all GPU specs in gpus_cell  
    ?gpus_cell{1}.deviceIndex;  
    result:  
    0
Obtain streaming processor count for the first detected GPU in the system.
    ?gpus_cell{1}.deviceSMCount;  
    result:  
    16

**另请参阅**

[List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834-Lumerical-scripting-language-By-category), [FDTD on GPU](https://optics.ansys.com/hc/en-us/articles/17518942465811-Getting-started-with-running-FDTD-on-GPU)
