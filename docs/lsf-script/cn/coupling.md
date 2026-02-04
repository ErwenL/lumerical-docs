<!-- Translation completed: 2026-02-04 -->
<!-- Original command: coupling -->

# coupling

**语法** | **描述**
---|---
out = coupling(mode2, mode1); | 
out = coupling(mode2, mode1, x, y); | 模式 alignment can be adjusted before coupling is calculated.

**示例**

This 示例 shows how to use the overlap 命令 to 计算 the overlap and 功率 coupling between two 模式. 
    copydcard("mode1","test_mode1");  
    copydcard("mode2","test_mode2");  
    out = overlap("test_mode1","test_mode2");  
    ?out(1);  # overlap  
    ?out(2);  # 功率 coupling  
    ?coupling("test_mode1","test_mode2"); # the 复数 coupling coefficient  
    ?abs(coupling("test_mode1","test_mode2"))^2; # same as out(2), the 功率 coupling

This 示例 shows how to use the overlap 命令 to 计算 the overlap and 功率 coupling between two 模式. 
    copydcard("mode1","test_mode1");  
    copydcard("mode2","test_mode2");  
    out = overlap("test_mode1","test_mode2");  
    ?out(1);  # overlap  
    ?out(2);  # 功率 coupling  
    ?coupling("test_mode1","test_mode2"); # the 复数 coupling coefficient  
    ?abs(coupling("test_mode1","test_mode2"))^2; # same as out(2), the 功率 coupling

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ copydcard ](/hc/en-us/articles/360034930233-copydcard) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ expand2 ](/hc/en-us/articles/360034406414-expand2)
