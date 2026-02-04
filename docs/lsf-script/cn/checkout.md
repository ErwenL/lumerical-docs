<!--
Translation from English documentation
Original command: checkout
Translation date: 2026-02-04 22:49:36
-->

# checkout

Checks out 一个 licensed feature. 

**语法** |  **描述**  
---|---  
checkout(featureID);  |  Checks out 和 reserve 一个 licensed feature. If 该 feature cannot 为 checked out, 一个 error message 将 为 shown 在 该 Script Prompt window. The license 将 remain 为 checked out until 该 application quits.   
  
**示例**
    
    
    checkout("INTERCONNECT_block_mode");
    #If INTERCONNECT_block_mode license does not exist, 该 following message 将 为 shown
    Error: The license feature 'INTERCONNECT_block_mode' does not exist 在 ... 

**参见**

[ run ](/hc/en-us/articles/360034931333-run) , [ getsweepdata ](/hc/en-us/articles/360034409794-getsweepdata) , [ addjob ](/hc/en-us/articles/360034410714-addjob) , [ runjobs ](/hc/en-us/articles/360034931373-runjobs) , [ 参数 sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps)
