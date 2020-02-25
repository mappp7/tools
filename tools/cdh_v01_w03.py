import maya.cmds as cmds
import maya.mel as mel
from util.controller import *
from util.homeNul import *

from util.getUParam import *

side = 'Z'
surfix = 'tentacle1'

#mel.eval('nurbsPlane -p 0 0 0 -ax 0 1 0 -w 24 -lr 0.04166666667 -d 3 -u 12 -v 2 -ch 1; objectMoveCommand;')
mel.eval('nurbsPlane -p 0 0 0 -ax 0 1 0 -w 24 -lr 0.04166666667 -d 3 -u 6 -v 2 -ch 1; objectMoveCommand;')
nsfName = cmds.rename( 'nurbsPlane1', side + '_' + surfix + '_NSF' )
nsfShape = cmds.listRelatives( nsfName, s=True )[0]

tentacleCurve = cmds.duplicateCurve( side + '_' + surfix + "_NSF.v[0.5]", ch=True, n=side + '_' + surfix + '_CRV' )[0]

# curve seting

moNode = pathToU( side, surfix, tentacleCurve, 25 )
outputLocator = [ i for i in moNode[0] ]
motionPathNode = [ i for i in moNode[1] ]
#print outputLocator
#print motionPathNode


cmds.delete( outputLocator, cn=True )
"""
follicleList = cmds.listConnections( nsfName + 'Shape', type='follicle' )
FL = list( set(follicleList) )
follocleShapeList = cmds.listRelatives( FL, s=True )
"""
follocleShapeList = []
# create follicle node and connections
for x in range( len(outputLocator) ):
    #create follicle
    flc = cmds.createNode( 'follicle', name=outputLocator[x].replace( 'LOC', 'FLCShape' ) )
    follocleShapeList.append( flc )

    cmds.connectAttr( '%s.outTranslate' % flc, '%s.translate' % flc[:-5] )
    cmds.connectAttr( '%s.outRotate' % flc, '%s.rotate' % flc[:-5] )
    
    cmds.connectAttr( '%s.local' % nsfShape, '%s.inputSurface' % flc )
    cmds.connectAttr( '%s.worldMatrix[0]' % nsfShape, '%s.inputWorldMatrix' % flc )
    
    cmds.setAttr( '%s.parameterV' % flc, 0.5 )
    
    
    
    #
    dcm = cmds.createNode( 'decomposeMatrix', n=outputLocator[x].replace('LOC', 'DCM') )
    cps = cmds.createNode( 'closestPointOnSurface', n=outputLocator[x].replace('LOC', 'CPS') )
    cmds.connectAttr( '%s.worldMatrix[0]' % outputLocator[x], '%s.inputMatrix' % dcm )
    cmds.connectAttr( '%s.outputTranslate' % dcm, '%s.inPosition' % cps )
    
    cmds.connectAttr( '%s.worldSpace[0]' % nsfShape, '%s.inputSurface' % cps )
    cmds.connectAttr( '%s.parameterU' % cps, '%s.parameterU' % flc, f=True )




# controller set
selectCurve = cmds.duplicate( tentacleCurve, n=tentacleCurve.replace( 'CRV', 'dupleCurve' ) )[0]
#mel.eval( 'rebuildCurve -ch 1 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 0 -kep 1 -kt 0 -s 6 -d 3 -tol 1e-06 "%s";' % selectCurve )
mel.eval( 'rebuildCurve -ch 1 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 0 -kep 1 -kt 0 -s 3 -d 3 -tol 1e-06 "%s";' % selectCurve )
curveShape = cmds.listRelatives( selectCurve, s=True )

cvNum = cmds.getAttr( '%s.cp' % selectCurve, s=True )

#cvPosition = []
nurbsBindJointList = []
conNulNameList = []
fkConNameList = []
fkConNulNameList = []
for i in range( cvNum ):
    pos = cmds.pointPosition( '%s.cv[%s]' % (selectCurve, i) )
    #print pos
    #cvPosition.append( pos )
    conName = controllerShape( side + '_IK_' + surfix + '_%s_CON' % i, 'rombus', 'red' )
    cmds.move( pos[0], pos[1], pos[2], conName )
    
    nurbsBindJoint = cmds.joint( n=conName.replace( 'CON', 'JNT' ) )
    nurbsBindJointList.append( nurbsBindJoint )
    cmds.select( cl=True )
    
    conNulName = homeNul( conName )
    conNulNameList.append( conNulName )

    
    # create FK node
    fkConName = controllerShape( side + '_FK_' + surfix + '_%s_CON' % i, 'dubleOctagon', 'blue' )
    
    if side == 'R':
        cmds.rotate( 0, 0, 180, fkConName )
    
    
    fkConNameList.append( fkConName )
    cmds.move( pos[0], pos[1], pos[2], fkConName )
    
    fkConNulName = homeNul( fkConName )
    fkConNulNameList.append( fkConNulName )    
# create FK node    
for x in range( len(fkConNulNameList[1:-2]) ):
    cmds.parent( fkConNulNameList[x+2], fkConNameList[x+1] )
    
cmds.delete( fkConNulNameList[0] )
cmds.delete( fkConNulNameList[-1] )

snapList =[ r for r in conNulNameList ]
del(snapList[1])
del(snapList[-2])
for x in range( len(fkConNulNameList[1:-1]) ):
    cmds.delete( cmds.pointConstraint( snapList[x], fkConNulNameList[1:-1][x] ) )

















    
cmds.delete( selectCurve )

"""
# controller align
for x in range( len(conNulNameList) ):
    FL = list( set(follicleList) )
    nFollicle = nearestJointsList( conNulNameList[x], FL )[0]
    cmds.delete( cmds.orientConstraint( nFollicle, conNulNameList[x] ) )
"""






# add start end controller

startConName = controllerShape( side + '_' + surfix + 'Start_CON', 'cube', 'yellow' )
startConNulName = homeNul( startConName )

cmds.delete( cmds.parentConstraint( conNulNameList[0], startConNulName )  )

endConName = controllerShape( side + '_' + surfix + 'End_CON', 'cube', 'yellow' )
endConNulName = homeNul( endConName )

cmds.delete( cmds.parentConstraint( conNulNameList[-1], endConNulName )  )

"""
cmds.parent( conNulNameList[:2], startConName )
cmds.parent( conNulNameList[-2:], endConName )
"""

 # addAttr
cmds.addAttr( startConName, at='float', dv=0, min=0, max=10, ln='stretch' )
cmds.addAttr( startConName, at='float', dv=0, min=-10, max=0, ln='squash' )
cmds.addAttr( startConName, at='float', dv=0, min=-10, max=10, ln='squashStretch', k=True )
 # create dg node
srgStretchNode = cmds.createNode( 'setRange', n='stretch_SRG' )
cmds.setAttr( "%s.maxX" % srgStretchNode, 1)
cmds.setAttr( "%s.oldMaxX" % srgStretchNode, 10)

srgSquashNode = cmds.createNode( 'setRange', n='squash_SRG' )
cmds.setAttr( "%s.maxX" % srgSquashNode, cmds.getAttr( '%s.restCurveLength' % tentacleCurve ))
cmds.setAttr( "%s.oldMinX" % srgSquashNode, -10)

rvNode = cmds.createNode( 'reverse' )

 # connectAttr
cmds.connectAttr( '%s.stretch' % startConName, '%s.valueX' % srgStretchNode )
cmds.connectAttr( '%s.outValueX' % srgStretchNode, '%s.inputX' % rvNode )
cmds.connectAttr( '%s.outputX' % rvNode, '%s.preserveLength' % tentacleCurve )

 
cmds.connectAttr( '%s.squash' % startConName, '%s.valueX' % srgSquashNode )
cmds.connectAttr( '%s.outValueX' % srgSquashNode, '%s.restCurveLength' % tentacleCurve )


cmds.connectAttr( '%s.squashStretch' % startConName, '%s.squash' % startConName )
cmds.connectAttr( '%s.squashStretch' % startConName, '%s.stretch' % startConName )






# outputLocator rotateUp
for x in range(len(motionPathNode)):
    cmds.setAttr( "%s.worldUpType" % motionPathNode[x], 2 )
    cmds.connectAttr( '%s.worldMatrix[0]' % startConName, '%s.worldUpMatrix' % motionPathNode[x] )






### attach master fk slave ik

fkSlaveList = [ startConNulName ] + conNulNameList[2:-2] + [ endConNulName ]

for x in range( len( fkSlaveList ) ):
    cmds.parentConstraint( fkConNameList[1:-1][x], fkSlaveList[x] )
    
    
    
    
    
if side == 'R':
    for x in conNulNameList[:2]:
        cmds.rotate( 0, 0, 180, x )
    for x in conNulNameList[-2:]:
        cmds.rotate( 0, 0, 180, x )    




cmds.parent( conNulNameList[:2], startConName )
cmds.parent( conNulNameList[-2:], endConName )






# arrangemrnt

cmds.group( outputLocator, n=side + '_' + surfix + '_closestPointLocator_GRP' )
controllerGRP = cmds.group( [ startConNulName ] + conNulNameList[2:-2] + [ endConNulName ] + [fkConNulNameList[1]], n=side + '_' + surfix + '_Controller_GRP' )
cmds.group( follocleShapeList, n=side + '_' + surfix + '_output_GRP' )


# global scale
if cmds.objExists( 'glovalScale_MPD' ):
    cmds.connectAttr( 'glovalScale_MPD.outputX', '%s.maxX' % srgSquashNode )
else:
    gs = cmds.createNode( 'multiplyDivide', n='glovalScale_MPD' )
    cmds.setAttr( '%s.input1X' % gs, cmds.getAttr( '%s.restCurveLength' % tentacleCurve ))
    
    cmds.connectAttr( '%s.outputX' % gs, '%s.maxX' % srgSquashNode )
    
    #########################################################################
    if cmds.objExists( 'place_CON' ):
        cmds.connectAttr( 'place_CON.initScale', '%s.input1X' % gs )
    else:
        print 'No object matches name: "place_CON"'
    #########################################################################    
    


# skin joint
skinJointList = []
for x in range(len(follocleShapeList)):
    cmds.select( cl=True )
    cmds.select( follocleShapeList[x][:-5] )
    skinJoint = cmds.joint( n=side + '_Skin_' + surfix + '_%s_JNT' % x )
    skinJointList.append( skinJoint )    
    cmds.parentConstraint( follocleShapeList[x][:-5], skinJoint )
    #cmds.scaleConstraint( follocleShapeList[x][:-5], skinJoint )
    cmds.connectAttr( '%s.scaleY' % follocleShapeList[x][:-5], '%s.scaleY' % skinJoint )
    cmds.connectAttr( '%s.scaleZ' % follocleShapeList[x][:-5], '%s.scaleZ' % skinJoint )
    
   
cmds.group( skinJointList, n=side + '_' + surfix + '_skinJoint_GRP', w=True )











# nurbsBind
cmds.skinCluster( nurbsBindJointList, nsfName, mi=2, dr=4 )










###############################################################################################################
# getUParam( pos, curve )
"""
guideCurve = lineVis( startConName, endConName, template=True )[0]

guideCurveShape = cmds.listRelatives( guideCurve, s=True )[0]

for x in range( len( conNulNameList ) ):
    
    mpt = cmds.createNode( 'motionPath' )
    guideLocator = cmds.spaceLocator( n='guide%s_LOC' % x )[0]
    cmds.connectAttr( '%s.worldSpace[0]' % guideCurveShape, '%s.geometryPath' % mpt )
    cmds.connectAttr( '%s.allCoordinates' % mpt, '%s.translate' % guideLocator )
    cmds.connectAttr( '%s.rotate' % mpt, '%s.rotate' % guideLocator )
    
    pos = cmds.xform( conNulNameList[x], ws=True, t=True, q=True )
    uValue = getUParam( pos, guideCurve )
    
    cmds.setAttr( '%s.uValue' % mpt, uValue )
    
    cmds.parentConstraint( guideLocator, conNulNameList[x], mo=True )
"""
###############################################################################################################













###  scale 

#outputLocator
#follocleShapeList

scaleConNulList = []

count = 0
while count < 25:
    stepList = outputLocator[count:count+5]
    stepfollicleList = follocleShapeList[count:count+5]
    #print stepList
    #print stepfollicleList
    
    scaleConStart = controllerShape( side + '_scale_' + surfix + 'start_%s_CON' % count, 'square', 'skyBlue' )
    scaleConNulStart = homeNul(scaleConStart)
    scaleConNulList.append(scaleConNulStart)
    scaleConEnd = controllerShape( side + '_scale_' + surfix + 'End_%s_CON' % count, 'square', 'skyBlue' )
    scaleConNulEnd = homeNul(scaleConEnd)
    scaleConNulList.append(scaleConNulEnd)
    
    cmds.parentConstraint( stepList[0], scaleConNulStart )
    cmds.parentConstraint( stepList[-1], scaleConNulEnd )
    
    
    cot = len(stepList)-1
    
    k = 1.0/cot
    i = 0
    j = 1
    for kro in range(len(stepList)):
        cmds.scaleConstraint(scaleConEnd,stepfollicleList[kro][:-5],weight =i,mo=True,skip='x')
        cmds.scaleConstraint(scaleConStart,stepfollicleList[kro][:-5],weight =j,mo=True,skip='x')
        i=i+k
        j=j-k
        
        
    count = count + 5

scaleControllerGRP = cmds.group( scaleConNulList, n=side + '_' + surfix + '_scaleController_GRP' )
cmds.parent( scaleControllerGRP, controllerGRP )


# scale controller vis set
cmds.addAttr( startConName, ln="scaleConVis", at="enum", en="off:on:", k=True )
cmds.connectAttr( '%s.scaleConVis' % startConName, '%s.visibility' % scaleControllerGRP )













# 
def increaseNum( nodeName, NodeType, starNum = 1 ):
    num = str(starNum)
    if cmds.objExists( nodeName + num + '_' + NodeType ):
        
        x = 1
        while cmds.objExists( nodeName + str(x) + '_' + NodeType ):
            x += 1
            
        num = x
        
    return num

##
def pathToU( side, surfix, curveName, divide ):
    # node name == name_CRV
    #curveSel = cmds.ls( selection = True )[0]
    curveSel = curveName
    curveShape = cmds.listRelatives( curveSel, s=True )[0]
    
    curveInfo = cmds.arclen( curveShape, ch=True )
    curveInfoNode = cmds.rename( curveInfo, curveShape.replace( 'CRVShape', 'CIF' ) )
    
    arcLength = cmds.getAttr( curveInfoNode + '.arcLength' )
    
    # addAttr
    cmds.addAttr( curveSel, ln='preserveLength', at='double', dv=1, k=True )
    cmds.addAttr( curveSel, ln ='restCurveLength', at='double', dv=arcLength, k=True )
    
    # create condition
    preserveLengthCND = cmds.createNode( 'condition', n='preserveLength%s_CND' % increaseNum( 'preserveLength', 'CND' ) )
    cmds.setAttr( '%s.operation' % preserveLengthCND, 3 )
    cmds.setAttr( '%s.colorIfTrueR' % preserveLengthCND, 1 )
    cmds.setAttr( '%s.colorIfFalseR' % preserveLengthCND, 0 )
    # connetAttr
    cmds.connectAttr( curveInfoNode + '.arcLength', preserveLengthCND + '.firstTerm' )
    cmds.connectAttr( curveSel + '.restCurveLength', preserveLengthCND + '.secondTerm' )
    
    # create multiplyDivide == mult
    preserveLengthMPD = cmds.createNode( 'multiplyDivide', n='preserveLength_MPD' )
    # connetAttr
    cmds.connectAttr( curveSel + '.preserveLength', preserveLengthMPD + '.input1X' )
    cmds.connectAttr( preserveLengthCND + '.outColorR', preserveLengthMPD + '.input2X' )
    
    # create blendTwoAttr
    preserveLengthIndexBTA = cmds.createNode( 'blendTwoAttr', n='preserveLengthIndex_BTA' )
    # connetAttr
    cmds.connectAttr( preserveLengthMPD + '.outputX', preserveLengthIndexBTA + '.attributesBlender' )
    cmds.connectAttr( curveSel + '.restCurveLength', preserveLengthIndexBTA + '.input[0]' )
    cmds.connectAttr( curveInfoNode + '.arcLength', preserveLengthIndexBTA + '.input[1]' )
    
    
    div = divide - 1
    # create multiplyDivide == divide
    lengthDivideMPD = cmds.createNode( 'multiplyDivide', n='lengthDivide_MPD' )
    cmds.setAttr( lengthDivideMPD + '.operation', 2 )
    cmds.connectAttr( preserveLengthIndexBTA + '.output', lengthDivideMPD + '.input1X' )
    cmds.setAttr( lengthDivideMPD + '.input2X', div )
    
    outputLOCList = []
    motionPathMPTList = []
    for i in range( div + 1 ):
        # create multDoubleLinear == ratio
        lengthRatioMDL = cmds.createNode( 'multDoubleLinear', n='length_Ratio%s_MDL' % i )
        cmds.connectAttr( lengthDivideMPD + '.outputX', lengthRatioMDL + '.input1' )
        if i == 0:
            cmds.setAttr( lengthRatioMDL + '.input2', i + 0.0001 )
        else:
            cmds.setAttr( lengthRatioMDL + '.input2', i )
        
        # create multiplyDivide == attr rest length divide / rest length
        restLengthDivideMPD = cmds.createNode( 'multiplyDivide', n='restLengthDivide%s_MPD' % i )
        cmds.setAttr( restLengthDivideMPD + '.operation', 2 )
        cmds.connectAttr( curveSel + '.restCurveLength', restLengthDivideMPD + '.input1X' )
        cmds.connectAttr( preserveLengthIndexBTA + '.output', restLengthDivideMPD + '.input2X' )
        
        # create multiplyDivide == ratio result divide
        ratioResultDivideMPD = cmds.createNode( 'multiplyDivide', n='ratioResultDivide%s_MPD' % i )
        cmds.setAttr( ratioResultDivideMPD + '.operation', 2 )
        cmds.connectAttr( preserveLengthIndexBTA + '.output', ratioResultDivideMPD + '.input1X' )
        cmds.connectAttr( lengthRatioMDL + '.output', ratioResultDivideMPD + '.input2X' )
        
        # create multiplyDivide == result U value
        resultUvalueMPD = cmds.createNode( 'multiplyDivide', n='resultUvalue%s_MPD' % i )
        cmds.setAttr( resultUvalueMPD + '.operation', 2 )
        cmds.connectAttr( restLengthDivideMPD + '.outputX', resultUvalueMPD + '.input1X' )
        cmds.connectAttr( ratioResultDivideMPD + '.outputX', resultUvalueMPD + '.input2X' )
        
        # create motionPathNode
        motionPathMPT = cmds.createNode( 'motionPath', n='motionPath%s_MPT' % i )
        motionPathMPTList.append( motionPathMPT )
        cmds.setAttr( motionPathMPT + '.fractionMode', True )# maya bug???
        cmds.connectAttr( resultUvalueMPD + '.outputX', motionPathMPT + '.uValue' )
        cmds.connectAttr( curveShape + '.worldSpace[0]', motionPathMPT + '.geometryPath' )
        
        # create output locator
        outputLOC = cmds.spaceLocator( n=side + '_' + surfix + '_output%s_LOC' % i )[0]
        outputLOCList.append( outputLOC )
        cmds.connectAttr( motionPathMPT + '.allCoordinates', outputLOC + '.translate' )
        cmds.connectAttr( motionPathMPT + '.rotate', outputLOC + '.rotate' )
        
    return outputLOCList, motionPathMPTList




def getDistance( pos1, pos2 ):
    distance = ( ( pos1[0] - pos2[0] ) **2 + ( pos1[1] - pos2[1] ) **2 + ( pos1[2] - pos2[2] ) **2 ) **0.5
    distance = round( distance, 4 )
    return distance
"""    
def get_dis( pos1, pos2 ):
    
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    
    distance = math.sqrt(math.pow(x2-x1, 2)
                    + math.pow(y2-y1, 2)
                    + math.pow(z2-z1, 2))
    return distance
"""

def nearestJointsList( base, objList ):
    nDisList = []
    disList = []
    for x in range( len( objList ) ):
        basePos = cmds.xform( base, ws=True, t=True, q=True )
        pos = cmds.xform( objList[x], ws=True, t=True, q=True )
        dis = getDistance( basePos, pos )
        disList.append( dis )
    for i in range( len( disList ) ):
        if len( disList ) != 0:
            disIndex = disList.index( min( disList ) )
            nDisList.append( objList[ disIndex ] )
            #print objList[ disIndex ]
            del disList[ disIndex ]
            del objList[ disIndex ]
            
    return nDisList
    

    
def lineVis( startName, endName, template = True ):
    """
    cmds.ls( sl=True )

    startName = sel[0]
    endName = sel[1]
    """
    curveName = cmds.curve( d=1, p=[(0,0,0),(0,0,0)], name = endName.replace( '_' + endName.split('_')[-1], 'GuideVis_CRV' ) )
    
    curveShape = cmds.listRelatives( curveName, s=True )[0]
    curveShapeName = cmds.rename( curveShape, '%sShape' % curveName )
    
    if template == True:
        cmds.setAttr( '%s.template' % curveShapeName, True )
    else:
        cmds.setAttr( '%s.template' % curveShapeName, False )
    
    startMMX = cmds.createNode( 'multMatrix', n=startName.replace( '_%s' % startName.split('_')[-1], 'Vis_MMX' ) )
    endDCM = cmds.createNode( 'decomposeMatrix', n=endName.replace( '_%s' % endName.split('_')[-1], 'Vis_DCM' ) )
    endMMX = cmds.createNode( 'multMatrix', n=endName.replace( '_%s' % endName.split('_')[-1], 'Vis_MMX' ) )
    startDCM = cmds.createNode( 'decomposeMatrix', n=startName.replace( '_%s' % startName.split('_')[-1], 'Vis_DCM' ) )
    
    # Connection Node
    cmds.connectAttr( '%s.worldMatrix[0]' % startName, '%s.matrixIn[0]' % startMMX )
    cmds.connectAttr( '%s.matrixSum' % startMMX, '%s.inputMatrix' % endDCM )
        
    cmds.connectAttr( '%s.worldInverseMatrix[0]' % curveName, '%s.matrixIn[1]' % startMMX )
    
    cmds.connectAttr( '%s.outputTranslate' % endDCM, '%s.controlPoints[0]' %  curveShapeName )
        
        
    cmds.connectAttr( '%s.worldMatrix[0]' % endName, '%s.matrixIn[0]' % endMMX )
    cmds.connectAttr( '%s.matrixSum' % endMMX, '%s.inputMatrix' % startDCM )
        
    cmds.connectAttr( '%s.worldInverseMatrix[0]' % curveName, '%s.matrixIn[1]' % endMMX )
    
    cmds.connectAttr( '%s.outputTranslate' % startDCM, '%s.controlPoints[1]' %  curveShapeName )

    return curveName, startMMX, endDCM, endMMX, startDCM