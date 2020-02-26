import maya.cmds as cmds
import maya.mel as mel

import os

#filePath = '/show/wwd/shot/BEAT/BEAT_0010/cloth/dev/scenes/'
#fileNmae = 'BEAT_0010_cloth_v03_w01_test.mb'

def nCacheMaker( filePath, fileName ):
    cmds.file( force=True, new=True )
    
    cmds.file( filePath + fileName + '.mb', force=True, open=True )
    print '!!!!!!!!!! OPEN !!!!!!!!!!'
    cmds.select( cl=True )
    #merge usd, inputChange, timeSlide and startFrame
 

    clothShape = cmds.ls( type='nCloth' )
    cmds.select( clothShape )
    
    basePath = os.path.abspath( filePath + '/../' )
    
    mel.eval("""doCreateNclothCache 5 { "2", "1", "10", "OneFile", "1", "%s/data/testNcache/%s","0","","0", "add", "0", "1", "1","0","1","mcx" } ;""" % ( basePath, fileName ))
    
    print 'OK!!!!!!!!!!!!!!!'
    
    cmds.file( force=True, save=True )
    
    print 'OK'
