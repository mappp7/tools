import maya.cmds as cmds


class tailRigClass:

    def greate_controler( self, CON_shape, CON_color, parent_list, name ):

        if CON_shape == 'circle':
            self.circle_NUL_list = []
            self.circle_CON_list = []

            for x in range(len(parent_list)):
                circle_CON = ( mel.eval ( 'circle -c 0 0 0 -nr 1 0 0 -sw 360 -r 2 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0 -n "%s%s_CON" ' %( name, (x+1) ) )[0] )
                circle_CONShape = cmds.listRelatives ( s=1 )[0]
                cmds.setAttr ( circle_CONShape+'.overrideEnabled', 1 )
                cmds.setAttr ( circle_CONShape+'.overrideColor', CON_color )
                self.circle_CON_list.append ( circle_CON )
    
                cmds.group ( n='%s%s_extra_NUL' % ( self.splitName, (x+1) ) )
                each_circle_NUL = cmds.group ( n='%s%s_NUL' % ( name, (x+1) ) )
                self.circle_NUL_list.append ( each_circle_NUL )    
                cmds.delete ( cmds.parentConstraint ( parent_list[x], each_circle_NUL ) )
                
            instance_circle_NUL_list = [] + self.circle_NUL_list
            instance_circle_CON_list = [] + self.circle_CON_list

            for x in range( len(parent_list)-1 ):
                cmds.parent ( instance_circle_NUL_list[-1], instance_circle_CON_list[-2] )
                del instance_circle_NUL_list[-1], instance_circle_CON_list[-1]
                
        elif CON_shape == 'sphere':
            self.sphere_NUL_list = []
            self.sphere_CON_list = []
            
            for x in range(len(parent_list)):          
                sphere_CON =  mel.eval ( '''curve -d 1 -p 0 0 1 -p 0 0.5 0.866025 -p 0 0.866025 0.5 -p 0 1 0 -p 0 0.866025 -0.5 -p 0 0.5 -0.866025 -p 0 0 -1 -p 0 -0.5 -0.866025
                                                -p 0 -0.866025 -0.5 -p 0 -1 0 -p 0 -0.866025 0.5 -p 0 -0.5 0.866025 -p 0 0 1 -p 0.707107 0 0.707107 -p 1 0 0 -p 0.707107 0 -0.707107
                                                -p 0 0 -1 -p -0.707107 0 -0.707107 -p -1 0 0 -p -0.866025 0.5 0 -p -0.5 0.866025 0 -p 0 1 0 -p 0.5 0.866025 0 -p 0.866025 0.5 0 -p 1 0 0
                                                -p 0.866025 -0.5 0 -p 0.5 -0.866025 0 -p 0 -1 0 -p -0.5 -0.866025 0 -p -0.866025 -0.5 0 -p -1 0 0 -p -0.707107 0 0.707107 -p 0 0 1
                                                -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24
                                                -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -n "%s%s_move_CON" ''' %( name, (x+1) ) )
    
                sphere_CONShape = cmds.listRelatives ( sphere_CON, s=1 )[0]
                cmds.setAttr ( sphere_CONShape+'.overrideEnabled', 1 )
                cmds.setAttr ( sphere_CONShape+'.overrideColor', CON_color )
    
                self.sphere_CON_list.append ( sphere_CON )
                cmds.group ( n='%s%s_move_extra_NUL' %( self.splitName, (x+1) ) )
                each_sphere_NUL = cmds.group ( n='%s%s_move_NUL' % ( name, (x+1) ) )
                self.sphere_NUL_list.append ( each_sphere_NUL )           

                cmds.delete ( cmds.parentConstraint ( parent_list[x], each_sphere_NUL ) )
                


    def create_joint( self, item ):

        cmds.select ( 'C_template_tail1_JNT', hi=1 )
        templateJointList = cmds.ls ( sl=1 )
        
        DJointList = cmds.duplicate( 'C_template_tail1_JNT', renameChildren=1 )

        self.joint_list = []
        
        for x in range(len(DJointList)):
            eachJoint = cmds.rename ( DJointList[x], DJointList[x].replace('template', item)[0:-1] )
            self.joint_list.append( eachJoint )

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
        
        self.LOC_NUL_list = []
        
        for x in range( self.cycle_num ):
            each_LOC = cmds.spaceLocator ( n='tail%s_LOC' %( x ) )[0]
            each_LOCShape = cmds.listRelatives ( each_LOC, s=1 )[0]
            each_LOC_GRP = cmds.group ( n='tail%s_locator_NUL' %( x ) )
            cmds.delete ( cmds.parentConstraint ( self.joint_list[x], each_LOC_GRP, mo=0 ) )
            cmds.connectAttr ( each_LOCShape+'.worldPosition', curveShape+'.controlPoints[%s]' %(x) )

            self.LOC_NUL_list.append(each_LOC_GRP)

            
        cmds.select ( self.LOC_NUL_list )
        self.LOC_NUL_GRP = cmds.group ( n='tail_curve_locator_GRP' )
        cmds.setAttr ( self.LOC_NUL_GRP+'.visibility', 0 )
        


    def upAxis_control_rig(self):
        
     
        self.up_loc_list = []
        
        for x in range( self.cycle_num ):
            each_up_LOC = cmds.spaceLocator ( n='tail%s_up_LOC' % (x+1) )[0]
            self.up_loc_list.append( each_up_LOC )
            cmds.delete ( cmds.parentConstraint ( self.sphere_CON_list[x], each_up_LOC, mo=0 ) )
            cmds.parent ( each_up_LOC, self.sphere_CON_list[x] )
        
        aim_vector = cmds.spaceLocator ( n='tail_aim_vector_LOC' )
        cmds.delete ( cmds.parentConstraint ( self.sphere_CON_list[-1], aim_vector, mo=0 ) )
        cmds.parent ( aim_vector, self.joint_list[-1] )
        cmds.select ( self.up_loc_list )
        cmds.move ( 0, 10, 0, r=1, os=1, wd=1 )
        cmds.move ( 8, 0, 0, aim_vector, r=1, os=1 )
         
        temp_joint_list = [] + self.joint_list
        del temp_joint_list[0]
        aim_parent_list = [] + temp_joint_list + aim_vector
        
        for x in range( self.cycle_num ):
            cmds.pointConstraint ( self.joint_list[x], self.Skin_joint_list[x], mo=1 )
            cmds.aimConstraint ( aim_parent_list[x], self.Skin_joint_list[x], mo=1, wut='object',  wuo=self.up_loc_list[x] )
            
            

    def create_controler(self):
         
        self.greate_controler( 'circle', 6, joint_list, 'tail' )
        self.greate_controler( 'sphere', 13, joint_list, 'tail' )
        
        for x in range( self.cycle_num ):
            cmds.parent ( self.sphere_NUL_list[x], self.circle_CON_list[x] )
            
        cmds.ikHandle ( sj=self.joint_list[0], ee=self.joint_list[-1], c=self.sel_curve, n=self.splitName+'_HDL', sol='ikSplineSolver', ccv=0, roc=0, pcv=0 )
        
        for x in range( self.cycle_num ):
            cmds.parentConstraint ( self.sphere_CON_list[x], self.LOC_NUL_list[x] )
            
            
            
def tailOP():
    IS = tailRigClass()
    IS.create_curve()
    rigJoint = IS.create_joint( 'Rig' )
    IKJoint = IS.create_joint( 'IK' )
    IS.curve_control_locator( IS.sel_curveShape )
    IS.greate_controler()

        
        
        
        
