import maya.cmds as cmds
from util.defaultGroupNode import *
from util.zeroOut import *
from util.controller import *

####### C A U T I O N #######
# check model's ahead direction. Need to ahead Z direction.
# This tool need "curveLength2ParamU" python api plug-in.

class path_rig():
    
    def __init__(self):
        
        self.disDMS = list()
        self.IKcurveAttatchLOC = list()
        self.IKcurveAttatchNUL = list()
        self.IKSubCon = list()
        self.IKSubNull = list()
        self.FKCon = list()
        self.FKNull = list()
        self.defaultGrp = defaultGroupNode()
        self.z = zeroOut()
        self.worldCON = ['place_CON','direction_CON','move_CON','root_CON']
        self.trs = ['t','r','s']
        self.xyz = ['x','y','z']
        self.XYZ = ['X','Y','Z']

    def rotateController(self,sel): # util --- control rotate 
        for i in sel:
            curveName = i
            curveShape = cmds.listRelatives( curveName, s=True )[0]
            cvNum = cmds.getAttr( '%s.spans' % curveShape ) + cmds.getAttr( '%s.degree' % curveShape )
            cmds.select( "%s.cv[0:%s]" %(curveName,cvNum))
            cmds.rotate(90,0,0,r=True,os=True)
        cmds.select(cl=True) 

    def setRigGroupStructure(self):  # util --- rig hierachy structure set
        self.defaultGrp.createGroupNode()
        tempDCM = cmds.createNode('decomposeMatrix' , n = 'transform_DCM')
        cmds.connectAttr('move_CON.worldMatrix[0]' , '%s.inputMatrix' %tempDCM)
        cmds.connectAttr('%s.outputTranslate' %tempDCM , 'transform_GRP.translate')
        cmds.connectAttr('%s.outputRotate' %tempDCM , 'transform_GRP.rotate')
        cmds.connectAttr('place_CON.globalScale' , 'transform_GRP.scaleX')
        cmds.connectAttr('place_CON.globalScale' , 'transform_GRP.scaleY')
        cmds.connectAttr('place_CON.globalScale' , 'transform_GRP.scaleZ')
        self.rotateController(self.worldCON)

    def jointsOrient(self,jnt): # util --- joint orient 
        cmds.setAttr('%s.ry' %jnt , 90)
        self.z.zeroOutJoint(jnt)

    def controllerScale(self, control, scaleValue ): # util --- controller scale modify
        controlerShapeName = cmds.listRelatives ( control, s=True )[0]
        CRV_span_num = cmds.getAttr( controlerShapeName+'.spans' ) + cmds.getAttr( controlerShapeName+'.degree' )    
        cmds.select ( control+'.cv[0:%s]' %(CRV_span_num)) 
        cmds.scale ( scaleValue, scaleValue, scaleValue, r=1 )
        cmds.select ( cl=1 )
    
    def matrixAttatch(self,parent,child,trs): # util
        temp_MMX = cmds.createNode('multMatrix' , n = parent.replace(parent.split('_')[-1],'MMX'))
        temp_DCM = cmds.createNode('decomposeMatrix' , n = parent.replace(parent.split('_')[-1],'MMX'))
        cmds.connectAttr('%s.worldMatrix[0]' %parent,'%s.matrixIn[0]' %temp_MMX)
        cmds.connectAttr('%s.matrixSum' %temp_MMX, '%s.inputMatrix' %temp_DCM)
        if 't' in trs:
            cmds.connectAttr('%s.outputTranslate' %temp_DCM , '%s.translate' %child)
        if 'r' in trs:
            cmds.connectAttr('%s.outputRotate' %temp_DCM , '%s.rotate' %child)
        if 's' in trs:
            cmds.connectAttr('%s.outputScale' %temp_DCM , '%s.scale' %child)
        cmds.connectAttr('%s.parentInverseMatrix[0]' %child  , '%s.matrixIn[1]' %temp_MMX)
        
    def getDistance(self,pos1,pos2): # util
        distance = ( (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2 + (pos1[2]-pos2[2])**2 )**0.5 
        distance = round(distance,2)
        return distance
        
    def setSkinJoints(self,divRatio):  # util
        self.skinBodySubJointList = list()
        self.skinBodyJointList = list()
        self.blendBodySubJointList = list()
        self.blendBodyJointList = list()
        self.IKBodySubJointList = list()
        self.IKBodyJointList = list()
        self.skinLengthDiv = self.disDMS / divRatio
        self.skinLengthDivList = list()
        x = 0
        count = 0
        cmds.select(cl=1)
        self.skinLengthDivList.append(count)
        while count < self.disDMS-self.skinLengthDiv:
            x = x+1
            count = count + self.skinLengthDiv
            self.skinBodyJoint = cmds.joint(n='C_Skin_body%s_JNT' %x , p = [self.endPos[0] , self.endPos[1] , self.endPos[2]+count], rad = 5 )
            self.skinBodySubJointList.append(self.skinBodyJoint)
            self.skinLengthDivList.append(count)
            cmds.select(cl=1)
        if cmds.getAttr('%s.tz' %self.skinBodySubJointList[-1]) == cmds.getAttr('%s.tz' %self.topJoint):
            cmds.delete(self.skinBodySubJointList[-1])
            del self.skinBodySubJointList[-1]
        else:
            pass 
        jointType = ['IK','Blend','Skin']
        for i in jointType:
            cmds.select([self.endJoint]+[self.topJoint],r=1)
            SEJoints = cmds.duplicate()
            cmds.rename(SEJoints[0],'C_%s_bodyEnd_JNT' %i)
            cmds.rename(SEJoints[1],'C_%s_bodyTop_JNT' %i)
            if i is not 'Skin':
                for k in range(len(self.skinBodySubJointList)):
                    dup = cmds.duplicate(self.skinBodySubJointList[k])
                    tempJNT = cmds.rename(dup,'C_%s_body%s_JNT' %(i,k+1))
                    if i == 'IK':
                        self.IKBodySubJointList.append(tempJNT)
                    if i == 'Blend':
                        self.blendBodySubJointList.append(tempJNT)
        self.skinBodyJointList = ['C_Skin_bodyEnd_JNT']+self.skinBodySubJointList+['C_Skin_bodyTop_JNT']
        self.blendBodyJointList = ['C_Blend_bodyEnd_JNT']+self.blendBodySubJointList+['C_Blend_bodyTop_JNT']
        self.IKBodyJointList = ['C_IK_bodyEnd_JNT']+self.IKBodySubJointList+['C_IK_bodyTop_JNT']
        cmds.ToggleLocalRotationAxes(cmds.select(self.skinBodyJointList,r=1))
        for i in self.IKBodyJointList:
            self.jointsOrient(i)
        for i in range(len(self.skinBodyJointList)):
            cmds.parentConstraint(self.blendBodyJointList[i],self.skinBodyJointList[i],mo=1)
            cmds.parentConstraint(self.IKBodyJointList[i],self.blendBodyJointList[i],mo=1)

    def nearestJointsList(self,basePos,objList): # util     # Recursive Funtion
        self.nDisList = list()
        disList = list()
        for x in range( len( objList ) ):
            pos = cmds.xform( objList[x], ws=True, t=True, q=True )
            dis = self.getDistance( basePos, pos )
            disList.append( dis )
        for i in range(len(disList)):
            if len( disList ) != 0:
                disIndex = disList.index( min( disList ) )
                self.nDisList.append(objList[ disIndex ])
                del disList[disIndex]
                del objList[disIndex]
            else:
                pass

    def setCustomDivJoints(self): # util set custum div joints
        self.customBodyJointsList = list()
        cmds.select('*template_body*_JNT*',r=1)
        cmds.select([self.endJoint]+[self.topJoint],tgl=1)
        self.customBodySubJointsList = cmds.ls(sl=1)
        self.nearestJointsList(self.endPos,self.customBodySubJointsList)
        for i in range(len(self.nDisList)):
            customJoint = cmds.rename(self.nDisList[i] , 'C_template_Body%s_JNT' %str(i+1))
            self.customBodyJointsList.append(customJoint)
        self.customBodyJointsList = [self.endJoint] + self.customBodyJointsList + [self.topJoint]
        cmds.select(self.customBodyJointsList , r=1)
        cmds.parent(w=1)
        self.customBodyJointsPos = list()
        for i in self.customBodyJointsList:
            jointPos = cmds.xform(i,ws=True, q=True, t=True)
            self.customBodyJointsPos.append(jointPos)
            
    def curveLenUvalue(self,obj,curve): # util   get curveLength and uValue
        self.localLengUval = list()
        tempDCM = cmds.createNode('decomposeMatrix')
        nearestNode = cmds.createNode('nearestPointOnCurve')
        arcLengthDMS = cmds.arcLengthDimension('%s.u[0]' %curve)
        curveShape = cmds.listRelatives(curve,s=1)[0]
        cmds.connectAttr('%s.worldMatrix[0]' %obj , '%s.inputMatrix' %tempDCM)
        cmds.connectAttr('%s.worldSpace[0]' %curveShape , '%s.inputCurve' %nearestNode)
        cmds.connectAttr('%s.outputTranslate' %tempDCM , '%s.inPosition' %nearestNode)
        nearParam = cmds.getAttr('%s.parameter' %nearestNode)
        cmds.setAttr('%s.uParamValue' %arcLengthDMS , nearParam)
        getLength = nearLength = cmds.getAttr('%s.arcLength' %arcLengthDMS)
        cmds.delete(tempDCM,nearestNode,arcLengthDMS)
        # print getLength
        print 'objectPosition.param = "%s"' %nearParam
        print 'objectPosition.length = "%s"' %getLength
        self.localLengUval.append(nearParam)
        self.localLengUval.append(getLength)
        
    def setStretchCurve(self): # stretch set 
        # create bodyRig curve 
        pathRig_crv = cmds.curve(p=self.customBodyJointsPos)
        self.pathBody_crv = cmds.rename(pathRig_crv ,'pathBody_CRV')
        self.pathBody_crvS = cmds.listRelatives(self.pathBody_crv , s=1)
        cmds.select(self.IKBodyJointList[-1],self.IKBodyJointList[0], r=1)
        # splineIK = self.pathIKHandle
        splineJoint = self.IKBodyJointList
        globalController = self.worldCON[0]
        # getting joint tx value
        jointXform = cmds.getAttr( '%s.translateX' %splineJoint[1] )
        # divide uValue
        curveMaxV = cmds.getAttr( '%s.maxValue' % self.pathBody_crvS[0])
        curveMinV = 0
        sumV = curveMaxV / (len(splineJoint)-1)
        valueList = [ curveMaxV ]
        while curveMinV < curveMaxV :
            valueList.insert( -1, curveMinV )
            curveMinV += sumV
        self.pathBody_CIF = cmds.createNode('curveInfo' , n = 'pathBody_CIF')
        divRatio_MPD = cmds.createNode('multiplyDivide', name='lengthDiv_MPD')
        cmds.connectAttr('%s.worldSpace[0]' %self.pathBody_crvS[0] , '%s.inputCurve' %self.pathBody_CIF)
        cmds.connectAttr('%s.arcLength' %self.pathBody_CIF, '%s.input1X' %divRatio_MPD)
        cmds.setAttr('%s.operation' % divRatio_MPD, 2 )
        cmds.setAttr('%s.input2X' %divRatio_MPD , len( splineJoint ) - 1)
        self.stCRV_loc = list()
        self.stPOCI_list = list()
        locatorShapeList = list()
        for x in range( len( splineJoint ) ):
        # create defaultSet nodes
            # create div ratio mmx 
            temp_divRatio_MPD = cmds.createNode('multiplyDivide', name='divRatio_%s_MPD' %int(x+1)) 
            cmds.setAttr('%s.input1X' %temp_divRatio_MPD  , float(x))
            # create pointOnCurveInfo
            POCI = cmds.createNode( 'pointOnCurveInfo', n = splineJoint[x].replace(splineJoint[x].split('_')[-1],'POCI')) 
            self.stPOCI_list.append(POCI)
            # create curveLength2ParamU
            LOC = cmds.spaceLocator( name='%s_LOC' % splineJoint[x].replace( 'JNT', 'stCRV' ))
            clp = cmds.createNode('curveLength2ParamU' , n = splineJoint[x].replace(splineJoint[x].split('_')[-1],'CLP')) 
            cmds.connectAttr('%s.outputX' %divRatio_MPD , '%s.input2X' %temp_divRatio_MPD)
            cmds.connectAttr('%s.worldSpace[0]' %self.pathBody_crvS[0] , '%s.inputCurve' %clp)
            cmds.connectAttr('%s.outputX'  %temp_divRatio_MPD , '%s.inputLength' %clp)
            cmds.connectAttr('%s.outputParamU' %clp , '%s.parameter' %POCI)
            cmds.connectAttr('%s.position' %POCI , '%s.translate' %LOC[0])
            self.stCRV_loc.append(LOC[0])
            LOCShape = cmds.listRelatives( LOC[0],s=1 )
            locatorShapeList.append( LOCShape[0] )
            cmds.setAttr('%s.template' % LOC[0], 1)
            cmds.connectAttr( '%s.worldSpace[0]' %self.pathBody_crvS[0], '%s.inputCurve' % POCI )
        self.tangentNormalAxisSet()
        
    def tangentNormalAxisSet(self):  # stretch locator attatch and twist setting
        # import var "self.stPOCI_list" , "stCRV_loc"
        self.upLoc_list = list()
        self.twistLoc_list = list()
        for k in self.IKBodyJointList:
            locXform = cmds.xform(k , ws=True, q=True, t=True)
            upLoc = cmds.spaceLocator(n = k.replace(k.split('_')[-1], 'upVec_LOC') , p =(locXform[0],locXform[1],locXform[2]))[0]
            cmds.CenterPivot(upLoc)
            cmds.setAttr('%s.template' % upLoc, 1)
            twistLoc = cmds.spaceLocator(n = k.replace(k.split('_')[-1], 'twist_LOC') , p =(locXform[0],locXform[1],locXform[2]))[0]
            twistLocS = cmds.listRelatives(twistLoc , s=1)[0]
            cmds.parent(twistLoc , self.stCRV_loc[self.IKBodyJointList.index(k)])
            for j in self.XYZ:
                cmds.setAttr('%s.localPosition%s' %(twistLoc,j) , 0 )
                cmds.setAttr('%s.translate%s' %(twistLoc,j) , 0 )
                cmds.setAttr('%s.rotate%s' %(twistLoc,j) , 0 )
            cmds.setAttr('%s.template' % twistLoc, 1)
            cmds.setAttr('%s.ty' %upLoc , 20)
            self.upLoc_list.append(upLoc)
            self.twistLoc_list.append(twistLoc)
        for i in self.stCRV_loc:
            cmds.tangentConstraint(self.pathBody_crv,i,wut='object',wuo='%s' %self.upLoc_list[self.stCRV_loc.index(i)])
        for i in range(len(self.twistLoc_list)):
            cmds.parentConstraint(self.twistLoc_list[i],self.IKBodyJointList[i],mo=1)
        cmds.hide('templateJoint_GRP')
        self.twistBodySet()
        self.upVecLocControlSet()

    def twistBodySet(self):  #  twist setting
        twistInput = cmds.createNode('transform' ,n='twistInput')
        for i in self.trs:
            for k in self.xyz:
                cmds.setAttr('%s.%s%s ' %(twistInput,i,k) , lock=True , keyable = False , channelBox = False)
        cmds.setAttr('%s.v' %twistInput , lock=True , keyable = False , channelBox = False)
        cmds.addAttr(twistInput , ln='twistTop' , at='double' , dv=0)
        cmds.setAttr('%s.twistTop' %twistInput , e=True , k=True)
        cmds.addAttr(twistInput , ln='twistEnd' , at='double' , dv=0)
        cmds.setAttr('%s.twistEnd' %twistInput , e=True , k=True)
        count = 0
        for i in range(len(self.twistLoc_list)): 
            twistDiv = cmds.createNode('multiplyDivide' , n=self.twistLoc_list[i].replace(self.twistLoc_list[i].split('_')[-1],'MPD'))
            twistDivRev = cmds.createNode('multiplyDivide' , n=self.twistLoc_list[i].replace(self.twistLoc_list[i].split('_')[-1],'rev_MPD'))
            mdl = cmds.createNode('multDoubleLinear',n=self.twistLoc_list[i].replace(self.twistLoc_list[i].split('_')[-1],'MDL'))
            mdlRev = cmds.createNode('multDoubleLinear',n=self.twistLoc_list[i].replace(self.twistLoc_list[i].split('_')[-1],'rev_MDL'))
            ADL = cmds.createNode('addDoubleLinear' , n=self.twistLoc_list[i].replace(self.twistLoc_list[i].split('_')[-1],'ADL'))
            cmds.setAttr('%s.operation' %twistDiv, 2)
            cmds.setAttr('%s.operation' %twistDivRev, 2)
            cmds.setAttr('%s.input1X' %twistDiv , i )
            cmds.setAttr('%s.input1X' %twistDivRev ,len(self.twistLoc_list) - count)
            cmds.setAttr('%s.input2X' %twistDiv ,len(self.twistLoc_list))
            cmds.setAttr('%s.input2X' %twistDivRev ,len(self.twistLoc_list))
            cmds.connectAttr('%s.twistTop' %twistInput , '%s.input1' %mdl)
            cmds.connectAttr('%s.twistEnd' %twistInput , '%s.input1' %mdlRev)
            cmds.connectAttr('%s.outputX' %twistDiv , '%s.input2' %mdl)
            cmds.connectAttr('%s.outputX' %twistDivRev , '%s.input2' %mdlRev)
            cmds.connectAttr('%s.output' %mdl , '%s.input1' %ADL)
            cmds.connectAttr('%s.output' %mdlRev , '%s.input2' %ADL)
            cmds.connectAttr('%s.output' %ADL , '%s.rx' %self.twistLoc_list[i])
            count = count + 1
        cmds.parent(twistInput,'twist_GRP')
        
    def upVecLocControlSet(self):  # body curve up vector setting
        self.upVecCon_list = list()
        self.upVecVisCrv = list()
        conName = 'C_IK_body_upVec_CON'
        controllerShape(conName , 'cube', 'yellow' )
        conGrp = cmds.group(conName, n = conName.replace(conName.split('_')[-1],'NUL'))
        cmds.addAttr(conName , ln='upVecVis' , min=0 , max=1 , dv=0)
        cmds.setAttr('%s.upVecVis' %conName , e=True , k=True)
        cmds.setAttr('%s.upVecVis' %conName  , 0 )
        cmds.delete(cmds.parentConstraint('C_IK_bodyTop_JNT' , conGrp , mo=0))
        cmds.setAttr('%s.ty' %conGrp, 20+float(self.customBodyJointsPos[0][1]))
        cmds.parentConstraint('move_CON',conGrp,mo=1)
        #cmds.connectAttr('place_CON.globalScale' , '%s.sx' %conGrp)
        #cmds.connectAttr('place_CON.globalScale' , '%s.sy' %conGrp)
        #cmds.connectAttr('place_CON.globalScale' , '%s.sz' %conGrp)
        for i in self.upLoc_list:
            upVecConName = i.replace(i.split('_')[-1],'CON')
            controllerShape( upVecConName, 'locator', 'skyBlue' )
            cmds.select(upVecConName,r=1)
            upVecconGrp = cmds.group(n = i.replace(i.split('_')[-1],'NUL'))
            cmds.delete(cmds.parentConstraint(i,upVecconGrp,mo=0))
            self.upVecCon_list.append(upVecConName)
            cmds.parentConstraint(upVecConName,i,mo=1)
            cmds.hide(upVecConName)
            cmds.parent(upVecconGrp ,conName)
            self.upVecVisCurveSet(self.stCRV_loc[self.upLoc_list.index(i)],i) # upvecCurveVis
            cmds.connectAttr( '%s.upVecVis' %conName ,'%s.visibility' %upVecConName)
        cmds.parent(conGrp,'IKControl_GRP')
        
    def upVecVisCurveSet(self,startName,endName): # make upVec vis curve
        crvName = cmds.curve( d=1, p=[(0,0,0),(0,0,0)], name = startName.replace( startName.split('_')[-1], 'CRV' ) )
        self.upVecVisCrv.append(crvName)
        curveShape = cmds.listRelatives( crvName, s=True )[0]
        curveShapeName = cmds.rename( curveShape, '%sShape' % crvName )
        cvNum = cmds.getAttr( '%s.spans' % curveShapeName ) + cmds.getAttr( '%s.degree' % curveShapeName )
        # Connection Node
        cmds.connectAttr( '%s.worldPosition[0]' % startName, '%s.controlPoints[0]' %  crvName )
        cmds.connectAttr( '%s.worldPosition[0]' % endName, '%s.controlPoints[1]' %  crvName )
        cmds.connectAttr( 'C_IK_body_upVec_CON.upVecVis' , '%s.visibility' %crvName)
        cmds.toggle(crvName,template=True)
        return crvName
        
    def headRigSet(self):  # head rigging 
        conName = 'C_FK_head_CON'
        controllerShape( conName, 'cube', 'yellow' )
        conSpaceGrp = cmds.group(conName , n = 'C_FK_head_space_NUL')
        conGrp = cmds.group(conSpaceGrp, n = 'C_FK_head_NUL')
        fkJnt = cmds.joint(n = 'C_FK_head_JNT')
        cmds.select(cl=1)
        blendJnt = cmds.joint(n = 'C_Blend_head_JNT')
        cmds.select(cl=1)
        skinJnt = cmds.joint(n = 'C_Skin_head_JNT')
        cmds.select(cl=1)
        cmds.parentConstraint(conName,fkJnt,mo=1)
        cmds.parentConstraint(fkJnt,blendJnt,mo=1)
        cmds.parentConstraint(blendJnt,skinJnt,mo=1)
        cmds.delete(cmds.parentConstraint('C_template_Head_JNT',conSpaceGrp,mo=0))
        
        attatch_local_NUL = cmds.createNode('transform' , n='C_FK_head_attatch_local_NUL')
        attatch_local_LOC = cmds.spaceLocator(n='C_FK_head_attatch_local_LOC')[0]
        attatch_world_NUL = cmds.createNode('transform' , n='C_FK_head_attatch_world_NUL')
        attatch_world_LOC = cmds.spaceLocator(n='C_FK_head_attatch_world_LOC')[0]
        cmds.parent(attatch_local_LOC,attatch_local_NUL)
        cmds.parent(attatch_world_LOC,attatch_world_NUL)
        cmds.delete(cmds.parentConstraint('C_Blend_bodyTop_JNT',attatch_local_NUL,mo=0))
        cmds.delete(cmds.parentConstraint('C_FK_head_CON',attatch_local_LOC,mo=0))
        cmds.delete(cmds.parentConstraint('move_CON',attatch_world_NUL,mo=0))
        cmds.delete(cmds.parentConstraint('C_FK_head_CON',attatch_world_LOC,mo=0))
        cmds.addAttr('C_FK_head_CON', ln='localSpace' , at='double' ,min=0,max=1)
        cmds.setAttr('C_FK_head_CON.localSpace' , keyable = 1 , e=1 )
        cmds.setAttr('C_FK_head_CON.localSpace' , 1)

        localIn_MMX = cmds.createNode('multMatrix' , n='C_FK_head_attatch_localIn_MMX')
        localIn_DCM = cmds.createNode('decomposeMatrix' , n='C_FK_head_attatch_localIn_DCM')
        worldIn_MMX = cmds.createNode('multMatrix' , n='C_FK_head_attatch_worldIn_MMX')
        worldIn_DCM = cmds.createNode('decomposeMatrix' , n='C_FK_head_attatch_worldIn_DCM')
        localOut_MMX = cmds.createNode('multMatrix' , n='C_FK_head_attatch_localOut_MMX')
        localOut_DCM = cmds.createNode('decomposeMatrix' , n='C_FK_head_attatch_localOut_DCM')
        worldOut_MMX = cmds.createNode('multMatrix' , n='C_FK_head_attatch_worldOut_MMX')
        worldOut_DCM = cmds.createNode('decomposeMatrix' , n='C_FK_head_attatch_worldOut_DCM')
        attatch_PBD = cmds.createNode('pairBlend' , n='C_FK_head_attatch_PBD')
        
        cmds.connectAttr('move_CON.worldMatrix[0]','%s.matrixIn[0]' %worldIn_MMX)
        cmds.connectAttr('%s.matrixSum' %worldIn_MMX, '%s.inputMatrix' %worldIn_DCM)
        cmds.connectAttr('%s.outputTranslate' %worldIn_DCM , '%s.translate' %attatch_world_NUL)
        cmds.connectAttr('%s.outputRotate' %worldIn_DCM , '%s.rotate' %attatch_world_NUL)
        cmds.connectAttr('%s.outputScale' %worldIn_DCM , '%s.scale' %attatch_world_NUL)
        cmds.connectAttr('%s.parentInverseMatrix[0]' %conSpaceGrp  , '%s.matrixIn[1]' %worldOut_MMX)
        cmds.connectAttr('%s.worldMatrix[0]' %attatch_world_LOC, '%s.matrixIn[0]' %worldOut_MMX)
        cmds.connectAttr('%s.matrixSum' %worldOut_MMX, '%s.inputMatrix' %worldOut_DCM)
        cmds.connectAttr('%s.parentInverseMatrix[0]' %attatch_world_NUL  , '%s.matrixIn[1]' %worldIn_MMX)
        cmds.connectAttr('%s.outputRotate' %worldOut_DCM , '%s.inRotate1' %attatch_PBD)
        
        cmds.connectAttr('C_IK_sub_bodyTop_CON.worldMatrix[0]' , '%s.matrixIn[0]' %localIn_MMX)
        cmds.connectAttr('%s.matrixSum' %localIn_MMX, '%s.inputMatrix' %localIn_DCM)
        cmds.connectAttr('%s.outputTranslate' %localIn_DCM , '%s.translate' %attatch_local_NUL)
        cmds.connectAttr('%s.outputRotate' %localIn_DCM , '%s.rotate' %attatch_local_NUL)
        cmds.connectAttr('%s.outputScale' %localIn_DCM , '%s.scale' %attatch_local_NUL)
        cmds.connectAttr('%s.parentInverseMatrix[0]' %conSpaceGrp  , '%s.matrixIn[1]' %localOut_MMX)
        cmds.connectAttr('%s.worldMatrix[0]' %attatch_local_LOC, '%s.matrixIn[0]' %localOut_MMX)
        cmds.connectAttr('%s.matrixSum' %localOut_MMX, '%s.inputMatrix' %localOut_DCM)
        cmds.connectAttr('%s.parentInverseMatrix[0]' %attatch_local_NUL  , '%s.matrixIn[1]' %localIn_MMX)
        cmds.connectAttr('%s.outputTranslate' %localOut_DCM , '%s.inTranslate1' %attatch_PBD)
        cmds.connectAttr('%s.outputTranslate' %localOut_DCM , '%s.inTranslate2' %attatch_PBD)
        cmds.connectAttr('%s.outputRotate' %localOut_DCM , '%s.inRotate2' %attatch_PBD)
        cmds.connectAttr('%s.outTranslate' %attatch_PBD , '%s.translate' %conSpaceGrp)
        cmds.connectAttr('%s.outRotate' %attatch_PBD , '%s.rotate' %conSpaceGrp)
        cmds.connectAttr('C_FK_head_CON.localSpace' , 'C_FK_head_attatch_PBD.weight')

        cmds.parent(fkJnt,'FKJoint_GRP')
        cmds.parent(conGrp,'FKControl_GRP')
        cmds.parent(blendJnt,'BlendJoint_GRP')
        cmds.parent(skinJnt,'SkinJoint_GRP')
        cmds.parent(attatch_local_NUL,'attach_GRP')
        cmds.parent(attatch_world_NUL,'attach_GRP')

    def IKFKcontrolSet(self):
        for i in self.customBodyJointsList:
            # IK attatch locator set
            loc = cmds.spaceLocator(n = i.replace(i.split('_')[-1],'LOC') )
            locR = loc[0].split('_') 
            locRn = cmds.rename(loc , locR[0]+'_IK_attatch_'+'%s_%s'%( locR[2], locR[3]))
            locRnS = cmds.listRelatives(locRn , s=1)
            null = cmds.group(n= locRn.replace('LOC','NUL'),r=1)
            self.IKcurveAttatchLOC.append(locRn)
            self.IKcurveAttatchNUL.append(null)
            cmds.select(null,i,r=1) 
            cmds.matchTransform(pos=1,rot=1)
            tempIndex = self.customBodyJointsList.index(i)
            cmds.connectAttr('%s.worldPosition[0]' %locRnS[0], '%s.controlPoints[%s]' %(self.pathBody_crvS[0],tempIndex))
            # Ik sub control set
            conName = locR[0]+'_IK_sub_'+'%s_%s'%(locR[2],'CON')
            controllerShape( conName, 'dubleOctagon', 'yellow' )
            self.IKSubCon.append(conName)
            self.rotateController([conName])
            conGrp = cmds.group(conName, n = conName.replace(conName.split('_')[-1],'NUL'))
            self.IKSubNull.append(conGrp)
            cmds.select(conGrp,i,r=1)
            cmds.matchTransform(pos=1,rot=1)
            self.matrixAttatch(conName,null,'trs') # matrix connection
            # Fk control set
            FKconName = locR[0]+'_FK_'+'%s_%s'%(locR[2],'CON')
            controllerShape( FKconName, 'octagon', 'skyBlue' )
            self.FKCon.append(FKconName)
            self.rotateController([FKconName])
            FKconGrp = cmds.group(FKconName, n = FKconName.replace(FKconName.split('_')[-1],'NUL'))
            self.FKNull.append(FKconGrp)
            cmds.select(FKconGrp,i,r=1)
            cmds.matchTransform(pos=1,rot=1)
            self.matrixAttatch(FKconName,conGrp,'trs') # matrix connection
            self.controllerScale(FKconName,1.5) # controller scale modify
        for i in self.FKNull:
            if self.FKNull[-1] is not i:
                cmds.parent( i, self.FKCon[self.FKNull.index(i)+1] )
        cmds.parent('C_FK_bodyTop_NUL','FKControl_GRP')
        
    def rootControlSet(self):  
        # root control set
        cmds.select('root_NUL','C_Skin_bodyTop_JNT',r=1) 
        cmds.matchTransform(pos=1,rot=1)
        self.controllerScale('root_CON',2.5) 
        root_space_NUL = cmds.createNode('transform' , n='root_space_NUL' , p='root_NUL')
        cmds.createNode('transform' , n='C_FK_bodyTop_root_NUL' , p='C_FK_bodyTop_NUL')
        cmds.parent(self.FKCon[-1],'C_FK_bodyTop_root_NUL')
        #cmds.group('C_FK_bodyTop_CON', n = 'C_FK_bodyTop_root_NUL')
        #cmds.setAttr('C_FK_bodyTop_NUL.tz' , 0)
        self.matrixAttatch('root_CON','C_FK_bodyTop_root_NUL','trs')
        cmds.parent('root_CON',root_space_NUL)
        cmds.showHidden('place_CON','direction_CON','move_CON','root_CON')
        cmds.addAttr('root_CON' , ln='twistTop' , at='double' , dv=0)
        cmds.setAttr('root_CON.twistTop' , e=True , k=True)
        cmds.addAttr('root_CON' , ln='twistEnd' , at='double' , dv=0)
        cmds.setAttr('root_CON.twistEnd' , e=True , k=True)
        cmds.connectAttr('root_CON.twistEnd','twistInput.twistEnd')
        cmds.connectAttr('root_CON.twistTop','twistInput.twistTop')

    def createPathTempJoints(self):  # command
        self.endJoint = cmds.joint(n='C_template_bodyEnd_JNT' , p=[0,0,0] , rad = 7 )
        self.topJoint = cmds.joint(n='C_template_bodyTop_JNT' , p=[0,0,12] , rad = 7 )
        for i in [self.endJoint]+[self.topJoint]:
            cmds.setAttr('%s.overrideEnabled' %i , 1)
            cmds.setAttr('%s.overrideColor' %i , 18)
        cmds.select(cl=1)
        self.headJoint = cmds.joint(n='C_template_Head_JNT' , p=[0,0,13] , rad = 10)
        cmds.setAttr('%s.overrideEnabled' %self.headJoint , 1)
        cmds.setAttr('%s.overrideColor' %self.headJoint , 17)
        self.setRigGroupStructure()
        cmds.hide('place_CON','direction_CON','move_CON','root_CON')

    def setBodyDivJoints(self,divRatio):  # command
        # set joint position and var
        self.tempBodySubJointList = list()
        self.tempBodyJointList = list()
        self.endPos = cmds.xform(self.endJoint, ws=True, q=True, t=True)
        self.toppos = cmds.xform(self.topJoint, ws=True, q=True, t=True)
        # get distance
        self.disDMS = self.getDistance(self.endPos,self.toppos)
        divNum = self.disDMS / divRatio
        x = 0
        count = 0
        cmds.select(cl=1)
        while count < self.disDMS-divNum:
            x = x+1
            count = count + divNum
            self.tempBodyJoint = cmds.joint(n='C_template_body%s_JNT' %x , p = [self.endPos[0] , self.endPos[1] , self.endPos[2]+count], rad = 5 )
            cmds.setAttr('%s.overrideEnabled' %self.tempBodyJoint , 1)
            cmds.setAttr('%s.overrideColor' %self.tempBodyJoint , 16)
            self.tempBodySubJointList.append(self.tempBodyJoint)
            cmds.select(cl=1)
        self.tempBodyJointList = [self.endJoint] + self.tempBodySubJointList + [self.topJoint]
        cmds.parent(self.tempBodyJointList,'templateJoint_GRP')
        cmds.parent('C_template_Head_JNT','templateJoint_GRP')
        if cmds.getAttr('%s.tz' %self.tempBodySubJointList[-1]) == cmds.getAttr('%s.tz' %self.topJoint):
            cmds.delete(self.tempBodySubJointList[-1]) 
            del self.tempBodySubJointList[-1]       
        else:
            pass 
    
    def pathCurveSet(self,plusLength):
        self.nearParam_list = list()
        self.getLength_list = list()
        self.pathCrv_attLoc_list = list()
        self.upPathLoc_list = list()
        
        cmds.addAttr('root_CON' , ln='run' , at='double' , dv=0)
        cmds.setAttr('root_CON.run' , e=True , k=True)
        cmds.createNode('transform' , n = 'pathSet_GRP' , p='noneTransform_GRP')
        cvStartPos = self.customBodyJointsPos[0]
        setLength = self.disDMS + plusLength
        curvePos = [0,cvStartPos[1],setLength]
        pathSet_crv = cmds.curve(p=[cvStartPos,curvePos],d=1)

        cmds.rebuildCurve(pathSet_crv,d=3,s=10)
        self.pathSet_crv = cmds.rename(pathSet_crv ,'pathSet_CRV')
        self.pathSet_crvShp = cmds.listRelatives(self.pathSet_crv, s=1)[0]
        pathSet_CIF = cmds.createNode('curveInfo', n = 'pathSet_CIF')

        for i in self.FKNull:
            nearDCM = cmds.createNode('decomposeMatrix')
            nearestNode = cmds.createNode('nearestPointOnCurve')
            arcLengthDMS = cmds.arcLengthDimension('%s.u[0]' %self.pathSet_crv)
            curveShape = cmds.listRelatives(self.pathSet_crv,s=1)[0]
            cmds.connectAttr('%s.worldMatrix[0]' %i , '%s.inputMatrix' %nearDCM)
            cmds.connectAttr('%s.worldSpace[0]' %curveShape , '%s.inputCurve' %nearestNode)
            cmds.connectAttr('%s.outputTranslate' %nearDCM , '%s.inPosition' %nearestNode)
            nearParam = cmds.getAttr('%s.parameter' %nearestNode)
            self.nearParam_list.append(nearParam)
            cmds.setAttr('%s.uParamValue' %arcLengthDMS , nearParam)
            getLength = cmds.getAttr('%s.arcLength' %arcLengthDMS)
            self.getLength_list.append(getLength)
            cmds.delete(nearDCM,nearestNode,arcLengthDMS)
            #return getLength
            print '%s.param = "%s"' %(i,nearParam)
            print '%s.length = "%s"' %(i,getLength)
            #return getLength,nearParam
            pathCrv_attLoc = cmds.spaceLocator(n = self.FKNull[self.FKNull.index(i)]+'_attatch_LOC')[0]
            self.pathCrv_attLoc_list.append(pathCrv_attLoc)
            cmds.setAttr('%s.template' % pathCrv_attLoc, 1)
            cmds.hide(pathCrv_attLoc)
            adl = cmds.createNode('addDoubleLinear' , n = pathCrv_attLoc.replace(pathCrv_attLoc.split('_')[-1],'ADL'))
            clp = cmds.createNode('curveLength2ParamU' , n = pathCrv_attLoc.replace(pathCrv_attLoc.split('_')[-1],'CLP'))
            poci = cmds.createNode('pointOnCurveInfo' ,  n = pathCrv_attLoc.replace(pathCrv_attLoc.split('_')[-1],'POCI'))
            cmds.connectAttr('root_CON.run' , '%s.input2' %adl)
            cmds.setAttr('%s.input1' %adl , getLength)
            cmds.connectAttr('%s.output' %adl , '%s.inputLength' %clp)
            cmds.connectAttr('%s.worldSpace[0]' %self.pathSet_crvShp, '%s.inputCurve' %clp)
            cmds.connectAttr('%s.worldSpace[0]' %self.pathSet_crvShp, '%s.inputCurve' %poci)
            cmds.connectAttr('%s.outputParamU' %clp , '%s.parameter' %poci)
            cmds.connectAttr('%s.position' %poci , '%s.translate' %pathCrv_attLoc)
        
        # reverse variable
        pathCrv_attLoc_list_rev_range = list()
        self.pathCrv_attLoc_list_rev = list() # pathCurve attatch Locator list reverse variable
        FKNull_rev_range = list()
        self.FKNull_rev = list() # fk null reverse variable
        for j in self.pathCrv_attLoc_list:
            pathCrv_attLoc_list_rev_range.append(self.pathCrv_attLoc_list.index(j))
        pathCrv_attLoc_list_rev_range.reverse()
        for i in pathCrv_attLoc_list_rev_range:
            self.pathCrv_attLoc_list_rev.append(self.pathCrv_attLoc_list[i])
        for j in self.FKNull:
            FKNull_rev_range.append(self.FKNull.index(j))
        FKNull_rev_range.reverse()
        for i in FKNull_rev_range:
            self.FKNull_rev.append(self.FKNull[i])

        for k in self.pathCrv_attLoc_list_rev: # controller upVec set and < pathCrv_attLoc connect to FKNull >
            locXform = cmds.xform(k , ws=True, q=True, t=True)
            upPathLoc = cmds.spaceLocator(n = k.replace(k.split('_')[-1], 'upVec_LOC') , p =(locXform[0],locXform[1],locXform[2]))[0]
            self.upPathLoc_list.append(upPathLoc)
            cmds.CenterPivot(upPathLoc)
            cmds.setAttr('%s.template' % upPathLoc, 1)
            cmds.setAttr('%s.ty' %upPathLoc , 20)
            temp_MMX = cmds.createNode('multMatrix' , n = k.replace(k.split('_')[-1],'MMX'))
            temp_DCM = cmds.createNode('decomposeMatrix' , n = k.replace(k.split('_')[-1],'DCM'))
            if self.pathCrv_attLoc_list_rev.index(k) is 0:
                cmds.connectAttr('%s.worldMatrix[0]' %k,'%s.matrixIn[0]' %temp_MMX)
                cmds.connectAttr('root_CON.worldInverseMatrix[0]','%s.matrixIn[1]' %temp_MMX)
                cmds.connectAttr('%s.matrixSum' %temp_MMX,'%s.inputMatrix' %temp_DCM)
                cmds.connectAttr('%s.outputTranslate' %temp_DCM , '%s.translate' %self.FKNull_rev[self.pathCrv_attLoc_list_rev.index(k)])
                cmds.connectAttr('%s.outputRotate' %temp_DCM , '%s.rotate' %self.FKNull_rev[self.pathCrv_attLoc_list_rev.index(k)])
            elif self.pathCrv_attLoc_list_rev.index(k) is not 0:
                cmds.connectAttr('%s.worldMatrix[0]' %k,'%s.matrixIn[0]' %temp_MMX)
                cmds.connectAttr('%s.worldInverseMatrix[0]'  %self.pathCrv_attLoc_list_rev[self.pathCrv_attLoc_list_rev.index(k)-1] ,'%s.matrixIn[1]' %temp_MMX)
                cmds.connectAttr('%s.matrixSum' %temp_MMX,'%s.inputMatrix' %temp_DCM)
                cmds.connectAttr('%s.outputTranslate' %temp_DCM , '%s.translate' %self.FKNull_rev[self.pathCrv_attLoc_list_rev.index(k)])
                cmds.connectAttr('%s.outputRotate' %temp_DCM , '%s.rotate' %self.FKNull_rev[self.pathCrv_attLoc_list_rev.index(k)])
        # IKSub_loc_list , for curveVis locator 
        self.IKSub_loc_list = list()
        for i in self.IKSubCon:
            IKSub_loc = cmds.spaceLocator(n = i.replace(i.split('_')[-1],'LOC'))[0]
            cmds.parentConstraint(i,IKSub_loc,mo=0)
            self.IKSub_loc_list.append(IKSub_loc)
            cmds.parent(IKSub_loc,'upVecVisCurve_GRP')
            cmds.toggle(IKSub_loc,template=True)
            cmds.hide(IKSub_loc)
        self.IKSub_loc_list.reverse()
        # set upvec con 
        self.upVecPathLocControlSet() 
        # tangent constraint 
        for i in self.pathCrv_attLoc_list:
            cmds.tangentConstraint(self.pathSet_crv , i , aim=[0.0,0.0,1.0] , u=[0.0,1.0,0.0], wut='object',wuo='%s' %self.upPathLoc_list[self.pathCrv_attLoc_list_rev.index(i)])
        # set root matrix
        self.addRootMatrix() 
        # set node hierachy structure
        self.setNodeHierachy_second()

    def addRootMatrix(self):
        worldInverse_move_loc = cmds.spaceLocator(n = 'move_attatchRoot_LOC')[0]
        cmds.select(worldInverse_move_loc,'root_CON',r=1) 
        cmds.matchTransform(pos=1,rot=1)
        cmds.parent(worldInverse_move_loc,'space_GRP')
        root_MMX = cmds.createNode('multMatrix' , n = 'move_attatchRoot_MMX')
        root_DCM = cmds.createNode('decomposeMatrix' , n = 'move_attatchRoot_DCM')
        cmds.connectAttr('%s.worldMatrix[0]' %self.pathCrv_attLoc_list_rev[0] , '%s.matrixIn[0]' %root_MMX)
        cmds.connectAttr('%s.matrixSum' %root_MMX , '%s.inputMatrix' %root_DCM)
        cmds.connectAttr('%s.worldInverseMatrix[0]' %worldInverse_move_loc , '%s.matrixIn[1]' %root_MMX)
        cmds.connectAttr('%s.outputTranslate' %root_DCM , 'root_space_NUL.translate' )
        cmds.parentConstraint('move_CON',worldInverse_move_loc,mo=1)
        cmds.connectAttr('%s.outputRotate' %root_DCM , 'root_space_NUL.rotate' )
        cmds.connectAttr('%s.outputScale' %root_DCM , 'root_space_NUL.scale' )

    def upVecPathLocControlSet(self):  # path curve upVector setting
        self.upVecPathCon_list = list()
        self.upVecPathVisCrv = list()
        for i in self.upPathLoc_list:
            upVecConName = i.replace(i.split('_')[-1],'CON')
            controllerShape( upVecConName, 'cube', 'skyBlue' )
            cmds.select(upVecConName,r=1)
            upVecconGrp = cmds.group(n = i.replace(i.split('_')[-1],'NUL'))
            cmds.delete(cmds.parentConstraint(i,upVecconGrp,mo=0))
            self.upVecCon_list.append(upVecConName)
            cmds.parentConstraint(upVecConName,i,mo=1)
            cmds.hide(upVecConName)
            cmds.parent(upVecconGrp ,'C_IK_body_upVec_CON')
            temp_loc = self.upVecVisCurveSet(self.IKSub_loc_list[self.upPathLoc_list.index(i)],i) # upvecCurveVis
            cmds.parent(temp_loc,'upVecVisCurve_GRP')
            cmds.connectAttr( 'C_IK_body_upVec_CON.upVecVis'  ,'%s.visibility' %upVecConName)
            self.controllerScale(upVecConName, 0.5)
        
    def makeLocOnCurve(self): # make locator on curve. it needs to select curve.
        locatorNull_list = list()
        selcv = cmds.ls(sl=True)
        selcvsh = cmds.listRelatives(s=True)[0]
        cvcot = cmds.getAttr( '%s.spans'%selcv[0])+2
        cmds.select('%s.cv[0:%s]'% (selcv[0],cvcot))
        cvlist = cmds.ls(sl=True, fl=True)
        i = 0
        for pointNumber in cvlist:
            loc = cmds.curve(p=[(0,0,0),(0.5,0,0),(-0.5,0,0),(0,0,0),(0,0,0.5),(0,0,-0.5),(0,0,0),(0,0.5,0),(0,-0.5,0)] , d=1)
            locR = cmds.rename(loc,'pathLocator_%s_CON' %int(i+1))
            locNull = cmds.group(locR, n = 'pathLocator_%s_NUL' %int(i+1))
            locatorNull_list.append(locNull)
            locsh = cmds.listRelatives(locR,s=True)[0]
            cmds.setAttr("%s.overrideEnabled" %locsh, 1)
            cmds.setAttr("%s.overrideColor" %locsh, 21)
            cvTr = cmds.xform(pointNumber,ws=True,t=True,q=True)
            cmds.setAttr("%s.translate"%locNull,cvTr[0],cvTr[1],cvTr[2])
            mtx = cmds.createNode('multMatrix')
            dmt = cmds.createNode('decomposeMatrix')
            cmds.connectAttr("%s.worldMatrix"%locsh,"%s.matrixIn[0]"%mtx)
            cmds.connectAttr("%s.worldInverseMatrix"%selcv[0],"%s.matrixIn[1]"%mtx)
            cmds.connectAttr("%s.matrixSum"%mtx, "%s.inputMatrix"%dmt)
            cmds.connectAttr('%s.outputTranslate'%dmt , '%s.controlPoints[%s]'% (selcvsh,i))
            i=i+1
        cmds.select(cl=True)
        control_GRP = cmds.createNode('transform' , n = 'pathControl_GRP')
        cmds.parent(locatorNull_list , control_GRP)
                      
    def setNodeHierachy_first(self):
        cmds.createNode('transform' , n='noneTransform_attatch_GRP', p='auxillary_GRP')
        cmds.createNode('transform' , n='upVecVisCurve_GRP' , p='noneTransform_GRP')
        cmds.parent(self.skinBodyJointList , 'SkinJoint_GRP')
        cmds.parent(self.blendBodyJointList , 'BlendJoint_GRP')
        cmds.parent(self.customBodyJointsList,'templateJoint_GRP')
        cmds.parent(self.IKBodyJointList , 'IKJoint_GRP')
        cmds.parent(self.pathBody_crv,'auxillary_GRP')
        cmds.parent(self.IKcurveAttatchNUL,'noneTransform_attatch_GRP')
        cmds.parent(self.IKSubNull,'IKControl_GRP')
        cmds.parent(self.stCRV_loc,'noneTransform_attatch_GRP')
        cmds.parent(self.upVecVisCrv,'upVecVisCurve_GRP')
        cmds.parent(self.upLoc_list , 'attach_GRP')
    
    def setNodeHierachy_second(self):
        cmds.parent(self.upPathLoc_list , 'upVecVisCurve_GRP')
        cmds.parent(self.pathCrv_attLoc_list, 'noneTransform_attatch_GRP')
        cmds.parent('pathSet_CRV' , 'pathSet_GRP')
    
    def setRig(self,skinDiv): 
        self.setCustomDivJoints() # customDiv joints set
        self.setSkinJoints(skinDiv)  # insert skin Joints Num
        self.setStretchCurve() # set stretch set
        self.IKFKcontrolSet() # ik fk control set 
        self.rootControlSet() # root control set 
        self.headRigSet() # head rig 
        self.setNodeHierachy_first()  # set node hierachy 

"""
# command
path = path_rig()
path.createPathTempJoints()
path.setBodyDivJoints(5) # insert default div joints num 
path.setRig(15) # insert skin Div 

path.pathCurveSet(30) # path set  - insert add curve length
path.makeLocOnCurve() # make con on curve / It needs to select pathCurve
"""
