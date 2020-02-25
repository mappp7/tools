
import maya.cmds as cmds
import MASH.api as mapi

targetList = cmds.ls(sl=True)

def overlappingMash( targetList ):

    cmds.select(cl=True)
    mashNetwork = mapi.Network()
    mashNetwork.createNetwork( name='MASH1', distributionStyle=7 )
    mashNetwork.setPointCount( len(targetList) )

    for x in range( len(targetList) ):
        locatorName = cmds.spaceLocator()[0]
        cmds.parentConstraint( targetList[x], locatorName )
        cmds.connectAttr( '%s.worldMatrix[0]' % locatorName, '%s.initialStateMatrix[%s]' % ( mashNetwork.distribute, x ) )

    idNode = mashNetwork.addNode( 'MASH_ID' )
    cmds.setAttr( idNode.name + '.numObjects', len(targetList) )

    pointNode = mashNetwork.addNode( 'MASH_Points' )

    delayNode = mashNetwork.addNode( 'MASH_Delay' )
    cmds.setAttr( delayNode.name + '.timeStep', 1)

    springNode = mashNetwork.addNode( 'MASH_Spring' )

    # output node create

    breakoutNode = mashNetwork.addNode( 'MASH_Breakout' )

    outputList = []
    for x in range( len(targetList) ):
        outputLocator = cmds.spaceLocator( name=targetList[x].replace( 'JNT', 'mashLoc' ) )[0]
        outputList.append( outputLocator )

        cmds.connectAttr( '%s.outputs[%s].translate' % ( breakoutNode.name, x ), outputLocator + '.translate' )


    for x in range( len(outputList)-1 ):
        cmds.aimConstraint( outputList[x+1], outputList[x], aimVector=[ 1, 0, 0 ], upVector=[ 0, 1, 0 ], worldUpType='objectrotation', worldUpObject=targetList[0] )

    cmds.orientConstraint( outputList[-2], outputList[-1] )



selected = cmds.ls(sl=True)

for i in range( len(selected) ):
    targetList = cmds.ls( selected[i], dag=True, type='joint' )[1:]
    overlappingMash( targetList )


