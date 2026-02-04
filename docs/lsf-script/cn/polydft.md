<!--
Translation from English documentation
Original command: polydft
Translation date: 2026-02-04 22:50:14
-->

# polydft

返回 该 chirped z-transform 的 一个 设置 的 数据. The polydft 函数 是 very similar 到 一个 two-dimensional czt 函数 使用 该 difference being 该 该 E 函数 does not need 到 为 finely sampled 和 only providing 该 vertices 的 一个 polygon as input range 的 该 函数 would 为 enough 到 perform 该 transform. The only limit however 是 该 E 是 considered constant within 该 limits 的 该 polygon. The polygon mesh 可以 为 created 使用 该 inpoly 函数. 

**语法** |  **描述**  
---|---  
out = polydft(E,kx,ky);  |  返回 该 two dimensional chirped z-transform 的 E. kx 和 ky 必须 为 linearly spaced 设置 的 wavenumbers but 可以 cover any range.   
  
**示例**

This example demonstrates two different approaches 用于 calculating 该 discrete Fourier transform (DFT) 的 一个 piecewise constant 2D 函数 在 该 xy-plane. The 函数 是 defined as having 该 值 的 one inside 该 polygonal area specified 通过 该 vertices poly_vert. One approach uses 该 polydft 命令 directly 在 该 polygon vertices, 该 other approach uses 一个 finely staircased representation 的 该 函数 和 该 czt 命令. 
    
    
    # -------
    # Inputs:
    # -------
    # xy-plane region
    x_span = y_span = 5.0;
    # area inside 该 above region 其中 函数 是 nonzero
    poly_vert = [0.25*x_span,0.35*y_span;
                 0.50*x_span,0.15*y_span;
                 0.75*x_span,0.35*y_span;
                 0.75*x_span,0.65*y_span;
                 0.50*x_span,0.85*y_span;
                 0.25*x_span,0.65*y_span];
    # grid 用于 staircasing 该 above polygon
    Nx = Ny = 2^8;
    # ---------
    # Function:
    # ---------
    delta_x = x_span/Nx;
    delta_y = y_span/Ny;
    x = delta_x*linspace(0.0,Nx-1,Nx);
    y = delta_y*linspace(0.0,Ny-1,Ny);
    X = meshgridx(x,y);
    Y = meshgridy(x,y);
    poly_fun = inpoly(poly_vert,X,Y);
    image(x,y,poly_fun,"x","y","staircased 函数");
    # ----
    # DFT:
    # ----
    # 使用 该 czt 命令
    delta_fx = 1.0/(Nx*delta_x);
    delta_fy = 1.0/(Ny*delta_y);
    fx = delta_fx*linspace(-0.5*(Nx-1),0.5*(Nx-1),Nx);
    kx = 2.0*pi*fx;
    fy = delta_fy*linspace(-0.5*(Ny-1),0.5*(Ny-1),Ny);
    ky = 2.0*pi*fy;
    poly_fun_czt = czt(poly_fun,x,y,kx,ky)/(Nx*Ny);
    image(kx,ky,abs(poly_fun_czt),"kx","ky","czt");
    # 使用 该 polydft 命令
    Kx = meshgridx(kx,ky);
    Ky = meshgridy(kx,ky);
    poly_fun_polydft = polydft(poly_vert,Kx,Ky)/(x_span*y_span);
    image(x,y,abs(poly_fun_polydft),"kx","ky","polydft");
    # ------------------------
    # Function Reconstruction:
    # ------------------------
    # 从 czt
    poly_fun_from_czt = czt(poly_fun_czt,-kx,-ky,x,y);
    image(x,y,real(poly_fun_from_czt),"x","y","reconstruction 从 czt");
    # 从 polydft
    poly_fun_from_polydft = czt(poly_fun_polydft,-kx,-ky,x,y);
    image(x,y,real(poly_fun_from_polydft),"x","y","reconstruction 从 polydft"); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ czt ](/hc/en-us/articles/360034926173-czt) , [ inpoly ](/hc/en-us/articles/360034926253-inpoly) , [ fft ](/hc/en-us/articles/360034926133-fft) , [ fftw ](/hc/en-us/articles/360034926153-fftw)
