% Generate the bivariate normal distribution
% Author: Hamed Shaker
% Created: 2019-04-07

function [y,x1,y1] = bvn_gen (sigma,mu,xl,yl,xscale,yscale)
    x1=(1:xl)*xscale;
    y1=(1:yl)*yscale;
    [X1,Y1] = meshgrid(x1,y1);
    X = [X1(:) Y1(:)];
    y = mvnpdf(X,mu,sigma);
    y = reshape(y,length(y1),length(x1));
end
