# gpuspecs

Obtains specifications of all GPUs in the system and return as a cell array. Each element of the cell array represents a physical GPU installed in the system, and contains a structure with fields showing its specifications.

**Syntax** |  **Description**  
---|---  
gpuspecs; |  Returns a cell array representing all installed GPUs in the system, elements to each cell are structs that show individual specifications. Details of each struct are shown below.  
  
Each structure in the cell array will have the following fields

**Field** |  **Description**  
---|---  
availableDeviceMemoryKb | Available Video RAM (VRAM) of the GPU in Kilobytes (KB).  
bus | Index for the bus of the device  
deviceSMCount | Number of streaming microprocessors in the GPU.  
deviceTotalMemoryKb | Total VRAM of the GPU in KB.  
deviceUUID | Unique Identifier for the GPU.  
domain | The Peripheral Component Interconnect (PCI) domain of the device.  
maxLinkSpeedMBPS | Maximum link speed of the GPU’s PCI express (PCIe) interface in MPBS.  
maxlinkWidth | Maximum link width of the GPU and its PCIe interface.  
memoryBusWidth | Memory bus width of the GPU in Megabytes-per-second (MBPS).  
nvmlDeviceIndex | Index of GPU for Resource Configuration.  
userReadableDeviceName | Human-readable name for the GPU.  
  
**Example**

Obtain the device index of the first detected GPU in the system
    
    
    gpus_cell = gpuspecs; #save cell array of all GPU specs in gpus_cell  
      
    ?gpus_cell{1}.deviceIndex;  
      
    result:  
      
    0

Obtain streaming processor count for the first detected GPU in the system.
    
    
    ?gpus_cell{1}.deviceSMCount;  
      
    result:  
      
    16

**See Also**

[List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834-Lumerical-scripting-language-By-category), [FDTD on GPU](https://optics.ansys.com/hc/en-us/articles/17518942465811-Getting-started-with-running-FDTD-on-GPU)
