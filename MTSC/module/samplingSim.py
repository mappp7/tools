import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma

def trimTimeRange(start, end):

    animCtrl = oma.MAnimControl()
    startTime = om.MTime(start)
    endTime = om.MTime(end)
    animCtrl.setAnimationStartEndTime (startTime, endTime)
    animCtrl.setMinMaxTime(startTime, endTime) 

def blendShapeSampling(node, interval=1):

    assert cmds.nodeType(node) == 'blendShape', \
        "node must be a blendShape type"
    start = cmds.currentTime(q=1)
    
    attrs = cmds.listAttr('%s.weight' % node, m=1)
    attrData = {node: [[attr, 0.0, 1.0] for attr in attrs]}
    
    currTime = attrsSampling(attrData, interval)

    end = currTime-1
    trimTimeRange(start, end)
    cmds.currentTime(start)    

def attrSampling(node, attr, minVal, maxVal, interval=1):
    
    currTime = cmds.currentTime(q=1)
    currVal = cmds.getAttr('%s.%s' % (node, attr))
    vals = [currVal, currVal+minVal, currVal+maxVal, currVal]

    for i, v in enumerate(vals):
        if i not in [0, len(vals)-1] and (currVal - v) == 0:
            continue
        
        cmds.setKeyframe(node, at=attr, v=v, t=currTime)
        currTime += interval
    return currTime
    
def attrsSampling(attrData, interval=1):

    currTime = cmds.currentTime(q=1)
    for node, attrVals in attrData.iteritems():        
        for vals in attrVals:
            attr, minVal, maxVal = vals
            if not cmds.objExists('.'.join([node, attr])):
                continue
            currTime = attrSampling(node, attr, minVal, maxVal, interval)
            currTime -= 2 * interval
            cmds.currentTime(currTime)
    return currTime+1 * interval