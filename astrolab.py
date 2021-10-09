import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
from math import atan, pi, sqrt,atan2,tan,sin,cos
import tkinter as tk
from PIL import Image, ImageDraw

def gamma_find(alfa,beta):
    gamma1 = (alfa + beta) - 90
    gamma2 = (alfa - beta) + 90
    return [gamma1,gamma2]

def cor_2D(R, teta, phi):
    res = R * np.tan(pi/4 - teta/2 * pi / 180)
    return [np.abs(res),phi]

def intersection_circle(r1,r2,d):
    [[x1,y1],[x2,y2]] = intersection_circle_general(0,0,0,d,r1,r2)
    x = x2
    y = y2
    theta = atan2(d-y,x)
    return [x,y,theta]

def intersection_circle_general(a,b,c,d,r0,r1):
    dd = sqrt((c-a)*(c-a)+(d-b)*(d-b))
    ss = 0.25 * sqrt ((dd+r0+r1) * (dd+r0-r1) * (dd-r0+r1) * (-dd+r0+r1))
    x1 = (a+c)/2 + (c-a)*(r0*r0-r1*r1)/(2*dd*dd) + 2 *(b-d)/(dd*dd)*ss
    x2 = (a+c)/2 + (c-a)*(r0*r0-r1*r1)/(2*dd*dd) - 2 *(b-d)/(dd*dd)*ss
    y1 = (b+d)/2 + (d-b)*(r0*r0-r1*r1)/(2*dd*dd) - 2 *(a-c)/(dd*dd)*ss
    y2 = (b+d)/2 + (d-b)*(r0*r0-r1*r1)/(2*dd*dd) + 2 *(a-c)/(dd*dd)*ss
    return [[x1,y1],[x2,y2]]

def has_intersection_circle_general(a,b,c,d,r0,r1):
    dd = sqrt((c-a)*(c-a)+(d-b)*(d-b))
    if (r0 + r1 > dd and abs(r0-r1) < dd):
        return True
    else:
        return False

def has_intersection_circle(r1,r2,d):
    return has_intersection_circle_general(0,0,0,d,r1,r2)

def circ_2D(r,theta1,theta2):
    if (theta1>-90 and theta1<90):
        ph1 = 0
    else: 
        ph1 = 180    
    if (theta2>-90 and theta2<90):
        ph2 = 0
    else: 
        ph2 = 180
    [r1,phi1] = cor_2D(r,theta1,ph1)
    [r2,phi2] = cor_2D(r,theta2,ph2)
    cent = (r1 * np.cos(phi1*pi/180) + r2 * np.cos(phi2*pi/180)) / 2
    rad = np.abs((r1 * np.cos(phi1*pi/180) - r2 * np.cos(phi2*pi/180)) / 2)
    return [cent,rad]       

def angle_find(lat,alpha):
    return (tan(alpha * pi / 180) / sin(lat * pi / 180))

def find_angle_general(x1,y1,x2,y2):
    x = x2 - x1
    y = y2 - y1
    res = atan2(y,x)
    if (res < 0):
        res = res + 2 * pi
    return [res,y/x]

def select_two_nearest(xy,x0,y0):
    dis = []
    for i in xy:
        ss = sqrt((i[0]-x0)*(i[0]-x0)+(i[1]-y0)*(i[1]-y0))
        dis.append (ss)        
    index_sort = [j[0] for j in sorted(enumerate(dis), key=lambda x:x[1])]
    return [xy[index_sort[0]],xy[index_sort[1]]]

def circle_from_3_points(x1,y1,x2,y2,x3,y3):
    mat = np.array ([[0,0,0,1],[x1*x1+y1*y1,x1,y1,1],[x2*x2+y2*y2,x2,y2,1],[x3*x3+y3*y3,x3,y3,1]])
    M12 = minor(mat,0,1)
    M11 = minor(mat,0,0)
    M13 = minor(mat,0,2)
    M14 = minor(mat,0,3)

    x0 = 0.5 * np.linalg.det(M12) / np.linalg.det(M11)
    y0 = -0.5 * np.linalg.det(M13) / np.linalg.det(M11)
    r = sqrt(x0*x0 + y0*y0+ np.linalg.det(M14) / np.linalg.det(M11))
    return [x0,y0,r]

def minor(arr,i,j):
    # ith row, jth column removed
    return arr[np.array(list(range(i))+list(range(i+1,arr.shape[0])))[:,np.newaxis],
               np.array(list(range(j))+list(range(j+1,arr.shape[1])))]

def draw_arc_3points(x1,y1,x2,y2,x3,y3,direction,cir):
    [x0,y0,r] = circle_from_3_points(x1,y1,x2,y2,x3,y3)
    ang = []
    ang.append(find_angle_general(x0,y0,x1,y1))
    ang.append(find_angle_general(x0,y0,x2,y2))
    ang.append(find_angle_general(x0,y0,x3,y3))
    ang.sort()

    if (direction):
        ang0 = ang[0][0] 
        ang2 =  ang[2][0]
    else:
        ang0 = ang[2][0] 
        ang2 =  ang[0][0]

    cir.append(Arc((x0,y0), r * 2, r * 2, angle = 0, theta1 = ang0 * 180 / pi , theta2 =  ang2 * 180 / pi, color = 'y'))
    cir.append(Arc((-x0,y0), r * 2, r * 2, angle = 0, theta1 = 180 - ang2 * 180 / pi , theta2 =  180 - ang0 * 180 / pi, color = 'y'))


#window = tk.Tk()
#greeting = tk.Label(text="Hello, Tkinter")
#entry1 = tk.Entry(text = "Latitude:")
#entry2 = tk.Entry(text = "Angle step:")
#entry1.pack()
#entry2.pack()
#greeting.pack()
#window.mainloop()

lat = float(input("Enter the Latitude(degree)[52.1579]:") or "52.1579")
st_an = float(input("Enter the step angle(degree)[10]:") or "10")
st_an2 = float(input("Enter the step angle2(degree)[15]:") or "15")
radius = float(input("Enter the equator radius[200]:") or "200")

circ = []
axial_tilt = 23.43646
[cent,rad] = circ_2D(radius,-axial_tilt,180 + axial_tilt)
rad1 = rad
rad_TofCap = rad
circ.append(plt.Circle((cent,0), rad1, fill=False, color = 'b'))  
plt.xlim((int(-rad1),int(rad1)))
plt.ylim((int(-rad1),int(rad1)))

[y_zenith,phi_zenith] = cor_2D(radius, lat, 0)

[cent,rad] = circ_2D(radius,0,180)
circ.append(plt.Circle((cent,0), rad, fill=False, color = 'b'))  

[cent,rad] = circ_2D(radius,axial_tilt,180 - axial_tilt)
rad_TofCan = rad
circ.append(plt.Circle((cent,0), rad, fill=False, color = 'b'))  

gamma = gamma_find(90 - axial_tilt,0)
[cent,rad] = circ_2D(radius,gamma[0],gamma[1])
circ.append(plt.Circle((0,-cent), rad, fill=False, color = 'g'))  

#w = int (rad * 2)
#h = w
#img = Image.new("RGB", (w, h))
#plt.xlim((-300,300))
#plt.ylim((-300,300))
#img1 = ImageDraw.Draw(img) 
#shape = [(40, 40), (w - 10, h - 10)] 
#img1.arc(shape, start = 20, end = 130, fill ="red")
#img.show()

for i in np.arange(0,90,st_an):
    gamma = gamma_find(lat,i)
    [cent,rad] = circ_2D(radius,gamma[0],gamma[1])
    if (i == 0):
        cent_h = cent
        rad_h = rad
    if has_intersection_circle(rad1,rad,cent):
        [x,y,theta] = intersection_circle(rad1,rad,cent)
        theta = theta * 180 / pi
        circ.append(Arc((0,cent), rad * 2, rad * 2, angle = 0, theta1 = 180 + theta , theta2 =  360 - theta))
    else:
        #print("No intersection")
        circ.append(plt.Circle((0,cent), rad, fill=False))  

gamma = gamma_find(lat + 90,0)
[cent,rad] = circ_2D(radius,gamma[0],gamma[1])
xy = [[0 for x in range(2)] for y in range(4)]
for j in np.arange(0,181,st_an2):
    centx = rad * angle_find(lat,j)
    if (centx > 10000 * rad):
        centx = 10000 * rad 
    rad_new = sqrt (rad * rad + centx * centx)

    xy[0:2] = intersection_circle_general(0,0,centx,cent,rad1,rad_new)
    xy[2:4] = intersection_circle_general(0,cent_h,centx,cent,rad_h,rad_new)
    xyn = select_two_nearest(xy,0,y_zenith)
    [angle1,tan1] = find_angle_general(centx,cent,xyn[0][0],xyn[0][1]) 
    [angle2,tan2] = find_angle_general(centx,cent,xyn[1][0],xyn[1][1])
    angle1 = angle1 * 180 / pi
    angle2 = angle2 * 180 / pi
    angle = [angle1,angle2]
    angle.sort()
    circ.append(Arc((centx,cent), rad_new * 2, rad_new * 2, angle = 0, theta1 = angle[0] , theta2 =  angle[1], color = 'r'))


[[x1,y1],[x2,y2]] = intersection_circle_general(0,0,0,cent_h,rad_TofCan,rad_h)
[theta1, tan1_r] = find_angle_general(0,0,x1,y1)
theta1 = theta1
ang_s_Tn = theta1 
ang_e_Tn = 3 * pi / 2 
stp_Tn = (ang_e_Tn - ang_s_Tn) / 6
#print([ang_s_Tn,ang_e_Tn,stp_Tn])

[[x1,y1],[x2,y2]] = intersection_circle_general(0,0,0,cent_h,radius,rad_h)
[theta1, tan1_r] = find_angle_general(0,0,x1,y1)
theta1 = theta1
ang_s_Eq = theta1 
ang_e_Eq = 3 * pi / 2  
stp_Eq = (ang_e_Eq - ang_s_Eq) / 6
#print([ang_s_Eq,ang_e_Eq,stp_Eq])

[[x1,y1],[x2,y2]] = intersection_circle_general(0,0,0,cent_h,rad_TofCap,rad_h)
[theta1, tan1_r] = find_angle_general(0,0,x1,y1)
theta1 = theta1
ang_s_Tp = theta1 
ang_e_Tp = 3 * pi / 2 
stp_Tp = (ang_e_Tp - ang_s_Tp) / 6
#print([ang_s_Tp,ang_e_Tp,stp_Tp])

ax=plt.gca()
for j in range(1,6):
    ang_Tn = ang_s_Tn + j * stp_Tn
    ang_Eq = ang_s_Eq + j * stp_Eq
    ang_Tp = ang_s_Tp + j * stp_Tp
    [xn,yn] = [rad_TofCan * cos(ang_Tn), rad_TofCan * sin(ang_Tn)]
    [xe,ye] = [radius * cos(ang_Eq), radius * sin(ang_Eq)]
    [xp,yp] = [rad_TofCap * cos(ang_Tp), rad_TofCap * sin(ang_Tp)]
    draw_arc_3points(xn,yn,xe,ye,xp,yp,True,circ)

ax.plot([0,0],[-rad1,rad1], color = 'b')
ax.plot([-rad1,rad1],[0,0], color = 'b')
for j in circ:
    ax.add_patch(j)
#plt.axis('scaled')
ax.set_aspect('equal', adjustable='box')
#manager = plt.get_current_fig_manager()
#manager.full_screen_toggle()
plt.show()