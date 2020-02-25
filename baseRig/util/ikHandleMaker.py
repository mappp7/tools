import maya.cmds as cmds
#solver(ikRPsolver,ikSplineSolver)
def ikHandleMaker( starJoint, endJoint, solver, *gCurve ):
    if len(gCurve) == 1:
        IKH = cmds.ikHandle( sj=starJoint, ee=endJoint, sol=solver, ccv=False , roc =True, pcv=False, c=gCurve[0] )
    else:
        IKH = cmds.ikHandle( sj=starJoint, ee=endJoint, sol=solver, ccv=True, scv=False )
    return IKH

"""
ikHandleMaker( 'joint6', 'joint9', 'ikSplineSolver', 'curve2' )

ikHandleMaker( 'joint10', 'joint13', 'ikSplineSolver', 'curve3' )

ikHandleMaker( 'joint14', 'joint16', 'ikRPsolver' )
"""