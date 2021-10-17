var x0 = width/2;
var y0 = height/2;
var rate = 0.95;

var drawShape = function(x, y, radius,i,r,g,b) {
    
    fill(r,g,b);
    if (i === 1)
    {
        arc(x + x0, y + y0, radius, radius,0,180);
    }
    else
    {
        arc(x + x0, y + y0, radius, radius,180,360);
    }
    
    
    var newRadius = radius*rate;
    if (newRadius >= 2) {
        drawShape(x + (1-rate)*radius/2*i, y, newRadius,-i,(r+20)%256,(g+30)%256,(g+10)*256);
    }
};

drawShape(0, 0, 380,1,8,0,90);