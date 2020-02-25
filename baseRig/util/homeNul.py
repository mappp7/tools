#encoding=utf-8

# 임포트 cmds
import maya.cmds as cmds

def homeNul( controllerObjet, *NulName ):
    
    replaceName = controllerObjet.replace( controllerObjet.split('_')[-1], 'NUL')# 써픽스를 _NUL로 교체
    
    parentGRP = cmds.listRelatives( controllerObjet, allParents=True )# 상위 그룹 판별
    if parentGRP == None:# 상위 그룹이없으면
    
        if len(NulName) == 0:
            #print replaceName 
            NUL = cmds.createNode( 'transform', name='%s' % replaceName, parent=controllerObjet )# Nul 그룹 만들기
            
            cmds.parent( NUL, w=True )
            cmds.parent( controllerObjet, NUL )
            
            return NUL
                
        if 0 < len(NulName):
            #print replaceName 
            NUL = cmds.createNode( 'transform', name=NulName[0], parent=controllerObjet )# Nul 그룹 만들기
            
            cmds.parent( NUL, w=True )
            cmds.parent( controllerObjet, NUL )
            
            return NUL
        
    else:# 상위 그룹이있으면
        if len(NulName) == 0:
            NUL = cmds.createNode( 'transform', name='%s' % replaceName, parent=controllerObjet )# Nul 그룹 만들기
        
            cmds.parent( NUL, parentGRP )
            cmds.parent( controllerObjet, NUL )
            
            return NUL
        
        if 0 < len(NulName):
            #print replaceName 
            NUL = cmds.createNode( 'transform', name=NulName[0], parent=controllerObjet )# Nul 그룹 만들기
            
            cmds.parent( NUL, w=True )
            
            cmds.parent( controllerObjet, NUL )
            cmds.parent( NUL, parentGRP )
            
            return NUL
