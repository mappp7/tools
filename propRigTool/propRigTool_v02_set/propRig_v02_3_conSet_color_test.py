#################################################    propRig_COLOR    #################################################
#                                                                                                                     #
#  propRigTool                                                                                                        #
#  color                                                                                                              #
#  (13. DEC. 2017)                                                                                                    #
#                                                                                                                     #
#######################################################################################################################

import maya.cmds as cmds

def con_overrideColor_SET () :
    colorNumber = int(cmds.textField('colorValueTF', query=True, tx=True))
    selected_CON = cmds.ls(sl=1)
    selected_CONShapes = cmds.listRelatives (selected_CON, shapes=True)
    for colorSET in selected_CONShapes :
        cmds.setAttr ('%s.overrideEnabled' % colorSET, 1)
        cmds.setAttr ('%s.overrideColor' % colorSET, colorNumber)



                                                                                                                            
def colorSet (a) :
    colorNumber = a
    menuItem0 = cmds.menuItem (color_OBJ, q = 1, sl = 1)
    menuItem1 = cmds.menuItem (color_outline, q = 1, sl = 1)	
    if menuItem0 == True :
	sel = cmds.ls(sl=1)
        sel_children = cmds.listRelatives (sel)

	    if 'GRP' in sel[0] :
	        cmds.textField ('colorValueTF', edit=1, tx=colorNumber)
    
	    if cmds.nodeType (sel_children[0]) == 'nurbsCurve' :
		cmds.textField ('colorValueTF', edit=1, tx=colorNumber)
		selectedCON = cmds.ls(sl=1)
		selectedCON_Shape = cmds.listRelatives (selectedCON, shapes=1)
		for l in selectedCON_Shape :
		    cmds.setAttr("%s.overrideEnabled" %l, 1)
		    cmds.setAttr("%s.overrideColor" %l, colorNumber)
            
   	    if cmds.nodeType (sel_children[0]) == 'locator' :
        	cmds.textField ('colorValueTF', edit=1, tx=colorNumber)
	        selectedLOC = cmds.ls(sl=1)
	        selectedLOC_Shape = cmds.listRelatives (selectedLOC, shapes=1)
	        for u in selectedLOC_Shape :
	            cmds.setAttr("%s.overrideEnabled" %u, 1)
	            cmds.setAttr("%s.overrideColor" %u, colorNumber)
            
    	    else :
        	cmds.textField ('colorValueTF', edit=1, tx=colorNumber)

    if menuItem1 == True :
	sel = cmds.ls(sl = 1)
	cmds.setAttr('%s.useOutlinerColor' %sel, 1)
	cmds.setAttr('%s.outlinerColor' %sel, colorNumber
	
	
        
def selectionHighliting_ON () :
    cmds.modelEditor ('modelPanel4', e=1, sel=1)
    
def selectionHighliting_OFF () :
    cmds.modelEditor ('modelPanel4', e=1, sel=0)
    

        
