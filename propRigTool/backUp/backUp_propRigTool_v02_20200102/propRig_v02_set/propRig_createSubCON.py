#############################################    propRig_Create.subCON    #############################################
#                                                                                                                     #
#  propRigTool                                                                                                        #
#  Create.subCON                                                                                                      #
#  (13. DEC. 2017)                                                                                                    #
#                                                                                                                     #
#######################################################################################################################
import maya.cmds as cmds

def sort_MC_or_SC () :
    selCON_several = cmds.ls(sl=1)
    for b in selCON_several :
        selCON_several_nameList = b.split('_')
        selCON_several_nameList_search = selCON_several_nameList[-2]
        bb = selCON_several_nameList_search[:3]
        if bb.count('sub') is 0 :
            copyMainCON ()
        else :
            copySubCON ()            
            return selCON_several
        
def copyMainCON () :
    selCON_several = cmds.ls(sl=1)
    for cc in selCON_several :            
        selMainCON_copy = cmds.duplicate (cc, n=cc.replace ('CON', 'sub1_CON')); cmds.select (selMainCON_copy[0])
        subCON_several = cmds.ls(sl=1)
        cmds.setAttr ("%s.sx" %subCON_several[0], k=1, l=0)
        cmds.setAttr ("%s.sy" %subCON_several[0], k=1, l=0)
        cmds.setAttr ("%s.sz" %subCON_several[0], k=1, l=0)
        subCON_NUL_several = cmds.group(em=1, n=subCON_several[0].replace ('CON', 'NUL'))
        cmds.parent (subCON_NUL_several, cc)
        cmds.setAttr ("%s.tx" %subCON_NUL_several, 0)
        cmds.setAttr ("%s.ty" %subCON_NUL_several, 0)
        cmds.setAttr ("%s.tz" %subCON_NUL_several, 0)
        cmds.parent (subCON_several[0], subCON_NUL_several)
        cmds.setAttr ("%s.sx" %subCON_NUL_several, 0.9)
        cmds.setAttr ("%s.sy" %subCON_NUL_several, 0.9)
        cmds.setAttr ("%s.sz" %subCON_NUL_several, 0.9)
        cmds.makeIdentity (subCON_NUL_several, apply=1, s=1)
        cmds.setAttr ("%s.sx" %subCON_several[0], k=0, l=1)
        cmds.setAttr ("%s.sy" %subCON_several[0], k=0, l=1)
        cmds.setAttr ("%s.sz" %subCON_several[0], k=0, l=1)
        cmds.addAttr (cc, longName='subConVis', at='bool', k=1, defaultValue=1.0)
        cmds.connectAttr("%s.subConVis" %cc, "%s.visibility" %subCON_NUL_several)
        ''' 
        < short name >
        SCL = scaleConstraint List
        PCL = parentConstraint List
        '''
        selMainCON_connectedSCL = cmds.listConnections (cc, s=1, t="scaleConstraint")
        selMainCON_connectedPCL = cmds.listConnections (cc, s=1, t="parentConstraint")
        selPLY_List = cmds.listRelatives (selMainCON_connectedPCL, p=1)
        cmds.select (selPLY_List) 
        selPLY = cmds.ls(sl=1)
        cmds.delete (selMainCON_connectedSCL, selMainCON_connectedPCL)
        for a in range(len(selPLY)) :
            cmds.parentConstraint (subCON_several[0], selPLY[a], mo=1)
        cmds.select (deselect=1) 

def copySubCON () :
    selCON = cmds.ls(sl=1)
    secondSubCON = cmds.confirmDialog (title='Warning : You already have It', message = 'Are you sure you want to create subCON ?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No')
    if secondSubCON == "Yes" :
        for a in selCON :
            selCON_rename = cmds.rename (a, a.replace('_CON',''))
            selSubCON_copy = cmds.duplicate (selCON_rename)
            selCON_rename_back = cmds.rename (selCON_rename, '%s_CON' %selCON_rename)
            selSubCON_copy_rename = cmds.rename (selSubCON_copy[0], '%s_CON' %selSubCON_copy[0]); cmds.select (selSubCON_copy_rename)
            subCON_new = cmds.ls(sl=1)
            cmds.setAttr ("%s.sx" %subCON_new[0], k=1, l=0)
            cmds.setAttr ("%s.sy" %subCON_new[0], k=1, l=0)
            cmds.setAttr ("%s.sz" %subCON_new[0], k=1, l=0)
            subCON_new_NUL = cmds.group(em=1, n=subCON_new[0].replace ('CON', 'NUL'))
            cmds.parent (subCON_new_NUL, selCON_rename_back)
            cmds.setAttr ("%s.tx" %subCON_new_NUL, 0)
            cmds.setAttr ("%s.ty" %subCON_new_NUL, 0)
            cmds.setAttr ("%s.tz" %subCON_new_NUL, 0)
            cmds.parent (subCON_new[0], subCON_new_NUL)
            cmds.setAttr ("%s.sx" %subCON_new_NUL, 0.9)
            cmds.setAttr ("%s.sy" %subCON_new_NUL, 0.9)
            cmds.setAttr ("%s.sz" %subCON_new_NUL, 0.9)
            cmds.makeIdentity (subCON_new_NUL, apply=1, s=1)
            cmds.setAttr ("%s.sx" %subCON_new[0], k=0, l=1)
            cmds.setAttr ("%s.sy" %subCON_new[0], k=0, l=1)
            cmds.setAttr ("%s.sz" %subCON_new[0], k=0, l=1)
            cmds.addAttr (selCON_rename_back, longName='subConVis', at='bool', k=1, defaultValue=1.0)
            cmds.connectAttr ("%s.subConVis" %selCON_rename_back, "%s.visibility" %subCON_new_NUL)
            ''' 
            < short name >
            SCL = scaleConstraint List
            PCL = parentConstraint List
            '''
            selSubCON_connectedSCL = cmds.listConnections (a, s=1, t="scaleConstraint")
            selSubCON_connectedPCL = cmds.listConnections (a, s=1, t="parentConstraint")
            selPLY_List = cmds.listRelatives (selSubCON_connectedPCL, p=1)
            cmds.select (selPLY_List) 
            selPLY = cmds.ls(sl=1)
            cmds.delete (selSubCON_connectedSCL, selSubCON_connectedPCL)
            for a in range(len(selPLY)) :
                cmds.parentConstraint (subCON_new[0], selPLY[a], mo=1)
            cmds.select (deselect=1)
