clear 
clc
for b = [1,1.2,2]
    x = linspace(0,15,50);

    fctn = @(x,b) log(b+sin(x));
    
    plot(x,fctn(x,b))
    xlabel("x","FontName","Comic Sans")
    ylabel("f(x,b)","FontName","Comic Sans")
    hold on
    legend("1","1.2","2")
end

%James-Edward Gray
%21015159