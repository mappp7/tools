import maya.cmds as cmds

from util.snap import *
from util.attach import *
from util.pairBlend import *
from util.homeNul import *

class spaceSwitch:
    
    def __init__(self, firstSpace, secondSpace, target):
        self.firstSpace = firstSpace
        self.secondSpace = secondSpace
        self.target = target
        
    def createSpace(self):
        if cmds.objExists( self.firstSpace.replace( self.firstSpace.split('_')[-1], 'space_SPC' ) ):
            self.firstSpaceNul = self.firstSpace.replace( self.firstSpace.split('_')[-1], 'space_SPC' )
            
            fLocatorName = self.target.replace( self.firstSpace.split('_')[-1], 'LOC' )
            self.firstSpaceLOC = cmds.spaceLocator( n=fLocatorName.replace( fLocatorName.split('_')[-2], '%sIn%s' % ( self.target.split('_')[-2], self.firstSpace.split('_')[-2].capitalize() ) ) )
            POsnap( self.firstSpaceLOC, self.target )
            
            cmds.parent( self.firstSpaceLOC, self.firstSpaceNul )    
            
        else:
            self.firstSpaceNul = cmds.createNode( 'transform', n=self.firstSpace.replace( self.firstSpace.split('_')[-1], 'space_SPC' ) )
            POsnap( self.firstSpaceNul, self.firstSpace )
            
            fLocatorName = self.target.replace( self.firstSpace.split('_')[-1], 'LOC' )
            self.firstSpaceLOC = cmds.spaceLocator( n=fLocatorName.replace( fLocatorName.split('_')[-2], '%sIn%s' % ( self.target.split('_')[-2], self.firstSpace.split('_')[-2].capitalize() ) ) )
            POsnap( self.firstSpaceLOC, self.target )
            
            cmds.parent( self.firstSpaceLOC, self.firstSpaceNul )
        
        
        if cmds.objExists( self.secondSpace.replace( self.secondSpace.split('_')[-1], 'space_SPC' ) ):
            self.secondSpaceNul = self.secondSpace.replace( self.secondSpace.split('_')[-1], 'space_SPC' )
            sLocatorName = self.target.replace( self.secondSpace.split('_')[-1], 'LOC' )
            self.secondSpaceLOC = cmds.spaceLocator( n=sLocatorName.replace( sLocatorName.split('_')[-2], '%sIn%s' % ( self.target.split('_')[-2], self.secondSpace.split('_')[-2].capitalize() ) ) )
            
            POsnap( self.secondSpaceLOC[0], self.target )
            
            cmds.parent( self.secondSpaceLOC, self.secondSpaceNul )
        
        else:
            self.secondSpaceNul = cmds.createNode( 'transform', n=self.secondSpace.replace( self.secondSpace.split('_')[-1], 'space_SPC' ) )
            POsnap( self.secondSpaceNul, self.secondSpace )
            
            sLocatorName = self.target.replace( self.secondSpace.split('_')[-1], 'LOC' )
            self.secondSpaceLOC = cmds.spaceLocator( n=sLocatorName.replace( sLocatorName.split('_')[-2], '%sIn%s' % ( self.target.split('_')[-2], self.secondSpace.split('_')[-2].capitalize() ) ) )
            
            POsnap( self.secondSpaceLOC[0], self.target )
            
            cmds.parent( self.secondSpaceLOC, self.secondSpaceNul )
        return [ self.firstSpaceNul, self.secondSpaceNul]
        """
        # firstSpace 
        if cmds.objExists('C_move_CONSpace_SPC'):
            
            firstSpaceNul = '%sSpace_SPC' % self.firstSpace
            
            nameLOC = '%s%sSpace_LOC' % (self.firstSpace, self.target.split('_')[-2])
            self.firstSpaceLOC = cmds.spaceLocator( n=nameLOC.replace( nameLOC.split('_')[0] + '_', self.target.split('_')[0] + '_' ) )
            
            POsnap( self.firstSpaceLOC, self.target )
            
            cmds.parent( self.firstSpaceLOC, firstSpaceNul )
        else:
            firstSpaceNul = cmds.createNode( 'transform', n='%sSpace_SPC' % self.firstSpace )
            POsnap( firstSpaceNul, self.firstSpace )
            
            nameLOC = '%s%sSpace_LOC' % (self.firstSpace, self.target.split('_')[-2])
            self.firstSpaceLOC = cmds.spaceLocator( n=nameLOC.replace( nameLOC.split('_')[0] + '_', self.target.split('_')[0] + '_' )  )
            
            POsnap( self.firstSpaceLOC, self.target )
            
            cmds.parent( self.firstSpaceLOC, firstSpaceNul )
            
        # secondSpace    
        if cmds.objExists('C_FK_hip_CONSpace_SPC'):
            
            self.secondSpaceNul = '%sSpace_SPC' % self.secondSpace
            print self.secondSpaceNul
            
            nameLOC = '%s%sSpace_LOC' % (self.secondSpace, self.target.split('_')[-2])
            self.secondSpaceLOC = cmds.spaceLocator( n=nameLOC.replace( nameLOC.split('_')[0] + '_', self.target.split('_')[0] + '_' )  )
            
            POsnap( self.secondSpaceLOC, self.target )
            
            cmds.parent( self.secondSpaceLOC, self.secondSpaceNul )
        else:
            self.secondSpaceNul = cmds.createNode( 'transform', n='%sSpace_SPC' % self.secondSpace )
            POsnap( self.secondSpaceNul, self.secondSpace )
            
            nameLOC = '%s%sSpace_LOC' % (self.secondSpace, self.target.split('_')[-2])
            self.secondSpaceLOC = cmds.spaceLocator( n=nameLOC.replace( nameLOC.split('_')[0] + '_', self.target.split('_')[0] + '_' ) )
            
            POsnap( self.secondSpaceLOC, self.target )
            
            cmds.parent( self.secondSpaceLOC, self.secondSpaceNul )
            
        return [ firstSpaceNul, self.secondSpaceNul]
        """
        
    def spaceBlend( self ):
        self.spaceNul = homeNul( self.target, self.target.replace( self.target.split('_')[-1], 'SPC') )
        #print self.spaceNul
        
        FAN = attachNode( self.firstSpaceLOC[0], self.spaceNul )
        SAN = attachNode( self.secondSpaceLOC[0], self.spaceNul )
        
        self.namePBD = createPairBlendNode( FAN[1], SAN[1], self.spaceNul, self.spaceNul.replace(self.spaceNul.split('_')[-1], 'PBD'), 'rotate' )
        
    def setSpaceSwitch(self):
        if cmds.objExists( 'C_FK_hip_space_SPC' ):#'R_FK_hip_CONlegSpace_LOC' ):
            pass
        else:
            #print self.target.replace( self.target.split('_')[-1], 'NUL' ) + 'Attach_NUL'
            if cmds.objExists( self.target.replace( self.target.split('_')[-1], 'NUL' ) + 'Attach_NUL' ):
                attachNode( self.secondSpace, self.secondSpaceNul, 'translate', 'rotate', 'scale', 'shear' )
                
            else:
                #.................................................................................
                targetNUL = cmds.listRelatives( self.spaceNul, parent=True )
                #
                self.attachNUL = attachPart( self.secondSpace, targetNUL[0], 'translate', 'rotate', 'scale', 'shear' )
                #
                attachNode( self.secondSpace, self.secondSpaceNul, 'translate', 'rotate', 'scale', 'shear' )
                
                #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
                cmds.addAttr( self.target, ln='localSpace', at='double' ,min=0, max=10, keyable=True )
                
                SRG = cmds.createNode( 'setRange', n=self.namePBD.replace( self.namePBD.split('_')[-1], 'SRG' ) )
                cmds.setAttr( '%s.maxX' % SRG, 1)
                cmds.setAttr( '%s.oldMaxX' % SRG, 10)
                
                cmds.connectAttr( '%s.localSpace' % self.target, '%s.valueX' % SRG )
                cmds.connectAttr( '%s.outValueX' % SRG, '%s.weight' % self.namePBD )
                
                
                
                #.................................................................................
                return self.attachNUL
        #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        cmds.addAttr( self.target, ln='localSpace', at='double' ,min=0, max=10, keyable=True )
        
        SRG = cmds.createNode( 'setRange', n=self.namePBD.replace( self.namePBD.split('_')[-1], 'SRG' ) )
        cmds.setAttr( '%s.maxX' % SRG, 1)
        cmds.setAttr( '%s.oldMaxX' % SRG, 10)
        
        cmds.connectAttr( '%s.localSpace' % self.target, '%s.valueX' % SRG )
        cmds.connectAttr( '%s.outValueX' % SRG, '%s.weight' % self.namePBD )
        
        
"""        
S = spaceSwitch( 'pCube1_CON', 'pCube2_CON', 'pCube3_CON' )
S.createSpace()
S.spaceBlend()
S.setSpaceSwitch()
"""