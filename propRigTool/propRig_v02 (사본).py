import maya.cmds as cmds
import site
site.addsitedir('/dexter/Cache_DATA/CRT/riggingTeamShelf/propRigTool/propRigTool_v02_set')


import propRig_v02_2_dxRigGRP as DX;		reload(DX)
import propRig_v02_3_conSet_color as CL;		reload(CL)
import propRig_createCON_JNT as CJ;		reload(CJ)
import propRig_createCON_JoinBT as CJB;		reload(CJB)
import propRig_createCON_SingleBT as CSB;		reload(CSB)
import propRig_createSubCON as SC;		reload(SC)
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





#___________________________________________________________________________________________________________________________#
#  /////////////////////////////////////////////////////////////////////
# ///                    1. CREATE WINDOW                           ///
#/////////////////////////////////////////////////////////////////////                                                                              #
bt_bgc = (0, 0.8, 0)
createCON_menuItemWidth = 180
menuItem_hlc = (0, 0.5, 0)
colorBt_h = 30
frameLayout_color = (0.2, 0.2, 0.2)
extraBt_h = 35



def propRig_v02_Window () :
    propRig_v02_Window = 'propRig_v02'                                                                                             #
    if cmds.window (propRig_v02_Window, q=1, ex=1):                                                                                #
        cmds.deleteUI (propRig_v02_Window)    
    
    cmds.window (propRig_v02_Window, h=50)
    
    
    
    
#  /////////////////////////////////////////////////////////////////////
# ///                    2. dxRig setting                           ///
#/////////////////////////////////////////////////////////////////////
    cmds.columnLayout (adj=1, parent = propRig_v02_Window)
    cmds.frameLayout (l='dxRig', collapsable=1, collapse = 0, bgc=frameLayout_color)
    cmds.text ('2. CREATE dxRig NODE', font='obliqueLabelFont', h=20)
    cmds.rowColumnLayout (numberOfColumns=3, columnWidth=[(1,50), (2,200), (3,30)])
    cmds.separator (st = 'none' )
    cmds.button (l='Create !    ', w=200, h=40, bgc=bt_bgc, c='DX.Create_propRig_group()') 
    cmds.separator (st = 'none' )
    cmds.setParent('..')
    
    
    
    
    
#  /////////////////////////////////////////////////////////////////////
# ///                   3. Controller Setting                       ///
#/////////////////////////////////////////////////////////////////////    

    cmds.columnLayout (adj=1, parent = propRig_v02_Window)    
    conSet_frameLayout = cmds.frameLayout (l='Controller', collapsable=1, collapse=1, bgc=frameLayout_color)
    con_form = cmds.formLayout (numberOfDivisions = 100 )    
    # 1 #
    conCreateBt = cmds.button ( l = 'Create CON ', h = 86, bgc = bt_bgc)
    # 2 #
    sub_column = cmds.columnLayout (rs = 2)
    con_nodeType = cmds.optionMenu ( l = '   nodeType    :', w = createCON_menuItemWidth, hlc = menuItem_hlc)
    cmds.menuItem ( l = ' constraint' )
    cmds.menuItem ( l = ' joint' )
    cmds.menuItem ( l = ' none' )
    con_pivot = cmds.optionMenu ( l = '           pivot    :', w = createCON_menuItemWidth, hlc = menuItem_hlc)
    cmds.menuItem (l = ' model center' )
    cmds.menuItem (l = ' grid center' )
    con_conType = cmds.optionMenu ( l = '     conType    :', w = createCON_menuItemWidth, hlc = menuItem_hlc)
    cmds.menuItem ( l = ' con' )
    cmds.menuItem ( l = ' subCON ' )
    cmds.menuItem ( l = ' rootCON ' )
    con_model = cmds.optionMenu ( l = '    structure    :', w = createCON_menuItemWidth, hlc = menuItem_hlc)    
    cmds.menuItem ( l = ' each')
    cmds.menuItem ( l = ' join' )
    
    cmds.formLayout (con_form, e = 1,
    attachForm = [ ( conCreateBt, 'right', 1 ), (sub_column, 'top', 0), (sub_column, 'left', 1) ],
    attachPosition = [ ( conCreateBt, 'left', 10, 60 ) ] )

    cmds.rowColumnLayout (numberOfColumns = 3, cw = [ (1, 170), (2, 70), (3, 50) ] )  
    cmds.separator ( st = 'none' )
    lw = cmds.text ( 'lineWidth    :', font = 'obliqueLabelFont')
    cmds.textField (lw, tx = '-1', ed = 1, h = 20, font = 'boldLabelFont', bgc = frameLayout_color)
    

    cmds.setParent ('..')
#  /////////////////////////////////////////////////////////////////////
# ///                       4. COLOR                                ///
#/////////////////////////////////////////////////////////////////////    
    cmds.columnLayout (adj=1, parent = propRig_v02_Window)    
    colorControl = cmds.frameLayout (l='COLOR', collapsable=1, collapse=1, bgc=frameLayout_color)
    cmds.separator (st = 'none', h = 2)
     
    cmds.rowColumnLayout (numberOfColumns=3, columnWidth=[(1,70), (2, 50), (3, 170)])

    cmds.text ('Color    :', font='obliqueLabelFont' )
    cmds.textField ('colorValueTF', tx="0", ed=0, bgc = frameLayout_color)
    color_categories = cmds.optionMenu (l = '    Categories : ', w = 150)
    cmds.menuItem ( l = 'object' )
    cmds.menuItem ( l = 'Outliner' )
    cmds.menuItem ( l = 'Tint.USD' )

 #   cmds.text (" ")
 #   cmds.checkBox (l='selection Highlighting', onCommand='selectionHighliting_ON ()', offCommand='selectionHighliting_OFF ()', v=1)
    cmds.columnLayout (adj=1, p=colorControl)


    a = 73
    cmds.rowColumnLayout (numberOfColumns=4, cw= [(1, a), (2, a), (3, a), (4, a)])

    cmds.button(l='1', h = colorBt_h, bgc=[0, 0, 0], c='CL.colorSet (1)')
    cmds.button(l='2', bgc=[0.247, 0.247, 0.247], c='CL.colorSet (2)')
    cmds.button(l='3', bgc=[0.498, 0.498, 0.498], c='CL.colorSet (3)')
    cmds.button(l='4', bgc=[1, 1, 1], c='CL.colorSet (4)')
    
    ###########    RED    ###########
    cmds.button(l='11', h = colorBt_h, bgc=[1, 0, 0], c='CL.colorSet (11)')
    cmds.button(l='12', bgc=[0.6, 0.145, 0], c='CL.colorSet (12)')    
    cmds.button(l='13', bgc=[0.399, 0.234, 0.314], c='CL.colorSet (13)')
    cmds.button(l='14', bgc=[0.615, 0.454, 0.565], c='CL.colorSet (14)')  
    
    ###########    OR    ###########
    cmds.button(l='21', h = colorBt_h, bgc=[1, 0.35, 0], c='CL.colorSet (21)')
    cmds.button(l='22', bgc=[1, 0.5, 0], c='CL.colorSet (22)')
    cmds.button(l='23', bgc=[1, 0.7, 0.3], c='CL.colorSet (23)')
    cmds.button(l='24', bgc=[0.855, 0.8, 0.6], c='CL.colorSet (24)')
    
    ###########    YL    ###########    
    cmds.button(l='31', h = colorBt_h, bgc=[1, 1, 0], c='CL.colorSet (31)')
    cmds.button(l='32', bgc=[0.6, 0.6, 0.1], c='CL.colorSet (32)')
    cmds.button(l='33', bgc=[0.5, 0.5, 0], c='CL.colorSet (33)')  
    cmds.button(l='34', bgc=[1, 1, 0.5], c='CL.colorSet (34)')
    
    ###########    GN    ###########
    cmds.button(l='41',  h = colorBt_h, bgc=[0, 0.275, 0.094], c='CL.colorSet (41)')
    cmds.button(l='42', bgc=[0.188, 0.627, 0.365], c='CL.colorSet (42)')
    cmds.button(l='43', bgc=[0.408, 0.627, 0.188], c='CL.colorSet (43)')
    cmds.button(l='44', bgc=[0.263, 1, 0.635], c='CL.colorSet (44)')

    ###########    BL    ###########    
    cmds.button(l='51', h = colorBt_h, bgc=[0, 0, 1], c='CL.colorSet (51)')
    cmds.button(l='52', bgc=[0.188, 0.404, 0.8], c='CL.colorSet (52)')
    cmds.button(l='53', bgc=[0.2, 0.627, 0.8], c='CL.colorSet (53)')
    cmds.button(l='54', bgc=[0.240, 0.844, 0.914], c='CL.colorSet (54)')
    
    ###########    PINK    ###########
    cmds.button(l='61', h = colorBt_h, bgc=[1, 0, 0.5], c='CL.colorSet (61)')
    cmds.button(l='62', bgc=[1, 0, 1], c='CL.colorSet (62)')    
    cmds.button(l='63', bgc=[1, 0.6, 0.8], c='CL.colorSet (63)')
    cmds.button(l='64', bgc=[1, 0.8, 1], c='CL.colorSet (64)')    
    
    cmds.separator (st = 'none' , h = 10)
    cmds.setParent ('..')    
    
    
    
    
    
    
    
    

#  ///////////////////////////////////////////////////////////////////////    
# //////                     5. EXTRA                          //////////
#///////////////////////////////////////////////////////////////////////    
    cmds.columnLayout (adj=1, bgc=([0.2, 0.2, 0.2]), parent = propRig_v02_Window)
    cmds.frameLayout (l='EXTRA', collapsable=1, collapse=1, bgc=frameLayout_color)
    cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1, 2), (2,145), (3,4), (4, 145)])
    
    
    
    cmds.separator (st='none')
    cmds.button (l='SELECT Hierarchy', h=extraBt_h, bgc=[0.5, 0.5, 0.5], c='EX.selectHierarchy ()')
    cmds.separator (st='none')
    cmds.button (l='DELETE Constraints', h=extraBt_h, bgc=[0.5, 0.5, 0.5], c='EX.deleteConstraint ()')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')

    cmds.separator (st='none')
    cmds.button (l='attach LOC', h=extraBt_h, bgc=[0.5, 0.5, 0.5], c='EX.attachLOC ()')
    cmds.separator (st='none')
    cmds.button (l='create NUL', h=extraBt_h, bgc=[0.5, 0.5, 0.5], c='EX.createNUL ()')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    cmds.separator (st='none')
    cmds.button (l='LRA ON', h=extraBt_h, bgc=[0.5, 0.5, 0.5], c='EX.localRotationAxes (1)')
    cmds.separator (st='none')
    cmds.button (l='LRA OFF', h=extraBt_h, bgc=[0.5, 0.5, 0.5], c='EX.localRotationAxes (0)')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    cmds.separator (st='none')
    cmds.button (l='CENTER JOINT', h=extraBt_h, bgc=[0.5, 0.5, 0.5], c='EX.center_JNT ()')
    cmds.separator (st='none')
    cmds.button (l='JNT ZERO OUT', h=extraBt_h, bgc=[0.5, 0.5, 0.5], c='EX.zeroOut ()')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    

    
    cmds.separator (st='none')
    cmds.button (l='SNAP', h=extraBt_h, bgc=[0.5, 0.5, 0.5], c='EX.snap ()')
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none', h=2)
    cmds.separator (st='none')
    cmds.separator (st='none')
    cmds.separator (st='none')
    
    
    
    
    
    
    
    # window GUI : Size
    cmds.window (propRig_v02_Window, e=1, width=300, h = 10,sizeable=1)
    cmds.showWindow(propRig_v02_Window) 
    
propRig_v02_Window()                                                                                    
#                                                                                                                     # 
#                                                                                                                     # 
#                                                                                                                     # 
###################################################    Window GUI    ##################################################    
