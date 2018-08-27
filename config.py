#encoding=utf-8
from PyQt5.QtGui import QColor
#方块的形状
I = 1
leftL = 2
rightL = 3
square = 4
leftZ = 5
T = 6
rightZ = 7

#方块的颜色
colorI = QColor(0, 255, 255)
colorLeftL = QColor(106, 90, 205)
colorRightL = QColor(255, 215, 0)
colorSquare = QColor(173, 255,47)
colorLeftZ = QColor(0, 255, 127)
colorT = QColor(160, 32, 240)
colorRightZ = QColor(255, 0, 0)

#画布背景色
canvasColor = QColor(33, 33, 33)

BoxColor = [canvasColor, colorI, colorLeftL, colorRightL, colorSquare, colorLeftZ, colorT, colorRightZ]

#小块的边长
blockSize = 30

#画布的大小
canvasWidth = 15
canvasHeight = 25

#主窗口的大小
tetrixsWidth = 700
tetrixsHeight = 800

#画布的间隔
margin = 20

#主界面背景色
mainWindowColor="background-color:#263238"


#LCD和Button的背景色
lcdNumberColor = "background-color:#212121"
buttonColor = "background-color:#212121"

#方块下降速度
speed = 1000


#关于方块的操作
actionPosition = 0
actionLeft = 1
actionRight = 2
actionDown = 3
actionRotateLeft = 4
actionRotateRight = 5


#等级间距
levelStep = 50
percent = 0.9

#最大速度
maxSpeed = 100



