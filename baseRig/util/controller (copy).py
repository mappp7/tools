import maya.cmds as cmds
import maya.mel as mel

def controllerShape( conName, conShape, setColor ):
    
    Color = { 'black':0 , 'red':12, 'blue':6, 'yellow':17 , 'skyBlue':18 , 'peach':20 }
    
    if conShape == 'cube':
        cubeCon = mel.eval("""curve -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 
                            -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 
                            -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 
                            -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 
                            -p -0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 
                            -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -n %s ;""" % conName)
        
        cmds.setAttr('%s.overrideEnabled' % cubeCon, 1)
        cmds.setAttr('%s.overrideColor' % cubeCon, Color[setColor])
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
        
    elif conShape == 'circle':
        circleCon = mel.eval("""circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 0.5 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0 -n %s;""" % conName)
        cmds.setAttr('%s.overrideEnabled' % circleCon[0], 1)
        cmds.setAttr('%s.overrideColor' % circleCon[0], Color[setColor])
        
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
        
    elif conShape == 'dubleCircle':
        dubleCircleCon = mel.eval("""curve -d 1 -p -0.504004 -0.0167178 -1.8995e-06 
        -p -0.486389 -0.0167178 0.130304 -p -0.436069 -0.0167178 0.251787 -p -0.356385 -0.0167178 0.356383 
        -p -0.251789 -0.0167178 0.436067 -p -0.130306 -0.0167178 0.486387 -p 0 -0.0167178 0.504002 
        -p 0.130306 -0.0167178 0.486387 -p 0.251789 -0.0167178 0.436067 -p 0.356385 -0.0167178 0.356383 
        -p 0.436069 -0.0167178 0.251787 -p 0.486389 -0.0167178 0.130304 -p 0.504004 -0.0167178 -1.8995e-06 
        -p 0.486389 -0.0167178 -0.130308 -p 0.436069 -0.0167178 -0.251791 -p 0.356385 -0.0167178 -0.356387 
        -p 0.251789 -0.0167178 -0.436071 -p 0.130306 -0.0167178 -0.486392 -p 0 -0.0167178 -0.504002 
        -p -0.130306 -0.0167178 -0.486392 -p -0.251789 -0.0167178 -0.436071 -p -0.356385 -0.0167178 -0.356387 
        -p -0.436069 -0.0167178 -0.251791 -p -0.486389 -0.0167178 -0.130308 -p -0.504004 -0.0167178 -1.8995e-06 
        -p -0.504004 0.0167178 -1.8995e-06 -p -0.486389 0.0167178 0.130304 -p -0.436069 0.0167178 0.251787 
        -p -0.356385 0.0167178 0.356383 -p -0.251789 0.0167178 0.436067 -p -0.130306 0.0167178 0.486387 
        -p 0 0.0167178 0.504002 -p 0 -0.0167178 0.504002 -p 0 0.0167178 0.504002 -p 0.130306 0.0167178 0.486387 
        -p 0.251789 0.0167178 0.436067 -p 0.356385 0.0167178 0.356383 -p 0.436069 0.0167178 0.251787 
        -p 0.486389 0.0167178 0.130304 -p 0.504004 0.0167178 -1.8995e-06 -p 0.504004 -0.0167178 -1.8995e-06 
        -p 0.504004 0.0167178 -1.8995e-06 -p 0.486389 0.0167178 -0.130308 -p 0.436069 0.0167178 -0.251791 
        -p 0.356385 0.0167178 -0.356387 -p 0.251789 0.0167178 -0.436071 -p 0.130306 0.0167178 -0.486392 
        -p 0 0.0167178 -0.504002 -p 0 -0.0167178 -0.504002 -p 0 0.0167178 -0.504002 
        -p -0.130306 0.0167178 -0.486392 -p -0.251789 0.0167178 -0.436071 -p -0.356385 0.0167178 -0.356387 
        -p -0.436069 0.0167178 -0.251791 -p -0.486389 0.0167178 -0.130308 -p -0.504004 0.0167178 -1.8995e-06 
        -p -0.504004 -0.0167178 -1.8995e-06 -p -0.504004 0.0167178 -1.8995e-06 -n %s ;""" % conName)
        
        cmds.setAttr('%s.overrideEnabled' % dubleCircleCon, 1)
        cmds.setAttr('%s.overrideColor' % dubleCircleCon, Color[setColor])
        
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
        
    elif conShape == 'cross':
        crossCon = mel.eval("""curve -d 1 -p 0.165 0 0.495 -p 0.165 0 0.165 
        -p 0.495 0 0.165 -p 0.495 0 -0.165 -p 0.165 0 -0.165 -p 0.165 0 -0.495 
        -p -0.165 0 -0.495 -p -0.165 0 -0.165 -p -0.495 0 -0.165 -p -0.495 0 0.165 
        -p -0.165 0 0.165 -p -0.165 0 0.495 -p 0.165 0 0.495 -n %s ;""" % conName)
        
        cmds.setAttr('%s.overrideEnabled' % crossCon, 1)
        cmds.setAttr('%s.overrideColor' % crossCon, Color[setColor])
        
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
        
    elif conShape == 'fatCross':
        fatCrossCon = mel.eval("""curve -d 1 -p 0.25 0 0.5 -p 0.25 0 0.25 -p 0.5 0 0.25 
        -p 0.5 0 -0.25 -p 0.25 0 -0.25 -p 0.25 0 -0.5 -p -0.25 0 -0.5 -p -0.25 0 -0.25 
        -p -0.5 0 -0.25 -p -0.5 0 0.25 -p -0.25 0 0.25 -p -0.25 0 0.5 -p 0.25 0 0.5 -n %s ;""" % conName)
        
        cmds.setAttr('%s.overrideEnabled' % fatCrossCon, 1)
        cmds.setAttr('%s.overrideColor' % fatCrossCon, Color[setColor])
        
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )

    elif conShape == 'locator':
        locator = mel.eval("""curve -d 1 -p 0 0 0 -p 0.5 0 0 -p -0.5 0 0 -p 0 0 0 -p 0 0 0.5 -p 0 0 -0.5 
        -p 0 0 0 -p 0 -0.5 0 -p 0 0.5 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -n %s ;""" % conName)
        
        cmds.setAttr('%s.overrideEnabled' % locator, 1)
        cmds.setAttr('%s.overrideColor' % locator, Color[setColor])
        
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )

    elif conShape == 'sphere':
        sphereCon = mel.eval("""curve -d 1 -p 0 0 0.5 -p 0.353554 0 0.353554 -p 0.5 0 0 
        -p 0.353554 0 -0.353554 -p 0 0 -0.5 -p -0.353554 0 -0.353554 -p -0.5 0 0 
        -p -0.353554 0 0.353554 -p 0 0 0.5 -p 0 0.25 0.433013 -p 0 0.433013 0.25 
        -p 0 0.5 0 -p 0 0.433013 -0.25 -p 0 0.25 -0.433013 -p 0 0 -0.5 -p 0 -0.25 -0.433013 
        -p 0 -0.433013 -0.25 -p 0 -0.5 0 -p 0 -0.433013 0.25 -p 0 -0.25 0.433013 -p 0 0 0.5 
        -p 0.353554 0 0.353554 -p 0.5 0 0 -p 0.433013 0.25 0 -p 0.25 0.433013 0 -p 0 0.5 0 
        -p -0.25 0.433013 0 -p -0.433013 0.25 0 -p -0.5 0 0 -p -0.433013 -0.25 0 -p -0.25 -0.433013 0 
        -p 0 -0.5 0 -p 0.25 -0.433013 0 -p 0.433013 -0.25 0 -p 0.5 0 0 -n %s ;""" % conName)
                            
        cmds.setAttr('%s.overrideEnabled' % sphereCon, 1)
        cmds.setAttr('%s.overrideColor' % sphereCon, Color[setColor])
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
        
    elif conShape == 'octagon':
        octagonCon = mel.eval("""curve -d 1 -p 0.246168 0 0.492335 -p 0.492335 0 0.246168 
        -p 0.492335 0 -0.246168 -p 0.246168 0 -0.492335 -p -0.246168 0 -0.492335 
        -p -0.492335 0 -0.246168 -p -0.492335 0 0.246168 -p -0.246168 0 0.492335 
        -p 0.246168 0 0.492335 -n %s ;""" % conName)
                            
        cmds.setAttr('%s.overrideEnabled' % octagonCon, 1)
        cmds.setAttr('%s.overrideColor' % octagonCon, Color[setColor])
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
        
    elif conShape == 'dubleOctagon':
        dubleOctagonCon = mel.eval("""curve -d 1 -p 0.246503 -0.044 0.493007 
        -p 0.493007 -0.044 0.246503 -p 0.493007 -0.044 -0.246503 -p 0.246503 -0.044 -0.493007 
        -p -0.246503 -0.044 -0.493007 -p -0.493007 -0.044 -0.246503 -p -0.493007 -0.044 0.246503 
        -p -0.246503 -0.044 0.493007 -p 0.246503 -0.044 0.493007 -p 0.246503 0.044 0.493007 
        -p 0.493007 0.044 0.246503 -p 0.493007 -0.044 0.246503 -p 0.493007 0.044 0.246503 
        -p 0.493007 0.044 -0.246503 -p 0.493007 -0.044 -0.246503 -p 0.493007 0.044 -0.246503 
        -p 0.246503 0.044 -0.493007 -p 0.246503 -0.044 -0.493007 -p 0.246503 0.044 -0.493007 
        -p -0.246503 0.044 -0.493007 -p -0.246503 -0.044 -0.493007 -p -0.246503 0.044 -0.493007 
        -p -0.493007 0.044 -0.246503 -p -0.493007 -0.044 -0.246503 -p -0.493007 0.044 -0.246503 
        -p -0.493007 0.044 0.246503 -p -0.493007 -0.044 0.246503 -p -0.493007 0.044 0.246503 
        -p -0.246503 0.044 0.493007 -p -0.246503 -0.044 0.493007 -p -0.246503 0.044 0.493007 
        -p 0.246503 0.044 0.493007 -p 0.246503 -0.044 0.493007 -n %s ;""" % conName)
                            
        cmds.setAttr('%s.overrideEnabled' % dubleOctagonCon, 1)
        cmds.setAttr('%s.overrideColor' % dubleOctagonCon, Color[setColor])
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
        
    elif conShape == 'rombus':
        rombusCon = mel.eval("""curve -d 1 -p 0 0.5 0 -p 0.5 0 0 -p 0 0 0.5 -p -0.5 0 0 -p 0 0 -0.5 -p 0 0.5 0 -p 0 0 0.5 -p 0 -0.5 0 -p 0 0 -0.5
                                      -p 0.5 0 0 -p 0 0.5 0 -p -0.5 0 0 -p 0 -0.5 0 -p 0.5 0 0 -n %s;""" % conName )
                            
        cmds.setAttr('%s.overrideEnabled' % rombusCon, 1)
        cmds.setAttr('%s.overrideColor' % rombusCon, Color[setColor])
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
        
    elif conShape == 'root':
        rootCon = mel.eval("""curve -d 3 -p 0 0 0.514016 -p 0.215045 0 0.43009 -p 0.215045 0 0.43009 -p 0.215045 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.43009 -p 0.107523 0 0.348839 -p 0.107523 0 0.348839 -p 0.107523 0 0.348839 -p 0.165418 0 0.3301 -p 0.269267 0 0.268173 -p 0.330916 0 0.164045 -p 0.348514 0 0.107561 -p 0.348514 0 0.107561 -p 0.348514 0 0.107561 -p 0.348514 0 0.107561 -p 0.43009 0 0.107523 -p 0.43009 0 0.107523 -p 0.43009 0 0.107523 -p 0.43009 0 0.215045 -p 0.43009 0 0.215045 -p 0.43009 0 0.215045 -p 0.514016 0 0 -p 0.514016 0 0 -p 0.514016 0 0 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.215045 -p 0.43009 0 -0.107523 -p 0.43009 0 -0.107523 -p 0.43009 0 -0.107523 -p 0.34749 0 -0.107523 -p 0.34749 0 -0.107523 -p 0.34749 0 -0.107523 -p 0.330753 0 -0.16432 -p 0.268043 0 -0.270089 -p 0.161744 0 -0.33227 -p 0.103842 0 -0.349651 -p 0.103842 0 -0.349651 -p 0.103842 0 -0.349651 -p 0.107523 0 -0.43009 -p 0.107523 0 -0.43009 -p 0.107523 0 -0.43009 -p 0.215045 0 -0.43009 -p 0.215045 0 -0.43009 -p 0.215045 0 -0.43009 -p 0 0 -0.514016 -p 0 0 -0.514016 -p 0 0 -0.514016 -p -0.215045 0 -0.43009 -p -0.215045 0 -0.43009 -p -0.215045 0 -0.43009 -p -0.215045 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.107523 0 -0.43009 -p -0.106926 0 -0.348711 -p -0.106926 0 -0.348711 -p -0.106926 0 -0.348711 -p -0.106926 0 -0.348711 -p -0.163653 0 -0.331148 -p -0.268767 0 -0.269043 -p -0.330943 0 -0.163999 -p -0.348078 0 -0.107523 -p -0.348078 0 -0.107523 -p -0.348078 0 -0.107523 -p -0.348078 0 -0.107523 -p -0.43009 0 -0.107523 -p -0.43009 0 -0.107523 -p -0.43009 0 -0.107523 -p -0.43009 0 -0.215045 -p -0.43009 0 -0.215045 -p -0.43009 0 -0.215045 -p -0.43009 0 -0.215045 -p -0.514016 0 0 -p -0.514016 0 0 -p -0.514016 0 0 -p -0.514016 0 0 -p -0.43009 0 0.215045 -p -0.43009 0 0.215045 -p -0.43009 0 0.215045 -p -0.43009 0 0.215045 -p -0.43009 0 0.107523 -p -0.43009 0 0.107523 -p -0.43009 0 0.107523 -p -0.43009 0 0.107523 -p -0.347279 0 0.107523 -p -0.347279 0 0.107523 -p -0.347279 0 0.107523 -p -0.347279 0 0.107523 -p -0.331036 0 0.163843 -p -0.269226 0 0.268353 -p -0.164939 0 0.330385 -p -0.109006 0 0.348061 -p -0.109006 0 0.348061 -p -0.109006 0 0.348061 -p -0.109006 0 0.348061 -p -0.107523 0 0.43009 -p -0.107523 0 0.43009 -p -0.107523 0 0.43009 -p -0.107523 0 0.43009 -p -0.215045 0 0.43009 -p -0.215045 0 0.43009 -p -0.215045 0 0.43009 -p 0 0 0.514016 -p 0 0 0.514016 -p 0 0 0.514016 -p 0 0 0.514016 -n %s ;""" % conName)
                            
        cmds.setAttr('%s.overrideEnabled' % rootCon, 1)
        cmds.setAttr('%s.overrideColor' % rootCon, Color[setColor])
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
        
    elif conShape == 'hexagon':
        hexagonCon = mel.eval("""curve -d 1 -p -0.257187 0 0.445461 -p 0.257187 0 0.445461 -p 0.514375 0 2.51218e-07 -p 0.257187 0 -0.445461 -p -0.257187 0 -0.445461 -p -0.514375 0 1.69509e-07 -p -0.257187 0 0.445461 -n %s""" % conName)
                            
        cmds.setAttr('%s.overrideEnabled' % hexagonCon, 1)
        cmds.setAttr('%s.overrideColor' % hexagonCon, Color[setColor])
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
    
    elif conShape == 'square':
        squareCon = mel.eval("""curve -d 1 -p -0.5 0 0.5 -p 0.5 0 0.5 -p 0.5 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 0.5 -n %s""" % conName)
                            
        cmds.setAttr('%s.overrideEnabled' % squareCon, 1)
        cmds.setAttr('%s.overrideColor' % squareCon, Color[setColor])
        # Shape Name
        shapeName = cmds.listRelatives( conName )
        cmds.rename( shapeName, conName + 'Shape' )
    return conName
"""
controllerShape( 'cube_CON', 'square', 'red' )
"""