#encoding:utf-8
#==============================
#
#
#==============================
import maya.cmds as cmds
import maya.mel as mel
from util.defaultGroupNode import*
from util.setUniqueName import*
from util.homeNul import*




class stretchyLock():

    def __init__(self):

        z=defaultGroupNode()
        z.createGroupNode()
        
        return
    
    
    def setStretchyLock(self,con,polVec,guide,*jnt):   
        
        msLenght=0
        
        #name
        if '_CON' in con:
            name= con.replace('_CON','')
            
        elif '_LOC' in con:
            name= con.replace('_LOC','')    
            
        else:
            name= con
            
        tm= cmds.getAttr(str(jnt[-1])+'.tx')
        b= tm/(abs(tm))
        
        for i in range(len(jnt)-1):
            tmp= abs(cmds.getAttr (jnt[i+1]+".translateX"))
            msLenght= tmp+msLenght
               
        dcm= cmds.createNode ('decomposeMatrix')
        cmds.connectAttr (con+'.worldMatrix[0]',dcm+'.inputMatrix',f=True)
        
        #어트리뷰트 생성
        cmds.addAttr (con,k=True,ln= 'stretchy' ,at= 'double' ,min= 0 ,max =10 ,dv= 0)
        cmds.addAttr (con,k=True,ln= 'antiPop' ,at= 'double' ,min= 0 ,max =10 ,dv= 0)
        
        IKSetRangeStretch= cmds.createNode ('setRange',n='IKSetRangeStretch')
        IKSetRangeAntiPop= cmds.createNode ('setRange',n='IKSetRangeAntiPop')
        
        cmds.setAttr (IKSetRangeStretch+'.maxX', 1)
        cmds.setAttr (IKSetRangeAntiPop+'.maxX', 1)
        cmds.setAttr (IKSetRangeStretch+'.oldMaxX', 10)
        cmds.setAttr (IKSetRangeAntiPop+'.oldMaxX', 10)
        cmds.connectAttr (con+'.stretchy',IKSetRangeStretch+'.valueX',f=True)
        cmds.connectAttr (con+'.antiPop',IKSetRangeAntiPop+'.valueX',f=True)
        
        
        tempString= cmds.spaceLocator()
        IKmessureTmp= cmds.rename (tempString[0],name+'messureStart')
        IKmessureLoc1= setUniqueName (IKmessureTmp,'LOC')
        cmds.delete(cmds.pointConstraint (jnt[0],IKmessureLoc1,w=True))
        cmds.pointConstraint (jnt[0],IKmessureLoc1,mo=True)
        
        
        tempString= cmds.spaceLocator()
        IKmessureTmp= cmds.rename (tempString[0],name+'messureEnd')
        IKmessureLoc2= setUniqueName (IKmessureTmp,'LOC')
        cmds.pointConstraint (guide,IKmessureLoc2,w=True)
        
           
        #create distance     
        IKdistance= cmds.createNode ('distanceDimShape',n=name+'distance')
        
        tempString= cmds.group (IKmessureLoc1,IKmessureLoc2,IKdistance,n=name+'messure')
        IKmessureGrp= setUniqueName (tempString,'GRP')
        cmds.parent (IKmessureGrp,'stretchy_GRP')
        
        
        cmds.connectAttr (IKmessureLoc1+'.translate',IKdistance+'.startPoint') 
        cmds.connectAttr (IKmessureLoc2+'.translate',IKdistance+'.endPoint')
        		
        IKmessureDiv= cmds.createNode ('multiplyDivide',n='IKmessureDiv')
        cmds.setAttr (IKmessureDiv+'.operation',2)
        cmds.setAttr (IKmessureDiv+'.input2X',msLenght)
        
        distance= cmds.getAttr (IKdistance+'.distance')
        IKmessureBlendAntiPop= cmds.createNode ('blendTwoAttr',n='IKmessureBlendAntiPop')
        cmds.connectAttr (IKSetRangeAntiPop+'.outValueX' ,IKmessureBlendAntiPop+'.attributesBlender')
        cmds.addAttr (IKdistance,ln='antiPop',at= 'double')
        
        IKmessureBlendReverse= cmds.createNode ('multiplyDivide',n='IKmessureBlendReverse')
        cmds.setAttr (IKmessureBlendReverse+'.input2X',1)
        cmds.connectAttr (IKmessureBlendAntiPop+'.output',IKmessureBlendReverse+'.input1X',f=True)
        
        
        
        
        cmds.setDrivenKeyframe (IKdistance+'.antiPop',itt= 'spline', ott = 'linear' ,v= msLenght ,dv= msLenght 
        ,cd= IKdistance+'.distance')

        IKdistance_antiPop=cmds.listConnections(IKdistance+'.antiPop')

        cmds.setKeyframe (IKdistance_antiPop[0],itt= "spline" ,ott= "spline" ,v= msLenght ,f= msLenght*0.1)
        cmds.setKeyframe (IKdistance_antiPop[0],itt= "spline" ,ott= "spline" ,v= msLenght*1.2 ,f= msLenght*1.2)
        cmds.setKeyframe (IKdistance_antiPop[0],itt= "linear" ,ott= "spline" ,v= msLenght ,f= msLenght*0.70 )
        
        cmds.setKeyframe (IKdistance_antiPop[0],itt= "spline" ,ott= "spline" ,v= msLenght*0.9 ,f= msLenght*0.85 )

        cmds.selectKey (IKdistance_antiPop[0])
        cmds.setInfinity (poi= 'linear')
        IKdistance_normal= cmds.duplicate (IKdistance_antiPop,n=IKdistance_antiPop[0].replace('antiPop','normal'))

        cmds.cutKey (IKdistance_normal[0],clear=True ,time= (msLenght*0.1,msLenght*0.85),float= (msLenght*0.1,msLenght*0.85),option= 'keys' ,hierarchy ='none')

        cmds.connectAttr (IKdistance+".distance",IKdistance_normal[0]+'.input',f=True)

        cmds.connectAttr (IKdistance_normal[0]+'.output',IKmessureBlendAntiPop+'.input[0]',f=True)
        cmds.connectAttr (IKdistance_antiPop[0]+'.output',IKmessureBlendAntiPop+'.input[1]',f=True)
        
        
        IKdistanceClamp= cmds.createNode ('clamp',n='IKdistanceClamp')
        
        cmds.setAttr (IKdistanceClamp+'.maxR',abs(msLenght))
        
        cmds.connectAttr (IKmessureBlendReverse+'.outputX', IKdistanceClamp+'.inputR',f=True)
        
        IKmessureBlendStretch= cmds.createNode ('blendTwoAttr',n='IKmessureBlendStretch')
        cmds.connectAttr (IKSetRangeStretch+'.outValueX',IKmessureBlendStretch+'.attributesBlender',f=True)
        cmds.connectAttr (IKdistanceClamp+'.outputR',IKmessureBlendStretch+'.input[0]',f=True)
        cmds.connectAttr (IKmessureBlendReverse+'.outputX',IKmessureBlendStretch+'.input[1]',f=True)
        cmds.connectAttr (IKmessureBlendStretch+'.output',IKmessureDiv+'.input1X',f=True)
        
        cmds.addAttr (polVec,k=True,ln='lock',at= 'double' ,min= 0 ,max= 10)
        unitConversion= cmds.createNode ('unitConversion')
        cmds.setAttr (unitConversion+'.conversionFactor',0.1)
        cmds.connectAttr (polVec+'.lock',unitConversion+'.input',f=True)
        
        
        
        #lenght average
        lenghtAverage= cmds.createNode ('plusMinusAverage',n='lenghtAverage')
        cmds.setAttr (lenghtAverage+'.operation',3)
        cmds.setAttr (lenghtAverage+'.input1D[0]',1)
        
        #lenght average
        lenghtSum= cmds.createNode ('plusMinusAverage',n='lenghtSum')
        cmds.setAttr (lenghtSum+'.input1D[0]',msLenght)
        
        '''
        if b ==1:
            cmds.connectAttr (lenghtSum+'.output1D',IKdistanceClamp+'.maxR',f=True)
        else:
            cmds.connectAttr (lenghtSum+'.output1D',IKdistanceClamp+'.minR',f=True)
        '''
            
        distanceDiv= cmds.createNode ('multiplyDivide',n='distanceDiv')
        cmds.setAttr (distanceDiv+'.operation', 2)
        cmds.connectAttr (distanceDiv+'.outputX',IKdistance_antiPop[0]+'.input',f=True)
        cmds.connectAttr (distanceDiv+'.outputX',IKdistance_normal[0]+'.input',f=True)
        
        cmds.connectAttr (IKdistance+'.distance',distanceDiv+'.input1X',f=True)
        cmds.connectAttr (lenghtAverage+'.output1D',distanceDiv+'.input2X',f=True)
        
        for i in range(len(jnt)-1):
        
            v= cmds.getAttr (jnt[i+1]+".translateX")
            eIKmessureDiv= cmds.createNode ('multiplyDivide',n='eIKmessureDiv')
            cmds.setAttr (eIKmessureDiv+'.input2X',v)
            cmds.connectAttr (IKmessureDiv+'.output.outputX',eIKmessureDiv+'.input1X',f=True)
            
            #IkLengtControl
            cmds.addAttr (con,k= 1 ,ln= 'lenght'+str(i+1) ,at='double' ,min=0,max=2,dv= 1)
            IKLenghtDiv= cmds.createNode ('multiplyDivide',n='IKLenghtDiv')
            
            cmds.connectAttr (con+'.lenght'+str(i+1),IKLenghtDiv+".input1X",f=True)
            cmds.connectAttr (IKLenghtDiv+".outputX",lenghtSum+'.input1D['+str(i)+']',f=True)
            cmds.setAttr (IKLenghtDiv+".input2X",v)
        
            #
            cmds.connectAttr (con+'.lenght'+str(i+1),lenghtAverage+'.input1D['+str(i)+']',f=True)
            
            cmds.connectAttr (IKLenghtDiv+'.outputX',eIKmessureDiv+'.input2X',f=True)
            
            #pole.lock
            PoleLockBlender= cmds.createNode ('blendTwoAttr',n='PoleLockBlender')
            cmds.connectAttr (eIKmessureDiv+".output.outputX",PoleLockBlender+".input[0]",f=True)
            cmds.connectAttr (PoleLockBlender+".output",jnt[i+1]+".translateX",f=True)
            cmds.connectAttr (unitConversion+".output",PoleLockBlender+".attributesBlender",f=True)
            eDistance= cmds.createNode ('distanceBetween',n='eDistance')
            cmds.connectAttr (polVec+".worldMatrix[0]",eDistance+'.inMatrix1',f=True)
            
            if i ==0:
                cmds.connectAttr (IKmessureLoc1+".worldMatrix[0]",eDistance+'.inMatrix2',f=True)
            else:
                cmds.connectAttr (IKmessureLoc2+'.worldMatrix[0]',eDistance+'.inMatrix2',f=True)
            
            PoleDistanceSideReverse= cmds.createNode ('unitConversion',n='PoleDistanceSideReverse')
            cmds.setAttr (PoleDistanceSideReverse+'.conversionFactor',b)
            
            #divide by Main.sy scale
            PoleLockMainScaler= cmds.createNode ('multiplyDivide',n='PoleLockMainScaler')
            cmds.setAttr (PoleLockMainScaler+'.operation',2)
            cmds.connectAttr (eDistance+'.distance', PoleLockMainScaler+".input1X",f=True)
            cmds.connectAttr (dcm+'.outputScaleX',PoleLockMainScaler+".input2X",f=True)
            cmds.connectAttr (PoleLockMainScaler+".outputX",PoleDistanceSideReverse+".input",f=True)
            
            cmds.connectAttr (PoleDistanceSideReverse+".output",PoleLockBlender+".input[1]",f=True)
        
        return
        

