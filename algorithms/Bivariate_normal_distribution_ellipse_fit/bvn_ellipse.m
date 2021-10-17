% Find the parameters and the elliptical fit of the bivariate normal distribution
% Author: Hamed Shaker
% Created: 2019-04-07

function [a,b,theta,mux,muy,asym,sigma]=bvn_ellipse(data,xscale,yscale,Fpp)  
    [yl,xl]=size(data); % row->y column ->x
	p=data/sum(sum(data)); %normalized data
	x=(1:xl)*xscale; 
	y=(1:yl)*yscale; 
	%Find the data center
    mux=sum(p)*x';
    muy=sum(p')*y';  
	xp=x-mux;
    yp=y-muy;
    %Calculate the Sigma matrix
	sigma=zeros(2,2);	%M=zeros(2,2) % optional M matrix M=[sigma(2,2),-sigma(1,2);-sigma(2,1),sigma(1,1)]
	sigma(1,1)=sum(p*(xp'.^2));
	sigma(2,2)=sum((yp.^2)*p);
	sigma(1,2)=yp*p*xp';
    sigma(2,1)=sigma(1,2);
     %Calculate the ellipse parameters
	landa=eig(sigma); % sigma matrix eigen value. They are equals to M matrix eigenvalues
    Fp=2*det(sigma)*Fpp; % (or if you prefer) Fp=-2*det(sigma)*log(precentage);
    a=sqrt(Fp/landa(1)); % major ellipse axis
    b=sqrt(Fp/landa(2)); % minor ellipse axis 
    theta=180/pi*atan2(2*sigma(1,2),sigma(1,1)-sigma(2,2))/2; % orientation of major axis
    asym=landa(2)/landa(1)-1; % assymetry figure of merit = (a/b)^2-1
end