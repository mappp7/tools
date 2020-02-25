import maya.cmds as cmds
import maya.mel as mel
# EYE CENTER LOC ''' eyeCenterLoc / eyeAimLoc '''
gd = 'L'

eyeCenterLoc = cmds.ls(cmds.spaceLocator(n = gd + '_eyeCenter_LOC'))[0]
# EYE AIM LOC
eyeAimLoc = cmds.ls(cmds.spaceLocator(n = gd + '_eyeAim_LOC'))[0]

cmds.move(0,0,2 ,eyeAimLoc)
cmds.parent(eyeAimLoc , eyeCenterLoc)

##                  ##
## Locator Template ##
##                  ##

# i = 갯수   
upLocList = []
upNulList = []
downLocList = []
downNulList = []
dir = gd

#grp = cmds.group(n='temp_GRP' , em = True)

num = 4# custom 
firstNul = cmds.group(n = eyeCenterLoc.replace('_LOC' , '_zero_attach_sp_NUL') , em = True)
lastNul = cmds.group(n = eyeCenterLoc.replace('_LOC' , '_last_attach_sp_NUL') , em = True)

firstLoc = cmds.spaceLocator(n = eyeCenterLoc.replace('_LOC' , '_zero_attach_LOC'))
lastLoc = cmds.spaceLocator(n = eyeCenterLoc.replace('_LOC' , '_last_attach_LOC'))

cmds.select(eyeCenterLoc , firstNul)
mel.eval('delete`parentConstraint`')
#cmds.parent (firstLoc , firstNul)

cmds.select(eyeCenterLoc , lastNul)
mel.eval('delete`parentConstraint`')
#cmds.parent (lastLoc , lastNul)

cmds.move( -1 * (num + 1) , 0 , 0 , firstLoc)
cmds.move( num + 1 , 0 , 0 , lastLoc)


for i in range(num):
    
    upNul = cmds.group(n = eyeCenterLoc.replace('_LOC' , '_up_attach{}_sp_NUL'.format(i)) , em = True)
    upLoc = cmds.spaceLocator(n = eyeCenterLoc.replace('_LOC' , '_up_attach{}_LOC'.format(i)))
    cmds.select(eyeCenterLoc , upNul)
    mel.eval('delete`parentConstraint`')
    #cmds.parent (upLoc , upNul)
    
    cmds.move( i , 2 , 0 , upLoc)
    
    upLocList.append(upLoc[0])
    upNulList.append(upNul)
    
for i in range(num):
    dwNul = cmds.group(n = eyeCenterLoc.replace('_LOC' , '_down_attach{}_sp_NUL'.format(i)) , em = True)
    dwLoc = cmds.spaceLocator(n = eyeCenterLoc.replace('_LOC' , '_down_attach{}_LOC'.format(i)))
    cmds.select(eyeCenterLoc , dwNul)
    mel.eval('delete`parentConstraint`')
    #cmds.parent (dwLoc , dwNul)
    cmds.move( i , -2 , 0 , dwLoc)

    downLocList.append(dwLoc[0])
    downNulList.append(dwNul)

attList = cmds.ls(gd + '_eyeCenter_*_attach*_LOC')
emGrp =cmds.group(n='emGroup' , em = True)
cmds.parent(attList , emGrp)
cmds.select(eyeAimLoc , emGrp)
mel.eval('delete`parentConstraint`')
allList = upLocList + downLocList + firstLoc + lastLoc

for i in range(len(allList)):
    a = allList[i].replace('_LOC' , '_sp_NUL')
    cmds.parent(allList[i] , a)
    cmds.rename(allList[i] , dir + '_eyeLid{}_LOC'.format(i+1) )
    cmds.rename(a , dir + '_eyeLid{}_space_NUL'.format(i+1) )
    
cmds.delete(emGrp)
    















# add1x pmm make ''' x1Pmm '''
x1Pmm = cmds.createNode('pointMatrixMult' , n= eyeCenterLoc.replace('_LOC','_add1X_PMM'))
cmds.connectAttr('{}.worldMatrix[0]'.format(eyeCenterLoc) , '{}.inMatrix'.format(x1Pmm) ,f = True )
cmds.setAttr('{0}.inPointX'.format(x1Pmm) , 1)
# add1x pmm make ''' x1Pmm '''
y1Pmm = cmds.createNode('pointMatrixMult' , n= eyeCenterLoc.replace('_LOC','_add1y_PMM'))
cmds.connectAttr('{}.worldMatrix[0]'.format(eyeCenterLoc) , '{}.inMatrix'.format(y1Pmm) ,f = True )
cmds.setAttr('{0}.inPointY'.format(y1Pmm) , 1)

# decompose center , aim  ''' centerDCM / aimDCM '''

centerDCM = cmds.createNode('decomposeMatrix' , n = eyeCenterLoc.replace('_LOC','_DCM') )
aimDCM = cmds.createNode('decomposeMatrix' , n = eyeAimLoc.replace('_LOC','_DCM') )

cmds.connectAttr('{}.worldMatrix[0]'.format(eyeCenterLoc),'{}.inputMatrix'.format(centerDCM) ,f = True )
cmds.connectAttr('{}.worldMatrix[0]'.format(eyeAimLoc),'{}.inputMatrix'.format(aimDCM) ,f = True )

# vector Make 
#XVec
xVec = cmds.createNode('plusMinusAverage' , n = eyeCenterLoc.replace('_LOC' , '_xVec_PMA'))
cmds.setAttr('{}.operation'.format(xVec) , 2)
cmds.connectAttr('{}.output'.format(x1Pmm),'{}.input3D[0]'.format(xVec) , f = True )
cmds.connectAttr('{}.outputTranslate'.format(centerDCM),'{}.input3D[1]'.format(xVec) , f = True )

#aimVec
aimVec = cmds.createNode('plusMinusAverage' , n = eyeCenterLoc.replace('_LOC' , '_aimVec_PMA'))
cmds.setAttr('{}.operation'.format(aimVec) , 2)
cmds.connectAttr('{}.outputTranslate'.format(aimDCM),'{}.input3D[0]'.format(aimVec) , f = True )
cmds.connectAttr('{}.outputTranslate'.format(centerDCM),'{}.input3D[1]'.format(aimVec) , f = True )

#YVec
yVec = cmds.createNode('plusMinusAverage' , n = eyeCenterLoc.replace('_LOC' , '_yVec_PMA'))
cmds.setAttr('{}.operation'.format(yVec) , 2)
cmds.connectAttr('{}.output'.format(y1Pmm),'{}.input3D[0]'.format(yVec) , f = True )
cmds.connectAttr('{}.outputTranslate'.format(centerDCM),'{}.input3D[1]'.format(yVec) , f = True )

#xDotProduct 
xDot = cmds.createNode('vectorProduct' , n = eyeCenterLoc.replace('_LOC' , '_xDot_VPD'))
cmds.connectAttr('{}.output3D'.format(xVec),'{}.input1'.format(xDot) , f = True )
cmds.connectAttr('{}.output3D'.format(aimVec),'{}.input2'.format(xDot) , f = True )

#yDotProduct 
yDot = cmds.createNode('vectorProduct' , n = eyeCenterLoc.replace('_LOC' , '_yDot_VPD'))
cmds.connectAttr('{}.output3D'.format(yVec),'{}.input1'.format(yDot) , f = True )
cmds.connectAttr('{}.output3D'.format(aimVec),'{}.input2'.format(yDot) , f = True )

#globalmultControl
xGlobalVal = cmds.createNode('multDoubleLinear' , n = gd + '_' + 'globalXvalue_MDL' )

yGlobalVal = cmds.createNode('multDoubleLinear' , n = gd + '_' +  'globalYvalue_MDL' ) 
















#### condition connect #####

dict_ = {1:'up_1_' , 2:'up_2_' ,3:'up_3_' ,4:'up_4_',5:'dn_1_',6:'dn_2_',7:'dn_3_',8:'dn_4_',9:'in_',10:'out_'}

# input con 

cmds.group(n = gd + '_eyeLidInput_CON_dontTouch' , em = True)
inputCon = gd + '_eyeLidInput_CON_dontTouch'# MAKING PROCESS

for x in dict_:
    cmds.addAttr(gd + '_eyeLidInput_CON_dontTouch' , ln = '___________'+str(x) ,at='enum',en='___________:')
    cmds.setAttr(gd + '_eyeLidInput_CON_dontTouch' + '.' + '___________'+str(x) ,e=1,keyable=1)
    
    cmds.addAttr(gd + '_eyeLidInput_CON_dontTouch', ln = dict_[x]+'X_Min' , at = 'double' , dv = 0)
    cmds.setAttr(gd + '_eyeLidInput_CON_dontTouch' + '.' + dict_[x]+'X_Min' ,e=1,keyable=1)
    cmds.addAttr(gd + '_eyeLidInput_CON_dontTouch', ln = dict_[x]+'X_Max' , at = 'double' , dv = 0)
    cmds.setAttr(gd + '_eyeLidInput_CON_dontTouch' + '.' + dict_[x]+'X_Max' ,e=1,keyable=1)
    cmds.addAttr(gd + '_eyeLidInput_CON_dontTouch', ln = dict_[x]+'Y_Min' , at = 'double' , dv = 0)
    cmds.setAttr(gd + '_eyeLidInput_CON_dontTouch' + '.' + dict_[x]+'Y_Min' ,e=1,keyable=1)
    cmds.addAttr(gd + '_eyeLidInput_CON_dontTouch', ln = dict_[x]+'Y_Max' , at = 'double' , dv = 0)
    cmds.setAttr(gd + '_eyeLidInput_CON_dontTouch' + '.' + dict_[x]+'Y_Max' ,e=1,keyable=1)
    
#dict_[1]

dir = gd
    
yVec = gd+ '_eyeCenter_yDot_VPD'
xVec = gd + '_eyeCenter_xDot_VPD'

for i in range(10):
    
    i += 1
    a = cmds.createNode('multDoubleLinear')
    b =  cmds.createNode('multDoubleLinear')
    c =  cmds.createNode('multDoubleLinear')
    d =  cmds.createNode('multDoubleLinear')
    e = cmds.createNode('condition')
    f = cmds.createNode('condition')
    
    reA = cmds.rename(a , '{0}_{1}_y_min_MDL'.format(dir , dict_[i]))
    reB = cmds.rename(b , '{0}_{1}_y_max_MDL'.format(dir , dict_[i]))
    reC = cmds.rename(c , '{0}_{1}_x_min_MDL'.format(dir , dict_[i]))
    reD = cmds.rename(d , '{0}_{1}_x_max_MDL'.format(dir , dict_[i]))
    reE = cmds.rename(e , '{0}_eyeLid{1}_y_CDT'.format(dir , str(i)))
    reF = cmds.rename(f , '{0}_eyeLid{1}_x_CDT'.format(dir , str(i)))
    
    cmds.connectAttr('{0}.outputX'.format(yVec),'{0}.input1'.format(reA) , f = 1)
    cmds.connectAttr('{0}.{1}X_Min'.format(inputCon,dict_[i]),'{0}.input2'.format(reA), f = 1)
    
    cmds.connectAttr('{0}.outputX'.format(yVec),'{0}.input1'.format(reB), f = 1)
    cmds.connectAttr('{0}.{1}X_Max'.format(inputCon,dict_[i]),'{0}.input2'.format(reB), f = 1)
    
    cmds.connectAttr('{0}.outputX'.format(xVec),'{0}.input1'.format(reC), f = 1)
    cmds.connectAttr('{0}.{1}Y_Min'.format(inputCon,dict_[i]),'{0}.input2'.format(reC), f = 1)
    
    cmds.connectAttr('{0}.outputX'.format(xVec),'{0}.input1'.format(reD), f = 1)
    cmds.connectAttr('{0}.{1}Y_Max'.format(inputCon,dict_[i]),'{0}.input2'.format(reD), f = 1)
    
    cmds.setAttr('{}.operation'.format(reE) , 2)
    cmds.setAttr('{}.operation'.format(reF) , 2)
    
    cmds.connectAttr('{0}.outputX'.format(yVec),'{0}.firstTerm'.format(reE), f = 1)
    cmds.connectAttr('{0}.output'.format(reB),'{0}.colorIfTrueR'.format(reE), f = 1)
    cmds.connectAttr('{0}.output'.format(reA),'{0}.colorIfFalseR'.format(reE), f = 1)
    
    cmds.connectAttr('{0}.outputX'.format(xVec),'{0}.firstTerm'.format(reF), f = 1)
    cmds.connectAttr('{0}.output'.format(reD),'{0}.colorIfTrueR'.format(reF), f = 1)
    cmds.connectAttr('{0}.output'.format(reC),'{0}.colorIfFalseR'.format(reF), f = 1)
    
    cmds.connectAttr('{0}_eyeLid{1}_x_CDT.outColorR'.format(dir ,str(i)),'{0}_eyeLid{1}_space_NUL.rotateY'.format(dir ,str(i)), f = 1)
   
    # create Node reverseMult 
    cn = cmds.createNode('multDoubleLinear')
    ncn = cmds.rename(cn , '{0}_eyeLid{1}_y_reverse_MDL'.format(dir , str(i)))
    
    cmds.connectAttr('{0}_eyeLid{1}_y_CDT.outColorR'.format(dir ,str(i)) , ncn + '.input1',f=1)  
    cmds.setAttr(ncn + '.input2' , -1)
      
    cmds.connectAttr(ncn + '.output' , '{0}_eyeLid{1}_space_NUL.rotateX'.format(dir ,str(i)), f = 1)
    
    
    
    
    










