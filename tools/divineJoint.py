#==========================
#encoding:utf-8
#==========================
#divine Joint 
#========================== 
import maya.cmds as cmds

#_divine Joint    

def divineJoint():
    locList = cmds.ls(sl=True)
    parentLOC = locList[0]
    childLOC = locList[1]
    sel_sLOC = cmds.xform(parentLOC,q=True,t=True)    
    sel_eLOC = cmds.xform(childLOC,q=True,t=True)
    distMaker = cmds.distanceDimension(sp=(sel_sLOC[0],sel_sLOC[1],sel_sLOC[2]),ep=(sel_eLOC[0],sel_eLOC[1],sel_eLOC[2]))
    cmds.rename(distMaker ,'distance1')
    distanceValue = cmds.getAttr('distance1.distance')
    
    ######## jointNumber ##########
    jn = cmds.intFieldGrp('jointNumber' ,q=1 ,value=1)
    jNUM = jn[0]
    ###############################
    
    #aim Xaxis focus LOC 
    aimLocator = cmds.spaceLocator()
    cmds.xform(aimLocator,t=(sel_eLOC[0],sel_eLOC[1],sel_eLOC[2]))
    parentJoint = cmds.joint(p=(sel_sLOC[0],sel_sLOC[1],sel_sLOC[2]))

    cmds.ungroup(aimLocator)
    cmds.aimConstraint(aimLocator,parentJoint,wut=0)
    cmds.delete(aimLocator)
    
    #parentJoint zeroOut
    y = cmds.xform(parentJoint,q=1,ro=1)
    cmds.joint(parentJoint,e=1,o=(y[0],y[1],y[2]))
    cmds.xform(parentJoint,ro=(0,0,0))
      
    for i in range(1,jNUM+1):
        iFloating = i*1.0
        dvPlace = iFloating/jNUM
        transValue = distanceValue*dvPlace
        dpJoint = cmds.duplicate(parentJoint,rr=1)
        #jointOrient
        x = cmds.xform(dpJoint,q=1,ro=1)
        cmds.joint(dpJoint,e=1,o=(y[0],y[1],y[2]))
        cmds.xform(dpJoint,ro=(0,0,0))
        cmds.select(dpJoint)
        cmds.move(transValue,0,0,r=1,os=1,wd=1)
        
    cmds.delete('distanceDimension1')
          
        

myName = 'divineJoint_Tool'
        
if cmds.window(myName,exists=True):
    cmds.deleteUI(myName, window=True)
        
myWin = cmds.window( myName, iconName='Djoint Tool', widthHeight=(200,500))
    
cmds.rowColumnLayout( numberOfColumns=1 , columnWidth=(1,200))
cmds.separator(style= "out" ,w=200 ,h=10)
    
cmds.rowColumnLayout( numberOfColumns=2 , columnWidth=[(1,80), (2,280)])
cmds.text( label="  jointNumber : " ,align = "right")
    
cmds.intFieldGrp('jointNumber')
cmds.setParent( '..' )
    
cmds.rowColumnLayout( numberOfColumns=1 , columnWidth=(1,200))
cmds.separator(style='in' ,w=200 ,h=15)
cmds.button( label = 'create Divine Joint' ,h=40 ,command = 'divineJoint()')
    
cmds.rowColumnLayout( numberOfColumns=1 , columnWidth=(1,200))
cmds.separator(style= "out" ,w=200,h=20)

cmds.window ( myWin, e=1, widthHeight=(210, 120) )
cmds.showWindow(myWin)     

