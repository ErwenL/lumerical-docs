<!-- Translation completed: 2026-02-04 -->
<!-- Original command: checkout -->

# checkout

**语法** | **描述**
---|---
checkout(featureID); | Checks out and reserve a licensed feature. If the feature cannot be checked out, an error message will be shown in the 脚本 Prompt window. The license will remain be checked out until the application quits.

**示例**

    checkout("INTERCONNECT_block_mode");
    #If INTERCONNECT_block_mode license does not exist, the following message will be shown
    Error: The license feature 'INTERCONNECT_block_mode' does not exist on ... 

    checkout("INTERCONNECT_block_mode");
    #If INTERCONNECT_block_mode license does not exist, the following message will be shown
    Error: The license feature 'INTERCONNECT_block_mode' does not exist on ... 

**另请参阅**

[ run ](/hc/en-us/articles/360034931333-run) , [ getsweepdata ](/hc/en-us/articles/360034409794-getsweepdata) , [ addjob ](/hc/en-us/articles/360034410714-addjob) , [ runjobs ](/hc/en-us/articles/360034931373-runjobs) , [ parameter sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps)
