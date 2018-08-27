### 基于pyqt5的俄罗斯方块游戏

1. 编写这个小游戏的目的

   > 花了一个月自学了python后，算法方面在leetcode刷了一百道题
   >
   > 面向对象方面没有锻炼，因为我以前学过qt5,所以打算写个俄罗斯方块
   >
   > 来锻炼自己的面向对象编程

2. 对源文件进行说明

   主要是``board.py,  box.py,  config.py和main.py``这几个文件

   其他的都是无关紧要的

   - box.py

     box.py封装了方块的逻辑，一共七种方块

     ![](https://raw.githubusercontent.com/zyxdSTU/Tetrixs/master/block.png)

     box共有的操作，封装在父类中，包括顺时针旋转，逆时针旋转，左右移动，和向下移动

     各个子Box，有自己的形状``self.shape``，颜色``color``和初始位置``self.position``

   - config.py主要是一些配置参数，文件里面都有说明

   - board.py 是Canvas类, 继承QWidget，一个作为游戏区的画布

     介绍几个主要的函数

     - paintEvent函数，重写的绘画函数mdispose函数， 方块下落到底端后，之后的处理，包括是否得分，是否下一个方块出不来，游戏结束

     - downDirect函数：瞬间下落到底端，忽略时间等待

   - main.py

     main.py描述了游戏的主界面，包括一个Canvas类， 和两个QLCDNumber类,一个Score, 一个Level

     和两个按钮，一个Start, 一个Pause

3. 操作说明

   ![](https://github.com/zyxdSTU/Tetrixs/raw/master/Tetrixs.png)

   ```
   方向键左右，可以控制方块左右移动， 上下键分别对应逆时针旋转，和顺时针旋转
   
   空格键可以直接加快方块下落
   
   PAUSE按钮暂停游戏，CONTINUE按钮继续游戏
   
   START按钮开始游戏
   
   当游戏结束的时候，YES重新开始， NO退出游戏
   ```

4. 以后的更新

   ```
   俄罗斯方块的等级制度，只是消了50行，加一级， 速度变成原来的0.9
   可以考虑越到后面，增加等级越来越难，速度越来越快
      
   还有就是可以增加消行时的动画，不单单是声音提示，
   可以在右边栏显示下一个方块
   ```




