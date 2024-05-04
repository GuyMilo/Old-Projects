clear 
clc

b = input("enter a value for b: ");
x = linspace(0,15,50);

fctn = f(x,b);
plot(x,fctn,"b-*")
xlabel("x","FontName","Comic Sans")
ylabel("f(x,b)","FontName","Comic Sans")

%James-Edward Gray
%21015159