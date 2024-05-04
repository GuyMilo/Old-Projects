close
clear
clc

x = linspace(0,2*pi,30);
subplot(2,1,1) %2 = rows, 1 = cols, 1 = index

fctn_1 = sin(x);
fctn_2 = cos(x);

hold on
plot(x,fctn_1,"k-+")
plot(x,fctn_2, "k-.")
legend("sin(x)","cos(x)")
axis([0,2*pi,-1,1])
hold off

subplot(2,1,2)%2 = rows, 1 = cols, 1 = index

fctn_3 = 2.*sin(x).*cos(x);
fctn_4 = sin(x)./cos(x);

hold on
xlabel("x (between 0 and 2\pi)")
xlim([0,2*pi])
yyaxis left
ax = gca;
plot(x,fctn_3,"k")
set(ax,"YColor",'k')
ylabel("2sin(x)cos(x)",'Color','k')
ylim([-1 1])

yyaxis right
ax = gca;
plot(x,fctn_4,"k-.")
ylabel("sin(x)/cos(x)",'Color','k')
ylim([-20 20])
set(ax,"YColor",'k')
legend("2sin(x)cos(x)","sin(x)/cos(x)")
hold off

%James-Edward Gray
%21015159
