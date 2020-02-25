import maya.cmds as cmds
import maya.mel as mel

def curveAttachLocator(int_):
    crv = cmds.ls(sl=1)[0]

    cont = mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1; objectMoveCommand;')
    ncont = cmds.rename(cont, 'contCore_CON')
    
    cmds.addAttr(ncont , longName = 'stretch', at = 'double' , dv = 0 )
    cmds.setAttr(ncont+'.stretch' ,e=1 , keyable = True)
    
    if not cmds.pluginInfo( 'curveLength2ParamU', q=True, l=True ):
        cmds.loadPlugin( 'curveLength2ParamU' )
 
    x=int_
    lenLoc = int(x)
    ci = cmds.createNode('curveInfo')
    cmds.connectAttr(crv+'.worldSpace[0]' , ci+'.inputCurve',f=1)
    garc = cmds.getAttr(ci+'.arcLength')
    
    def calculCrv(lengDivi , int):
        mpd = cmds.createNode('multiplyDivide')
        cmds.connectAttr(ci+'.arcLength' , mpd+'.input1X' ,f=1 )
        cmds.setAttr(mpd+'.input2X' , lengDivi)
        cmds.setAttr(mpd+'.operation' , 2)
        mpd2 = cmds.createNode('multiplyDivide')
        cmds.connectAttr(mpd+'.outputX' , mpd2+'.input1X' ,f=1 )
        cmds.setAttr(mpd2+'.input2X' , int)
        
        rmv = cmds.createNode('remapValue')
        cmds.connectAttr(mpd2 + '.outputX' , rmv + '.outputMax',f=1)
        cmds.setAttr(rmv+'.outputMin' , cmds.getAttr(mpd2 + '.outputX'))
        cmds.connectAttr('contCore_CON.stretch',rmv + '.inputValue',f=1)
        
        clp = cmds.createNode('curveLength2ParamU')
        cmds.connectAttr(crv+'.worldSpace[0]' , clp + '.inputCurve' , f=1)
        cmds.connectAttr(rmv+'.outValue' ,clp+'.inputLength',f=1)
      
        pci = cmds.createNode('pointOnCurveInfo')
        cmds.connectAttr(crv+'.worldSpace[0]',pci+'.inputCurve',f=1)
        cmds.connectAttr(clp+'.outputParamU',pci+'.parameter',f=1)
        newLoc = cmds.spaceLocator(n = 'C_attach_curve_{}_LOC'.format(int))[0]
        cmds.connectAttr(pci+'.position',newLoc+'.translate',f=1)
        
    for i in range(lenLoc):
        calculCrv(lenLoc, i)
        
    calculCrv(i+1 , i+1)
        
        
