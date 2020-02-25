import maya.cmds as cmds
import Template.Lib.Util.util as util
import os
import Template.Tool.ComponentManager.globalPath as globalPath

class footComponent(object):
    def __init__(self, name):
        self.name = name
        self.fitNode = None
        self.component_str = self.name
        self.component_val = 'foot'
        self.fitComponent_str = 'fit'
        self.moduleComponent_str = 'module'
        self.componentType_str = ''
        self.pathInfo = globalPath.globalPath('Foot')
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
        self.fitMatchDic = {}
        self.filterStrList = ['heel', 'tip', 'ball']
        self.snapOps = []
        self.setCurrentNamespace(self.currentNamespace)

        self._side = 'R'
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
        self.topFitNodeStr = self.fitNamespace[1:] + ':' + self.component_val + '_fit_system'
        fitSpaceNodeStr = self.topFitNodeStr + '|' + self.fitNamespace[1:] + ':foot'
        if self._side == 'L':
            transX = cmds.getAttr(fitSpaceNodeStr+'.translateX')
            transX_neg = transX * -1
            cmds.setAttr(fitSpaceNodeStr+'.translateX', transX_neg)        
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
        self._parentSocketNodes, self._childPlugNodes, self._useConnectionConNodes = self.setConnectionInfo()

    def setModulePathVariable(self):
        self.modulePathDic['top'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':' + self.component_val + '_system'
        self.modulePathDic['init'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':init'
        self.modulePathDic['control'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_control'
        self.modulePathDic['input'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_input'
        self.modulePathDic['output'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_output'
        self.modulePathDic['outputOffset'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_output_offset'
        return self.modulePathDic

    def getNodeList(self):
        util.getChildrenNodes(self.modulePathDic['top'], '', self.outputs, 1)
        return self.outputs

    def getNodeGroupByFilter(self):

        initNodes = {}

        motionInputPlacementNodes = {}
        motionInputPlugNodes = {}

        motionOutputPlacementNodes = {}
        motionOutputNodes = {}
        motionOutputSpaceNodes = {}

        motionOutputoffsetPlacementNodes = {}
        motionOutputOffsetSocketNodes = {}
        motionOutputOffsetNodes = {}
        motionOutputOffsetSpaceNodes = {}

        controlPlacementNodes = {}
        controlSpaceNodes = {}
        fkConNodes = {}

        spaceWeightNode = {}

        for key in self.outputs.iterkeys():
            if self.outputs[key]['parent'] == self.modulePathDic['top']:
                if key.rfind(self.modulePathDic['init'][1:]) != -1:
                    util.getChildrenNodes(key, 'init', initNodes, 1)

                elif key.rfind(self.modulePathDic['input'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionInputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'child_plug', motionInputPlugNodes, 1)

                elif key.rfind(self.modulePathDic['output'][1:]) != -1 and key.rfind(self.modulePathDic['outputOffset'][1:]) == -1:
                    util.getChildrenNodes(key, 'placement', motionOutputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'space', motionOutputSpaceNodes, 1)
                    util.getChildrenNodes(key, '', motionOutputNodes, 1)

                elif key.rfind(self.modulePathDic['outputOffset'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionOutputoffsetPlacementNodes, 1)
                    util.getChildrenNodes(key, 'parent_socket', motionOutputOffsetSocketNodes, 1)
                    util.getChildrenNodes(key, 'node', motionOutputOffsetNodes, 1)
                    util.getChildrenNodes(key, 'space', motionOutputOffsetSpaceNodes, 1)

                elif key.rfind(self.modulePathDic['control'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', controlPlacementNodes, 1)
                    util.getChildrenNodes(key, 'fk_Con', fkConNodes, 1)
                    util.getChildrenNodes(key, 'space', controlSpaceNodes, 1)
                    util.getChildrenNodes(key, 'Weights', spaceWeightNode, 1)

                else:
                    continue

        self.filterGroupNodeDic['init'] = initNodes

        self.filterGroupNodeDic['inputPlacement'] = motionInputPlacementNodes
        self.filterGroupNodeDic['inputChildPlug'] = motionInputPlugNodes

        self.filterGroupNodeDic['outputPlacement'] = motionOutputPlacementNodes
        self.filterGroupNodeDic['outputNode'] = motionOutputNodes
        self.filterGroupNodeDic['outputSpace'] = motionOutputSpaceNodes

        self.filterGroupNodeDic['outputOffsetPlacement'] = motionOutputoffsetPlacementNodes
        self.filterGroupNodeDic['outputOffsetParentSocket'] = motionOutputOffsetSocketNodes
        self.filterGroupNodeDic['outputOffsetNode'] = motionOutputOffsetNodes
        self.filterGroupNodeDic['outputOffsetSpaceNode'] = motionOutputOffsetSpaceNodes

        self.filterGroupNodeDic['controlPlacement'] = controlPlacementNodes
        self.filterGroupNodeDic['controlFkCon'] = fkConNodes
        self.filterGroupNodeDic['controlSpace'] = controlSpaceNodes
        self.filterGroupNodeDic['spaceWeight'] = spaceWeightNode
        return self.filterGroupNodeDic

    def setConnectionInfo(self):
        parentSocketNodes = {}
        childPlugNodes = {}
        useConnectionConNodes = {}
        
        if self.filterGroupNodeDic['outputOffsetParentSocket'] != None:
            for socketNode in self.filterGroupNodeDic['outputOffsetParentSocket'].keys():
                socketLocalNode = util.fullPathName2Local(socketNode)
                parentSocketNodes[socketLocalNode[1]] = socketNode
        if self.filterGroupNodeDic['inputChildPlug'] != None:
            for plugNode in self.filterGroupNodeDic['inputChildPlug'].keys():
                plugLocalNode = util.fullPathName2Local(plugNode)
                childPlugNodes[plugLocalNode[1]] = plugNode
        if self.filterGroupNodeDic['controlFkCon'] != None:
            for plugNode in self.filterGroupNodeDic['controlFkCon'].keys():
                plugLocalNode = util.fullPathName2Local(plugNode)
                customAttributes = cmds.listAttr(plugNode, ud=True)
                if customAttributes != None:
                    for customAttr in customAttributes:
                        if customAttr == 'useConnection':
                            useConnectionConNodes[plugLocalNode[1]] = plugNode
                            
        return parentSocketNodes, childPlugNodes, useConnectionConNodes

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

        initNodeFullName = cmds.ls(self.modulePathDic['init'], l=True)[0]
        for match in self.fitNodeInfo.iterkeys():
            matrixOps = util.localMatrixOp(self.moduleNameSpace, match + '_init')
            snapOps += matrixOps
            if match.rfind('piv') == -1:
                cmds.connectAttr(initNodeFullName+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(self.fitNodeInfo[match]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], self.fitMatchDic[match])
            else:
                cmds.connectAttr(self.fitMatchDic['ball']+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(self.fitNodeInfo[match]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
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

        initNodeFullName = cmds.ls(self.modulePathDic['init'], l=True)[0]
        initNodeParents = []
        for key, value in self.filterGroupNodeDic['init'].iteritems():
            if value['parent'] == initNodeFullName:
                initNodeParents.append(key)

        ballInit = None
        printInit = None
        otherInits = {}
        matrixOpDic = {}
        heelInit = None
        tipInit = None
        footInit = None

        for node in initNodeParents:
            nodeLocalDic = util.fullPathName2Local(node)
            if nodeLocalDic[1].rfind('ball_') != -1:
                ballInit = node
            elif nodeLocalDic[1].rfind('heel_') != -1:
                otherInits['heel'] = node
            elif nodeLocalDic[1].rfind('tip_') != -1:
                tipInit = node
            elif nodeLocalDic[1].rfind('foot_') != -1:
                otherInits['foot'] = node
            else:
                printInit = node
                continue

        for key, value in otherInits.iteritems():
            name = ''
            if key == 'heel':
                name = 'ball_piv_bk'
            else:
                name = key+'_roll'
            matrixOps = util.localMatrixOp(self.moduleNameSpace, name + '_init')
            matrixOpDic[name] = matrixOps
            cmds.connectAttr(ballInit+'.inverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
            cmds.connectAttr(value+'.matrix', matrixOps[0]+'.matrixIn[0]', f=True)

        for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement']:
            nodeList = util.fullPathName2Local(motionOutputPlacementNode)
            if nodeList[1].rfind('ball_piv_bk') != -1:
                util.decompChannelBinding(matrixOpDic['ball_piv_bk'][1], motionOutputPlacementNode, option=0)
            elif nodeList[1].rfind('foot_roll') != -1:
                util.decompChannelBinding(matrixOpDic['foot_roll'][1], motionOutputPlacementNode, option=0)

        #key = 'heel'
        #key2 = 'tip'
        #key3 = 'ball'

        matrixOps = util.localMatrixOp(self.moduleNameSpace, self.filterStrList[2] + '_roll_init')
        cmds.connectAttr(tipInit +'.inverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(ballInit +'.matrix', matrixOps[0]+'.matrixIn[0]', f=True)
        matrixOpDic[self.filterStrList[2] + '_roll'] = matrixOps
        for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement']:
            nodeList = util.fullPathName2Local(motionOutputPlacementNode)
            if nodeList[1].rfind(self.filterStrList[2] + '_roll') != -1:
                util.decompChannelBinding(matrixOpDic[self.filterStrList[2] + '_roll'][1], motionOutputPlacementNode, option=0)

        for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement']:
            nodeList = util.fullPathName2Local(motionOutputPlacementNode)
            if nodeList[1].rfind(self.filterStrList[1] + '_roll') != -1 and nodeList[1].rfind(self.filterStrList[2]) == -1:
                multOp = util.createOpNode(self.moduleNameSpace, "multMatrix", self.filterStrList[2] + '_twist_offset_multM')
                cmds.connectAttr(matrixOpDic[self.filterStrList[2] + '_roll'][0]+'.matrixSum', multOp+'.matrixIn[0]')
                cmds.connectAttr(motionOutputPlacementNode+'.worldMatrix[0]', multOp+'.matrixIn[1]')
                matrixOps = util.localMatrixOp(self.moduleNameSpace, self.filterStrList[2] + '_twist_offset')

                nodeInput = None
                nodeOutput = None
                for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement']:
                    nodeList = util.fullPathName2Local(motionOutputPlacementNode)
                    if nodeList[1].rfind(self.filterStrList[2] + '_roll') != -1:
                        nodeInput = motionOutputPlacementNode
                for motionOutputSpaceNode in self.filterGroupNodeDic['outputSpace']:
                    nodeList = util.fullPathName2Local(motionOutputSpaceNode)
                    if nodeList[1].rfind(self.filterStrList[2] + '_twist') != -1:
                        nodeOutput = motionOutputSpaceNode

                cmds.connectAttr(nodeInput+'.worldInverseMatrix[0]', matrixOps[0]+'.matrixIn[1]')
                cmds.connectAttr(multOp+'.matrixSum', matrixOps[0]+'.matrixIn[0]')
                util.decompChannelBinding(matrixOps[1], nodeOutput, option=0)

                matrixOps = util.localMatrixOp(self.moduleNameSpace, self.filterStrList[2] + '_twist_con')
                for fkConNode in self.filterGroupNodeDic['controlFkCon']:
                    nodeList = util.fullPathName2Local(fkConNode)
                    if nodeList[1].rfind(self.filterStrList[0] + '_twist') != -1:
                        nodeInput = fkConNode
                for controlSpaceNode in self.filterGroupNodeDic['controlSpace']:
                    nodeList = util.fullPathName2Local(controlSpaceNode)
                    if nodeList[1].rfind(self.filterStrList[2] + '_twist') != -1:
                        nodeOutput = controlSpaceNode

                cmds.connectAttr(nodeInput+'.worldInverseMatrix[0]', matrixOps[0]+'.matrixIn[1]')
                cmds.connectAttr(multOp+'.matrixSum', matrixOps[0]+'.matrixIn[0]')
                util.decompChannelBinding(matrixOps[1], nodeOutput, option=0)


        matrixOps = util.localMatrixOp(self.moduleNameSpace, self.filterStrList[2] + '_piv_fnt_init')
        cmds.connectAttr(ballInit +'.inverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(tipInit +'.matrix', matrixOps[0]+'.matrixIn[0]', f=True)
        matrixOpDic[self.filterStrList[2] + '_piv_fnt'] = matrixOps

        for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement']:
            nodeList = util.fullPathName2Local(motionOutputPlacementNode)
            if nodeList[1].rfind(self.filterStrList[2] + '_piv_fnt') != -1:
                util.decompChannelBinding(matrixOpDic[self.filterStrList[2] + '_piv_fnt'][1], motionOutputPlacementNode, option=0)

        matrixOps = util.localMatrixOp(self.moduleNameSpace,  'ball_' + self.filterStrList[1] + '_roll_init')
        cmds.connectAttr(otherInits[self.filterStrList[0]]+'.inverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(tipInit+'.matrix', matrixOps[0]+'.matrixIn[0]', f=True)
        matrixOpDic['ball_' + self.filterStrList[1] + '_roll'] = matrixOps
        for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement']:
            nodeList = util.fullPathName2Local(motionOutputPlacementNode)
            if nodeList[1].rfind('ball_' + self.filterStrList[1] + '_roll') != -1:
                util.decompChannelBinding(matrixOpDic['ball_' + self.filterStrList[1] + '_roll'][1], motionOutputPlacementNode, option=0)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, self.filterStrList[0] + '_twist_init')
        cmds.connectAttr(tipInit+'.inverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(otherInits[self.filterStrList[0]]+'.matrix', matrixOps[0]+'.matrixIn[0]', f=True)
        matrixOpDic[self.filterStrList[0] + '_twist'] = matrixOps
        for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement']:
            nodeList = util.fullPathName2Local(motionOutputPlacementNode)
            if nodeList[1].rfind(self.filterStrList[0] + '_twist') != -1:
                util.decompChannelBinding(matrixOpDic[self.filterStrList[0] + '_twist'][1], motionOutputPlacementNode, option=0)
        for controlPlacementNode in self.filterGroupNodeDic['controlPlacement']:
            nodeList = util.fullPathName2Local(controlPlacementNode)
            if nodeList[1].rfind(self.filterStrList[0] + '_twist') != -1:
                util.decompChannelBinding(matrixOpDic[self.filterStrList[0] + '_twist'][1], controlPlacementNode, option=0)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, self.filterStrList[1] + '_twist_init')
        cmds.connectAttr(printInit+'.inverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(tipInit+'.matrix', matrixOps[0]+'.matrixIn[0]', f=True)
        matrixOpDic[self.filterStrList[1] + '_twist'] = matrixOps
        for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement']:
            nodeList = util.fullPathName2Local(motionOutputPlacementNode)
            if nodeList[1].rfind(self.filterStrList[1] + '_twist') != -1:
                util.decompChannelBinding(matrixOpDic[self.filterStrList[1] + '_twist'][1], motionOutputPlacementNode, option=0)
        for controlSpaceNode in self.filterGroupNodeDic['controlSpace']:
            nodeList = util.fullPathName2Local(controlSpaceNode)
            if nodeList[1].rfind(self.filterStrList[1] + '_twist') != -1:
                util.decompChannelBinding(matrixOpDic[self.filterStrList[1] + '_twist'][1], controlSpaceNode, option=0)

        placementNodesList = []
        placementNodesList.append(self.filterGroupNodeDic['inputPlacement'])
        placementNodesList.append(self.filterGroupNodeDic['outputPlacement'])
        placementNodesList.append(self.filterGroupNodeDic['outputOffsetPlacement'])
        placementNodesList.append(self.filterGroupNodeDic['controlPlacement'])

        footprintPlacements = []
        for placementNodes in placementNodesList:
            for key in placementNodes.keys():
                keyLocal = util.fullPathName2Local(key)
                if keyLocal[1].rfind('footprint') != -1:
                    footprintPlacements.append(key)

        for footprintPlacement in footprintPlacements:
            util.transformChannelBinding(printInit, footprintPlacement)

        for key, value in self.filterGroupNodeDic['init'].iteritems():
            valueLocal = util.fullPathName2Local(value['parent'])
            if valueLocal[1].rfind('ball') != -1:
                keyLocal = util.fullPathName2Local(key)
                prefix = keyLocal[1].replace('init', '')
                for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement'].iterkeys():
                    outNode = util.fullPathName2Local(motionOutputPlacementNode)
                    if outNode[1] == prefix + "placement":
                        cmds.connectAttr(key+'.translate', motionOutputPlacementNode+'.translate', f=True)
                for motionOutputoffsetPlacementNode in self.filterGroupNodeDic['outputOffsetPlacement'].iterkeys():
                    outNode = util.fullPathName2Local(motionOutputoffsetPlacementNode)
                    if outNode[1] == prefix + "placement":
                        cmds.connectAttr(key+'.translate', motionOutputoffsetPlacementNode+'.translate', f=True)
            elif valueLocal[1].rfind('tip') != -1:
                keyLocal = util.fullPathName2Local(key)
                prefix = keyLocal[1].replace('init', '')
                for motionOutputoffsetPlacementNode in self.filterGroupNodeDic['outputOffsetPlacement'].iterkeys():
                    outNode = util.fullPathName2Local(motionOutputoffsetPlacementNode)
                    if outNode[1] == prefix + "placement":
                        cmds.connectAttr(key+'.translate', motionOutputoffsetPlacementNode+'.translate', f=True)
            else:
                continue

    def applyMotionNodeConnections(self):

        for node in self.filterGroupNodeDic['inputChildPlug'].iterkeys():
            nodeLocal = util.fullPathName2Local(node)
            filterStr = nodeLocal[1].replace('_child_plug', '')
            matrixOps = []
            for controlPlacementNode in self.filterGroupNodeDic['controlPlacement'].iterkeys():
                controlPlacementNodeLocal = util.fullPathName2Local(controlPlacementNode)
                if controlPlacementNodeLocal[1].rfind(filterStr) != -1:
                    matrixOps = util.localMatrixOp(self.moduleNameSpace, filterStr + '_plug_con')
                    cmds.connectAttr(controlPlacementNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                    cmds.connectAttr(node+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
            for controlSpaceNode in self.filterGroupNodeDic['controlSpace'].iterkeys():
                controlSpaceNodeLocal = util.fullPathName2Local(controlSpaceNode)
                if controlSpaceNodeLocal[1].rfind(filterStr) != -1:
                    util.decompChannelBinding(matrixOps[1], controlSpaceNode)

            for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement'].iterkeys():
                motionOutputPlacementNodeLocal = util.fullPathName2Local(motionOutputPlacementNode)
                if motionOutputPlacementNodeLocal[1].rfind(filterStr) != -1:
                    matrixOps = util.localMatrixOp(self.moduleNameSpace, filterStr + '_plug_output')
                    cmds.connectAttr(motionOutputPlacementNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                    cmds.connectAttr(node+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
            for motionOutputSpaceNode in self.filterGroupNodeDic['outputSpace'].iterkeys():
                motionOutputSpaceNodeLocal = util.fullPathName2Local(motionOutputSpaceNode)
                if motionOutputSpaceNodeLocal[1].rfind(filterStr) != -1:
                    util.decompChannelBinding(matrixOps[1], motionOutputSpaceNode)

        # motion_input connections

        for fkConNode in self.filterGroupNodeDic['controlFkCon'].iterkeys():
            fkConNodeLocal = util.fullPathName2Local(fkConNode)
            filterStr = fkConNodeLocal[1].replace('_fk_Con', '')
            for motionOutputNode in self.filterGroupNodeDic['outputNode'].iterkeys():
                motionOutputNodeLocal = util.fullPathName2Local(motionOutputNode)
                if motionOutputNodeLocal[1] == filterStr:
                    if filterStr.rfind('twist') != -1:
                        cmds.connectAttr(fkConNode+'.rotateY', motionOutputNode+'.rotateY', f=True)
                    elif filterStr.rfind('piv') != -1:
                        cmds.connectAttr(fkConNode+'.translate', motionOutputNode+'.translate', f=True)
                    else:
                        cmds.connectAttr(fkConNode+'.translate', motionOutputNode+'.translate', f=True)
                        cmds.connectAttr(fkConNode+'.rotate', motionOutputNode+'.rotate', f=True)
            for motionOutputOffsetNode in self.filterGroupNodeDic['outputOffsetNode'].iterkeys():
                motionOutputOffsetNodeLocal = util.fullPathName2Local(motionOutputOffsetNode)
                if motionOutputOffsetNodeLocal[1] == filterStr+'_node':
                    cmds.connectAttr(fkConNode+'.rotate', motionOutputOffsetNode+'.rotate', f=True)

        # motion control fk only

        sourceNode = None
        targetNode = None
        for fkConNode in self.filterGroupNodeDic['controlFkCon'].iterkeys():
            fkConNodeLocal = util.fullPathName2Local(fkConNode)
            if fkConNodeLocal[1].rfind('footprint') != -1:
                if fkConNodeLocal[1].rfind('piv') != -1:
                    sourceNode = fkConNode
                else:
                    targetNode = fkConNode
        cmds.connectAttr(sourceNode+'.translate', targetNode+'.rotatePivot', f=True)
        for motionOutputNode in self.filterGroupNodeDic['outputNode'].iterkeys():
            motionOutputNodeLocal = util.fullPathName2Local(motionOutputNode)
            if motionOutputNodeLocal[1].rfind('footprint') != -1 and motionOutputNodeLocal[1].rfind('space') == -1 and motionOutputNodeLocal[1].rfind('placement') == -1:
                if motionOutputNodeLocal[1].rfind('piv') != -1:
                    sourceNode = motionOutputNode
                else:
                    targetNode = motionOutputNode
        cmds.connectAttr(sourceNode+'.translate', targetNode+'.rotatePivot', f=True)

        # footprint piv connections

        inNode = None
        outNode = None
        fntNode = None
        bkNode = None
        conNode = None
        targetNode = None
        ballrollNode = None
        ballspaceNode = None

        for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement']:
            motionOutputPlacementNodeLocal = util.fullPathName2Local(motionOutputPlacementNode)
            if motionOutputPlacementNodeLocal[1].rfind('ball_piv') != -1:
                if motionOutputPlacementNodeLocal[1].rfind('in') != -1:
                    inNode = motionOutputPlacementNode
                elif motionOutputPlacementNodeLocal[1].rfind('out') != -1:
                    outNode = motionOutputPlacementNode
                elif motionOutputPlacementNodeLocal[1].rfind('fnt') != -1:
                    fntNode = motionOutputPlacementNode
                elif motionOutputPlacementNodeLocal[1].rfind('bk') != -1:
                    bkNode = motionOutputPlacementNode
                else:
                    continue

        for fkConNode in self.filterGroupNodeDic['controlFkCon'].iterkeys():
            fkConNodeLocal = util.fullPathName2Local(fkConNode)
            if fkConNodeLocal[1].rfind('footprint') != -1 and fkConNodeLocal[1].rfind('piv') == -1:
                conNode = fkConNode

        for motionOutputNode in self.filterGroupNodeDic['outputNode'].iterkeys():
            motionOutputNodeLocal = util.fullPathName2Local(motionOutputNode)
            if motionOutputNodeLocal[1].rfind('ball_tip_roll') != -1 and motionOutputNodeLocal[1].rfind('space') == -1 and motionOutputNodeLocal[1].rfind('placement') == -1:
                targetNode = motionOutputNode

        inputConOp = util.createOpNode(self.moduleNameSpace, 'condition', 'ball_roll_inout_piv_cond_op')
        cmds.setAttr(inputConOp+'.operation', 2)
        inputConOpZerooutOp = util.createOpNode(self.moduleNameSpace, 'condition', 'ball_roll_inout_piv_cond_zeroout_op')
        cmds.setAttr(inputConOpZerooutOp+'.operation', 1)
        cmds.setAttr(inputConOpZerooutOp+'.colorIfFalseR', 0)
        cmds.setAttr(inputConOpZerooutOp+'.colorIfFalseG', 0)
        cmds.setAttr(inputConOpZerooutOp+'.colorIfFalseB', 0)
        rotOffsetCompOp = util.createOpNode(self.moduleNameSpace, 'plusMinusAverage', 'rot_offset_from_roll_start_op')
        cmds.setAttr(rotOffsetCompOp+'.operation', 2)
        tipRollConOp = util.createOpNode(self.moduleNameSpace, 'condition', 'tip_roll_cond_op')
        cmds.setAttr(tipRollConOp+'.operation', 3)
        cmds.setAttr(tipRollConOp+'.colorIfFalseR', 0)
        cmds.setAttr(tipRollConOp+'.colorIfFalseG', 0)
        cmds.setAttr(tipRollConOp+'.colorIfFalseB', 0)

        cmds.connectAttr(inNode+'.translate', inputConOp+'.colorIfFalse')
        cmds.connectAttr(outNode+'.translate', inputConOp+'.colorIfTrue')

        rollInOutDirOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', 'roll_inout_dir_op')
        cmds.setAttr(rollInOutDirOp+'.operation', 1)
        cmds.setAttr(rollInOutDirOp+'.input2X', 1)
        cmds.connectAttr(conNode+'.rollInOut', rollInOutDirOp+'.input1X')
        
        if self._side == 'L':
            cmds.setAttr(rollInOutDirOp+'.input2X', -1)

        cmds.connectAttr(rollInOutDirOp+'.outputX', inputConOp+'.firstTerm')
        cmds.connectAttr(rollInOutDirOp+'.outputX', inputConOpZerooutOp+'.firstTerm')
        cmds.connectAttr(rollInOutDirOp+'.outputX', targetNode+'.rotateZ')
        
        cmds.connectAttr(inputConOp+'.outColor', inputConOpZerooutOp+'.colorIfTrue')
        cmds.connectAttr(inputConOpZerooutOp+'.outColor', targetNode+'.rotatePivot')
        cmds.connectAttr(conNode+'.rollFntBk', rotOffsetCompOp+'.input1D[0]')
        cmds.connectAttr(conNode+'.rollCompStart', rotOffsetCompOp+'.input1D[1]')
        cmds.connectAttr(rotOffsetCompOp+'.output1D', tipRollConOp+'.colorIfTrueR')
        cmds.connectAttr(conNode+'.rollFntBk', tipRollConOp+'.firstTerm')
        cmds.connectAttr(conNode+'.rollCompStart', tipRollConOp+'.secondTerm')
        cmds.connectAttr(tipRollConOp+'.outColorR', targetNode+'.rotateX')

        # ball_tip_roll

        for motionOutputNode in self.filterGroupNodeDic['outputNode'].iterkeys():
            motionOutputNodeLocal = util.fullPathName2Local(motionOutputNode)
            if motionOutputNodeLocal[1].rfind('ball_roll') != -1 and motionOutputNodeLocal[1].rfind('space') == -1 and motionOutputNodeLocal[1].rfind('placement') == -1:
                ballrollNode = motionOutputNode

        ball_roll_fntbk_comp_remapOp = util.createOpNode(self.moduleNameSpace, 'remapValue', 'ball_roll_fntbk_comp_remapOp')
        cmds.setAttr(ball_roll_fntbk_comp_remapOp+'.outputMax', 1)
        cmds.setAttr(ball_roll_fntbk_comp_remapOp+'.value[0].value_Interp',2)
        ball_roll_fntbk_condOp = util.createOpNode(self.moduleNameSpace, 'condition', 'ball_roll_fntbk_condOp')
        cmds.setAttr(ball_roll_fntbk_condOp+'.operation', 4)
        cmds.setAttr(ball_roll_fntbk_condOp+'.colorIfFalseG', 0)
        cmds.setAttr(ball_roll_fntbk_condOp+'.colorIfFalseB', 0)
        ball_roll_fntbk_piv_condOp = util.createOpNode(self.moduleNameSpace, 'condition', 'ball_roll_fntbk_piv_condOp')
        cmds.setAttr(ball_roll_fntbk_piv_condOp+'.operation', 4)
        cmds.setAttr(ball_roll_fntbk_piv_condOp+'.colorIfFalseR', 0)
        cmds.setAttr(ball_roll_fntbk_piv_condOp+'.colorIfFalseG', 0)
        cmds.setAttr(ball_roll_fntbk_piv_condOp+'.colorIfFalseB', 0)
        cmds.connectAttr(conNode+'.rollCompStart', ball_roll_fntbk_comp_remapOp+'.outputMin')
        cmds.connectAttr(conNode+'.rollCompEnd', ball_roll_fntbk_comp_remapOp+'.inputMax')
        cmds.connectAttr(conNode+'.rollCompStart', ball_roll_fntbk_comp_remapOp+'.inputMin')
        cmds.connectAttr(conNode+'.rollFntBk', ball_roll_fntbk_comp_remapOp+'.inputValue')
        cmds.connectAttr(ball_roll_fntbk_comp_remapOp+'.outValue', ball_roll_fntbk_condOp+'.colorIfFalseR')
        cmds.connectAttr(conNode+'.rollCompStart', ball_roll_fntbk_condOp+'.secondTerm')
        cmds.connectAttr(conNode+'.rollFntBk', ball_roll_fntbk_condOp+'.colorIfTrueR')
        cmds.connectAttr(conNode+'.rollFntBk', ball_roll_fntbk_condOp+'.firstTerm')
        cmds.connectAttr(conNode+'.rollFntBk', ball_roll_fntbk_piv_condOp+'.firstTerm')
        cmds.connectAttr(bkNode+'.translate', ball_roll_fntbk_piv_condOp+'.colorIfTrue')
        cmds.connectAttr(ball_roll_fntbk_piv_condOp+'.outColor', ballrollNode+'.rotatePivot')
        cmds.connectAttr(ball_roll_fntbk_condOp+'.outColorR', ballrollNode+'.rotateX')

        # ball_roll

        for motionOutputSpaceNode in self.filterGroupNodeDic['outputSpace'].iterkeys():
            motionOutputSpaceNodeLocal = util.fullPathName2Local(motionOutputSpaceNode)
            if motionOutputSpaceNodeLocal[1] == 'ball_space':
                ballspaceNode = motionOutputSpaceNode

        cmds.connectAttr(ball_roll_fntbk_piv_condOp+'.outColor', ballspaceNode+'.rotatePivot')
        ball_rot_comp_condOp = util.createOpNode(self.moduleNameSpace, 'condition', 'ball_rot_comp_condOp')
        cmds.setAttr(ball_rot_comp_condOp+'.operation', 2)
        cmds.setAttr(ball_rot_comp_condOp+'.colorIfFalseR', 0)
        cmds.setAttr(ball_rot_comp_condOp+'.colorIfFalseG', 0)
        cmds.setAttr(ball_rot_comp_condOp+'.colorIfFalseB', 0)
        cmds.connectAttr(ballrollNode+'.rotateX', ball_rot_comp_condOp+'.firstTerm')
        cmds.connectAttr(ballrollNode+'.rotate', ball_rot_comp_condOp+'.colorIfTrue')
        cmds.connectAttr(ball_rot_comp_condOp+'.outColorR', ballspaceNode+'.rotateX')

        # ball_space

        ##################################
        ballRollPlacementNode = None
        tipRollPlacementNode = None
        tipPlacementNode = None
        for motionOutputPlacementNode in self.filterGroupNodeDic['outputPlacement'].iterkeys():
            motionOutputPlacementNodeLocal = util.fullPathName2Local(motionOutputPlacementNode)
            if motionOutputPlacementNodeLocal[1].rfind('ball_roll') != -1:
                ballRollPlacementNode = motionOutputPlacementNode
            elif motionOutputPlacementNodeLocal[1].rfind('tip_roll') != -1 and motionOutputPlacementNodeLocal[1].rfind('ball') == -1:
                tipRollPlacementNode = motionOutputPlacementNode
            elif motionOutputPlacementNodeLocal[1].rfind('tip') != -1 and motionOutputPlacementNodeLocal[1].rfind('roll') == -1 and motionOutputPlacementNodeLocal[1].rfind('twist') == -1:
                tipPlacementNode = motionOutputPlacementNode
            else:
                continue

        ball_roll_mat_sumOp = util.createOpNode(self.moduleNameSpace, 'multMatrix', 'ball_roll_mat_sumOp')
        ball_mat_inverseOp = util.createOpNode(self.moduleNameSpace, 'inverseMatrix', 'ball_mat_inverseOp')
        ball_roll_fntbk_dir_condOp = util.createOpNode(self.moduleNameSpace, 'condition', 'ball_roll_fntbk_dir_condOp')
        cmds.setAttr(ball_roll_fntbk_dir_condOp+'.operation', 2)
        cmds.setAttr(ball_roll_fntbk_dir_condOp+'.colorIfTrueR', 1)
        cmds.setAttr(ball_roll_fntbk_dir_condOp+'.colorIfTrueG', 0)
        cmds.setAttr(ball_roll_fntbk_dir_condOp+'.colorIfTrueB', 0)
        cmds.setAttr(ball_roll_fntbk_dir_condOp+'.colorIfFalseR', 0)
        cmds.setAttr(ball_roll_fntbk_dir_condOp+'.colorIfFalseG', 0)
        cmds.setAttr(ball_roll_fntbk_dir_condOp+'.colorIfFalseB', 0)
        tip_local_mat_selectorOp = util.createOpNode(self.moduleNameSpace, 'choice', 'tip_local_mat_selectorOp')
        ball_mat_decompOp = util.createOpNode(self.moduleNameSpace, 'decomposeMatrix', 'ball_mat_decompOp')

        cmds.connectAttr(ballRollPlacementNode+'.matrix', ball_roll_mat_sumOp+'.matrixIn[1]')
        cmds.connectAttr(ballrollNode+'.matrix', ball_roll_mat_sumOp+'.matrixIn[0]')
        cmds.connectAttr(ball_roll_mat_sumOp+'.matrixSum', ball_mat_inverseOp+'.inputMatrix')
        cmds.connectAttr(conNode+'.rollFntBk', ball_roll_fntbk_dir_condOp+'.firstTerm')
        cmds.connectAttr(ball_roll_fntbk_dir_condOp+'.outColorR', tip_local_mat_selectorOp+'.selector')
        cmds.connectAttr(fntNode+'.matrix', tip_local_mat_selectorOp+'.input[0]')
        cmds.connectAttr(ball_mat_inverseOp+'.outputMatrix', tip_local_mat_selectorOp+'.input[1]')
        cmds.connectAttr(tip_local_mat_selectorOp+'.output', ball_mat_decompOp+'.inputMatrix')
        util.decompChannelBinding(ball_mat_decompOp, tipRollPlacementNode)
        util.transformChannelBinding(tipRollPlacementNode, tipPlacementNode)

        # tip_roll_placement

        ballrollChildNodes = []
        ballspaceChildNodes = []
        for node, parentInfo in self.filterGroupNodeDic['outputPlacement'].iteritems():
            if parentInfo['parent'] == ballrollNode:
                ballrollChildNodes.append(node)
            elif parentInfo['parent'] == ballspaceNode:
                ballspaceChildNodes.append(node)

        for ballrollChildNode in ballrollChildNodes:
            ballrollChildNodeLocal = util.fullPathName2Local(ballrollChildNode)
            if ballrollChildNodeLocal[1].rfind('foot') != -1:
                for ballspaceChildNode in ballspaceChildNodes:
                    ballspaceChildNodeLocal = util.fullPathName2Local(ballspaceChildNode)
                    if ballspaceChildNodeLocal[1].rfind('foot') != -1:
                        util.transformChannelBinding(ballrollChildNode, ballspaceChildNode)
            elif ballrollChildNodeLocal[1].rfind('heel') != -1:
                for ballspaceChildNode in ballspaceChildNodes:
                    ballspaceChildNodeLocal = util.fullPathName2Local(ballspaceChildNode)
                    if ballspaceChildNodeLocal[1].rfind('heel') != -1:
                        util.transformChannelBinding(ballrollChildNode, ballspaceChildNode)
        pivNode = None
        heelNode = None
        for ballrollChildNode in ballrollChildNodes:
            ballrollChildNodeLocal = util.fullPathName2Local(ballrollChildNode)
            if ballrollChildNodeLocal[1].rfind('piv_bk') != -1:
                pivNode = ballrollChildNode
            elif ballrollChildNodeLocal[1].rfind('heel') != -1:
                heelNode = ballrollChildNode
        util.transformChannelBinding(pivNode, heelNode)

        # placement node connections

        outputOffsetSpaceList = {}
        footSpaceNode = None
        heelSpaceNode = None
        ballSpaceNode = None
        tipSpaceNode = None
        for node, parentInfo in self.filterGroupNodeDic['outputOffsetSpaceNode'].iteritems():
            parentLocal = util.fullPathName2Local(parentInfo['parent'])
            if parentLocal[1].rfind('jnt') == -1:
                nodeLocal = util.fullPathName2Local(node)
                if nodeLocal[1].rfind('foot') != -1:
                    outputOffsetSpaceList['foot'] = node
                    for ballspaceChildNode in ballspaceChildNodes:
                        ballspaceChildNodeLocal = util.fullPathName2Local(ballspaceChildNode)
                        if ballspaceChildNodeLocal[1].rfind('foot') != -1:
                            footSpaceNode = ballspaceChildNode
                            matrixOps = util.localMatrixOp(self.moduleNameSpace, 'foot_offset')
                            cmds.connectAttr(parentInfo['parent']+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                            cmds.connectAttr(footSpaceNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                            util.decompChannelBinding(matrixOps[1], node)

                elif nodeLocal[1].rfind('heel') != -1:
                    outputOffsetSpaceList['heel'] = node
                    for ballspaceChildNode in ballspaceChildNodes:
                        ballspaceChildNodeLocal = util.fullPathName2Local(ballspaceChildNode)
                        if ballspaceChildNodeLocal[1].rfind('foot') != -1:
                            footSpaceNode = ballspaceChildNode
                        elif ballspaceChildNodeLocal[1].rfind('heel') != -1:
                            heelSpaceNode = ballspaceChildNode
                    matrixOps = util.localMatrixOp(self.moduleNameSpace, 'heel_offset')
                    cmds.connectAttr(footSpaceNode+'.inverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                    cmds.connectAttr(heelSpaceNode+'.matrix', matrixOps[0]+'.matrixIn[0]', f=True)
                    util.decompChannelBinding(matrixOps[1], node)

                elif nodeLocal[1].rfind('ball') != -1:
                    outputOffsetSpaceList['ball'] = node
                    for ballspaceChildNode in ballspaceChildNodes:
                        ballspaceChildNodeLocal = util.fullPathName2Local(ballspaceChildNode)
                        if ballspaceChildNodeLocal[1].rfind('heel') != -1:
                            heelSpaceNode = ballspaceChildNode
                        elif ballspaceChildNodeLocal[1].rfind('ball') != -1:
                            ballSpaceNode = ballspaceChildNode
                    matrixOps = util.localMatrixOp(self.moduleNameSpace, 'heel_offset')
                    cmds.connectAttr(heelSpaceNode+'.inverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                    cmds.connectAttr(ballSpaceNode+'.matrix', matrixOps[0]+'.matrixIn[0]', f=True)
                    util.decompChannelBinding(matrixOps[1], node)

                elif nodeLocal[1].rfind('tip') != -1:
                    outputOffsetSpaceList['tip'] = node
                    for ballspaceChildNode in ballspaceChildNodes:
                        ballspaceChildNodeLocal = util.fullPathName2Local(ballspaceChildNode)
                        if ballspaceChildNodeLocal[1].rfind('ball') != -1:
                            ballSpaceNode = ballspaceChildNode
                        elif ballspaceChildNodeLocal[1].rfind('tip') != -1:
                            tipSpaceNode = ballspaceChildNode
                    matrixOps = util.localMatrixOp(self.moduleNameSpace, 'heel_offset')
                    cmds.connectAttr(ballSpaceNode+'.inverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                    cmds.connectAttr(tipSpaceNode+'.matrix', matrixOps[0]+'.matrixIn[0]', f=True)
                    util.decompChannelBinding(matrixOps[1], node)

                else:
                    continue

        # output offset space connections

        for node, parentInfo in self.filterGroupNodeDic['controlSpace'].iteritems():
            nodeLocal = util.fullPathName2Local(node)
            if nodeLocal[1].rfind('offset') != -1:
                filterStr = nodeLocal[1].replace('_offset_fk_space','')
                parentNode = parentInfo['parent']
                childNode = outputOffsetSpaceList[filterStr]
                matrixOps = util.localMatrixOp(self.moduleNameSpace, filterStr+'_offset_fk_space')
                cmds.connectAttr(parentNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(childNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], node)

                if nodeLocal[1].rfind('foot') != -1:
                    cmds.connectAttr(conNode+'.offsetFkConDisplay', node+'.visibility')


        # extra
        
        source = self._side + ':' + self.component_str + ':module:tip_offset_fk_Con.rotate'
        target = self._side + ':' + self.component_str + ':module:tip_jnt_offset_space.rotate'
        cmds.connectAttr(source, target)

        # control offset space connections

        reampOp = util.createOpNode(self.moduleNameSpace, 'remapValue', 'body2all_remapOP')
        cmds.setAttr(reampOp+'.outputMin', 1)
        cmds.setAttr(reampOp+'.outputMax', 0)
        applyWeightOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', 'apply_hip2body_weightOp')
        cmds.setAttr(applyWeightOp+'.operation', 1)
        remainHipWeightOp = util.createOpNode(self.moduleNameSpace, 'plusMinusAverage', 'remain_hip_weightOp')

        cmds.connectAttr(conNode+'.spaceBody2All', reampOp+'.inputValue')
        cmds.connectAttr(conNode+'.spaceHip2Body', applyWeightOp+'.input2X')
        cmds.connectAttr(conNode+'.spaceBody2All', self.filterGroupNodeDic['spaceWeight'].keys()[0]+'.All')
        cmds.connectAttr(reampOp+'.outValue', applyWeightOp+'.input1X')
        cmds.connectAttr(reampOp+'.outValue', remainHipWeightOp+'.input3D[0].input3Dx')
        cmds.connectAttr(applyWeightOp+'.outputX', remainHipWeightOp+'.input3D[1].input3Dx')
        cmds.connectAttr(applyWeightOp+'.outputX', self.filterGroupNodeDic['spaceWeight'].keys()[0]+'.Body')
        cmds.connectAttr(remainHipWeightOp+'.output3Dx', self.filterGroupNodeDic['spaceWeight'].keys()[0]+'.Hip')

        # spaceWeight
