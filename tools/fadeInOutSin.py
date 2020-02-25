import math
import numpy as np
import maya.cmds as cmds
for i in range(0,90):
    
    cmds.currentTime(i)
    i=math.radians(i)
    a= i-(math.pi/2)
    c = np.sin((a*2)+(math.pi/2))
    b= c+1
    b=b/2
    print b
    #cmds.move(0,float(b),0,'locator1',r=1,os=1,wd=1)
    cmds.xform('locator1',t=(0,float(b),0))
    cmds.setKeyframe('locator1')


