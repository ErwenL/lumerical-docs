# unwrap

Removes changes of more than 2  π  from a 1D array. It can be useful after angle(x) to see phase without discontinuities. 

The unwrap function is primarily intended for 1D arrays. Care must be taken when applying it to matrices with more than one dimension. 

**Syntax** |  **Description**  
---|---  
out = unwrap(x);  |  Return the values of x without discontinuities.   
  
**Example**

Apply the unwrap function to a 1D array. 
    
    
    vec=linspace(0,10,100);
    A=cos(vec) + sin(vec)*1i;
    B=angle(A);
    C=unwrap(B);
    plot(vec,real(A),B,C);
    legend("cos(x)","angle", "unwrap");

The following figure will be generated: 

Apply the unwrap function to a 2D matrix. The unwrap function will treat the 2D matrix as a 1D vector (i.e. concatenate each row), meaning that the unwrapped phase of the 2nd row will start at the phase of the end of the first row. Notice that the values in all 5 rows of matrix D are identical, but after the unwrap function is applied, the lines are 'stacked' on top of each other. This is because the unwrap treated the matrix as a large 1D array, rather than treating each row independently. 
    
    
    vec=linspace(0,10,100);
    A=cos(vec) + sin(vec)*1i; # create complex sinusoid
    B=1:5;           # vector from 1:5
    C=meshgridx(A,B);     # 2D matrix with 5 copies of sinusoid
    D=angle(C);        # get angle of matrix 
    image(vec,B,D,"vec","5 copies","angle");  # image plot of matrix
    plot(vec,D,"vec","angle");         # line plot (all 5 lines are identical)
    legend("row 1","row 2","row 3","row 4","row 5");
    plot(vec,unwrap(D),"vec","unwrap angle"); # unwrap. Now lines are stacked
    legend("row 1","row 2","row 3","row 4","row 5");

To apply the unwrap function to 2D phase data in 2D fashion (rather than treating it as a single large 1D vector), see the following example. The unwrap function must be applied to one row at a time, then one column at a time. 

Note: A 2D unwrap operation is non-trivial. This example code works in some cases, but not always. Please do some testing to determine if it works for your application. 
    
    
    x=linspace(-5,5,100); y=x;
    nx=length(x); ny=length(y);
    data = exp( 1i* (meshgridx(x,y)+meshgridy(x,y)) );
    phase = angle(data); 
    image(x,y,phase,"x","y","raw phase (rad)");
    # unwrap over both dimensions 
    for (i=1:nx) {
     phase(i,1:ny) = unwrap( pinch(phase,1,i) );
    }
    for (j=1:ny) {
     phase(1:nx,j) = unwrap( pinch(phase,2,j) );
    }
    image(x,y,phase,"x","y","unwrapped phase (rad)"); 

|   
---|---  
  
**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ real ](/hc/en-us/articles/360034925493-real) , [ imag ](/hc/en-us/articles/360034925513-imag) , [ angle ](/hc/en-us/articles/360034405614-angle)
