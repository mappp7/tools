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
        """
        self.title = 'QuadrupedRigWin'
        
        if cmds.window ( self.title, q=True, ex=True ):
            cmds.deleteUI ( self.title )
        
        cmds.window ( self.title, t='Quad Rig Tool', s=0 )
        cmds.columnLayout( 'maincolumn' )

        cmds.separator ()
        
        cmds.rowColumnLayout ( nc=2, cw=[(1, 130), (2, 30)] ) 
        cmds.text ( l='   Set Tail Number : ' )
        cmds.textField ( 'tailConNum', tx='7' )

        cmds.setParent('..')   

        cmds.rowColumnLayout () 
        cmds.button ( l='Import Templete Joint', h=35, w=200, c=self.importTemplateJoint )
        cmds.separator ()
        cmds.setParent('..')      
        
        cmds.rowColumnLayout () 
        cmds.button ( l='Neck Rig', h=30, c=self.neckRigOP )
        cmds.button ( l='Spine Rig', h=30, c=self.spineRigOP )
        cmds.button ( l='Tail Rig', h=30, c=self.tailOP )

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
        """
    
    def controlerScale(self, controlerList, scaleValue ):

        for x in controlerList:
            controlerShapeName = cmds.listRelatives ( x, s=True )[0]
            CRV_span_num = cmds. getAttr ( controlerShapeName+'.spans' )    
            cmds.select ( x+'.cv[0:%s]' %(CRV_span_num)) 
            cmds.scale ( scale_value, scale_value, scale_value, r=1 )
            
        cmds.select ( cl=1 )
        
        
    def controlerRotate(self, controlerList, x, y, z ):        
        
        for i in controlerList:
    		
    		controlerShapeName = cmds.listRelatives ( i, s=True )[0]
    		CRV_span_num = cmds. getAttr ( controlerShapeName+'.spans' ) 
    		cmds.select ( '%s.cv[0:%s]' % (i, CRV_span_num), r=1 )
    		cmds.rotate ( x, y, z, os=1, ocp=1, r=1 )
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
        
        
        
        tailJointNum = cmds.textField ( 'tailConNum', q=1, tx=1 )
        
        root_joint = cmds.joint ( p=( 0, 0, 0 ), n='C_template_tail1_JNT' )
        
        cmds.parent ( root_joint, 'templateJoint_GRP' )

        for x in range(int(tailJointNum)-1):
            cJoint = cmds.joint ( p=(0, 0, 0), n='C_template_tail%s_JNT' %(x+2) )
            pJoint = cmds.listRelatives ( p=1 )
            cmds.joint ( pJoint, e=1, zso=1, oj='xyz', sao='yup')
            cmds.select ( cJoint )
        
        cmds.select ( 'C_template_tail1_JNT', hi=1 )
        tailJointList = cmds.ls ( sl=1 )
        
        for x in tailJointList:
            cmds.setAttr ( x+'.tx', 2 )
            
        cmds.setAttr ( 'C_template_tail1_JNT.jointOrientY', 90 )
        cmds.setAttr ( 'C_template_tail1_JNT.tx', 0 )
        cmds.setAttr ( 'C_template_tail1_JNT.ty', 15 )
        cmds.setAttr ( 'C_template_tail1_JNT.tz', -11 )
        
        cmds.select ( cl=1 )
        


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



    def tailOP( self, *args ):
        
        
        import advance_tail
        
        advance_tail.tailOP()
        


    def finishOP( self, *args ):
        self.etc_set()
        self.create_skin_joint()
        
        

    def create_skin_joint( self ):
        
        tempJoint_rootList = [ 'R_template_clavicle_JNT','C_template_root_JNT','C_template_neck1_JNT','L_template_clavicle_JNT','L_template_hip_JNT','R_template_hip_JNT', 'C_template_tail1_JNT' ]
        
        for x in tempJoint_rootList:    
            
            IKJoint = x.replace( 'template', 'IK' )
            cmds.select ( IKJoint, hi=1 )
            IKJointList = cmds.ls ( sl=1 )
            
            DJointList = cmds.duplicate( x, renameChildren=1 )
            
            for y in range(len(DJointList)):
                skinJoint = cmds.rename ( DJointList[y], DJointList[y].replace('template', 'Skin')[0:-1] )
                cmds.parentConstraint ( IKJointList[y], skinJoint )
                
           
        cmds.parent('C_Skin_neck1_JNT', 'C_Skin_chest_JNT')
        cmds.parent('L_Skin_clavicle_JNT', 'C_Skin_chest_JNT')
        cmds.parent('R_Skin_clavicle_JNT', 'C_Skin_chest_JNT')
        cmds.parent('L_Skin_hip_JNT', 'C_Skin_root_JNT')
        cmds.parent('R_Skin_hip_JNT', 'C_Skin_root_JNT')
        cmds.parent('C_Skin_root_JNT', 'SkinJoint_GRP')
        cmds.parent( 'C_Skin_tail1_JNT', 'C_Skin_root_JNT' )
        
        


    def etc_set( self ):        

        ### attribute
        
        # sup con vis

        for x in range(8):
            cmds.addAttr ( TP.AA['PL'][x], ln='sub_con_vis', at='enum', en='off:on:' )
            cmds.setAttr ( TP.AA['PL'][x]+'.sub_con_vis', e=1, keyable=1 )
            cmds.connectAttr ( TP.AA['PL'][x]+'.sub_con_vis', TP.AA['CL'][x]+'.visibility' )
            
        
        # FK / IK switch
        for x in range(2):
            switchCon = controllerShape( TP.conVis['key'][x][0]+'_CON', 'cross', 'yellow' )
            switchNul = cmds.group ( switchCon, n=TP.conVis['key'][x][0]+'_NUL' )
        
            cmds.delete ( cmds.pointConstraint ( TP.conVis['key'][x][1], switchNul ) )
            cmds.parent( switchNul, TP.conVis['key'][x][1] )
            cmds.move( 5, 0, 0, ws=1, r=1 )
            
            cmds.addAttr ( switchCon, ln=TP.conVis['attr'][0], at='enum', en='off:on:' )
            cmds.setAttr ( switchCon+'.'+TP.conVis['attr'][0], e=1, keyable=1 )
            
            cmds.addAttr ( switchCon, ln=TP.conVis['attr'][1], at='enum', en='off:on:' )
            cmds.setAttr ( switchCon+'.'+TP.conVis['attr'][1], e=1, keyable=1 )
            
        
        for x in range(2):
            top_list = TP.conVis['vis'][x]
            for y in top_list:
                for z in y:
                    if len(y)==1:
                        cmds.connectAttr( TP.conVis['key'][x][0]+'_CON.'+TP.conVis['attr'][0], z+'.visibility' )
                    else:
                        cmds.connectAttr( TP.conVis['key'][x][0]+'_CON.'+TP.conVis['attr'][1], z+'.visibility' )
                        
                    cmds.setAttr ( TP.conVis['key'][x][0]+'_CON.IK_con_vis', 1 )
        
        
        ### Parent node
        
        cmds.group ( p='noneTransform_GRP', em=1, n='locator_GRP' )
        cmds.parent ( TP.noneTrans_list, 'locator_GRP' )
        cmds.parent ( TP.attach_list, 'attach_GRP' )
        cmds.parent ( TP.auxillary_list, 'auxillary_GRP' )
        cmds.parent ( TP.neck_list, 'C_neck_GRP' )
        cmds.parent ( TP.spine_list, 'C_spine_GRP' )
        cmds.parent ( TP.L_foreLeg_list, 'L_foreLeg_GRP' )
        cmds.parent ( TP.R_foreLeg_list, 'R_foreLeg_GRP' )
        cmds.parent ( TP.L_hindLeg_list, 'L_hindLeg_GRP' )
        cmds.parent ( TP.R_hindLeg_list, 'R_hindLeg_GRP' )
        cmds.parent ( TP.tail_list, 'C_tail_GRP' )
        
        cmds.delete ( TP.delete_list )
        
        cmds.select ( TP.noneTrans_list, 'templateJoint_GRP', TP.hide_list, TP.hide_list2 )
        cmds.HideSelectedObjects ()
        
        ### Rotate controler

        self.controlerRotate( TP.rotate_con_list_A, 0, 0, -90 )
        self.controlerRotate( TP.rotate_con_list_B, -90, 0, 0 )
        
        
        ### controler Color
        
        for x in TP.R_con_list:
            conShapeName = cmds.listRelatives ( x, s=1 )[0]
            cmds.setAttr ( conShapeName+'.overrideEnabled', 1 )
            cmds.setAttr ( conShapeName+'.overrideColor', 13 )
            
        for x in TP.switch_con_list:
            conShapeName = cmds.listRelatives ( x, s=1 )[0]
            cmds.setAttr ( conShapeName+'.overrideEnabled', 1 )
            cmds.setAttr ( conShapeName+'.overrideColor', 14 )

        ### controler Scale
        
        for x in TP.scale_con_list:
            scale_value = 2
            CRV_shape_name = cmds.listRelatives (x, s=1)[0]
            CRV_span_num = cmds. getAttr ( CRV_shape_name+'.spans' )    
            cmds.select ( x+'.cv[0:%s]' %(CRV_span_num)) 
            cmds.scale ( scale_value, scale_value, scale_value, r=1 )
            
        ### controler Parent 
        
        for x in range(2):
            PL = TP.parent_list['PL'][x]
            for y in TP.parent_list['CL'][x]:
                cmds.parentConstraint ( PL, y, mo=1 )
            

        
      




def openWin():
    QD = quadrupedRigClass()
    
openWin()


