tList = [u'L_template_hip_LOC', u'L_template_knee_LOC', u'L_template_ankle_LOC', u'L_template_ball_LOC', u'L_template_toe_LOC', u'L_template_toeTip_LOC']
templateJoint = []

for x in range( len(tList) ):
    tJoint = cmds.joint( tList[x], n=tList[x].replace( 'LOC', 'JNT' ) )
    templateJoint.append(tJoint)
    
for x in range( len(templateJoint)-1 ):
    cmds.parent( templateJoint[x+1], templateJoint[x] )

cmds.parent( templateJoint[0], w=True )