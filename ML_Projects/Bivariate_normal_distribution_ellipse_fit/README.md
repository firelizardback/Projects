**Bivariate normal distribution fit to the image**

When there is a correlation between horizontal and vertical orientation in our image, which is normal to observe in PITZ, the bivariate normal (Gaussian) distribution is a good choice to fit data instead of multiplication of two horizontal and vertical Gaussian distribution.

Bivariate normal distribution is 2-D multivariate normal distribution.  The D-dimensional multivariate normal distribution is defined as below:

Pq;μ,Σ=1(2π)DΣexp⁡(-12q-μTΣ-1(q-μ))

Which q is D X 1 position matrix, μ is the center of the distribution and Σ is D X D covariance matrix. For our special case ,D=2, the equations becomes: 
Pq;μ,Σ=12πΣexp⁡(-12q-μTΣ-1(q-μ))

q=xy, q-μ=x'y'

I define Σ as below for the reason you will see soon.

Σ=C-B2-B2A⇒Σ-1=1ΣAB2B2C=1AC-B24AB2B2C

Now I rearrange the distribution by replacing q and Σ in the eqaution.

Px',y';Σ=12πΣexp-12ΣxyAB2B2Cxy=12πΣexp-12Σ(Ax2+Bxy+Cy2)

-12ΣAx2+Bxy+Cy2=-F'' for the constant F’’ is the contour line of the distribution function. F’’ is simply defines in which σ the contour line should be located. Now if we rearrange it:

-12ΣAx2+Bxy+Cy2=-F''=F2Σ⇒Ax2+Bxy+Cy2+F=0

It is interesting because it shows the ellipse equation.

The general form of ellipse equation is Ax2+Bxy+Cy2+Dx+Ey+F=0 if B2-4AC<0 . Without losing the generality if we moved the ellipse center to the origin, D and E becomes zero and  the equation reduces to:

Ax2+Bxy+Cy2+F=0 and F>0

This is exactly what we found for the contour lines equation and also it is the reason I define the Σ as above. Now we can build the M and M0 to find the ellipse parameters.

M=AB2B2C & M0=FD2E2D2AB2E2B2C

Then the ellipse parameters can be calculated by these equations:

a=-M0M1λ1=F'λ1

b=-M0M1λ2=F'λ2

θ=12atan2(B,A-C)

a,b are the major and minor axis of ellipse respectively and θ is the orientation of the major axis.

We have now all tools except we don’t know how to find the Σ and μ matrix from the image data. They are calculated by these equations:

μ=x,yP(x,y)×xyx,yPΣ=x,yPx,y×x'y'×x'y'x,yPx'y'=xy-μ

Now all of them can be transferred to a loop-free MATLAB function, the Matrix magic:

function [a,b,theta,mux,muy,asym,sigma]=bvn\_ellipse(data,xscale,yscale,Fpp)  

`    `[yl,xl]=size(data); % row->y column ->x

`    `p=data/sum(sum(data)); %normalized data

`    `x=(1:xl)\*xscale; %Find the data center

`    `y=(1:yl)\*yscale; 

`    `mux=sum(p)\*x';

`    `muy=sum(p')\*y';  

`    `xp=x-mux;

`    `yp=y-muy;    

`    `sigma=zeros(2,2);       

`    `sigma(1,1)=sum(p\*(xp'.^2)); %Calculate the Sigma matrix

`    `sigma(2,2)=sum((yp.^2)\*p);

`    `sigma(1,2)=yp\*p\*xp';

`    `sigma(2,1)=sigma(1,2);

`    `landa=eig(sigma); %Calculate the ellipse parameters    

`    `Fp=2\*det(sigma)\*Fpp; 

`    `a=sqrt(Fp/landa(1)); % major ellipse axis

`    `b=sqrt(Fp/landa(2)); % minor ellipse axis 

`    `theta=180/pi\*atan2(2\*sigma(1,2),sigma(1,1)-sigma(2,2))/2; % orientation 

`    `asym=landa(2)/landa(1)-1; % assymetry figure of merit = (a/b)^2-1

end



I attached this function with extra one function and two scripts. Now let look at them. 

The ‘normal\_distribution\_test\_generation\_fit.m’ script file just an example which generate a bivariate distribution function and then fit the ellipse based on the ‘bvn\_ellipse.m’ function which I showed above. This script use the ‘bvn\_gen.m’ function to generate the distribution.

The ‘imageloader\_MK\_BVN.m’ script is another example. I used the script written by Mikhail which loads an image and reduces the background. I just add the bivariate normal distribution fit at the end.  Here you can see some outputs from the script:





Here, In the left I sliced the data to [0.8,1], [0.6,0.8], [0.4,06], [0.2,0.4] of the maximum value and fit the ellipse for each of them. In the right I sliced the data to [1,0], [0.8,0], [0.6,0], [0.4,0], [0.2,0] of the maximum value. Just to be mention that the contour line is somewhere in this range and then it is not really shows the border. In the below image, you can see how the orientation and asymmetry can change from the center to the border then you should think which slice is more suitable for this kind of study. In the above image, more symmetric case, the elliptical parameters seems more or less identical. 

I defined the (a/b)^2-1 as the measure for asymmetry in the ‘bvn\_ellipse.m’ function. It should be zero for the symmetric case.

Feel free to use these codes.

Hamed

08.04.2019

