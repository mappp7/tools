#encoding:utf-8
#==============================
# line_rig_tool
#==============================

import maya.cmds as cmds
import sys




if '/dexter/Cache_DATA/CRT/RiggingRnD/Quadruped/script' not in sys.path:
    sys.path.append ( '/dexter/Cache_DATA/CRT/RiggingRnD/Quadruped/script' )


from util.controller import *

import tuple as TP


reload( TP )


class quadrupedRigClass:
    
    def __init__(self):
        
        self.title = 'QuadrupedRigWin'
        
        if cmds.window ( self.title, q=True, ex=True ):
            cmds.deleteUI ( self.title )
        
        cmds.window ( self.title, t='Quad Rig Tool', s=0 )
        cmds.columnLayout( 'maincolumn' )

        cmds.separator ()
        
        cmds.rowColumnLayout ( nc=2, cw=[(1, 130), (2, 30)] ) 
        cmds.text ( l='   Set Tail Number : ' )
        cmds.textField ( 'tailConNum', tx='6' )

        cmds.setParent('..')   

        cmds.rowColumnLayout () 
        cmds.button ( l='Import Templete Joint', h=35, w=200, c=self.importTemplateJoint )
        cmds.separator ()
        cmds.setParent('..')      
        
        cmds.rowColumnLayout () 
        cmds.button ( l='Neck Rig', h=30, c=self.neckRigOP )
        cmds.button ( l='Spine Rig', h=30, c=self.spineRigOP )
        cmds.button ( l='Tail Rig', h=30 )

        cmds.separator()
        
        cmds.rowColumnLayout ( nc=2, cw=[(1, 100), (2, 100)] ) 
        cmds.button ( l='ForeLeg Rig (L)', h=30, c=self.L_foreLegOP )
        cmds.button ( l='ForeLeg Rig (R)', h=30, c=self.R_foreLegOP )
        cmds.setParent('..')
        
        cmds.rowColumnLayout ( nc=2, cw=[(1, 100), (2, 100)] ) 
        cmds.button ( l='HindLeg Rig (L)', h=30, c=self.L_hindLegOP )
        cmds.button ( l='HindLeg Rig (R)', h=30, c=self.R_hindLegOP )
        cmds.setParent('..')
        
        cmds.separator()
        
        cmds.rowColumnLayout () 
        cmds.button ( l='Finish Setting', h=35, w=200, c=self.finishOP )
        
        
        cmds.showWindow( self.title )
        
    
    def controlerScale(self, controlerList, scaleValue ):

        for x in controlerList:
            controlerShapeName = cmds.listRelatives ( x, s=True )[0]
            CRV_span_num = cmds. getAttr ( CRV_shape_name+'.spans' )    
            cmds.select ( x+'.cv[0:%s]' %(CRV_span_num)) 
            cmds.scale ( scale_value, scale_value, scale_value, r=1 )
            
        cmds.select ( cl=1 )
        
        
    def controlerRotate(self, controlerList, cvNum ):        
        
        for x in controlerList:
    		
    		cmds.select ( '%s.cv[0:%s]' % (x, cvNum), r=1 )
    		cmds.rotate ( 0,0,-90, os=1, ocp=1, r=1 )
    		cmds.select ( cl=1 )
    		

    def createHindLegTempJoint(self, side):
        
        jointNamelist = [ '%s_template_hip_JNT' %side, '%s_template_knee_JNT' %side, '%s_template_ankle_JNT' %side, '%s_template_ball_JNT' %side, '%s_template_toe_JNT' %side, '%s_template_toeTip_JNT' %side ]
        templateJoint = []
    
        for x in range( len(jointNamelist) ):
            eachJoint = cmds.joint ( jointNamelist[x], n=jointNamelist[x].replace( 'template', 'IK' ) )
            templateJoint.append(eachJoint)
    
        for x in range( len(templateJoint)-1 ):
            cmds.parent( templateJoint[x+1], templateJoint[x] )
    
        cmds.parent( templateJoint[0], w=True )
        cmds.select( cl=True )

    
    
    def importTemplateJoint( self, *args ):
        
        cmds.file( '/dexter/Cache_DATA/CRT/RiggingRnD/Quadruped/script/template.mb', i=True, type='mayaBinary', mergeNamespacesOnClash=False, rpr='clash', options='v=0', pr=True )



    def neckRigOP( self, *args ):
        
        import ikNeck
        ikNeck.ikNeckOP()
        
        import fkAddNeck
        fkAddNeck.fkAddNeckOP()

        import add_SS_neck
        add_SS_neck.add_SS_neckOP()
        

        
    def spineRigOP( self, *args ):
        
        import ikSpine
        ikSpine.ikSpineOP()    
        
        import fkAddSpine
        fkAddSpine.fkAddSpineOP()
        
        import add_SS_spine
        add_SS_spine.add_SS_spineOP()
        
        

    def L_foreLegOP( self, *args ):
    	
    	import L_foreLeg    
    	L_foreLeg.ForeLegOP()
        

 
    def R_foreLegOP( self, *args ):
    	
    	import R_foreLeg 
    	R_foreLeg.ForeLegOP() 
        
        
        
    def L_hindLegOP( self, *args ):
        
        self.createHindLegTempJoint('L')
        
        import L_ikHindLeg
        L_ikHindLeg.L_ikHindLegOP()
 
        import pivotToController
        pivotToController.pivotToControllerOP('L')
        
        
        
    def R_hindLegOP( self, *args ):
        
        self.createHindLegTempJoint('R')
        
        import R_ikHindLeg
        R_ikHindLeg.R_ikHindLegOP()
        
        import pivotToController
        pivotToController.pivotToControllerOP('R')
            


    def finishOP( self, *args ):
        
        ### attribute
        
        # sup con vis
        
        for x in range(4):
            cmds.addAttr ( TP.AA['PL'][x], ln='sub_con_vis', at='enum', en='off:on:' )
            cmds.setAttr ( TP.AA['PL'][x]+'.sub_con_vis', e=1, keyable=1 )
            cmds.connectAttr ( TP.AA['PL'][x]+'.sub_con_vis', TP.AA['CL'][x]+'.visibility' )
            
        
        # FK / IK switch
        for x in range(2):
            switchCon = controllerShape( TP.conVis['key'][x][0]+'_CON', 'cross', 'yellow' )
            switchNul = cmds.group ( switchCon, n=TP.conVis['key'][x][0]+'_NUL' )
        
            cmds.delete ( cmds.pointConstraint ( TP.conVis['key'][x][1], switchNul ) )
            cmds.parent( switchNul, TP.conVis['key'][x][1] )
            cmds.move( 0,0,-3, os=1, r=1 )
            
            cmds.addAttr ( switchCon, ln=TP.conVis['attr'][0], at='enum', en='off:on:' )
            cmds.setAttr ( switchCon+'.'+TP.conVis['attr'][0], e=1, keyable=1 )
            
            cmds.addAttr ( switchCon, ln=TP.conVis['attr'][1], at='enum', en='off:on:' )
            cmds.setAttr ( switchCon+'.'+TP.conVis['attr'][1], e=1, keyable=1 )
            
        
        for x in range(2):
            top_list = TP.conVis['vis'][x]
            for y in top_list:
                for z in y:
                    if len(y)==1:
                        cmds.connectAttr( conVis['key'][x][0]+'_CON.'+TP.conVis['attr'][0], z+'.visibility' )
                    else:
                        cmds.connectAttr( conVis['key'][x][0]+'_CON.'+TP.conVis['attr'][1], z+'.visibility' )
        
        
 




def openWin():
    QD = quadrupedRigClass()
    
openWin()


