from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import astrolabGUI
import astrolab

def convertColor(color):
    if color == 'r':
        return QtCore.Qt.red
    elif color == 'g':
        return QtCore.Qt.green
    elif color == 'b':
        return QtCore.Qt.blue
    elif color == 'w':
        return QtCore.Qt.white
    elif color == 'y':
        return QtCore.Qt.yellow
    elif color == 'k':
        return QtCore.Qt.black
    else:
        return QtCore.Qt.black

class MainApp(QtWidgets.QMainWindow, astrolabGUI.Ui_MainWindow,astrolab.Astrolab):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.borderX = 30
        self.borderY = 30
        self.sizeXY = self.spinBox_4.value()
        self.startX = self.gridLayoutWidget.width() + self.borderX
        self.startY = self.menubar.height() + self.borderY 
        self.zeroX = self.startX + self.sizeXY / 2
        self.zeroY = self.startY + self.sizeXY / 2
        self.resizeMain(self.sizeXY)
        #self.spinBox.setValue(35)
        #self.spinBox_2.setValue(10)
        #self.spinBox_3.setValue(15)
        self.spinBox.valueChanged['int'].connect(self.update)
        self.spinBox_2.valueChanged['int'].connect(self.update)
        self.spinBox_3.valueChanged['int'].connect(self.update)
        self.spinBox_4.valueChanged['int'].connect(self.resizeMain)
        self.spinBox_5.valueChanged['int'].connect(self.updateEclAng)
        #self.spinBox_5.valueChanged['int'].connect(self.dial.setValue)
        #self.spinBox_6.valueChanged['int'].connect(self.dial_2.setValue)
        self.spinBox_6.valueChanged['int'].connect(self.updateRulAng)
        self.checkBox.stateChanged.connect(self.update)
        self.checkBox_2.stateChanged.connect(self.update)
        self.checkBox_3.stateChanged.connect(self.update)
        #self.setVal()
        #self.draw()
        #self.showDrawing(self.painter)

    def updateEclAng(self,val):
        self.dial.setValue(val)
        self.update()

    def updateRulAng(self,val):
        self.dial_2.setValue(val)
        self.update()

    def resizeEvent(self, event):
        maxDim = min(self.size().width() - self.startX - self.borderX,self.size().height() - self.startY - self.borderY)
        self.spinBox_4.setValue(maxDim)
        self.sizeXY = self.spinBox_4.value()
        self.zeroX = self.startX + self.sizeXY / 2
        self.zeroY = self.startY + self.sizeXY / 2
        return super().resizeEvent(event)

    def resizeMain(self,x):
        self.resize(x + self.startX + self.borderX,x + self.startY + self.borderY)
        self.sizeXY = x
        self.zeroX = self.startX + self.sizeXY / 2
        self.zeroY = self.startY + self.sizeXY / 2

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        self.getInput()
        self.setVal()
        self.draw()
        self.showDrawing(painter)
    
    class CircleGUI(astrolab.Astrolab.CircleGUI):
        def draw(self, ax = None, zeroX = 0, zeroY = 0):
            x1 = self.x - self.r + zeroX 
            y1 = -self.y - self.r + zeroY
            col = convertColor(self.color)
            if self.type == None:
                type = QtCore.Qt.SolidLine
            ax.setPen(QtGui.QPen(col, self.size, type))
            ax.drawEllipse(x1,y1,2 * self.r, 2 * self.r)

    class ArcGUI(astrolab.Astrolab.ArcGUI):
        def draw(self, ax = None, zeroX = 0, zeroY = 0):
            x1 = self.x - self.r + zeroX 
            y1 = -self.y - self.r + zeroY
            theta1 = self.theta1 * 16 
            theta2 = (self.theta2 - self.theta1) * 16 
            col = convertColor(self.color)
            if self.type == None:
                type = QtCore.Qt.SolidLine
            ax.setPen(QtGui.QPen(col, self.size, type))
            ax.drawArc(x1,y1,2 * self.r, 2 * self.r,theta1 ,theta2)

    class LineGUI(astrolab.Astrolab.LineGUI):
        def draw(self,ax = None, zeroX = 0, zeroY = 0):
            x1 = self.x1 + zeroX 
            y1 = self.y1 + zeroY
            x2 = self.x2 + zeroX 
            y2 = self.y2 + zeroY
            col = convertColor(self.color)
            if self.type == None:
                type = QtCore.Qt.SolidLine
            ax.setPen(QtGui.QPen(col, self.size, type))
            ax.drawLine(x1,y1,x2,y2)

    class PointGUI(astrolab.Astrolab.PointGUI):
        def draw(self,ax = None, zeroX = 0, zeroY = 0):
            x = self.x + zeroX 
            y = self.y + zeroY
            col = convertColor(self.color)
            if self.type == None:
                type = QtCore.Qt.SolidLine
            #ax.setPen(QtGui.QPen(col, self.size, type))
            #ax.setBrush(col)
            ax.setPen(QtGui.QPen(col, 4 , type))
            r = self.size / 3
            ax.drawEllipse(x - r ,y - r ,2 * r, 2 * r)
            #ax.drawPoint(x,y)
    
    def showDrawing(self, ax = None):
        for element in self.drawings:
            element.draw(ax,self.zeroX,self.zeroY)
            #print("hello")

    def getInput(self):
        #return super().getVal()
        self.axial_tilt = 23.43646 # Also known as the obliquity of the ecliptic
        self.navigationStars = self.tableOfStars()
        self.latitude = self.spinBox.value()
        self.diurnalCircleStep = self.spinBox_2.value()
        self.meridianStep = self.spinBox_3.value()
        [cent,rad] = self.circ_2D(100.0,-self.axial_tilt,180 + self.axial_tilt)
        self.radiusEquator = int(self.spinBox_4.value() * 100.0 / rad / 2.0)
        #self.radiusEquator = self.spinBox_4.value()
        self.eclipticAngle = self.spinBox_5.value()
        self.rulerAngle = self.spinBox_6.value()
        self.eclipticON = self.checkBox_2.isChecked()
        self.starsON = self.checkBox_3.isChecked()
        self.rulerON = self.checkBox.isChecked()
    #def setVal(self):
    #    return super().setVal()
    #def draw(self):
    #    return super().draw() 
    

def main():
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()