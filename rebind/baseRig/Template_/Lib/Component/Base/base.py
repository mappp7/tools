import maya.cmds as cmds
import Template.Lib.Util.util as util
import os
import Template.Tool.ComponentManager.globalPath as globalPath

class baseComponent(object):
    def __init__(self, name):
        self.name = name
        self.fitNode = None
        self.component_str = self.name
        self.component_val = 'base'
        self.fitComponent_str = 'fit'
        self.moduleComponent_str = 'module'
        self.componentType_str = ''
        self.pathInfo = globalPath.globalPath('Base')
        self.templateDir = self.pathInfo.templateDirPath
        self.file_extenstion_str = 'ma'
        self.fitNodeInfo = {}
        self.fitMatchDic = {}
        self.fitNamespace = ''
        self.moduleNameSpace = ''
        self.currentNamespace = ':'
        self.outputs = {}
        self.modulePathDic = {}
        self.filterGroupNodeDic = {}
        self.filterStrList = ['upbody', 'chest', 'hip', 'head']
        self.snapOps = []
        self.setCurrentNamespace(self.currentNamespace)

        self._side = 'M'
        self._childPlugNodes = {}
        self._parentSocketNodes = {}
        self._useConnectionConNodes = {}
        
        self._params = [{
            'name' : 'live Connection',
            'type' : 'checkBox',
            'default' : False,
            'value': False,
            'callback': 'test'
            }]
    @property
    def childPlugNodes(self):
        return self._childPlugNodes

    @property
    def parentSocketNodes(self):
        return self._parentSocketNodes

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value

    def prepNamespace(self):
        self.componentType_str = self.setComponentType('fit')
        self.fitNamespace = util.prepNamespace(self._side, self.component_str, self.fitComponent_str)
        self.moduleNameSpace = self.fitNamespace.replace(self.fitComponent_str, self.moduleComponent_str)
        return

    def reloadFit(self):
        util.fileLoad(self.componentType_str, self.templateDir, self.component_val, self.fitNamespace, self.file_extenstion_str)
        self.fitNodeInfo = self.getFitNodeInfo(self.fitNamespace, self.component_val)
        self.setCurrentNamespace(self.fitNamespace)

    def reloadModule(self):
        self.componentType_str = self.setComponentType(self.moduleComponent_str)
        util.fileLoad(self.componentType_str, self.templateDir, self.component_val, self.moduleNameSpace, self.file_extenstion_str)
        self.setCurrentNamespace(self.moduleNameSpace)

    def deleteComponent(self, namespaceStr):
        cmds.select(clear=True)
        dependants = []
        self.setCurrentNamespace(namespaceStr)
        dependants = cmds.namespaceInfo(lod=True, dp=True, fn=True)
        cmds.select(clear=True)
        cmds.select(dependants)
        selecteds = cmds.ls(selection=True, l=True)
        if dependants != None and selecteds != []:
            cmds.delete(selecteds)
        if cmds.namespace(exists=namespaceStr):
            cmds.namespace( set=':')
            cmds.namespace( rm=namespaceStr, mnr=True, f=True )
            
    def getFitNodeInfo(self, fitNamespace, fitCompoenent):
        fitNodeInfo = util.getFitInfo(fitNamespace, fitCompoenent)
        return fitNodeInfo

    def setCurrentNamespace(self, namespaceStr):
        currentNamespace = cmds.namespace(setNamespace=namespaceStr)
        self.currentNamespace = currentNamespace
        return self.currentNamespace

    def setComponentType(self, compType):
        if compType == 'fit':
            componentType_str = self.fitComponent_str
        else:
            componentType_str = self.moduleComponent_str
        return componentType_str

    def updateVariables(self):

        self.topFitNodeStr = self.fitNamespace[1:] + ':' + self.component_val + '_fit_system'
        self.fitNodeInfo = self.getFitNodeInfo(self.fitNamespace, self.component_val)
        self.modulePathDic = self.setModulePathVariable()
        self.outputs = self.getNodeList()
        self.filterGroupNodeDic = self.getNodeGroupByFilter()
        self.fitMatchDic = self.createMatchDic(self.fitNodeInfo, self.filterGroupNodeDic['init'])
        self._parentSocketNodes, self._childPlugNodes = self.setConnectionInfo()
        
    def setModulePathVariable(self):
        self.modulePathDic['top'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':' + self.component_val + '_system'
        self.modulePathDic['init'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':init'
        self.modulePathDic['control'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_control'
        self.modulePathDic['input'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_input'
        self.modulePathDic['output'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_output'
        return self.modulePathDic

    def getNodeList(self):
        util.getChildrenNodes(self.modulePathDic['top'], '', self.outputs, 1)
        return self.outputs

    def getNodeGroupByFilter(self):
        initNodes = {}
        motionOutputPlacementNodes = {}
        motionOutputSocketNodes = {}
        motionOutputNodes = {}
        motionOutputSpaceNodes = {}
        controlPlacementNodes = {}
        controlSpaceNodes = {}
        controlPlugNodes = {}
        fkConNodes = {}
        spaceRefNodes = {}

        for key in self.outputs.iterkeys():
            if self.outputs[key]['parent'] == self.modulePathDic['top']:
                if key.rfind(self.modulePathDic['init'][1:]) != -1:
                    util.getChildrenNodes(key, 'init', initNodes, 1)
                elif key.rfind(self.modulePathDic['output'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionOutputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'parent_socket', motionOutputSocketNodes, 1)
                    util.getChildrenNodes(key, 'node', motionOutputNodes, 1)
                    util.getChildrenNodes(key, 'space', motionOutputSpaceNodes, 1)
                elif key.rfind(self.modulePathDic['control'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', controlPlacementNodes, 1)
                    util.getChildrenNodes(key, 'child_plug', controlPlugNodes, 1)
                    util.getChildrenNodes(key, 'fk_Con', fkConNodes, 1)
                    util.getChildrenNodes(key, 'ref', spaceRefNodes, 1)
                    util.getChildrenNodes(key, 'space', controlSpaceNodes, 1)
                else:
                    continue

        self.filterGroupNodeDic['init'] = initNodes
        self.filterGroupNodeDic['outputPlacement'] = motionOutputPlacementNodes
        self.filterGroupNodeDic['outputParentSocket'] = motionOutputSocketNodes
        self.filterGroupNodeDic['outputNode'] = motionOutputNodes
        self.filterGroupNodeDic['outputSpace'] = motionOutputSpaceNodes
        self.filterGroupNodeDic['controlPlacement'] = controlPlacementNodes
        self.filterGroupNodeDic['controlChildPlug'] = controlPlugNodes
        self.filterGroupNodeDic['controlFkCon'] = fkConNodes
        self.filterGroupNodeDic['controlRef'] = spaceRefNodes
        self.filterGroupNodeDic['controlSpace'] = controlSpaceNodes
        return self.filterGroupNodeDic

    def setConnectionInfo(self):
        parentSocketNodes = {}
        childPlugNodes = {}
        for socketNode in self.filterGroupNodeDic['outputParentSocket'].keys():
            socketLocalNode = util.fullPathName2Local(socketNode)
            parentSocketNodes[socketLocalNode[1]] = socketNode
        if self.filterGroupNodeDic['controlChildPlug'] != None:
            for plugNode in self.filterGroupNodeDic['controlChildPlug'].keys():
                plugLocalNode = util.fullPathName2Local(plugNode)
                childPlugNodes[plugLocalNode[1]] = plugNode
        return parentSocketNodes, childPlugNodes

    def createMatchDic(self, fitNodeInfo, initNodes):
        fitMatchDic = {}
        for match in fitNodeInfo.iterkeys():
            for initNode in initNodes.keys():
                initNodeLocal = util.fullPathName2Local(initNode)
                if initNodeLocal[1].replace('_init','') == match:
                    fitMatchDic[match] = initNode
        return fitMatchDic

    def updateInitByFit(self, liveConnection=False):
        snapOps = []
        
        self.fitNodeInfo = self.getFitNodeInfo(self.fitNamespace, self.component_val)
        initNodeFullName = cmds.ls(self.modulePathDic['init'], l=True)[0]
        
        for match in self.fitNodeInfo.iterkeys():
            matrixOps = util.localMatrixOp(self.moduleNameSpace, match + '_init')
            snapOps += matrixOps
            if match == 'root' or match == 'body':
                cmds.connectAttr(initNodeFullName+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=False)
                cmds.connectAttr(self.fitNodeInfo[match]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=False)
                util.decompChannelBinding(matrixOps[1], self.fitMatchDic[match])
            else:
                cmds.connectAttr(self.fitMatchDic['body']+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=False)
                cmds.connectAttr(self.fitNodeInfo[match]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=False)
                util.decompChannelBinding(matrixOps[1], self.fitMatchDic[match])

        liveConnection = self.params[0]['value']
        if liveConnection != True:
            if snapOps != None:
                cmds.delete(snapOps)
            return None
        else:
            return snapOps

    def sceneCleanupAndPrep(self):
        self.deleteComponent(self.fitNamespace)
        systemNode = util.namespace2Prefix(self.moduleNameSpace)
        componentNs = ':'+ self._side + ':' + self.component_str
        if cmds.namespace(exists=componentNs):
            cmds.namespace( rm=componentNs, mnr=True, f=True )
        return systemNode

    def applyInitNodeConnections(self):

        rootNode = None
        controlNode = None
        outputPlacementNode = None
        initNodeLocal = None
        filterStr = 'root'

        for initNode in self.filterGroupNodeDic['init'].iterkeys():
            initNodeLocal = util.fullPathName2Local(initNode)
            if initNodeLocal[1].rfind(filterStr) != -1:
                rootNode = initNode
        for outPNode in self.filterGroupNodeDic['outputPlacement'].iterkeys():
            outPNodeLocal = util.fullPathName2Local(outPNode)
            if outPNodeLocal[1].rfind(filterStr) != -1: #and initNodeLocal[1].rfind('upbody') == -1:
                outputPlacementNode = outPNode
        for controlPNode in self.filterGroupNodeDic['controlPlacement'].iterkeys():
            controlPNodeLocal = util.fullPathName2Local(controlPNode)
            if controlPNodeLocal[1].rfind(filterStr) != -1:
                controlNode = controlPNode

        util.transformChannelBinding(rootNode, controlNode)
        util.transformChannelBinding(rootNode, outputPlacementNode)

        filterStr = 'body'
        matrixOp = []
        bodyInitNode = None
        bodySocketNode = None

        for outPNode in self.filterGroupNodeDic['outputPlacement'].iterkeys():
            outPNodeLocal = util.fullPathName2Local(outPNode)
            if outPNodeLocal[1].rfind(filterStr) != -1 and outPNodeLocal[1].rfind('upbody') == -1:
                outputPlacementNode = outPNode
        for controlPNode in self.filterGroupNodeDic['controlPlacement'].iterkeys():
            controlPNodeLocal = util.fullPathName2Local(controlPNode)
            if controlPNodeLocal[1].rfind(filterStr) != -1:
                controlNode = controlPNode

        for initNode in self.filterGroupNodeDic['init'].iterkeys():
            initNodeLocal = util.fullPathName2Local(initNode)
            if initNodeLocal[1].rfind(filterStr) != -1 and initNodeLocal[1].rfind('upbody') == -1:
                bodyInitNode = initNode
                matrixOps = util.localMatrixOp(self.moduleNameSpace, filterStr+'_init')

        cmds.connectAttr(rootNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(bodyInitNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)

        util.decompChannelBinding(matrixOps[1], controlNode)
        util.decompChannelBinding(matrixOps[1], outputPlacementNode)

        for socketNode in self.filterGroupNodeDic['outputParentSocket']:
            socketLocalNode = util.fullPathName2Local(socketNode)
            if socketLocalNode[1].rfind(filterStr) != -1 and socketLocalNode[1].rfind('upbody') == -1:
                bodySocketNode = socketNode

        bodyNegYOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', filterStr+'_space_neg_y')
        cmds.setAttr(bodyNegYOp+'.input2Y', -1)
        cmds.connectAttr(outputPlacementNode+'.translate', bodyNegYOp+'.input1', f=True)
        cmds.connectAttr(bodyNegYOp+'.outputY', bodySocketNode+'.translateY', f=True)

        upbodyInitNode = None
        chestInitNode = None
        hipInitNode = None
        headInitNode = None

        for initNode in self.filterGroupNodeDic['init'].iterkeys():
            initNodeLocal = util.fullPathName2Local(initNode)
            if initNodeLocal[1].rfind(self.filterStrList[0]) != -1:
                upbodyInitNode = initNode
            elif initNodeLocal[1].rfind(self.filterStrList[1]) != -1:
                chestInitNode = initNode
            elif initNodeLocal[1].rfind(self.filterStrList[2]) != -1:
                hipInitNode = initNode
            elif initNodeLocal[1].rfind(self.filterStrList[3]) != -1:
                headInitNode = initNode
            else:
                continue

        upbodyOutputNodes = []
        chestOutputNodes = []
        hipOutputNodes = []
        headOutputNodes = []

        for outPNode in self.filterGroupNodeDic['outputPlacement'].iterkeys():
            outPNodeLocal = util.fullPathName2Local(outPNode)
            if outPNodeLocal[1].rfind(self.filterStrList[0]) != -1:
                upbodyOutputNodes.append(outPNode)
            elif outPNodeLocal[1].rfind(self.filterStrList[1]) != -1:
                chestOutputNodes.append(outPNode)
            elif outPNodeLocal[1].rfind(self.filterStrList[2]) != -1:
                hipOutputNodes.append(outPNode)
            elif outPNodeLocal[1].rfind(self.filterStrList[3]) != -1:
                headOutputNodes.append(outPNode)
            else:
                continue

        upbodyControlNodes = []
        chestControlNodes = []
        hipControlNodes = []
        headControlNodes = []

        for controlPNode in self.filterGroupNodeDic['controlPlacement'].iterkeys():
            controlPNodeLocal = util.fullPathName2Local(controlPNode)
            if controlPNodeLocal[1].rfind(self.filterStrList[0]) != -1:
                upbodyControlNodes.append(controlPNode)
            elif controlPNodeLocal[1].rfind(self.filterStrList[1]) != -1:
                chestControlNodes.append(controlPNode)
            elif controlPNodeLocal[1].rfind(self.filterStrList[2]) != -1:
                hipControlNodes.append(controlPNode)
            elif controlPNodeLocal[1].rfind(self.filterStrList[3]) != -1:
                headControlNodes.append(controlPNode)
            else:
                continue

        upbodyConnections = upbodyOutputNodes + upbodyControlNodes
        for upbodyConnection in upbodyConnections:
            util.transformChannelBinding(upbodyInitNode, upbodyConnection)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, self.filterStrList[1]+'_init')
        cmds.connectAttr(upbodyInitNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(chestInitNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)

        util.decompChannelBinding(matrixOps[1], chestControlNodes[0])
        util.decompChannelBinding(matrixOps[1], chestOutputNodes[0])

        util.transformChannelBinding(hipInitNode, hipOutputNodes[0])
        util.transformChannelBinding(hipInitNode, hipControlNodes[0])

        matrixOps = util.localMatrixOp(self.moduleNameSpace, self.filterStrList[3]+'_init')
        cmds.connectAttr(chestInitNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(headInitNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)

        util.decompChannelBinding(matrixOps[1], headControlNodes[0])
        util.decompChannelBinding(matrixOps[1], headOutputNodes[0])


    def applyMotionNodeConnections(self):

        bodyNode= None
        bodyFkCons = {}
        for fkConNode in self.filterGroupNodeDic['controlFkCon']:
            fkConLocalNode = util.fullPathName2Local(fkConNode)
            if fkConLocalNode[1].rfind('space') == -1:
                if fkConLocalNode[1].rfind('body') != -1 and fkConLocalNode[1].rfind('upbody') == -1:
                    if fkConLocalNode[1].rfind('piv') != -1:
                        bodyFkCons['piv'] = fkConNode
                    else:
                        bodyFkCons['con'] = fkConNode
                fkLocalNodeStr = fkConLocalNode[1].replace('fk_Con', 'node')
                for motionOutputNode in self.filterGroupNodeDic['outputNode']:
                    motionOutputLocalNode = util.fullPathName2Local(motionOutputNode)
                    if motionOutputLocalNode[1].rfind('body') != -1 and motionOutputLocalNode[1].rfind('upbody') == -1:
                        bodyNode = motionOutputNode
                    if motionOutputLocalNode[1] == fkLocalNodeStr:
                        util.transformChannelBinding(fkConNode, motionOutputNode)

        cmds.connectAttr(bodyFkCons['piv']+'.translate', bodyFkCons['con']+'.rotatePivot', f=True)
        cmds.connectAttr(bodyFkCons['piv']+'.translate', bodyNode+'.rotatePivot', f=True)

        upbody_hip_blend_socket_node = None
        for socketNode in self.filterGroupNodeDic['outputParentSocket']:
            if socketNode.rfind('upbody') != -1 and socketNode.rfind('hip') != -1:
                upbody_hip_blend_socket_node = socketNode

        targetNodes = []
        for motionOutputNode in self.filterGroupNodeDic['outputNode']:
            motionOutputLocalNode = util.fullPathName2Local(motionOutputNode)
            if motionOutputLocalNode[1].rfind('upbody') != -1 or motionOutputLocalNode[1].rfind('hip') != -1 and motionOutputLocalNode[1].rfind('placement') == -1:
                targetNodes.append(motionOutputNode)

        upbody_hip_blend_ori = cmds.orientConstraint(targetNodes[0], targetNodes[1], upbody_hip_blend_socket_node)
        upbody_hip_blend_pos = cmds.pointConstraint(targetNodes[0], targetNodes[1], upbody_hip_blend_socket_node)

        hipFkCon = None
        headFkCon = None
        for fkConNode in self.filterGroupNodeDic['controlFkCon']:
            fkConLocalNode = util.fullPathName2Local(fkConNode)
            if fkConLocalNode[1].rfind('hip') != -1 and fkConLocalNode[1].rfind('space') == -1:
                hipFkCon = fkConNode
            elif fkConLocalNode[1].rfind('head') != -1 and fkConLocalNode[1].rfind('space') == -1 and fkConLocalNode[1].rfind('comp') == -1:
                headFkCon = fkConNode
            else:
                continue

        check = cmds.attributeQuery('hip_nodeW0', node=upbody_hip_blend_pos[0], ex=True )
        attr = ''
        if check:
            attr = 'hip_nodeW0'
        else:
            attr = 'hip_nodeW1'

        cmds.connectAttr(hipFkCon+'.hipPosWeight', upbody_hip_blend_pos[0] + '.' + attr, f=True)
        check = cmds.attributeQuery('hip_nodeW0', node=upbody_hip_blend_ori[0], ex=True )
        attr = ''
        if check:
            attr = 'hip_nodeW0'
        else:
            attr = 'hip_nodeW1'
        cmds.connectAttr(hipFkCon+'.hipOriWeight', upbody_hip_blend_ori[0] + '.' + attr, f=True)

        headCompSpaceOp = util.createOpNode(self.moduleNameSpace, 'choice', self.filterStrList[3]+'_compSpace_selector')

        spaceRefNodeList = self.filterGroupNodeDic['controlRef'].keys()
        for i in range(len(spaceRefNodeList)):
            cmds.connectAttr(spaceRefNodeList[i]+'.worldMatrix', headCompSpaceOp+'.input['+str(i)+']', f=True)

        cmds.connectAttr(headFkCon+'.headCompSpace', headCompSpaceOp+'.selector', f=True)

        headConPlacementNode = None
        for controlPNode in self.filterGroupNodeDic['controlPlacement'].iterkeys():
            controlPNodeLocal = util.fullPathName2Local(controlPNode)
            if controlPNodeLocal[1].rfind(self.filterStrList[3]) != -1:
                headConPlacementNode = controlPNode

        matrixOps = util.localMatrixOp(self.moduleNameSpace, self.filterStrList[3]+'_compSpace_cal')
        cmds.connectAttr(headCompSpaceOp+'.output', matrixOps[0]+'.matrixIn[0]', f=True)
        cmds.connectAttr(headConPlacementNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        headCompWeightApplyOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', self.filterStrList[3]+'_compWeight_apply')
        cmds.connectAttr(matrixOps[1]+'.outputRotate', headCompWeightApplyOp+'.input1', f=True)
        cmds.connectAttr(headFkCon+'.headCompWeight', headCompWeightApplyOp+'.input2X', f=True)
        cmds.connectAttr(headFkCon+'.headCompWeight', headCompWeightApplyOp+'.input2Y', f=True)
        cmds.connectAttr(headFkCon+'.headCompWeight', headCompWeightApplyOp+'.input2Z', f=True)
        cmds.setAttr(headCompWeightApplyOp+'.operation', 1)

        headConCompSpaceNode = None
        for controlSpaceNode in self.filterGroupNodeDic['controlSpace'].iterkeys():
            controlSpaceLocalNode = util.fullPathName2Local(controlSpaceNode)
            if controlSpaceLocalNode[1].rfind('head_fk') != -1 and controlSpaceLocalNode[1].rfind('comp') != -1:
                headConCompSpaceNode = controlSpaceNode
        cmds.connectAttr(headCompWeightApplyOp+'.output', headConCompSpaceNode+'.rotate', f=True)

        headOutputSpaceNode = None
        for motionOutputSpaceNode in self.filterGroupNodeDic['outputSpace'].iterkeys():
            motionOutputSpaceLocalNode = util.fullPathName2Local(motionOutputSpaceNode)
            if motionOutputSpaceLocalNode[1].rfind('head') != -1:
                headOutputSpaceNode = motionOutputSpaceNode
        cmds.connectAttr(headConCompSpaceNode+'.rotate', headOutputSpaceNode+'.rotate', f=True)
