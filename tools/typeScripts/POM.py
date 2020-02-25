import maya.cmds as cmds
import string
import json
import os


class PropertiesOfMatter:
    def __init__(self):
        
        self.sceneFullName = cmds.file( sceneName=True, q=True )
        self.sceneFileName = cmds.file( sceneName=True, shortName=True, q=True )
		
        nucleusList = cmds.ls( type='nucleus' )
        nClothList = cmds.ls( type='nCloth' )
        hairSystemList = cmds.ls( type='hairSystem' )
        fieldList = cmds.ls( type='field' )
        
        self.dnyNodeList = nucleusList + nClothList + hairSystemList + fieldList
        
        self.dnyNodeAttrList = []
        
        for i in range( len(self.dnyNodeList) ):
            self.dnyNodeAttrList.append( cmds.listAttr( self.dnyNodeList[i], keyable=True, visible=True, connectable=True, multi=True, output=True ) )
            
    def jsonDump(self):
        # properties of matter
        POM = {}
        
        count = 0
        while count < len( self.dnyNodeList ):
            POM[self.dnyNodeList[count]] = {}
            
            for i in range( len(self.dnyNodeAttrList[count]) ):
                value = cmds.getAttr( '%s.%s' % ( self.dnyNodeList[count], self.dnyNodeAttrList[count][i] ) )
                
                POM[self.dnyNodeList[count]][self.dnyNodeAttrList[count][i]] = value
                
            count = count + 1
            
        #print POM
        
        dataPath = os.path.abspath( self.sceneFullName.split( self.sceneFileName )[0] + '/../data/dynamicPOM/' )
        
        # make dir
        if not os.path.isdir( dataPath ):
            os.makedirs( dataPath )
            print 'make dynamicPOM DIR'
        else:
            print 'already DIR'
            
        jsonPath = dataPath + '/' + self.sceneFileName.split('.')[0] + '.json'
        
        # write
        with open( jsonPath, 'w' ) as outFile:
            outFile.write(json.dumps( POM, indent = 4 ))
            
            print jsonPath
            
            
"""            
POM = PropertiesOfMatter()
dir(POM)
POM.jsonDump()
"""

