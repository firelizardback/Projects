**Bivariate normal distribution fit to the image**

When there is a correlation between horizontal and vertical orientation in our image, which is normal to observe in PITZ, the bivariate normal (Gaussian) distribution is a good choice to fit data instead of multiplication of two horizontal and vertical Gaussian distribution.

Bivariate normal distribution is 2-D multivariate normal distribution. The D-dimensional multivariate normal distribution is defined as below:

Which q is D X 1 position matrix, μ is the center of the distribution and Σ is D X D covariance matrix. For our special case ,D=2, the equations becomes:

I define Σ as below for the reason you will see soon.

Now I rearrange the distribution by replacing q and Σ in the eqaution.

for the constant F&#39;&#39; is the contour line of the distribution function. F&#39;&#39; is simply defines in which σ the contour line should be located. Now if we rearrange it:

It is interesting because it shows the ellipse equation.

The general form of ellipse equation is if . Without losing the generality if we moved the ellipse center to the origin, D and E becomes zero and the equation reduces to:

and F\&gt;0

This is exactly what we found for the contour lines equation and also it is the reason I define the Σ as above. Now we can build the M and M0 to find the ellipse parameters.

Then the ellipse parameters can be calculated by these equations:

a,b are the major and minor axis of ellipse respectively and θ is the orientation of the major axis.

We have now all tools except we don&#39;t know how to find the Σ and μ matrix from the image data. They are calculated by these equations:

Now all of them can be transferred to a loop-free MATLAB function, the Matrix magic:

function [a,b,theta,mux,muy,asym,sigma]=bvn\_ellipse(data,xscale,yscale,Fpp)

[yl,xl]=size(data); % row-\&gt;y column -\&gt;x

p=data/sum(sum(data)); %normalized data

x=(1:xl)\*xscale; %Find the data center

y=(1:yl)\*yscale;

mux=sum(p)\*x&#39;;

muy=sum(p&#39;)\*y&#39;;

xp=x-mux;

yp=y-muy;

sigma=zeros(2,2);

sigma(1,1)=sum(p\*(xp&#39;.^2)); %Calculate the Sigma matrix

sigma(2,2)=sum((yp.^2)\*p);

sigma(1,2)=yp\*p\*xp&#39;;

sigma(2,1)=sigma(1,2);

landa=eig(sigma); %Calculate the ellipse parameters

Fp=2\*det(sigma)\*Fpp;

a=sqrt(Fp/landa(1)); % major ellipse axis

b=sqrt(Fp/landa(2)); % minor ellipse axis

theta=180/pi\*atan2(2\*sigma(1,2),sigma(1,1)-sigma(2,2))/2; % orientation

asym=landa(2)/landa(1)-1; % assymetry figure of merit = (a/b)^2-1

end

I attached this function with extra one function and two scripts. Now let look at them.

The &#39;normal\_distribution\_test\_generation\_fit.m&#39; script file just an example which generate a bivariate distribution function and then fit the ellipse based on the &#39;bvn\_ellipse.m&#39; function which I showed above. This script use the &#39;bvn\_gen.m&#39; function to generate the distribution.

The &#39;imageloader\_MK\_BVN.m&#39; script is another example. I used the script written by Mikhail which loads an image and reduces the background. I just add the bivariate normal distribution fit at the end. Here you can see some outputs from the script:

![](RackMultipart20211021-4-1cmp6j7_html_e6399d78ecc0716b.png)

![](RackMultipart20211021-4-1cmp6j7_html_ceee4201e4f58b.png)

Here, In the left I sliced the data to [0.8,1], [0.6,0.8], [0.4,06], [0.2,0.4] of the maximum value and fit the ellipse for each of them. In the right I sliced the data to [1,0], [0.8,0], [0.6,0], [0.4,0], [0.2,0] of the maximum value. Just to be mention that the contour line is somewhere in this range and then it is not really shows the border. In the below image, you can see how the orientation and asymmetry can change from the center to the border then you should think which slice is more suitable for this kind of study. In the above image, more symmetric case, the elliptical parameters seems more or less identical.

I defined the (a/b)^2-1 as the measure for asymmetry in the &#39;bvn\_ellipse.m&#39; function. It should be zero for the symmetric case.

Feel free to use these codes.

Hamed

08.04.2019
