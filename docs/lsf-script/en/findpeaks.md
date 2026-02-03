# findpeaks

Returns the position of peaks in a matrix. A peak (or local maximum) is defined as a data point that is larger than its nearest neighbors. 

**Syntax** |  **Description**  
---|---  
out = findpeaks(y);  |  Returns the position of the peak with the largest value in y. The length of y must be at least 2. If no peak is found in the data, a value of 1 is returned.   
findpeaks(y,n);  |  Returns a matrix containing the positions of the largest n peaks found in the data. The returned values are ordered from largest to smallest. The returned matrix is always of dimension nX1. If less than n peaks are found, the remaining values of the returned matrix are 1.   
  
**Example**

The following example calculates the location of the two largest peaks in a data set. 
    
    
    x=linspace(-20,20,1000);
    y=x*cos(x);
    ?pos=findpeaks(y,2);
    plot(x,y);
    ?"largest peak is at x=" + num2str(x(pos(1)));
    ?"largest peak height is y=" + num2str(y(pos(1)));
    ?"2nd largest peak is at x=" + num2str(x(pos(2)));
    ?"2nd largest peak height is y=" + num2str(y(pos(2)));
    result: 
    973 
    107 
    largest peak is at x=18.9189
    largest peak height is y=18.8734
    2nd largest peak is at x=-15.7558
    2nd largest peak height is y=15.7378

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ find ](/hc/en-us/articles/360034405874-find)
