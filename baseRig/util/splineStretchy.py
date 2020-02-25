#encoding:utf-8
#==============================
#
#
#==============================
#st=splineStertchy()
#st.stretchy('C_IK_upBody_CON','curveShape1','C_IK_spine1_JNT','C_IK_spine2_JNT','C_IK_spine3_JNT','C_IK_chest_JNT')

import maya.cmds as cmds
import maya.mel as mel
from baseRig.util.defaultGroupNode import*

class splineStretchy():

    def __init__(self):
        z=defaultGroupNode()
        z.createGroupNode()
          
        return

    def stretchy(self,con,crv,*jnt):

        info=cmds.createNode ('curveInfo')
        mpd=cmds.createNode ('multiplyDivide')
        stretchy_rng=cmds.createNode ('setRange')
        squash_rng=cmds.createNode ('setRange')
        cmp=cmds.createNode ('clamp')
        cmds.setAttr (stretchy_rng+'.oldMaxX',10)
        cmds.setAttr (stretchy_rng+'.maxX',1)

        cmds.setAttr (squash_rng+'.oldMaxX',10)
        cmds.setAttr (squash_rng+'.maxX',0.8)
        cmds.setAttr (squash_rng+'.minX',1)


        #add 'th'
        scaleMPD = cmds.createNode( 'multiplyDivide', n='strechyScale_MPD' )
        cmds.setAttr( '%s.operation' % scaleMPD, 2 )



        #set squash/stretchy min/max value
        #stretchy
        cmds.setAttr (cmp+'.maxR',1.5)

        #set divide
        cmds.setAttr (mpd+'.operation',2)

        #add attr
        cmds.addAttr (con,k=True,ln= 'stretchy' ,at= 'double' ,min= 0 ,max =10 ,dv= 0)
        cmds.addAttr (con,k=True,ln= 'squash' ,at= 'double' ,min= 0 ,max =10 ,dv= 0)

        #quary crv shape name
        crvShape= cmds.listRelatives (crv,s=True)[0]
        #connect nodes
        cmds.connectAttr (crvShape+'.worldSpace[0]', info+'.inputCurve',f=True)
        lenght= cmds.getAttr (info+'.arcLength')

        cmds.connectAttr (info+'.arcLength', mpd+'.input1X',f=True)
        cmds.setAttr (mpd+'.input2X',lenght)

        cmds.connectAttr (con+'.stretchy',stretchy_rng+'.valueX',f=True)



        #global Scale connection
        cmds.connectAttr (stretchy_rng+'.outValueX', '%s.input1X' % scaleMPD )#cmp+'.inputR',f=True)
        cmds.connectAttr ('%s.outputX' % scaleMPD, '%s.inputR' % cmp )
        cmds.connectAttr ('place_CON.globalScale', '%s.input2X' % scaleMPD )





        cmds.connectAttr (con+'.squash',squash_rng+'.valueX',f=True)

        cmds.connectAttr (mpd+'.outputX',stretchy_rng+'.maxX',f=True)
        cmds.connectAttr (squash_rng+'.outValueX',cmp+'.minR',f=True)
        #cmds.connectAttr (stretchy_rng+'.outValueX', cmp+'.inputR',f=True)

        #connect stretchy scale
        for e in jnt:
            cmds.connectAttr (cmp+'.outputR', e+'.scaleX',f=True)

        return
