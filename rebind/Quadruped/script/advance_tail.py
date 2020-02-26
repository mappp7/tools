import maya.cmds as cmds
import maya.mel as mel


class tailRigClass:

    def greate_controler( self, CON_shape, CON_color, parent_list, name ):

        if CON_shape == 'circle':
            circle_NUL_list = []
            circle_CON_list = []

            for x in range(len(parent_list)):
                circle_CON = ( mel.eval ( 'circle -c 0 0 0 -nr 1 0 0 -sw 360 -r 2 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0 -n "tail%s_CON" ' %( x+1 ) )[0] )
                circle_CONShape = cmds.listRelatives ( s=1 )[0]
                cmds.setAttr ( circle_CONShape+'.overrideEnabled', 1 )
                cmds.setAttr ( circle_CONShape+'.overrideColor', CON_color )
                circle_CON_list.append ( circle_CON )

                cmds.group ( n='tail%s_extra_NUL' % ( x+1 ) )
                each_circle_NUL = cmds.group ( n='tail%s_NUL' % ( x+1 ) )
                circle_NUL_list.append ( each_circle_NUL )
                cmds.delete ( cmds.parentConstraint ( parent_list[x], each_circle_NUL ) )

            instance_circle_NUL_list = [] + circle_NUL_list
            instance_circle_CON_list = [] + circle_CON_list

            for x in range( len(parent_list)-1 ):
                cmds.parent ( instance_circle_NUL_list[-1], instance_circle_CON_list[-2] )
                del instance_circle_NUL_list[-1], instance_circle_CON_list[-1]

            return circle_NUL_list, circle_CON_list

        elif CON_shape == 'sphere':

            sphere_NUL_list = []
            sphere_CON_list = []

            for x in range(len(parent_list)):
                sphere_CON =  mel.eval ( '''curve -d 1 -p 0 0 1 -p 0 0.5 0.866025 -p 0 0.866025 0.5 -p 0 1 0 -p 0 0.866025 -0.5 -p 0 0.5 -0.866025 -p 0 0 -1 -p 0 -0.5 -0.866025
                                                -p 0 -0.866025 -0.5 -p 0 -1 0 -p 0 -0.866025 0.5 -p 0 -0.5 0.866025 -p 0 0 1 -p 0.707107 0 0.707107 -p 1 0 0 -p 0.707107 0 -0.707107
                                                -p 0 0 -1 -p -0.707107 0 -0.707107 -p -1 0 0 -p -0.866025 0.5 0 -p -0.5 0.866025 0 -p 0 1 0 -p 0.5 0.866025 0 -p 0.866025 0.5 0 -p 1 0 0
                                                -p 0.866025 -0.5 0 -p 0.5 -0.866025 0 -p 0 -1 0 -p -0.5 -0.866025 0 -p -0.866025 -0.5 0 -p -1 0 0 -p -0.707107 0 0.707107 -p 0 0 1
                                                -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24
                                                -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -n "tail%s_move_CON" ''' %( x+1 ) )

                sphere_CONShape = cmds.listRelatives ( sphere_CON, s=1 )[0]
                sphere_CONShape = cmds.rename ( sphere_CONShape, sphere_CON+'Shape' )
                cmds.setAttr ( sphere_CONShape+'.overrideEnabled', 1 )
                cmds.setAttr ( sphere_CONShape+'.overrideColor', CON_color )

                sphere_CON_list.append ( sphere_CON )
                cmds.group ( n='tail%s_move_extra_NUL' %( x+1 ) )
                each_sphere_NUL = cmds.group ( n='tail%s_move_NUL' % ( x+1 ) )
                sphere_NUL_list.append ( each_sphere_NUL )

                cmds.delete ( cmds.parentConstraint ( parent_list[x], each_sphere_NUL ) )

            return sphere_NUL_list, sphere_CON_list




    def create_joint( self, item, sourceJoint ):

        DJointList = cmds.duplicate( 'C_%s_tail1_JNT' %(sourceJoint), renameChildren=1 )

        joint_list = []

        for x in range(len(DJointList)):
            eachJoint = cmds.rename ( DJointList[x], DJointList[x].replace( sourceJoint, item )[0:-1] )
            joint_list.append( eachJoint )

        return joint_list




    def create_IK_joint( self, num ):
        
        cmds.select ( 'C_template_tail1_JNT', hi=1 )
        joint_list = cmds.ls ( sl=1 )

        IKJointDis = cmds.getAttr ( joint_list[1]+'.translateX' )

        startZValue_list = cmds.getAttr ( joint_list[0]+'.worldMatrix' )
        startZValue = startZValue_list[-2]
        endZValue = cmds.getAttr ( joint_list[-1]+'.worldMatrix' )[-2]

        tailDis = startZValue - endZValue

        bindJointDis = IKJointDis / ( num + 1 )
        bindJointNum = int( tailDis / bindJointDis )

        joint_position = [ startZValue_list[-4], startZValue_list[-3], startZValue_list[-2] ]

        cmds.select ( cl=1 )
        root_joint = cmds.joint ( p=joint_position, n='C_IK_tail1_JNT' )

        Z_position = startZValue_list[-2]

        for x in range(bindJointNum):
    
            Z_position = Z_position - bindJointDis
            
            cJoint = cmds.joint ( p=(joint_position[0], joint_position[1], Z_position ), n='C_IK_tail%s_JNT' %(x+2) )
            pJoint = cmds.listRelatives ( p=1 )
            cmds.joint ( pJoint, e=1, zso=1, oj='xyz', sao='yup')
            cmds.select ( cJoint )

        cmds.select ( root_joint, hi=1 )
        joint_list = cmds.ls ( sl=1 )

        return joint_list




    def create_curve( self ):

        root_joint = 'C_template_tail1_JNT'
        cmds.select ( 'C_template_tail1_JNT', hi=1 )
        self.joint_list = cmds.ls ( sl=1 )
        self.cycle_num = len( self.joint_list )

        self.point_list = []

        for x in range( self.cycle_num ):
            self.point_list.append ( cmds.xform ( self.joint_list[x], q=1, ws=1, t=1 ) )

        self.sel_curve = cmds.curve ( p=self.point_list, n='tail_curve' )
        self.sel_curveShape = cmds.listRelatives ( self.sel_curve, s=1 )[0]




    def curve_control_locator( self, curveShape ):

        LOC_NUL_list = []

        for x in range( self.cycle_num ):
            each_LOC = cmds.spaceLocator ( n='tail%s_LOC' %( x ) )[0]
            each_LOCShape = cmds.listRelatives ( each_LOC, s=1 )[0]
            each_LOC_GRP = cmds.group ( n='tail%s_locator_NUL' %( x ) )
            cmds.delete ( cmds.parentConstraint ( self.joint_list[x], each_LOC_GRP, mo=0 ) )
            cmds.connectAttr ( each_LOCShape+'.worldPosition', curveShape+'.controlPoints[%s]' %(x) )

            LOC_NUL_list.append(each_LOC_GRP)


        cmds.select ( LOC_NUL_list )
        self.LOC_NUL_GRP = cmds.group ( n='tail_curve_locator_GRP' )
        cmds.setAttr ( self.LOC_NUL_GRP+'.visibility', 0 )

        return LOC_NUL_list




    def upAxis_control_rig(self, IKJoint_list, rigJoint_list, circle_list ):


        self.up_loc_list = []

        for x in range( self.cycle_num ):
            each_up_LOC = cmds.spaceLocator ( n='tail%s_up_LOC' % (x+1) )[0]
            self.up_loc_list.append( each_up_LOC )
            cmds.delete ( cmds.parentConstraint ( circle_list[1][x], each_up_LOC, mo=0 ) )
            cmds.parent ( each_up_LOC, circle_list[1][x] )

        aim_vector = cmds.spaceLocator ( n='tail_aim_vector_LOC' )
        cmds.delete ( cmds.parentConstraint ( circle_list[1][-1], aim_vector, mo=0 ) )
        cmds.parent ( aim_vector, self.joint_list[-1] )
        cmds.select ( self.up_loc_list )
        cmds.move ( 0, 10, 0, r=1, os=1, wd=1 )
        cmds.move ( 8, 0, 0, aim_vector, r=1, os=1 )

        temp_joint_list = [] + self.joint_list

        del temp_joint_list[0]
        aim_parent_list = [] + temp_joint_list + aim_vector

        for x in range( self.cycle_num ):
            cmds.pointConstraint ( IKJoint_list[x], rigJoint_list[x], mo=1 )
            cmds.aimConstraint ( aim_parent_list[x], rigJoint_list[x], mo=1, wut='object',  wuo=self.up_loc_list[x] )




def tailOP(type,jointNum):
    IS = tailRigClass()
    IS.create_curve()
    
    sel_type = type
    inter_num = jointNum
    
    

    if sel_type == 'Normal':
        IKJoint_list = IS.create_joint( 'IK', 'template' )
        rigJoint_list = IS.create_joint( 'rig', 'template' )
        SkinJoint_list = IS.create_joint( 'Skin', 'template' )
        
    else:

        IKJoint_list = IS.create_IK_joint( inter_num )
        rigJoint_list = IS.create_joint( 'rig', 'IK' )
        SkinJoint_list = IS.create_joint( 'Skin', 'rig' )
        
        for x in range( len(IKJoint_list) ):
            cmds.parentConstraint ( IKJoint_list[x], rigJoint_list[x] )
            
    
    for x in range( len(IKJoint_list) ):
        cmds.parentConstraint ( rigJoint_list[x], SkinJoint_list[x] )
            
        
    

    LOC_NUL_list = IS.curve_control_locator( IS.sel_curveShape )

    circle_list = IS.greate_controler( 'circle', 6, IS.joint_list, 'tail' )
    sphere_list = IS.greate_controler( 'sphere', 13, IS.joint_list, 'tail' )

    for x in range( IS.cycle_num ):
        cmds.parent ( sphere_list[0][x], circle_list[1][x] )
        cmds.parentConstraint ( sphere_list[1][x], LOC_NUL_list[x] )

    cmds.ikHandle ( sj=IKJoint_list[0], ee=IKJoint_list[-1], c='tail_curve', n='tail_HDL', sol='ikSplineSolver', ccv=0, roc=0, pcv=0 )

    if sel_type == 'Normal':    
        IS.upAxis_control_rig( IKJoint_list, rigJoint_list, circle_list )
        
    cmds.parent ( 'C_IK_tail1_JNT', 'C_rig_tail1_JNT', 'C_tail_GRP' )
    cmds.parentConstraint ( 'tail1_move_CON', 'C_IK_tail1_JNT' )

    cmds.select ( cl=1 )



