% Test script to generate and fit the bivariate normal distribution
% Author: Hamed Shaker
% Created: 2019-04-07

clear all;
sigma0=[0.05,0.02;0.02,0.09];
mu=[3.5,2.5];
yl=680; %680
xl=512; %512
xscale=0.01;
yscale=0.01;

[y,x1,y1]=bvn_gen(sigma0,mu,xl,yl,xscale,yscale);
%for i=1:xl,
%    for j=1:yl,
%        pos=[i,j]-mu;
%        da(j,i)=1/(2*pi*sqrt(detsi))*exp(-0.5*pos*invsi*pos');
%    end
%end

%y=y/sum(sum(y));
aa=max(max(y));
%data=y.*(y<aa*0.9 & y>aa*0.3);
data=y;
figure(1);
imagesc(x1,y1,data);
%contour(x1,y1,data);
xscale=0.01;
yscale=0.01;
[a,b,theta,mux,muy,asym,sigma]=bvn_ellipse(data,xscale,yscale,1);

t = linspace(0,2*pi,100);
thetar = deg2rad(theta);
x0 = mux;
y0 = muy;
xa = x0 + a*cos(t)*cos(thetar) - b*sin(t)*sin(thetar);
yb = y0 + b*sin(t)*cos(thetar) + a*cos(t)*sin(thetar);
hold on;
plot(xa,yb,'r');
axis equal;

a
b
a/b
asym
theta
sigma-sigma0