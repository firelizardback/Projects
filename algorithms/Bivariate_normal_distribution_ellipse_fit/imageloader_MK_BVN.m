%upgrade M.Krasilnikov, November 2015
%upgrade H. Shaker, April 2019, add the bivariate normal distribution fit

clear all;
close all;
clc;


%======================PARAMETERS===================================
%FrameNum=1;

%BkgFlag='Average';
%BkgFlag='AveragePlus3RMS';
BkgFlag='Envelope';


NegPix='No';
%=====================Read imc file==================================
[sIMCFileName, sIMCPathName] = uigetfile('*.imc', 'Select laser image file');



[aIMCData, aIMCHeader] = avine_load_video_images_from_file([sIMCPathName sIMCFileName]);



%====================Read bkc file ===================================

sBKCPathName=sIMCPathName;
sBKCFileName=strrep(sIMCFileName,'imc','bkc');

[aBKCData, aBKCHeader] = avine_load_video_images_from_file([sBKCPathName sBKCFileName]);

%============ Get camera dimensions ================================
aHeaderDataSingle = aIMCHeader(1);
sCamWidth = aHeaderDataSingle{1}.width;
sCamHeight = aHeaderDataSingle{1}.height;
sCamScale  = aHeaderDataSingle{1}.scale;

%========= Prepare arrays for averaging=============================
aIMCDataAverage = zeros(sCamHeight,sCamWidth);
aIMCDataRMS = zeros(sCamHeight,sCamWidth);
aBKCDataAverage = zeros(sCamHeight,sCamWidth);
aBKCDataRMS = zeros(sCamHeight,sCamWidth);
aBKCDataEnvelope = zeros(sCamHeight,sCamWidth);

MOI = zeros(sCamHeight,sCamWidth);

%================= Get number of frames=============================
sNumFramesTemp = size(aIMCData);
sNumFrames = sNumFramesTemp(1);

%==#1==================Average data===================================
for i = 1:sNumFrames
    aIMCDataSingle = aIMCData(i);
    aIMCDataDouble = double(aIMCDataSingle{1});
    aIMCDataAverage = aIMCDataAverage + aIMCDataDouble;
    aIMCDataRMS=aIMCDataRMS+ aIMCDataDouble.^2;
    
    
    aBKCDataSingle = aBKCData(i);
    
    aBKCDataDouble = double(aBKCDataSingle{1});
    aBKCDataAverage = aBKCDataAverage + aBKCDataDouble;
    aBKCDataRMS = aBKCDataRMS + aBKCDataDouble.^2;
    
    aBKCDataEnvelope =max(aBKCDataEnvelope,aBKCDataDouble);
end

aIMCDataAverage = aIMCDataAverage./sNumFrames;
aIMCDataRMS=aIMCDataRMS./sNumFrames-aIMCDataAverage.^2;
aIMCDataRMS=sqrt(aIMCDataRMS);

aBKCDataAverage = aBKCDataAverage./sNumFrames;
aBKCDataRMS=aBKCDataRMS./sNumFrames-aBKCDataAverage.^2;
aBKCDataRMS=sqrt(aBKCDataRMS);


%====#2======background calculation=====================

switch BkgFlag
 
    case 'Average'
      disp('Background method is average')
      aBKCData=aBKCDataAverage;
    
    case 'AveragePlus3RMS'
      disp('Background method is average+3*RMS')
      aBKCData=aBKCDataAverage+3*aBKCDataRMS;
  
    case 'Envelope'
     disp('Background method is envelope') 
     aBKCData=aBKCDataEnvelope;
   
    otherwise
      disp('Unknown background method');
      return
end

%========== Average image - Average background=========================
IMCmBKC = aIMCDataAverage - aBKCData;

switch NegPix
 
    case 'No'
      disp('Negative pixels->0')
      
   [N1,N2]=size(IMCmBKC);
for i=1:N1
    for j=1:N2
   if IMCmBKC(i,j)<0
       IMCmBKC(i,j)=0.;
   end
    end
  end
 
       
    otherwise
      disp('Negative pixels are alowed');
    
end

%====================================================================
['plotting raw image...']


figure(1);

imagesc(IMCmBKC);
axis equal;
grid on;
colorbar;
drawnow;

da=IMCmBKC;

aa=max(max(da));
xscale=1;
yscale=1;
%data=y;

for k=1:-0.2:0.2,
    %data=da.*(da<aa*k & da>aa*(k-0.2));
    data=da.*(da>aa*(k-0.2));
    sum(sum(data))/sum(sum(da))
	[a,b,theta,mux,muy,asym,sigma]=bvn_ellipse(data,xscale,yscale,-log(k-0.1));
    
    t = linspace(0,2*pi,100);
    thetar = deg2rad(theta);
    x0 = mux;
    y0 = muy;
    xa = x0 + a*cos(t)*cos(thetar) - b*sin(t)*sin(thetar);
    yb = y0 + b*sin(t)*cos(thetar) + a*cos(t)*sin(thetar);
    %figure;
    hold on;
    plot(xa/xscale,yb/yscale,'r');
    %plot(xa,yb,'r');
    axis equal;
end
