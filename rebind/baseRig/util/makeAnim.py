#  !!!usage!!!
#1. save file
#2. select CON
#3. do it 

import maya.cmds as cmds
import os




def makeAnim():
    
    
	sel = cmds.ls(sl=True)
	min = cmds.playbackOptions(q=True, min=True)
	max = cmds.playbackOptions(q=True, max=True)
	path = cmds.file(q=True,sn=True)
	namespace = path.split('/')
	chara_nameSpace = sel[0].rsplit(':')

	camPath = "/"+namespace[1]+"/"+namespace[2]+"/"+namespace[3]+"/"+namespace[4]+"/"+namespace[5]+"/"+namespace[6]+"/"+namespace[7]+"/data/anim/"
	shotName = namespace[9].split('.')
	shotPath = "/"+namespace[1]+"/"+namespace[2]+"/"+namespace[3]+"/"+namespace[4]+"/"+namespace[5]+"/"+namespace[6]+"/"+namespace[7]+"/data/anim/"+shotName[0]+"/"
	charaPath = shotPath + chara_nameSpace[0] + "/"    

	    
	lot = cmds.spaceLocator()
	#const_lot = cmds.parentConstraint(sel[1],lot, w=1)
	const = cmds.parentConstraint(sel[0], lot, w=1)
	panel = cmds.getPanel(wf=True)
	#cmds.select(dp[0], r=True)
	cmds.isolateSelect(panel, s=True)
	cmds.bakeResults(lot, sm=True, t = ( min-1, max+1 ), sb=1)
	cmds.isolateSelect(panel, s=False)
	cmds.delete(const)
	cmds.select (lot, r=True)

	if not os.path.exists(camPath): os.makedirs(camPath)
	if not os.path.exists(shotPath): os.makedirs(shotPath)
	if not os.path.exists(charaPath): os.makedirs(charaPath)
	    
	expPath = charaPath+chara_nameSpace[0]
	    
	cmds.file (expPath, f=True, options='v=0' ,type='animExport',  es=True)
	cmds.delete(lot)
	cmds.select (cl = True)

	if cmds.window('exportedAnim', q=1, ex=1) :
	    cmds.deleteUI('exportedAnim')
	cmds.window('exportedAnim')
	cmds.columnLayout(adjustableColumn=True)
	cmds.text(label="%s.anim" %expPath,fn ="fixedWidthFont"  ,h=40,w=800, align='center',bgc=[255,200,200],hl=True)
	cmds.window('exportedAnim', e=1, width=100, height=30)
	cmds.showWindow ('exportedAnim')
	    
    
    
    








    
