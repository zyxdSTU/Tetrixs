#encoding=utf-8
from config import *


class Box:
    #向左旋转
    def rotateLeft(self):
        for element in self.shape:
            element[0], element[1] = -element[1], element[0]


    #向右旋转    
    def rotateRight(self):
        for element in self.shape:
            element[0], element[1] = element[1], -element[0]

    #向左移动
    def moveLeft(self):
        self.position[1] -= 1

    #向右移动
    def moveRight(self):
        self.position[1] += 1

    #向下移动
    def down(self):
        self.position[0] += 1
        
    #Box各个方块的位置
    def getPosition(self):
        positionAbsolute = []
        for element in self.shape:
            one = element[0] + self.position[0]
            two = element[1] + self.position[1] 
            positionAbsolute.append([one,two])
        return positionAbsolute

    def getRotateLeftPosition(self):
        positionAbsolute = []

        #先左转
        self.rotateLeft()

        for element in self.shape:
            one = element[0] + self.position[0]
            two = element[1] + self.position[1] 
            positionAbsolute.append([one,two])

        #后右转
        self.rotateRight()

        return positionAbsolute

    def getRotateRightPosition(self):
        positionAbsolute = []

        #先右转
        self.rotateRight()

        for element in self.shape:
            one = element[0] + self.position[0]
            two = element[1] + self.position[1] 
            positionAbsolute.append([one,two])

        #后左转
        self.rotateLeft()
            
        return positionAbsolute


class IBox(Box):
    #初始化方块颜色
    color = I

    def __init__(self):
        #初始化方块的形状
        self.shape = [[0, -1], [0, 0], [0, 1], [0, 2]]
        self.position = [1, 7]


class LeftLBox(Box):
    color = leftL

    def __init__(self):
        self.shape = [[0, -1], [0, 0], [0,1], [-1,-1]]
        self.position = [1, 7]

class RightLBox(Box):
    color = rightL

    def __init__(self):
        self.shape = [[0, -1], [0,0], [0, 1], [-1, 1]]
        self.position = [1, 7]

class SquareBox(Box):
    color = square

    def __init__(self):
        self.shape = [[-1, -1], [0, -1], [-1, 0], [0, 0]]
        self.position = [1, 7]

    #正方形的方块没有旋转
    def rotateLeft(self):
        return 

    def rotateRight(self):
        return

class LeftZBox(Box):
    color = leftZ

    def __init__(self):
        self.shape = [[0, -1], [0, 0], [-1, 0], [-1, 1]]
        self.position = [1, 7]

class TBox(Box):
    color = T

    def __init__(self):
        self.shape = [[0, -1], [0, 0], [-1, 0], [0, 1]]
        self.position = [1, 7]

class RightZBox(Box):
    color = rightZ

    def __init__(self):
        self.shape = [[-1, -1], [0, 0], [-1, 0], [0, 1]]
        self.position = [1, 7]



