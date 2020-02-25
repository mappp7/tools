import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaUI as omu
#cmds.getAttr("defaultResolution.width")
lenIter = int(2000)
cam,camShape = cmds.camera()
mdag_path = om.MDagPath()
sel = om.MSelectionList()
sel.add(cam)
sel.getDagPath(0, mdag_path)

frustum_objs = []

for i in range(lenIter):
    
    draw_traversal = omu.MDrawTraversal()
    draw_traversal.setFrustum(mdag_path , i,i)
    draw_traversal.traverse()
    
    for i in range(draw_traversal.numberOfItems()):
        shape_dag = om.MDagPath()
        draw_traversal.itemPath(i,shape_dag)
        transform_dag = om.MDagPath()
        om.MDagPath.getAPathTo(shape_dag.transform(),transform_dag)
        obj = transform_dag.fullPathName()
        
        if not obj in frustum_objs :
            if cmds.objExists(obj):
                print obj
                frustum_objs.append(obj)
        
cmds.select(frustum_objs)



len(cmds.ls(sl=1))

a = cmds.ls(sl=1)
#a.sort()
#b = cmds.ls(sl=1)
#b.sort()

w = cmds.wire(a[1],w = a[0],gw=0,en=1,ce=0,li=0)
cmds.wire(w[0],e=1,dds=[(0,99999)])