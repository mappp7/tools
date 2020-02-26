#encoding:utf-8
#==============================
#
#
#==============================
import maya.cmds as cmds
import maya.mel as mel
from baseRig.util.setUniqueName import*

def setUpCurve(crv):

    res=[]

    sha= cmds.listRelatives (crv,s=1)
    span= cmds.getAttr (sha[0]+'.spans')
    deg= cmds.getAttr (sha[0]+'.degree')
    cvs=span+deg

    v=0.0
    add=1.0/cvs

    for i in range(cvs):
        inf= cmds.createNode ('pointOnCurveInfo')
        vpd= cmds.createNode ('vectorProduct')
        ffm= cmds.createNode ('fourByFourMatrix')
        dcm= cmds.createNode ('decomposeMatrix');

        cmds.setAttr (inf+'.turnOnPercentage',1)
        cmds.connectAttr (sha[0]+'.worldSpace',inf+'.inputCurve')
        cmds.setAttr (inf+'.parameter',v)
        cmds.setAttr (vpd+'.operation',2)

        tr= cmds.getAttr (inf+'.result.position')
        pos= cmds.pointPosition (sha[0]+'.cv['+str(i)+']')

        tmp= cmds.getAttr (inf+'.result.normal')

        cmds.connectAttr (inf+'.tangent',vpd+'.input1',f=True)
        cmds.connectAttr (inf+'.normal',vpd+'.input2',f=True)

        cmds.connectAttr (inf+'.tangentX',ffm+'.in00',f=True)
        cmds.connectAttr (inf+'.tangentY',ffm+'.in01',f=True)
        cmds.connectAttr (inf+'.tangentZ',ffm+'.in02',f=True)

        cmds.connectAttr (inf+'.normalX',ffm+'.in10',f=True)
        cmds.connectAttr (inf+'.normalY',ffm+'.in11',f=True)
        cmds.connectAttr (inf+'.normalZ',ffm+'.in12',f=True)

        cmds.connectAttr (vpd+'.outputX',ffm+'.in20',f=True)
        cmds.connectAttr (vpd+'.outputY',ffm+'.in21',f=True)
        cmds.connectAttr (vpd+'.outputZ',ffm+'.in22',f=True)

        cmds.connectAttr (ffm+'.output',dcm+'.inputMatrix',f=True)

        rot= cmds.getAttr (dcm+'.outputRotate')
        if '_CRV' in crv:
            buffer= crv.split('_')[0]+'_'+crv.split('_')[1]+'_'+crv.split('_')[2]

        else:
            buffer=crv

        tmp=cmds.spaceLocator (n=buffer)
        loc=setUniqueName(tmp[0],'LOC')

        mmx=cmds.createNode ('multMatrix')
        dcm=cmds.createNode ('decomposeMatrix')

        cmds.setAttr (loc+'.t',pos[0],pos[1],pos[2])
        cmds.setAttr (loc+'.r',rot[0][0],rot[0][1],rot[0][2])

        cmds.connectAttr (loc+'.worldMatrix',mmx+'.matrixIn[0]',f=True)
        cmds.connectAttr (crv+'.parentInverseMatrix',mmx+'.matrixIn[1]',f=True)

        cmds.connectAttr (mmx+'.matrixSum',dcm+'.inputMatrix',f=True)
        cmds.connectAttr (dcm+'.outputTranslate',sha[0]+'.cv['+str(i)+']',f=True)

        aim= cmds.spaceLocator (n=crv+str(i)+'Aim_LOC')
        up= cmds.spaceLocator (n=crv+str(i)+'Up_LOC')
        cmds.delete(cmds.parentConstraint (loc,aim[0],w=True))
        cmds.delete(cmds.parentConstraint (loc,up[0],w=True))

        cmds.move (1,0,0,aim[0],os=True,r=True)
        cmds.move (1,0,0,up[0],ws=True,r=True)
        cmds.delete(cmds.aimConstraint (aim[0],loc,w=True,aim=[0,1,0],u=[1,0,0],wuo=up[0],wut='object'))

        cmds.delete(aim,up)
        v=v+add

        res.append(loc)

    return res
