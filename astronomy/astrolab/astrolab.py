import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
from math import pi, sqrt,atan2,tan,sin,cos
import pandas as pd

class Astrolab:

    class CircleGUI:
        def __init__(self,x,y,r,color,size = 3,type = None):
            self.x = x
            self.y = y
            self.r = r
            self.color = color
            self.size = size
            self.type = type
        def draw(self, ax = None):
            return plt.Circle((self.x,self.y), self.r, fill=False, color = self.color)

    class ArcGUI:
        def __init__(self,x,y,r,theta1,theta2,color,size = 3,type = None):
            self.x = x
            self.y = y
            self.r = r
            self.theta1 = theta1
            self.theta2 = theta2
            self.color = color
            self.size = size
            self.type = type
        def draw(self , ax = None):
            #if self.x == 0:
            #    print(self.x,self.y,self.theta1,self.theta2)
            return Arc((self.x,self.y), self.r * 2, self.r * 2, angle = 0, theta1 = self.theta1 , theta2 =  self.theta2, color = self.color)

    class LineGUI:
        def __init__(self,x1,y1,x2,y2,color,size = 3, type = None):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
            self.color = color
            self.size = size
            self.type = type
        def draw(self,ax = None):
            ax.plot([self.x1,self.x2],[self.y1,self.y2], color = self.color)

    class PointGUI:
        def __init__(self,x,y,color,size = 3, type = None):
            self.x = x
            self.y = y
            self.color = color
            self.size = size
            self.type = type
        def draw(self,ax = None):
            ax.scatter(self.x, self.y, s = self.size)


    def __init__(self) -> None:
        self.axial_tilt = 23.43646 # Also known as the obliquity of the ecliptic
        self.eclipticAngle = 0
        self.rulerAngle = 0  
        self.navigationStars = self.tableOfStars()
        self.getInput()
        self.setVal()
        self.draw()
        self.showDrawing() 

    def showDrawing(self, ax = None):
        ax=plt.gca()
        #self.radiusTropicOfCapricorn = radiusTropicOfCapricorn
        #plt.xlim((int(-radiusTropicOfCapricorn),int(radiusTropicOfCapricorn)))
        #plt.ylim((int(-radiusTropicOfCapricorn),int(radiusTropicOfCapricorn)))
        plt.xlim((int(-self.radiusTropicOfCapricorn),int(self.radiusTropicOfCapricorn)))
        plt.ylim((int(-self.radiusTropicOfCapricorn),int(self.radiusTropicOfCapricorn)))
        #self.ax=plt.gca()
        for element in self.drawings:
            if isinstance(element,self.CircleGUI) or isinstance(element,self.ArcGUI):
                ax.add_patch(element.draw())
            elif isinstance(element,self.LineGUI) or isinstance(element,self.PointGUI):
                element.draw(ax)
        #plt.axis('scaled')
        ax.set_aspect('equal', adjustable='box')
        #manager = plt.get_current_fig_manager()
        #manager.full_screen_toggle()
        plt.show()    

    def getInput(self):
        self.latitude = float(input("Enter the earth latitude(degree)[52.1579]:") or "52.1579")
        self.diurnalCircleStep = float(input("Enter the diurnal circle step angle(degree)[10]:") or "10")
        self.meridianStep = float(input("Enter the celestial meridian step angle(degree)[15]:") or "15")
        self.radiusEquator = float(input("Enter the celestial equator radius[200]:") or "200")
        self.eclipticON = True
        self.starsON = True
        self.rulerON = True 

    def setVal(self):
        [cent,rad] = self.circ_2D(self.radiusEquator,-self.axial_tilt,180 + self.axial_tilt)
        self.radiusTropicOfCapricorn = rad

        [cent,rad] = self.circ_2D(self.radiusEquator,self.axial_tilt,180 - self.axial_tilt)
        self.radiusTropicOfCancer = rad

        [self.centerHorizon,self.radiusHorizon] = self.circ_2D(self.radiusEquator,self.latitude - 90,self.latitude + 90)
        [self.distZenith,self.phiZenith] = self.cor_2D(self.radiusEquator, self.latitude, 0)

        gamma = self.gamma_find(90 - self.axial_tilt,0)
        [self.centerEcliptic,self.radiusEcliptic] = self.circ_2D(self.radiusEquator,gamma[0],gamma[1])

    def draw(self):
        self.drawings = []
        self.drawAxis()
        self.drawBorderAngles()      
        self.drawTropicOfCapricorn()
        self.drawEquator()
        self.drawTropicOfCancer()
        if self.eclipticON:
            self.drawEcliptic()        
        if self.starsON:
            self.drawStars()        
        if self.rulerON:
            self.drawRuler()
        self.drawDiurnalCircles()
        self.drawMeridian()
        self.drawUnderHorizonDivider()        
             
    def tableOfStars(self):
        df = pd.read_csv("table-2.csv")
        df = df.drop(columns = ['References'])
        res = df.values.tolist()
        return res

    def drawAxis(self):
        #self.drawings.append(self.LineGUI(0, 0, -self.radiusTropicOfCapricorn, self.radiusTropicOfCapricorn, color = 'b'))
        #self.drawings.append(self.LineGUI(-self.radiusTropicOfCapricorn, self.radiusTropicOfCapricorn, 0, 0, color = 'b'))
        self.drawings.append(self.LineGUI(0, -self.radiusTropicOfCapricorn, 0, self.radiusTropicOfCapricorn, color = 'k', size =2))
        self.drawings.append(self.LineGUI(-self.radiusTropicOfCapricorn, 0, self.radiusTropicOfCapricorn, 0, color = 'k', size = 2))
    
    def drawBorderAngles(self):
        for i in range(360):
            x1 = self.radiusTropicOfCapricorn * sin(i * pi / 180)
            y1 = self.radiusTropicOfCapricorn * cos(i * pi / 180)
            if i % 5 == 0:
                ll = 15
            else:
                ll = 8
            x2 = (self.radiusTropicOfCapricorn + ll) * sin(i * pi / 180)
            y2 = (self.radiusTropicOfCapricorn + ll) * cos(i * pi / 180)
            self.drawings.append(self.LineGUI(x1, y1, x2 , y2, color = 'k', size = 2))
        self.drawings.append(self.CircleGUI(0, 0, self.radiusTropicOfCapricorn + 15, color = 'b', size = 2))

    def drawTropicOfCapricorn(self):
        self.drawings.append(self.CircleGUI(0, 0, self.radiusTropicOfCapricorn, color = 'b'))

    def drawEquator(self):
        self.drawings.append(self.CircleGUI(0, 0, self.radiusEquator, color = 'b'))

    def drawTropicOfCancer(self):
        self.drawings.append(self.CircleGUI(0, 0, self.radiusTropicOfCancer, color = 'b'))

    def drawEcliptic(self):
        centx = self.centerEcliptic * sin(self.eclipticAngle * pi / 180)
        centy = -self.centerEcliptic * cos(self.eclipticAngle * pi / 180)
        self.drawings.append(self.CircleGUI(centx, centy, self.radiusEcliptic, color = 'y', size = 5))

    def drawRuler(self):
        x = self.radiusTropicOfCapricorn * sin(self.rulerAngle * pi / 180)
        y = self.radiusTropicOfCapricorn * cos(self.rulerAngle * pi / 180)        
        self.drawings.append(self.LineGUI(x, y, -x , -y, color = 'b'))

    def drawStars(self):
        for star in self.navigationStars:
            [r,theta] = self.cor_2D(self.radiusEquator, star[4], star[3])
            theta -= self.eclipticAngle + 90
            x = r * cos(theta * pi / 180)
            y = r * sin(theta * pi / 180)
            brightness = int((-star[5] + 4) * 5)
            if r < self.radiusTropicOfCapricorn:
                self.drawings.append(self.PointGUI(x, y, color = 'k', size = brightness))

    def drawDiurnalCircles(self):
        for i in np.arange(0,90,self.diurnalCircleStep):
            gamma = self.gamma_find(self.latitude,i)
            [cent,rad] = self.circ_2D(self.radiusEquator,gamma[0],gamma[1])
            if self.has_intersection_circle(self.radiusTropicOfCapricorn,rad,cent):
                [x,y,theta] = self.intersection_circle(self.radiusTropicOfCapricorn,rad,cent)
                theta = theta * 180 / pi
                self.drawings.append(self.ArcGUI(0, cent, rad, 180 + theta, 360 - theta, color = 'r', size = 2))
            else:  # No intersection
                self.drawings.append(self.CircleGUI(0, cent, rad, color = 'r', size = 2))
    
    def drawMeridian(self):
        gamma = self.gamma_find(self.latitude + 90,0)
        [cent,rad] = self.circ_2D(self.radiusEquator,gamma[0],gamma[1])
        xy = [[0 for x in range(2)] for y in range(4)]
        for j in np.arange(0,181,self.meridianStep):
            centx = rad * self.angle_find(self.latitude,j)
            if (centx > 10000 * rad):
                centx = 10000 * rad 
            rad_new = sqrt (rad * rad + centx * centx)
            stat = False
            if self.has_intersection_circle_general(0,0,centx,cent,self.radiusTropicOfCapricorn,rad_new):
                xy[0:2] = self.intersection_circle_general(0,0,centx,cent,self.radiusTropicOfCapricorn,rad_new)
            else: 
                xy[0] = [1000000,1000000]
                xy[1] = [1000000,1000000]
                stat = True

            if self.has_intersection_circle_general(0,self.centerHorizon,centx,cent,self.radiusHorizon,rad_new):
                xy[2:4] = self.intersection_circle_general(0,self.centerHorizon,centx,cent,self.radiusHorizon,rad_new)
                stat = False
            else:
                xy[2] = [1000000,1000000]
                xy[3] = [1000000,1000000]

            if stat:
                self.drawings.append(self.CircleGUI(centx, cent, rad_new, color = 'r', size = 2))
            else:
                xyn = self.select_two_nearest(xy,0,self.distZenith)
                [angle1,tan1] = self.find_angle_general(centx,cent,xyn[0][0],xyn[0][1]) 
                [angle2,tan2] = self.find_angle_general(centx,cent,xyn[1][0],xyn[1][1])
                angle1 = angle1 * 180 / pi
                angle2 = angle2 * 180 / pi
                angle = [angle1,angle2]
                angle.sort()
                self.drawings.append(self.ArcGUI(centx, cent, rad_new, angle[0], angle[1], color = 'r', size = 2))
 
    def drawUnderHorizonDivider(self):
        [[x1,y1],[x2,y2]] = self.intersection_circle_general(0,0,0,self.centerHorizon,self.radiusTropicOfCancer,self.radiusHorizon)
        [theta1, tan1_r] = self.find_angle_general(0,0,x1,y1)
        theta1 = theta1
        ang_s_Tn = theta1 
        ang_e_Tn = 3 * pi / 2 
        stp_Tn = (ang_e_Tn - ang_s_Tn) / 6
        #print([ang_s_Tn,ang_e_Tn,stp_Tn])

        [[x1,y1],[x2,y2]] = self.intersection_circle_general(0,0,0,self.centerHorizon,self.radiusEquator,self.radiusHorizon)
        [theta1, tan1_r] = self.find_angle_general(0,0,x1,y1)
        theta1 = theta1
        ang_s_Eq = theta1 
        ang_e_Eq = 3 * pi / 2  
        stp_Eq = (ang_e_Eq - ang_s_Eq) / 6
        #print([ang_s_Eq,ang_e_Eq,stp_Eq])

        [[x1,y1],[x2,y2]] = self.intersection_circle_general(0,0,0,self.centerHorizon,self.radiusTropicOfCapricorn,self.radiusHorizon)
        [theta1, tan1_r] = self.find_angle_general(0,0,x1,y1)
        theta1 = theta1
        ang_s_Tp = theta1 
        ang_e_Tp = 3 * pi / 2 
        stp_Tp = (ang_e_Tp - ang_s_Tp) / 6
        #print([ang_s_Tp,ang_e_Tp,stp_Tp])

        for j in range(1,6):
            ang_Tn = ang_s_Tn + j * stp_Tn
            ang_Eq = ang_s_Eq + j * stp_Eq
            ang_Tp = ang_s_Tp + j * stp_Tp
            [xn,yn] = [self.radiusTropicOfCancer * cos(ang_Tn), self.radiusTropicOfCancer * sin(ang_Tn)]
            [xe,ye] = [self.radiusEquator * cos(ang_Eq), self.radiusEquator * sin(ang_Eq)]
            [xp,yp] = [self.radiusTropicOfCapricorn * cos(ang_Tp), self.radiusTropicOfCapricorn * sin(ang_Tp)]
            self.draw_arc_3points(xn,yn,xe,ye,xp,yp,True)     

    
    def cor_2D(self,R, teta, phi):
        res = R * np.tan(pi/4 - teta/2 * pi / 180)
        return [np.abs(res),phi]
    
    def gamma_find(self,alfa,beta):
        gamma1 = (alfa + beta) - 90
        gamma2 = (alfa - beta) + 90
        return [gamma1,gamma2]

    def intersection_circle(self,r1,r2,d):
        [[x1,y1],[x2,y2]] = self.intersection_circle_general(0,0,0,d,r1,r2)
        x = x2
        y = y2
        theta = atan2(d-y,x)
        return [x,y,theta]

    def intersection_circle_general(self,a,b,c,d,r0,r1):
        dd = sqrt((c-a)*(c-a)+(d-b)*(d-b))
        ss = 0.25 * sqrt ((dd+r0+r1) * (dd+r0-r1) * (dd-r0+r1) * (-dd+r0+r1))
        x1 = (a+c)/2 + (c-a)*(r0*r0-r1*r1)/(2*dd*dd) + 2 *(b-d)/(dd*dd)*ss
        x2 = (a+c)/2 + (c-a)*(r0*r0-r1*r1)/(2*dd*dd) - 2 *(b-d)/(dd*dd)*ss
        y1 = (b+d)/2 + (d-b)*(r0*r0-r1*r1)/(2*dd*dd) - 2 *(a-c)/(dd*dd)*ss
        y2 = (b+d)/2 + (d-b)*(r0*r0-r1*r1)/(2*dd*dd) + 2 *(a-c)/(dd*dd)*ss
        return [[x1,y1],[x2,y2]]

    def has_intersection_circle_general(self,a,b,c,d,r0,r1):
        dd = sqrt((c-a)*(c-a)+(d-b)*(d-b))
        if (r0 + r1 > dd and abs(r0-r1) < dd):
            return True
        else:
            return False

    def has_intersection_circle(self,r1,r2,d):
        return self.has_intersection_circle_general(0,0,0,d,r1,r2)

    def circ_2D(self,r,theta1,theta2):
        if (theta1>-90 and theta1<90):
            ph1 = 0
        else: 
            ph1 = 180    
        if (theta2>-90 and theta2<90):
            ph2 = 0
        else: 
            ph2 = 180
        [r1,phi1] = self.cor_2D(r,theta1,ph1)
        [r2,phi2] = self.cor_2D(r,theta2,ph2)
        cent = (r1 * np.cos(phi1*pi/180) + r2 * np.cos(phi2*pi/180)) / 2
        rad = np.abs((r1 * np.cos(phi1*pi/180) - r2 * np.cos(phi2*pi/180)) / 2)
        return [cent,rad]       

    def angle_find(self,lat,alpha):
        return (tan(alpha * pi / 180) / sin(lat * pi / 180))

    def find_angle_general(self,x1,y1,x2,y2):
        x = x2 - x1
        y = y2 - y1
        res = atan2(y,x)
        if (res < 0):
            res = res + 2 * pi
        return [res,y/x]

    def select_two_nearest(self,xy,x0,y0):
        dis = []
        for i in xy:
            ss = sqrt((i[0]-x0)*(i[0]-x0)+(i[1]-y0)*(i[1]-y0))
            dis.append (ss)        
        index_sort = [j[0] for j in sorted(enumerate(dis), key=lambda x:x[1])]
        return [xy[index_sort[0]],xy[index_sort[1]]]

    def circle_from_3_points(self,x1,y1,x2,y2,x3,y3):
        mat = np.array ([[0,0,0,1],[x1*x1+y1*y1,x1,y1,1],[x2*x2+y2*y2,x2,y2,1],[x3*x3+y3*y3,x3,y3,1]])
        M12 = self.minor(mat,0,1)
        M11 = self.minor(mat,0,0)
        M13 = self.minor(mat,0,2)
        M14 = self.minor(mat,0,3)

        x0 = 0.5 * np.linalg.det(M12) / np.linalg.det(M11)
        y0 = -0.5 * np.linalg.det(M13) / np.linalg.det(M11)
        r = sqrt(x0*x0 + y0*y0+ np.linalg.det(M14) / np.linalg.det(M11))
        return [x0,y0,r]

    def minor(self,arr,i,j):
        # ith row, jth column removed
        return arr[np.array(list(range(i))+list(range(i+1,arr.shape[0])))[:,np.newaxis],
                np.array(list(range(j))+list(range(j+1,arr.shape[1])))]

    def draw_arc_3points(self,x1,y1,x2,y2,x3,y3,direction):
        [x0,y0,r] = self.circle_from_3_points(x1,y1,x2,y2,x3,y3)
        ang = []
        ang.append(self.find_angle_general(x0,y0,x1,y1))
        ang.append(self.find_angle_general(x0,y0,x2,y2))
        ang.append(self.find_angle_general(x0,y0,x3,y3))
        ang.sort()

        if (direction):
            ang0 = ang[0][0] 
            ang2 = ang[2][0]
        else:
            ang0 = ang[2][0] 
            ang2 = ang[0][0]

        self.drawings.append(self.ArcGUI(x0, y0, r, ang0 * 180 / pi, ang2 * 180 / pi, color = 'g', size = 2))
        self.drawings.append(self.ArcGUI(-x0, y0, r, 180 - ang2 * 180 / pi, 180 - ang0 * 180 / pi, color = 'g', size = 2))

if __name__ == '__main__':
    start =  Astrolab()