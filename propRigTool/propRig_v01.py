import maya.cmds as cmds


import site
site.addsitedir('/dexter/Cache_DATA/CRT/riggingTeamShelf/checkTool')
import site
site.addsitedir('/dexter/Cache_DATA/CRT/riggingTeamShelf/propRigTool/propRigTool_v01_set')


import Checker_v01 as CK;		reload(CK)
import propRig_color as CL;		reload(CL)
import propRig_createCON_JNT as CJ;		reload(CJ)
import propRig_createCON_JoinBT as CJB;		reload(CJB)
import propRig_createCON_SingleBT as CSB;		reload(CSB)
import propRig_createSubCON as SC;		reload(SC)
import propRig_dxRigGRP as DX;		reload(DX)
import propRig_extraButtons as EX;		reload(EX)
import propRig_rootCON as RC;		reload(RC)







############################################    radioButton : Node Type    ############################################
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
def create_SingleCON () :
    xx = 0
    rb0 = cmds.radioButton (RButton_Constraints, q=1, sl=1)
    rb1 = cmds.radioButton (RButton_JointBinding, q=1, sl=1)
    rb2 = cmds.radioButton (RButton_None, q=1, sl=1)
    if rb0 == True :
        xx == 0
        CSB.create_CON_separate ()       
    if rb1 == True :
        xx == 1
        CJ.create_JNT_separate ()
    if rb2 == True :
        xx == 2
        CSB.create_CON_separate_noConnect () 

def create_JoinCON () :
    xx = 0
    rb0 = cmds.radioButton (RButton_Constraints, q=1, sl=1)
    rb1 = cmds.radioButton (RButton_JointBinding, q=1, sl=1)
    rb2 = cmds.radioButton (RButton_None, q=1, sl=1)
    if rb0 == True :
        xx == 0
        CJB.create_CON_combine ()       
    if rb1 == True :
        xx == 1
        CJ.create_JNT_combine ()
    if rb2 == True :
        xx == 2
        CJB.create_CON_combine_noConnect ()

def create_SingleCON_CT () :
    xx = 0
    rb0 = cmds.radioButton (RButton_Constraints, q=1, sl=1)
    rb1 = cmds.radioButton (RButton_JointBinding, q=1, sl=1)
    rb2 = cmds.radioButton (RButton_None, q=1, sl=1)
    if rb0 == True :
        xx == 0
        CSB.create_CON_separate_CT ()
    if rb1 == True :
        xx == 1
        CJ.create_JNT_separate_CT ()
    if rb2 == True :
        xx == 2
        CSB.create_CON_separate_CT_noConnect ()

def create_JoinCON_CT () :
    xx = 0
    rb0 = cmds.radioButton (RButton_Constraints, q=1, sl=1)
    rb1 = cmds.radioButton (RButton_JointBinding, q=1, sl=1)
    rb2 = cmds.radioButton (RButton_None, q=1, sl=1)
    if rb0 == True :
        xx == 0
        CJB.create_CON_combine_CT ()       
    if rb1 == True :
        xx == 1
        CJ.create_JNT_combine_CT ()
    if rb2 == True :
        xx == 2
        CJB.create_CON_combine_CT_noConnect ()       
#                                                                                                                     #
#                                                                                                                     # 
#                                                                                                                     #
############################################    radioButton : Node Type    ############################################





###################################################    Window GUI    ##################################################
#                                                                                                                     # 
#                                                                                                                     # 
#                                                                                                                     # 
#__________ Create Window __________#                                                                                 #
def propRigWindow () :
    propRig_Window = 'propRig_v01'                                                                                             #
    if cmds.window (propRig_Window, q=1, ex=1):                                                                                #
        cmds.deleteUI (propRig_Window)    
    
    cmds.window (propRig_Window, h=50)
    
    #__________ 1. Model Check __________#
    cmds.columnLayout (adj=1, bgc=([0.2, 0.2, 0.2]), parent = propRig_Window)
    cmds.frameLayout (l='Model Check', collapsable=1, collapse=1, bgc=[0.7, 0.3, 0.3])
    cmds.separator (st='single')
    cmds.text ('1. MODEL CHECK', font='obliqueLabelFont', h=15)
    cmds.separator (st='single')
    cmds.rowColumnLayout (numberOfColumns=3, columnWidth=[(1,50), (2,180), (3,50)])
    cmds.text (" ")
    cmds.button (l='Run Checker Tool ', w=150, h=30, bgc=([1, 0.8, 0.8]), c='CK.checker()')
    cmds.text (" ")
    cmds.separator (st='none', h=15)
    cmds.setParent ('..')

    #__________ 2. dxRig setting __________#
    cmds.columnLayout (adj=1, bgc=([0.2, 0.2, 0.2]), parent = propRig_Window)
    cmds.frameLayout (l='Create dxRig Node', collapsable=1, collapse=1, bgc=[0.75, 0.6, 0.15])
    cmds.separator (st='single', bgc=([0.5, 0.5, 0.1]))
    cmds.text ('2. CREATE dxRig NODE', font='obliqueLabelFont', h=20)
    cmds.separator (st='single', bgc=([0.5, 0.5, 0.1]))
    cmds.rowColumnLayout (numberOfColumns=3, columnWidth=[(1,50), (2,180), (3,50)])
    cmds.text (" ")
    cmds.button (l='Create !', w=150, h=30, bgc=([1, 0.87, 0.76]), c='DX.Create_propRig_group()') 
    cmds.text (" ")
    cmds.separator (st='none', h=20)
    cmds.setParent('..')
    
    #__________ 3. Controller Setting __________#
    cmds.columnLayout (adj=1, bgc=([0.2, 0.2, 0.2]), parent = propRig_Window)
    conSet_frameLayout = cmds.frameLayout (l='Create Controller', collapsable=1, collapse=1, bgc=[0.4, 0.55, 0.3])
    cmds.separator (st='none')
    cmds.separator (st='single', bgc=([0.5, 0.5, 0.25]))
    cmds.text ('3. CON SETTING', font='obliqueLabelFont', h=20, bgc=([0.7, 0.9, 0.7]))
    cmds.separator (st='single', bgc=([0.5, 0.5, 0.25]))    
    # NodeType #
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1,70), (2,75), (3,85), (4,50)])
    cmds.text ('Node Type   :', font='obliqueLabelFont')
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.setParent('..')
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1,20), (2,85), (3,100), (4,70)])
    cmds.separator (st='none')
    cmds.radioCollection()
    
    global RButton_Constraints, RButton_JointBinding, RButton_None
    RButton_Constraints = cmds.radioButton (l='Constraint')
    RButton_JointBinding = cmds.radioButton (l='Joint Binding')
    RButton_None = cmds.radioButton (l='None')
    
    cmds.separator (st='none', h=10)
    
    # COLOR #
    color_frameLayout = cmds.frameLayout (l=" ", p=conSet_frameLayout)
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1,70), (2, 70), (3, 10), (4,120)])
    
    cmds.separator (st="none", h=5)
    cmds.separator (st="none", h=5)
    cmds.separator (st="none", h=5)
    cmds.separator (st="none", h=5)
    
    cmds.text ('Color    :', font='obliqueLabelFont')
    cmds.textField ('colorValueTF', tx="0", ed=0)
    cmds.text (" ")
    cmds.checkBox (l='selection Highlighting', onCommand='selectionHighliting_ON ()', offCommand='selectionHighliting_OFF ()', v=1)
    
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='single', bgc=([0.5, 0.5, 0.2]))
    
    cmds.columnLayout (adj=1, h=100, p=color_frameLayout)
    cmds.rowColumnLayout (numberOfColumns=5, columnWidth= [(1,56), (2,56), (3,56), (4,56), (5,56)])
    cmds.button(l='13', bgc=[1, 0, 0], c='CL.colorSet (13)')
    cmds.button(l='4', bgc=[0.608, 0, 0.157], c='CL.colorSet (4)')
    cmds.button(l='31', bgc=[0.631, 0.188, 0.412], c='CL.colorSet (31)')
    cmds.button(l='30', bgc=[0.435, 0.188, 0.627], c='CL.colorSet (30)')
    cmds.button(l='20', bgc=[1, 0.686, 0.686], c='CL.colorSet (20)')
    cmds.button(l='17', bgc=[1, 1, 0], c='CL.colorSet (17)')
    cmds.button(l='22', bgc=[1, 1, 0.384], c='CL.colorSet (22)')
    cmds.button(l='25', bgc=[0.62, 0.627, 0.188], c='CL.colorSet (25)')
    cmds.button(l='26', bgc=[0.408, 0.627, 0.188], c='CL.colorSet (26)')
    cmds.button(l='23', bgc=[0, 0.6, 0.325], c='CL.colorSet (23)')
    cmds.button(l='6', bgc=[0, 0, 1], c='CL.colorSet (6)')
    cmds.button(l='29', bgc=[0.188, 0.404, 0.627], c='CL.colorSet (29)')
    cmds.button(l='28', bgc=[0.188, 0.627, 0.627], c='CL.colorSet (28)')
    cmds.button(l='18', bgc=[0.388, 0.863, 1], c='CL.colorSet (18)')
    cmds.button(l='14', bgc=[0, 1, 0], c='CL.colorSet (14)')
    cmds.button(l='16', bgc=[1, 1, 1], c='CL.colorSet (16)')
    cmds.button(l='24', bgc=[0.627, 0.412, 0.188], c='CL.colorSet (24)')
    cmds.button(l='10', bgc=[0.537, 0.278, 0.2], c='CL.colorSet (10)')
    cmds.button(l='21', bgc=[0.89, 0.675, 0.475], c='CL.colorSet (21)')
    cmds.button(l='default', bgc=[0.467, 0.467, 0.467], c='CL.colorSet (0)')
    #cmds.button(l='1', bgc=[0, 0, 0], c='CL.colorSet (1)')
    #cmds.button(l='2', bgc=[0.247, 0.247, 0.247], c='CL.colorSet (2)')
    #cmds.button(l='3', bgc=[0.498, 0.498, 0.498], c='CL.colorSet (3)')
    #cmds.button(l='5', bgc=[0, 0.016, 0.373], c='CL.colorSet (5)')
    #cmds.button(l='7', bgc=[0, 0.275, 0.094], c='CL.colorSet (7)')
    #cmds.button(l='8', bgc=[0.145, 0, 0.263], c='CL.colorSet (8)')
    #cmds.button(l='9', bgc=[0.78, 0, 0.78], c='CL.colorSet (9)')
    #cmds.button(l='11', bgc=[0.243, 0.133, 0.122], c='CL.colorSet (11)')
    #cmds.button(l='12', bgc=[0.6, 0.145, 0], c='CL.colorSet (12)')
    #cmds.button(l='19', bgc=[0.263, 1, 0.635], c='CL.colorSet (19)')
    #cmds.button(l='15', bgc=[0, 0.255, 0.6], c='CL.colorSet (15)')
    #cmds.button(l='27', bgc=[0.188, 0.627, 0.365], c='CL.colorSet (27)')
    
    # conSet #
    con_frameLayout = cmds.frameLayout (l=" ", p=conSet_frameLayout)
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1,140), (2,68), (3, 3), (4,68)])
    
    cmds.text ('<    Pivot Centre    >')
    cmds.separator( h=30)
    cmds.separator( h=30)
    cmds.separator( h=30)
    
    cmds.text (' +       MODELING     :', font='obliqueLabelFont')
    cmds.button (l='Single', h=30, backgroundColor=([0.2, .7, 0]), c='create_SingleCON ()')
    cmds.separator (st='none')
    cmds.button (l='Join',h=30, backgroundColor=([0.2, .7, 0]), c='create_JoinCON ()')
    
    cmds.separator (st='none', h=3)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    cmds.text (' +       GRID              :', font='obliqueLabelFont')
    cmds.button (l='Single', h=30,  backgroundColor=([1, 1, 1]), c='create_SingleCON_CT ()')
    cmds.separator (st='none')
    cmds.button (l='Join',h=30, backgroundColor=([1, 1, 1]), c='create_JoinCON_CT ()')
    
    # create subCON #
    subCON_frameLayout = cmds.frameLayout (l=" ", p=conSet_frameLayout)
    cmds.rowColumnLayout (numberOfColumns=2, columnWidth=[(1,140), (2,140)])
    cmds.separator (st='none', h=10)
    cmds.separator (st='none', h=10)
    cmds.text ('<    subCON    >        :')
    cmds.button (l='Create', h=30, bgc=[0.4, 0.4, 0.4], c='SC.sort_MC_or_SC ()')
    cmds.separator (st='none', h=5)

    
    #__________ 4. ROOT CON __________#
    cmds.columnLayout (adj=1, p=conSet_frameLayout)
    cmds.separator (st='single', bgc=([0.5, 0.3, 0.5]))    
    cmds.text ('4. ROOT_CON', font='obliqueLabelFont', h=20, bgc=([0.8, 0.8, 1]))
    cmds.separator (st='none', h=7)
    cmds.separator (st='single', bgc=([0.5, 0.3, 0.5]))
    cmds.rowColumnLayout (numberOfColumns=2, columnWidth=[(1,140), (2,140)])
    cmds.text ('<    Pivot Centre    >')
    cmds.separator( h=30)
    cmds.text (' +       MODELING    :', font='obliqueLabelFont')
    cmds.button (l='Create', h=30, backgroundColor=([0.6, 0.4, 1]), c='RC.create_rootCON ()')
    cmds.separator (st='none', h=3)
    cmds.separator (st='none', h=3)
    cmds.text (' +       GRID              :', font='obliqueLabelFont')
    cmds.button (l='Create', h=30,  backgroundColor=([1, 1, 1]), c='RC.create_rootCON_CT ()')
    cmds.separator (st='none', h=20)
    cmds.setParent ('..')
    
    
    
    #__________ 5. EXTRA __________#
    cmds.columnLayout (adj=1, bgc=([0.2, 0.2, 0.2]), parent = propRig_Window)
    cmds.frameLayout (l='EXTRA', collapsable=1, collapse=1, bgc=[0.3, 0.46, 0.5])
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1, 2), (2,136), (3,4), (4, 136)])
    
    
    
    cmds.separator (st='none')
    cmds.button (l='SELECT Hierarchy', h=30, bgc=[0.5, 0.5, 0.5], c='EX.selectHierarchy ()')
    cmds.separator (st='none')
    cmds.button (l='DELETE Constraints', h=30, bgc=[0.5, 0.5, 0.5], c='EX.deleteConstraint ()')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')

    cmds.separator (st='none')
    cmds.button (l='attach LOC', h=30, bgc=[0.5, 0.5, 0.5], c='EX.attachLOC ()')
    cmds.separator (st='none')
    cmds.button (l='create NUL', h=30, bgc=[0.5, 0.5, 0.5], c='EX.createNUL ()')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    cmds.separator (st='none')
    cmds.button (l='LRA ON', h=30, bgc=[0.5, 0.5, 0.5], c='EX.localRotationAxes (1)')
    cmds.separator (st='none')
    cmds.button (l='LRA OFF', h=30, bgc=[0.5, 0.5, 0.5], c='EX.localRotationAxes (0)')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    cmds.separator (st='none')
    cmds.button (l='CENTER JOINT', h=30, bgc=[0.5, 0.5, 0.5], c='EX.center_JNT ()')
    cmds.separator (st='none')
    cmds.button (l='JNT ZERO OUT', h=30, bgc=[0.5, 0.5, 0.5], c='EX.zeroOut ()')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    

    
    cmds.separator (st='none')
    cmds.button (l='SNAP', h=30, bgc=[0.5, 0.5, 0.5], c='EX.snap ()')
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    
    
    
    
    
    
    # window GUI : Size
    cmds.window (propRig_Window, e=1, width=290, sizeable=1)
    cmds.showWindow(propRig_Window) 
    
propRigWindow()                                                                                                      #
#                                                                                                                     # 
#                                                                                                                     # 
#                                                                                                                     # 
###################################################    Window GUI    ##################################################    
