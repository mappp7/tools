import maya.cmds as cmds

upLoc = cmds.ls(sl=1)#upventor
c = cmds.ls(sl=1)#curve
num=30

def xfrange(start , end , step):
	i=0
	while start + i * step < end:
		yield start + i * step
		i += 1
	yield end 	

for i in c:
    ci = cmds.createNode('curveInfo')
    cs = cmds.listRelatives(i,s=1)[0]
    cmds.connectAttr(cs+'.worldSpace[0]',ci+'.inputCurve',f=1)
    clen = cmds.getAttr(ci+'.arcLength')
    clen_div = [x for x in xfrange(0,1,1.0/num)]
    pj = None
    
    for y in clen_div:
         
        mpd = cmds.createNode('multDoubleLinear')
        cmds.connectAttr(ci+'.arcLength' , mpd + '.input1',f=1)
        cmds.setAttr(mpd+'.input2',y)
        
        c2p = cmds.createNode('curveLength2ParamU')
        cmds.connectAttr(cs+'.worldSpace[0]', c2p+'.inputCurve',f=1)
        cmds.connectAttr(mpd+'.output',c2p + '.inputLength',f=1)
        
        poci = cmds.createNode('pointOnCurveInfo')
        cmds.connectAttr(cs + '.worldSpace[0]',poci + '.inputCurve' , f=1)
        cmds.connectAttr(c2p + '.outputParamU' , poci + '.parameter' , f=1)
        cmds.select(cl=1)
        j = cmds.joint(n = 'C_Skin_horse' + '%s'%y + '_JNT')
        cmds.connectAttr(poci + '.position' , j + '.translate' , f=1)
        
        if pj:
            if y < 0.5:
                up=upLoc[0]
            else:
                up=upLoc[1]
            cmds.aimConstraint(pj,j,wut = 'object',wuo=up)
        pj = j

        
        
        
    