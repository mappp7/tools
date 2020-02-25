#############################################    propRig_EXTRA buttons    #############################################
#                                                                                                                     #
#  propRigTool                                                                                                        #
#  extra tool                                                                                                         #
#  (13. DEC. 2017)                                                                                                    #
#                                                                                                                     #
#######################################################################################################################

import maya.cmds as cmds

def selectHierarchy () :
    sel_selectHierarchy = cmds.ls(sl=1)
    cmds.select (hi=1)

def localRotationAxes (a) :
    sel_whatever = cmds.ls(sl=1)
    for d in sel_whatever :
        cmds.setAttr ("%s.displayLocalAxis" %d, a)
#def localRotationAxes_OFF () :
#    sel_whatever = cmds.ls(sl=1)
#    for e in sel_whatever :
#        cmds.toggle (localAxis=0)

def zeroOut () :
    selectJNT = cmds.ls(sl=1)
    for a in selectJNT :
        createNUL = cmds.group (em=1, n=a.replace('JNT', 'NUL'))
        cmds.parent (createNUL, a)
        cmds.makeIdentity (createNUL, t=1, r=1)
        cmds.parent (createNUL, w=1)
        cmds.parent (a, createNUL)
        cmds.makeIdentity (a, t=1, r=1)    
        cmds.setAttr ("%s.jointOrientX" %a, 0) 
        cmds.setAttr ("%s.jointOrientY" %a, 0) 
        cmds.setAttr ("%s.jointOrientZ" %a, 0)
        cmds.parent (a, w=1)
        cmds.delete (createNUL)

def center_JNT () :
    selectPLY = cmds.ls(sl=1)
    for b in selectPLY :
        bbInfo = cmds.xform(b, worldSpace=True, query=True, boundingBox=True)
        bbCT_X = (bbInfo[0] + bbInfo[3]) / 2.0 
        bbCT_Y = (bbInfo[1] + bbInfo[4]) / 2.0 
        bbCT_Z = (bbInfo[2] + bbInfo[5]) / 2.0 
        # create joint
        cmds.select (deselect=True)
        selectJNT_nameList = b.split('_')
        sepaJNT = cmds.joint (p=(bbCT_X, bbCT_Y, bbCT_Z), n=b.replace('PLY', 'JNT'))
        cmds.joint (sepaJNT, edit=True, radius = 0.5)
                
def deleteConstraint () :
    selectSomething = cmds.ls(sl=1, fl=1)
    for d in selectSomething :
        cmds.delete (d, cn=1)
        
def snap () :
    sel_snap = cmds.ls(sl=1)
    cmds.parentConstraint (sel_snap[0], sel_snap[1], mo=0)
    cmds.delete (sel_snap[1], cn=1)
    
def attachLOC () :        
    sel_something = cmds.ls(sl=1)
    cmds.select (deselect=1)
    for e in sel_something :
        sel_something_nameList = e.split('_')
        del sel_something_nameList[-1]
        sel_something_rename = '_'.join(sel_something_nameList)
        createLOC = cmds.spaceLocator (n='%s_attach_LOC' %sel_something_rename)
        cmds.parentConstraint (e, createLOC, mo=0)
        cmds.delete (createLOC, cn=1)
        
def createNUL () :
    sel = cmds.ls(sl=1)
    cmds.select (deselect=1)
    for d in sel :
        sel_nameList = d.split('_')
        del sel_nameList[-1]
        sel_reName = '_'.join(sel_nameList)
        createNUL = cmds.group (em=1, n='%s_NUL' %sel_reName)
        cmds.parentConstraint (d, createNUL, mo=0)
        sel_cn = cmds.pickWalk (d='down'); cmds.delete (sel_cn)
        cmds.parent (d, createNUL)
        
