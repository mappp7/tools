import maya.app.type.typeToolSetup as TEXT
import string

TEXT.createTypeTool()

##############################################################################


ST = 'Text write test !!\ngravity : %s' % 9.8

hex = []
for x in ST:
    hex.append(x.encode('hex'))

HC = string.join( hex, ' ' )

cmds.setAttr( 'type1.textInput', HC, type="string" )
cmds.setAttr( 'typeExtrude1.enableExtrusion', 0 )
cmds.setAttr( 'typeBlinn.color', 1, 0, 0, type='double3' )


