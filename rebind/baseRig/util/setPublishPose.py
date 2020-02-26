#encoding=utf-8
import maya.cmds as cmds
import math

def setPublishPose(rig,con):
    
    ###create pub group
    #query parent
    pnt = cmds.listRelatives (con,p=True)[0]
    pub_nul=''
    #name sort
    if cmds.attributeQuery ('publishPose',node='rig_GRP',ex=True) is False:
        cmds.addAttr (rig,k=True,ln= 'publishPose' ,at= 'double' ,min= 0 ,max =1 ,dv= 0)
        
    cmds.setAttr (rig+'.publishPose',1)
       

    pub_nul= cmds.group (con,n=con.replace('_CON','PublishPose_NUL'))

    cmds.xform(pub_nul,os=True,rp=(0,0,0))

    ###end create pub group
    ###set pub pose
    #
    loc =  cmds.spaceLocator (n=con.replace('_CON','PubPose_LOC'))[0]
    pbd =  cmds.createNode ('pairBlend')
    cmds.setAttr (pbd+'.rotInterpolation', 1)

    prefix = con.split('_')[0]

    if 'IK_foot' in con:
        pos1= cmds.xform (prefix+'_IK_leg_JNT',q=True,rp=True,ws=True)
        pos2= cmds.xform (prefix+'_IK_lowLeg_JNT',q=True,rp=True,ws=True)
        pos3= cmds.xform (prefix+'_IK_foot_JNT',q=True,rp=True,ws=True)
           
        dis1= abs(math.sqrt(math.pow(pos1[0]-pos2[0],2)+math.pow(pos1[1]-pos2[1],2)+math.pow(pos1[2]-pos2[2],2)))
        dis2= abs(math.sqrt(math.pow(pos2[0]-pos3[0],2)+math.pow(pos2[1]-pos3[1],2)+math.pow(pos2[2]-pos3[2],2)))
 
        distance= dis1+dis2
        cmds.delete (cmds.pointConstraint (prefix+'_IK_leg_JNT',loc,w=True))
        
        if 'Vec' in con:
            cmds.move (0,distance*-0.5,5,loc,r=True)
            pbd= cmds.listConnections(con.replace('_CON','Space_NUL')+'.t')[0]
            dcm1= cmds.listConnections(pbd+'.inTranslate1')[0]
            dcm2= cmds.listConnections(pbd+'.inTranslate2')[0]
            mmx1= cmds.listConnections(dcm1+'.inputMatrix')[0]
            mmx2= cmds.listConnections(dcm2+'.inputMatrix')[0]
            loc1= cmds.listConnections(mmx1+'.matrixIn[0]')[0]
            loc2= cmds.listConnections(mmx2+'.matrixIn[0]')[0]
            

            t1= cmds.getAttr (loc1+'.t')[0]
            cmds.delete (cmds.parentConstraint (loc,loc1,w=True))
            t2= cmds.getAttr (loc1+'.t')[0]
            
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inTranslate1',t1[0],t1[1],t1[2])
            cmds.setAttr (pbd+'.inTranslate2',t2[0],t2[1],t2[2])
            cmds.connectAttr (pbd+'.outTranslate',loc1+'.t',f=True)
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (loc1+'.t',t1[0],t1[1],t1[2]) 
            
            t1= cmds.getAttr (loc2+'.t')[0]
            cmds.delete (cmds.parentConstraint (loc,loc2,w=True))
            t2= cmds.getAttr (loc2+'.t')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inTranslate1',t1[0],t1[1],t1[2])
            cmds.setAttr (pbd+'.inTranslate2',t2[0],t2[1],t2[2])
            cmds.connectAttr (pbd+'.outTranslate',loc2+'.t',f=True)
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (loc2+'.t',t1[0],t1[1],t1[2]) 
            cmds.delete (cmds.parentConstraint (loc,con,w=True))
            cmds.setAttr (con+'.t',0,0,0)
        else:
            cmds.delete (cmds.pointConstraint (con,loc,w=True,skip=('x','z'))) 
            
            t1= cmds.getAttr (con+'.t')[0]        
            cmds.delete (cmds.pointConstraint (loc,con,w=True))
            t2= cmds.getAttr (con+'.t')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inTranslate1',t1[0],t1[1],t1[2])
            cmds.setAttr (pbd+'.inTranslate2',t2[0],t2[1],t2[2])

            cmds.connectAttr (pbd+'.outTranslate',pub_nul+'.t',f=True)
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.t',t1[0],t1[1],t1[2]) 

    if 'root' in con:
        
        pos0= cmds.xform (con,q=True,rp=True,ws=True)
        pos1= cmds.xform ('L_IK_leg_JNT',q=True,rp=True,ws=True)
        pos2= cmds.xform ('L_IK_lowLeg_JNT',q=True,rp=True,ws=True)
        pos3= cmds.xform ('L_IK_foot_JNT',q=True,rp=True,ws=True)
        pos4= cmds.xform ('L_IK_ball_JNT',q=True,rp=True,ws=True)
        
        dis1= abs(math.sqrt(math.pow(pos1[0]-pos1[0],2)+math.pow(pos0[1]-pos1[1],2)+math.pow(pos1[2]-pos1[2],2)))
        dis2= abs(math.sqrt(math.pow(pos1[0]-pos2[0],2)+math.pow(pos1[1]-pos2[1],2)+math.pow(pos1[2]-pos2[2],2)))
        dis3= abs(math.sqrt(math.pow(pos2[0]-pos3[0],2)+math.pow(pos2[1]-pos3[1],2)+math.pow(pos2[2]-pos3[2],2)))
        dis4= abs(math.sqrt(math.pow(pos3[0]-pos3[0],2)+math.pow(pos3[1]-pos4[1],2)+math.pow(pos3[2]-pos3[2],2)))

        dis5= abs(math.sqrt(math.pow(pos1[0]-pos3[0],2)+math.pow(pos1[1]-pos3[1],2)+math.pow(pos1[2]-pos3[2],2)))

        distance= dis1+dis2+dis3+dis4*0.95
        cmds.setAttr (loc+'.t',0,distance,0)
        t1= cmds.getAttr (con+'.t')[0]
        r1= cmds.getAttr (con+'.r')[0]      
        cmds.delete (cmds.parentConstraint (loc,con,w=True))
        t2= cmds.getAttr (con+'.t')[0]
        r2= cmds.getAttr (con+'.r')[0]
        pbd= cmds.createNode ('pairBlend')
        cmds.setAttr (pbd+'.inTranslate1',t1[0],t1[1],t1[2])
        cmds.setAttr (pbd+'.inTranslate2',t2[0],t2[1],t2[2])
        cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
        cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
        cmds.connectAttr (pbd+'.outTranslate',pub_nul+'.t',f=True)
        cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)

        cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
        cmds.setAttr (con+'.t',t1[0],t1[1],t1[2]) 
        cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
    if 'Body' in con:
        pos1= cmds.xform (con,q=True,rp=True,ws=True)
        pos2= cmds.xform ('root_CON',q=True,rp=True,ws=True)
        distance= abs(math.sqrt(math.pow(pos1[0]-pos2[0],2)+math.pow(pos1[1]-pos2[1],2)+math.pow(pos1[2]-pos2[2],2)))
        cmds.delete (cmds.pointConstraint ('root_CON',loc,w=True,offset=(0,distance,0)))
        t1= cmds.getAttr (con+'.t')[0]
        r1= cmds.getAttr (con+'.r')[0]      
        cmds.delete (cmds.parentConstraint (loc,con,w=True))
        t2= cmds.getAttr (con+'.t')[0]
        r2= cmds.getAttr (con+'.r')[0]
        pbd= cmds.createNode ('pairBlend')
        cmds.setAttr (pbd+'.inTranslate1',t1[0],t1[1],t1[2])
        cmds.setAttr (pbd+'.inTranslate2',t2[0],t2[1],t2[2])
        cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
        cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
        cmds.connectAttr (pbd+'.outTranslate',pub_nul+'.t',f=True)
        cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)

        cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
        cmds.setAttr (con+'.t',t1[0],t1[1],t1[2]) 
        cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
    
    if 'hip' in con:
        pos1= cmds.xform (con,q=True,rp=True,ws=True)
        pos2= cmds.xform ('root_CON',q=True,rp=True,ws=True)
        distance= abs(math.sqrt(math.pow(pos1[0]-pos2[0],2)+math.pow(pos1[1]-pos2[1],2)+math.pow(pos1[2]-pos2[2],2)))
        cmds.delete (cmds.pointConstraint ('root_CON',loc,w=True,offset=(0,distance*-1,0)))
        t1= cmds.getAttr (con+'.t')[0]
        r1= cmds.getAttr (con+'.r')[0]      
        cmds.delete (cmds.parentConstraint (loc,con,w=True))
        t2= cmds.getAttr (con+'.t')[0]
        r2= cmds.getAttr (con+'.r')[0]
        pbd= cmds.createNode ('pairBlend')
        cmds.setAttr (pbd+'.inTranslate1',t1[0],t1[1],t1[2])
        cmds.setAttr (pbd+'.inTranslate2',t2[0],t2[1],t2[2])
        cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
        cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
        cmds.connectAttr (pbd+'.outTranslate',pub_nul+'.t',f=True)
        cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)

        cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
        cmds.setAttr (con+'.t',t1[0],t1[1],t1[2]) 
        cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
   
    if 'head' in con:
        r1= cmds.getAttr (con+'.r')[0]      
        cmds.delete (cmds.orientConstraint (loc,con,w=True))
        r2= cmds.getAttr (con+'.r')[0]
        pbd= cmds.createNode ('pairBlend')
        cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
        cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
        cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)

        cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
        cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
                   
    if 'FK_leg' in con:

        cmds.delete (cmds.orientConstraint (prefix+'_IK_leg_JNT',loc,w=True))
        r1= cmds.getAttr (con+'.r')[0]      
        cmds.delete (cmds.orientConstraint (loc,con,w=True))
        r2= cmds.getAttr (con+'.r')[0]

        pbd= cmds.createNode ('pairBlend')
        cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
        cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
        cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)

        cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
        cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 

    if 'FK_lowLeg' in con:

        cmds.delete (cmds.orientConstraint (prefix+'_IK_lowLeg_JNT',loc,w=True))
        r1= cmds.getAttr (con+'.r')[0]      
        cmds.delete (cmds.orientConstraint (loc,con,w=True))
        r2= cmds.getAttr (con+'.r')[0]
        pbd= cmds.createNode ('pairBlend')
        cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
        cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
        cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)

        cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
        cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
    if 'FK_foot' in con:
        cmds.delete (cmds.orientConstraint (prefix+'_IK_foot_JNT',loc,w=True))
        r1= cmds.getAttr (con+'.r')[0]      
        cmds.delete (cmds.orientConstraint (loc,con,w=True))
        r2= cmds.getAttr (con+'.r')[0]
        pbd= cmds.createNode ('pairBlend')
        cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
        cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
        cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)

        cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
        cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
            
    if 'FK_upArm' in con:           
        if 'L' in prefix:
            cmds.setAttr (loc+'.r',0,5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
        if 'R' in prefix:
            cmds.setAttr (loc+'.r',-180,-5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2])
                 
    if 'FK_foreArm' in con:           
        if 'L' in prefix:
            cmds.setAttr (loc+'.r',0,-5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 

        if 'R' in prefix:
            cmds.setAttr (loc+'.r',-180,5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2])     
            
    if 'FK_hand' in con:           
        if 'L' in prefix:
            cmds.setAttr (loc+'.r',0,-5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 

        if 'R' in prefix:
            cmds.setAttr (loc+'.r',-180,5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2])                   
    if 'IK_hand' in con:
        if 'Vec' in con:
            cmds.delete (cmds.parentConstraint (prefix+'_FK_foreArm_CON',loc,w=True)) 
            pbd= cmds.listConnections(con.replace('_CON','Space_NUL')+'.t')[0]
            dcm1= cmds.listConnections(pbd+'.inTranslate1')[0]
            dcm2= cmds.listConnections(pbd+'.inTranslate2')[0]
            mmx1= cmds.listConnections(dcm1+'.inputMatrix')[0]
            mmx2= cmds.listConnections(dcm2+'.inputMatrix')[0]
            loc1= cmds.listConnections(mmx1+'.matrixIn[0]')[0]
            loc2= cmds.listConnections(mmx2+'.matrixIn[0]')[0]
            t1= cmds.getAttr (loc1+'.t')[0]
            cmds.delete (cmds.parentConstraint (loc,loc1,w=True))
            cmds.move (0,0,-2.5,loc1,r=True)
            t2= cmds.getAttr (loc1+'.t')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inTranslate1',t1[0],t1[1],t1[2])
            cmds.setAttr (pbd+'.inTranslate2',t2[0],t2[1],t2[2])
            cmds.connectAttr (pbd+'.outTranslate',loc1+'.t',f=True)
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (loc1+'.t',t1[0],t1[1],t1[2]) 
            
            t1= cmds.getAttr (loc2+'.t')[0]
            cmds.delete (cmds.parentConstraint (loc,loc2,w=True))
            cmds.move (0,0,-2.5,loc2,r=True)
            t2= cmds.getAttr (loc2+'.t')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inTranslate1',t1[0],t1[1],t1[2])
            cmds.setAttr (pbd+'.inTranslate2',t2[0],t2[1],t2[2])
            cmds.connectAttr (pbd+'.outTranslate',loc2+'.t',f=True)
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (loc2+'.t',t1[0],t1[1],t1[2]) 
            cmds.setAttr (con+'.t',0,0,0)
        else:
            cmds.delete (cmds.parentConstraint (prefix+'_FK_hand_CON',loc,w=True)) 
            t1= cmds.getAttr (con+'.t')[0]      
            cmds.delete (cmds.pointConstraint (loc,con,w=True))
            t2= cmds.getAttr (con+'.t')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inTranslate1',t1[0],t1[1],t1[2])
            cmds.setAttr (pbd+'.inTranslate2',t2[0],t2[1],t2[2])
            cmds.connectAttr (pbd+'.outTranslate',pub_nul+'.t',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.t',t1[0],t1[1],t1[2]) 
            if 'Sub' in con:
                r1= cmds.getAttr (con+'.r')[0]      
                cmds.delete (cmds.orientConstraint (loc,con,w=True))
                r2= cmds.getAttr (con+'.r')[0]
                pbd= cmds.createNode ('pairBlend')
                cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
                cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
                cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
        
                cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
                cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
        
                                    
    if 'thumb' in con:
        if 'L' in prefix:
            cmds.setAttr (loc+'.r',80,-30,-30)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
        if 'R' in prefix:
            cmds.setAttr (loc+'.r',-100,30,30)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2])     
    if 'index' in con:
        if 'L' in prefix:
            cmds.setAttr (loc+'.r',0,-5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
        if 'R' in prefix:
            cmds.setAttr (loc+'.r',-180,5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2])     
    if 'middle' in con:
        if 'L' in prefix:
            cmds.setAttr (loc+'.r',0,-5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
        if 'R' in prefix:
            cmds.setAttr (loc+'.r',-180,5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2])     
    if 'ring' in con:
        if 'L' in prefix:
            cmds.setAttr (loc+'.r',0,-5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
        if 'R' in prefix:
            cmds.setAttr (loc+'.r',-180,5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2])     
    if 'pinky' in con:
        if 'L' in prefix:
            cmds.setAttr (loc+'.r',0,-5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
        if 'R' in prefix:
            cmds.setAttr (loc+'.r',-180,5,0)
            r1= cmds.getAttr (con+'.r')[0]      
            cmds.delete (cmds.orientConstraint (loc,con,w=True))
            r2= cmds.getAttr (con+'.r')[0]
            pbd= cmds.createNode ('pairBlend')
            cmds.setAttr (pbd+'.inRotate1',r1[0],r1[1],r1[2])
            cmds.setAttr (pbd+'.inRotate2',r2[0],r2[1],r2[2])
            cmds.connectAttr (pbd+'.outRotate',pub_nul+'.r',f=True)
    
            cmds.connectAttr (rig+'.publishPose',pbd+'.weight',f=True)
            cmds.setAttr (con+'.r',r1[0],r1[1],r1[2]) 
    cmds.setAttr ('rig_GRP.publishPose',0)              
    cmds.delete(loc)
    return  