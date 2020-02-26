import maya.cmds as cmds
import Template.Lib.Util.util as util
import os
import Template.Tool.ComponentManager.globalPath as globalPath

class legComponent(object):
    def __init__(self, name):
        self.name = name
        self.fitNode = None
        self.component_str = self.name
        self.component_val = 'leg'
        self.fitComponent_str = 'fit'
        self.moduleComponent_str = 'module'
        self.componentType_str = ''
        self.pathInfo = globalPath.globalPath('Leg')
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
        fitSpaceNodeStr = self.topFitNodeStr + '|' + self.fitNamespace[1:] + ':space'
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
        fitNodeInfo = util.getFitInfo(fitNamespace, fitCompoenent, matchStr='fit')
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
        self.modulePathDic['input'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_input'
        self.modulePathDic['fk'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_fk'
        self.modulePathDic['ik'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_ik'
        self.modulePathDic['output'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_output'
        self.modulePathDic['control'] = ':' + self._side + ':' + self.component_str + ':' + self.moduleComponent_str + ':motion_control'
        return self.modulePathDic

    def getNodeList(self):
        util.getChildrenNodes(self.modulePathDic['top'], '', self.outputs, 1)
        return self.outputs

    def getNodeGroupByFilter(self):

        initNodes = {}

        motionInputPlacementNodes = {}
        motionInputPlugNodes = {}

        motionFkPlacementNodes = {}
        motionFkSpaceNodes = {}
        motionFkJnts = {}

        motionIkPlacementNodes = {}
        motionIkSpaceNodes = {}
        motionIkJnts = {}
        motionIkHandles = {}
        motionIkSoftNodes = {}

        motionOutputPlacementNodes = {}
        motionOutputSpaceNodes = {}
        motionOutputBlendJnts = {}
        motionOutputSocketNodes = {}
        motionOutputNodes = {}

        controlPlacementNodes = {}
        controlFkPlacementNodes = {}
        controlIkPlacementNodes = {}
        controlFkSpaceNodes = {}
        controlIkSpaceNodes = {}
        fkConNodes = {}
        ikConNodes = {}
        refNodes = {}
        poleAutoNodes = {}
        fk2ikConNodes = {}
        fk2ikSpaceNodes = {}

        for key in self.outputs.iterkeys():
            if self.outputs[key]['parent'] == self.modulePathDic['top']:
                if key.rfind(self.modulePathDic['init'][1:]) != -1:
                    util.getChildrenNodes(key, 'init', initNodes, 1)

                elif key.rfind(self.modulePathDic['input'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionInputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'child_plug', motionInputPlugNodes, 1)

                elif key.rfind(self.modulePathDic['fk'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionFkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'space', motionFkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'Jnt', motionFkJnts, 1, objectType='joint')

                elif key.rfind(self.modulePathDic['ik'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionIkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'space', motionIkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'Jnt', motionIkJnts, 1, objectType='joint')
                    util.getChildrenNodes(key, 'handle', motionIkHandles, 1)
                    util.getChildrenNodes(key, 'soft', motionIkSoftNodes, 1)

                elif key.rfind(self.modulePathDic['output'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionOutputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'space', motionOutputSpaceNodes, 1)
                    util.getChildrenNodes(key, 'blend', motionOutputBlendJnts, 1, objectType='joint')
                    util.getChildrenNodes(key, 'parent_socket', motionOutputSocketNodes, 1)
                    util.getChildrenNodes(key, '', motionOutputNodes, 1)

                elif key.rfind(self.modulePathDic['control'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', controlPlacementNodes, 1)
                    util.getChildrenNodes(key, 'fk_placement', controlFkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'ik_placement', controlIkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'fk_space', controlFkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'ik_space', controlIkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'fk_Con', fkConNodes, 1)
                    util.getChildrenNodes(key, 'ik_Con', ikConNodes, 1)
                    util.getChildrenNodes(key, 'ref', refNodes, 1)
                    util.getChildrenNodes(key, 'Auto', poleAutoNodes, 1)
                    util.getChildrenNodes(key, 'fk2ik_Con', fk2ikConNodes, 1)
                    util.getChildrenNodes(key, 'fk2ik_space', fk2ikSpaceNodes, 1)
                else:
                    continue

        self.filterGroupNodeDic['init'] = initNodes

        self.filterGroupNodeDic['inputPlacement'] = motionInputPlacementNodes
        self.filterGroupNodeDic['inputChildPlug'] = motionInputPlugNodes

        self.filterGroupNodeDic['fkPlacement'] = motionFkPlacementNodes
        self.filterGroupNodeDic['fkSpace'] = motionFkSpaceNodes
        self.filterGroupNodeDic['fkJnt'] = motionFkJnts

        self.filterGroupNodeDic['ikPlacement'] = motionIkPlacementNodes
        self.filterGroupNodeDic['ikSpace'] = motionIkSpaceNodes
        self.filterGroupNodeDic['ikJnt'] = motionIkJnts
        self.filterGroupNodeDic['ikHandle'] = motionIkHandles
        self.filterGroupNodeDic['ikSoft'] = motionIkSoftNodes

        self.filterGroupNodeDic['outputPlacement'] = motionOutputPlacementNodes
        self.filterGroupNodeDic['outputSpace'] = motionOutputSpaceNodes
        self.filterGroupNodeDic['outputBlend'] = motionOutputBlendJnts
        self.filterGroupNodeDic['outputParentSocket'] = motionOutputSocketNodes
        self.filterGroupNodeDic['outputNode'] = motionOutputNodes

        self.filterGroupNodeDic['controlPlacement'] = controlPlacementNodes
        self.filterGroupNodeDic['controlFkPlacement'] = controlFkPlacementNodes
        self.filterGroupNodeDic['controlIkPlacement'] = controlIkPlacementNodes
        self.filterGroupNodeDic['controlFkSpace'] = controlFkSpaceNodes
        self.filterGroupNodeDic['controlIkSpace'] = controlIkSpaceNodes
        self.filterGroupNodeDic['controlFkCon'] = fkConNodes
        self.filterGroupNodeDic['controlIkCon'] = ikConNodes
        self.filterGroupNodeDic['controlRef'] = refNodes
        self.filterGroupNodeDic['controlPoleAuto'] = poleAutoNodes
        self.filterGroupNodeDic['fk2ikCon'] = fk2ikConNodes
        self.filterGroupNodeDic['fk2ikSpace'] = fk2ikSpaceNodes
        return self.filterGroupNodeDic

    def setConnectionInfo(self):
        parentSocketNodes = {}
        childPlugNodes = {}
        if self.filterGroupNodeDic['outputParentSocket'] != None:
            for socketNode in self.filterGroupNodeDic['outputParentSocket'].keys():
                socketLocalNode = util.fullPathName2Local(socketNode)
                parentSocketNodes[socketLocalNode[1]] = socketNode
        if self.filterGroupNodeDic['inputChildPlug'] != None:
            for plugNode in self.filterGroupNodeDic['inputChildPlug'].keys():
                plugLocalNode = util.fullPathName2Local(plugNode)
                childPlugNodes[plugLocalNode[1]] = plugNode
        return parentSocketNodes, childPlugNodes

    def createMatchDic(self, fitNodeInfo, initNodes):
        fitMatchDic = {}
        for match in fitNodeInfo.iterkeys():
            for initNode in initNodes.keys():
                initNodeLocal = util.fullPathName2Local(initNode)
                if initNodeLocal[1].replace('_init','_fit') == match:
                    fitMatchDic[match] = initNode
        return fitMatchDic

    def updateInitByFit(self, liveConnection=False):
        snapOps = []

        initNodeFullName = cmds.ls(self.modulePathDic['init'], l=True)[0]
        for match in self.fitNodeInfo.iterkeys():
            matrixOps = util.localMatrixOp(self.moduleNameSpace, match + '_init')
            snapOps += matrixOps
            cmds.connectAttr(initNodeFullName+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
            cmds.connectAttr(self.fitNodeInfo[match]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
            util.decompChannelBinding(matrixOps[1], self.fitMatchDic[match])

        # foot control align to the world axis
        # still issue with live mode. 
        self.alignFootOffsetChild()

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
        placementNodesList = [self.filterGroupNodeDic['inputPlacement'], self.filterGroupNodeDic['fkPlacement'], self.filterGroupNodeDic['ikPlacement'], self.filterGroupNodeDic['outputPlacement'], self.filterGroupNodeDic['controlPlacement']]
        uplegInitFull = ''
        for initNode, parentNode in self.filterGroupNodeDic['init'].iteritems():
            initLocalNode = util.fullPathName2Local(initNode)
            matchStr = initLocalNode[1].replace('init', '')
            for placementNodes in placementNodesList:
                for placementNode in placementNodes:
                    placementLocalNode = util.fullPathName2Local(placementNode)
                    if placementLocalNode[1].rfind(matchStr) != -1:
                        util.transformChannelBinding(initNode, placementNode)

        uplegInitFull = ''
        lolegInitFull = ''
        footInitFull = ''
        ballInitFull = ''
        tipInitFull = ''
        spaceInitFull = ''
        controlInitFull = ''

        for initNode, parentNode in self.filterGroupNodeDic['init'].iteritems():
            initLocalNode = util.fullPathName2Local(initNode)
            partStr = initLocalNode[1].replace('_init', '')
            if initLocalNode[1].rfind('upleg') != -1:
                uplegInitFull = initNode
            elif initLocalNode[1].rfind('loleg') != -1:
                lolegInitFull = initNode
            elif initLocalNode[1].rfind('foot') != -1:
                footInitFull = initNode
            elif initLocalNode[1].rfind('ball') != -1:
                ballInitFull = initNode
            elif initLocalNode[1].rfind('tip') != -1:
                tipInitFull = initNode
            elif initLocalNode[1].rfind('space') != -1:
                spaceInitFull = initNode
            elif initLocalNode[1].rfind('control') != -1:
                controlInitFull = initNode

        jointListGroup = [self.filterGroupNodeDic['fkJnt'], self.filterGroupNodeDic['ikJnt'], self.filterGroupNodeDic['outputBlend']]
        for initNode, parentNode in self.filterGroupNodeDic['init'].iteritems():
            initLocalNode = util.fullPathName2Local(initNode)
            partStr = initLocalNode[1].replace('_init', '')
            if initLocalNode[1].rfind('loleg') != -1:
                for controlFkSpace in self.filterGroupNodeDic['controlFkSpace']:
                    controlLocalFkSpace = util.fullPathName2Local(controlFkSpace)
                    if controlLocalFkSpace[1].rfind('loleg') != -1:
                        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'loleg_init')
                        cmds.connectAttr(uplegInitFull+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                        cmds.connectAttr(initNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                        util.decompChannelBinding(matrixOps[1], controlFkSpace)
                        for jointList in jointListGroup:
                            for jnt in jointList:
                                jntLocal = util.fullPathName2Local(jnt)
                                if jntLocal[1].rfind('loleg') != -1:
                                    cmds.connectAttr(matrixOps[1]+'.outputTranslate', jnt+'.translate')
                                    cmds.connectAttr(matrixOps[1]+'.outputRotate', jnt+'.jointOrient')

            elif initLocalNode[1].rfind('foot') != -1:
                for controlFkSpace in self.filterGroupNodeDic['controlFkSpace']:
                    controlLocalFkSpace = util.fullPathName2Local(controlFkSpace)
                    if controlLocalFkSpace[1].rfind('foot') != -1:
                        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'foot_init')
                        cmds.connectAttr(lolegInitFull+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                        cmds.connectAttr(initNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                        util.decompChannelBinding(matrixOps[1], controlFkSpace)
                        for jointList in jointListGroup:
                            for jnt in jointList:
                                jntLocal = util.fullPathName2Local(jnt)
                                if jntLocal[1].rfind('foot') != -1:
                                    cmds.connectAttr(matrixOps[1]+'.outputTranslate', jnt+'.translate')
                                    cmds.connectAttr(matrixOps[1]+'.outputRotate', jnt+'.jointOrient')

            elif initLocalNode[1].rfind('ball') != -1:
                for controlFkSpace in self.filterGroupNodeDic['controlFkSpace']:
                    controlLocalFkSpace = util.fullPathName2Local(controlFkSpace)
                    if controlLocalFkSpace[1].rfind('ball') != -1:
                        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'ball_init')
                        cmds.connectAttr(footInitFull+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                        cmds.connectAttr(initNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                        util.decompChannelBinding(matrixOps[1], controlFkSpace)
                        for jointList in jointListGroup:
                            for jnt in jointList:
                                jntLocal = util.fullPathName2Local(jnt)
                                if jntLocal[1].rfind('ball') != -1:
                                    cmds.connectAttr(matrixOps[1]+'.outputTranslate', jnt+'.translate')
                                    cmds.connectAttr(matrixOps[1]+'.outputRotate', jnt+'.jointOrient')

            elif initLocalNode[1].rfind('tip') != -1:
                for controlFkSpace in self.filterGroupNodeDic['controlFkSpace']:
                    controlLocalFkSpace = util.fullPathName2Local(controlFkSpace)
                    if controlLocalFkSpace[1].rfind('tip') != -1:
                        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'ball_init')
                        cmds.connectAttr(ballInitFull+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                        cmds.connectAttr(initNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                        util.decompChannelBinding(matrixOps[1], controlFkSpace)
                        for jointList in jointListGroup:
                            for jnt in jointList:
                                jntLocal = util.fullPathName2Local(jnt)
                                if jntLocal[1].rfind('tip') != -1:
                                    cmds.connectAttr(matrixOps[1]+'.outputTranslate', jnt+'.translate')
                                    cmds.connectAttr(matrixOps[1]+'.outputRotate', jnt+'.jointOrient')

        for fkSpaceNode in self.filterGroupNodeDic['fkSpace']:
                fkSpaceLocalNode = util.fullPathName2Local(fkSpaceNode)
                if fkSpaceLocalNode[1].rfind('foot') != -1:
                    matrixOps = util.localMatrixOp(self.moduleNameSpace, 'foot_init')
                    cmds.connectAttr(lolegInitFull+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                    cmds.connectAttr(footInitFull+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                    util.decompChannelBinding(matrixOps[1], fkSpaceNode)

        # soft IK OP
        upleg2lolegDistanceOp = util.createOpNode(self.moduleNameSpace, 'distanceBetween', 'upleg2loleg_distasnce')
        loleg2footDistanceOp = util.createOpNode(self.moduleNameSpace, 'distanceBetween', 'loleg2foot_distasnce')
        legDistanceOp = util.createOpNode(self.moduleNameSpace, 'plusMinusAverage', 'leg_distance_sum')
        cmds.connectAttr(uplegInitFull+'.worldMatrix', upleg2lolegDistanceOp+'.inMatrix1', f=True)
        cmds.connectAttr(lolegInitFull+'.worldMatrix', upleg2lolegDistanceOp+'.inMatrix2', f=True)
        cmds.connectAttr(lolegInitFull+'.worldMatrix', loleg2footDistanceOp+'.inMatrix1', f=True)
        cmds.connectAttr(footInitFull+'.worldMatrix', loleg2footDistanceOp+'.inMatrix2', f=True)
        cmds.connectAttr(upleg2lolegDistanceOp+'.distance', legDistanceOp+'.input1D[0]', f=True)
        cmds.connectAttr(loleg2footDistanceOp+'.distance', legDistanceOp+'.input1D[1]', f=True)

        softIkAssetPath = self.pathInfo.assetDirPath + 'softIkOpAsset' + '.' + self.file_extenstion_str
        softIkOpNode = ''
        softIkOpNodeNew = ''
        fileCheck = cmds.file( softIkAssetPath, query=True, exists=True )
        if fileCheck:
            cmds.file( softIkAssetPath, i=True, mergeNamespacesOnClash=True )
            containerNodes = cmds.ls(type='container', l=True)
            if containerNodes != None:
                for containerNode in containerNodes:
                    localStr = containerNode.split(':')[-1]
                    if localStr == 'softIKOp':
                        softIkOpNode = containerNode
        if cmds.objExists(softIkOpNode):
            softIkOpNodeNew = cmds.rename(softIkOpNode, softIkOpNode + '_' + self.component_val)

        cmds.connectAttr(legDistanceOp+'.output1D', softIkOpNodeNew+'.In_initLength', f=True)
        
        softIkNode = ''
        for ikSoftNode in self.filterGroupNodeDic['ikSoft']:
            ikSoftNodeLocal = util.fullPathName2Local(ikSoftNode)
            if ikSoftNodeLocal[1].rfind('space') == -1:
                softIkNode = ikSoftNode
        
        cmds.connectAttr(softIkOpNodeNew+'.Out_softDistance', softIkNode +'.translateX', f=True)

        legIkSpaceNode = ''
        for ikSpaceNode in self.filterGroupNodeDic['ikSpace']:
            ikSpaceLocalNode = util.fullPathName2Local(ikSpaceNode)
            if ikSpaceLocalNode[1].rfind('leg') != -1 and ikSpaceLocalNode[1].rfind('soft') == -1:
                legIkSpaceNode = ikSpaceNode

        footikConLocalNode = ''
        footikConNode = ''
        for ikConNode in self.filterGroupNodeDic['controlIkCon']:
            ikConLocalNode = util.fullPathName2Local(ikConNode)
            if ikConLocalNode[1].rfind('foot') != -1:
                if ikConLocalNode[1].rfind('local') != -1:
                    footikConLocalNode = ikConNode
                else:
                    footikConNode = ikConNode

        ikControlDistanceOp = util.createOpNode(self.moduleNameSpace, 'distanceBetween', 'ik_control_distasnce')
        cmds.connectAttr(legIkSpaceNode+'.worldMatrix', ikControlDistanceOp+'.inMatrix1', f=True)
        cmds.connectAttr(footikConLocalNode+'.worldMatrix', ikControlDistanceOp+'.inMatrix2', f=True)
        cmds.connectAttr(ikControlDistanceOp+'.distance', softIkOpNodeNew+'.In_motionLength', f=True)
        cmds.connectAttr(footikConNode+'.softIK', softIkOpNodeNew+'.In_softWeight', f=True)

        for initNode, parentNode in self.filterGroupNodeDic['init'].iteritems():
            initNodeLocal = util.fullPathName2Local(initNode)
            partStr = initNodeLocal[1].replace('_init', '')
            if partStr in ['foot', 'ball', 'tip']:
                for ikSpace in self.filterGroupNodeDic['ikSpace']:
                    ikLocalSpace = util.fullPathName2Local(ikSpace)
                    if ikLocalSpace[1].rfind(partStr) != -1:
                        matrixOps = util.localMatrixOp(self.moduleNameSpace, partStr+'_init')
                        cmds.connectAttr(uplegInitFull+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                        cmds.connectAttr(initNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                        util.decompChannelBinding(matrixOps[1], ikSpace)

        uplegInitDecompOp = util.createOpNode(self.moduleNameSpace, 'decomposeMatrix', 'upleg_init_decomp')
        cmds.connectAttr(uplegInitFull+'.worldMatrix', uplegInitDecompOp+'.inputMatrix')

        lolegInitDecompOp = util.createOpNode(self.moduleNameSpace, 'decomposeMatrix', 'loleg_init_decomp')
        cmds.connectAttr(lolegInitFull+'.worldMatrix', lolegInitDecompOp+'.inputMatrix')

        footInitDecompOp = util.createOpNode(self.moduleNameSpace, 'decomposeMatrix', 'foot_init_decomp')
        cmds.connectAttr(footInitFull+'.worldMatrix', footInitDecompOp+'.inputMatrix')

        footVecOp = util.createOpNode(self.moduleNameSpace, 'plusMinusAverage', 'footVec')
        cmds.setAttr(footVecOp+'.operation',2)
        cmds.connectAttr(uplegInitDecompOp+'.outputTranslate', footVecOp+'.input3D[0]')
        cmds.connectAttr(footInitDecompOp+'.outputTranslate', footVecOp+'.input3D[1]')
        #cmds.connectAttr(footInitDecompOp+'.outputTranslate',  +'.translate')

        footVecMagOp = util.createOpNode(self.moduleNameSpace, 'distanceBetween', 'footVecMag')
        cmds.connectAttr(uplegInitDecompOp+'.outputTranslate', footVecMagOp+'.point1')
        cmds.connectAttr(footInitDecompOp+'.outputTranslate', footVecMagOp+'.point2')

        footVecUnitOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', 'footVecUnit')
        cmds.setAttr(footVecUnitOp+'.operation',2)
        cmds.connectAttr(footVecOp+'.output3D', footVecUnitOp+'.input1')
        cmds.connectAttr(footVecMagOp+'.distance', footVecUnitOp+'.input2X')
        cmds.connectAttr(footVecMagOp+'.distance', footVecUnitOp+'.input2Y')
        cmds.connectAttr(footVecMagOp+'.distance', footVecUnitOp+'.input2Z')

        lolegVecOp = util.createOpNode(self.moduleNameSpace, 'plusMinusAverage', 'lolegVec')
        cmds.setAttr(lolegVecOp+'.operation',2)
        cmds.connectAttr(lolegInitDecompOp+'.outputTranslate', lolegVecOp+'.input3D[0]')
        cmds.connectAttr(footInitDecompOp+'.outputTranslate', lolegVecOp+'.input3D[1]')

        lolegVecMagOp = util.createOpNode(self.moduleNameSpace, 'distanceBetween', 'lolegVecMag')
        cmds.connectAttr(lolegInitDecompOp+'.outputTranslate', lolegVecMagOp+'.point1')
        cmds.connectAttr(footInitDecompOp+'.outputTranslate', lolegVecMagOp+'.point2')

        lolegVecUnitOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', 'lolegVecUnit')
        cmds.setAttr(lolegVecUnitOp+'.operation',2)
        cmds.connectAttr(lolegVecOp+'.output3D', lolegVecUnitOp+'.input1')
        cmds.connectAttr(lolegVecMagOp+'.distance', lolegVecUnitOp+'.input2X')
        cmds.connectAttr(lolegVecMagOp+'.distance', lolegVecUnitOp+'.input2Y')
        cmds.connectAttr(lolegVecMagOp+'.distance', lolegVecUnitOp+'.input2Z')

        poleSideVecOp = util.createOpNode(self.moduleNameSpace, 'vectorProduct', 'poleSideVec')
        cmds.setAttr(poleSideVecOp+'.normalizeOutput', 1)
        cmds.setAttr(poleSideVecOp+'.operation',2)
        cmds.connectAttr(footVecUnitOp+'.output', poleSideVecOp+'.input1')
        cmds.connectAttr(lolegVecUnitOp+'.output', poleSideVecOp+'.input2')

        poleFntVecOp = util.createOpNode(self.moduleNameSpace, 'vectorProduct', 'poleFntVec')
        cmds.setAttr(poleFntVecOp+'.normalizeOutput', 1)
        cmds.setAttr(poleFntVecOp+'.operation',2)
        cmds.connectAttr(poleSideVecOp+'.output', poleFntVecOp+'.input1')
        cmds.connectAttr(footVecUnitOp+'.output', poleFntVecOp+'.input2')

        poleMatOp = util.createOpNode(self.moduleNameSpace, 'fourByFourMatrix', 'poleMat')
        # X axis
        cmds.connectAttr(poleSideVecOp+'.outputX', poleMatOp+'.in00')
        cmds.connectAttr(poleSideVecOp+'.outputY', poleMatOp+'.in01')
        cmds.connectAttr(poleSideVecOp+'.outputZ', poleMatOp+'.in02')
        # Y axis
        cmds.connectAttr(footVecUnitOp+'.outputX', poleMatOp+'.in10')
        cmds.connectAttr(footVecUnitOp+'.outputY', poleMatOp+'.in11')
        cmds.connectAttr(footVecUnitOp+'.outputZ', poleMatOp+'.in12')
        # Z axis
        cmds.connectAttr(poleFntVecOp+'.outputX', poleMatOp+'.in20')
        cmds.connectAttr(poleFntVecOp+'.outputY', poleMatOp+'.in21')
        cmds.connectAttr(poleFntVecOp+'.outputZ', poleMatOp+'.in22')
        # translate
        cmds.connectAttr(footInitDecompOp+'.outputTranslateX', poleMatOp+'.in30')
        cmds.connectAttr(footInitDecompOp+'.outputTranslateY', poleMatOp+'.in31')
        cmds.connectAttr(footInitDecompOp+'.outputTranslateZ', poleMatOp+'.in32')
        # decomp
        poleMatDecompOp = util.createOpNode(self.moduleNameSpace, 'decomposeMatrix', 'poleMat_decomp')
        cmds.connectAttr(poleMatOp+'.output', poleMatDecompOp+'.inputMatrix')

        cmds.connectAttr(poleMatDecompOp+'.outputTranslate', spaceInitFull+'.translate')
        cmds.connectAttr(poleMatDecompOp+'.outputRotate', spaceInitFull+'.rotate')

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'space_init')
        cmds.connectAttr(controlInitFull+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(spaceInitFull+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        for controlPoleNode in self.filterGroupNodeDic['controlPoleAuto']:
            controlPoleNodeLocal = util.fullPathName2Local(controlPoleNode)
            if controlPoleNodeLocal[1].rfind('Pole_Auto') != -1:
                util.decompChannelBinding(matrixOps[1], controlPoleNode)

        return

    def alignFootOffsetChild(self):
        for node in self.filterGroupNodeDic['inputChildPlug'].iterkeys():
            nodeLocal = util.fullPathName2Local(node)
            if nodeLocal[1].rfind('foot_offset') != -1:
                footOffsetPlug = node
                parentNodes = cmds.listRelatives(footOffsetPlug, p=True, f=True, typ='transform')
                footOffsetPlugNew = cmds.parent(footOffsetPlug, w=True)
                cmds.setAttr(footOffsetPlugNew[0]+'.rotateX', 0)
                cmds.setAttr(footOffsetPlugNew[0]+'.rotateZ', 0)
                cmds.parent(footOffsetPlugNew[0], parentNodes[0], absolute=True, relative=False)

    def applyMotionNodeConnections(self):
        spaceListGroup = [self.filterGroupNodeDic['fkSpace'], self.filterGroupNodeDic['ikSpace'], self.filterGroupNodeDic['outputSpace'], self.filterGroupNodeDic['controlFkSpace'], self.filterGroupNodeDic['controlIkSpace']]
        for node in self.filterGroupNodeDic['inputChildPlug'].iterkeys():
            nodeLocal = util.fullPathName2Local(node)
            if nodeLocal[1].rfind('upleg') != -1:
                for spaceList in spaceListGroup:
                    for spaceNode in spaceList:
                        spaceNodeLocal = util.fullPathName2Local(spaceNode)
                        if spaceNodeLocal[1].rfind('upleg') != -1:
                            util.transformChannelBinding(node, spaceNode)

            elif nodeLocal[1].rfind('ball_twist') != -1:
                for controlIkSpace in self.filterGroupNodeDic['controlIkSpace']:
                    controlIkSpaceLocal = util.fullPathName2Local(controlIkSpace)
                    if controlIkSpaceLocal[1].rfind('Pole_Rot') != -1:
                        cmds.orientConstraint(node, controlIkSpace)

            elif nodeLocal[1].rfind('foot_offset') != -1:

                footOffsetPlug = node
                ballJntOffsetPlug = ''
                tipJntOffsetPlug = ''
                
                uplegIkSpace = ''
                footIkSpace = ''
                ballIkSpaceLocal = ''
                tipIkSpaceLocal = ''

                controlIKSpaceLocalNodes = []
                for controlIkSpace in self.filterGroupNodeDic['controlIkSpace']:
                    controlIkSpaceLocal = util.fullPathName2Local(controlIkSpace)
                    if controlIkSpaceLocal[1].rfind('space_local') != -1:
                        controlIKSpaceLocalNodes.append(controlIkSpace)

                for spaceLocalNode in controlIKSpaceLocalNodes:
                    spaceLocalNodeBaseStr = util.fullPathName2Local(spaceLocalNode)
                    if spaceLocalNodeBaseStr[1].rfind('ball') != -1:
                        ballIkSpaceLocal = spaceLocalNode
                    elif spaceLocalNodeBaseStr[1].rfind('tip') != -1:
                        tipIkSpaceLocal = spaceLocalNode

                for plugNode in self.filterGroupNodeDic['inputChildPlug'].iterkeys():
                    plugNodeLocal = util.fullPathName2Local(plugNode)
                    if plugNodeLocal[1].rfind('ball_jnt') != -1:
                        ballJntOffsetPlug = plugNode
                    elif plugNodeLocal[1].rfind('tip_jnt') != -1:
                        tipJntOffsetPlug = plugNode

                for controlIkSpace in self.filterGroupNodeDic['controlIkSpace']:
                    controlIkSpaceLocalStr = util.fullPathName2Local(controlIkSpace)
                    if controlIkSpaceLocalStr[1].rfind('upleg_con_ik') != -1:
                        uplegIkSpace = controlIkSpace
                    elif controlIkSpaceLocalStr[1].rfind('foot_con_ik') != -1 and controlIkSpaceLocalStr[1].rfind('local') == -1:
                        footIkSpace = controlIkSpace

                matrixOps = util.localMatrixOp(self.moduleNameSpace, 'foot_Ik_Con_space')
                cmds.connectAttr(uplegIkSpace+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(footOffsetPlug+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], footIkSpace)

                matrixOps = util.localMatrixOp(self.moduleNameSpace, 'ball_ik_Con_space')
                cmds.connectAttr(footOffsetPlug+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(ballJntOffsetPlug+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], ballIkSpaceLocal)

                matrixOps = util.localMatrixOp(self.moduleNameSpace, 'tip_Ik_Con_space')
                cmds.connectAttr(footOffsetPlug+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(tipJntOffsetPlug+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], tipIkSpaceLocal)

        for controlFkCon in self.filterGroupNodeDic['controlFkCon']:
            controlFkConLocal = util.fullPathName2Local(controlFkCon)
            matchStr = controlFkConLocal[1].replace('_fk_Con', 'Jnt_fk')
            for fkJntNode in self.filterGroupNodeDic['fkJnt']:
                fkJntNodeLocal = util.fullPathName2Local(fkJntNode)
                if fkJntNodeLocal[1] == matchStr:
                    cmds.connectAttr(controlFkCon+'.rotate', fkJntNode+'.rotate', f=True)

        filterDic = {'foot':'ball', 'ball':'tip'}
        sourceNode = ''
        targetNode = ''
        targetUpNode = ''

        for key, value in filterDic.iteritems():
            for ikJnt in self.filterGroupNodeDic['ikJnt']:
                ikJntLocal = util.fullPathName2Local(ikJnt)
                if ikJntLocal[1].rfind(key) != -1:
                    sourceNode = ikJnt
            for controlRef in self.filterGroupNodeDic['controlRef']:
                controlRefLocal = util.fullPathName2Local(controlRef)
                if controlRefLocal[1].rfind(value) != -1:
                    if controlRefLocal[1].rfind('Handle') != -1:
                        targetNode = controlRef
                    elif controlRefLocal[1].rfind('Pole') != -1:
                        targetUpNode = controlRef
            cmds.aimConstraint(targetNode, sourceNode, aim = [1,0,0], u= [0,1,0], wut='object', wuo=targetUpNode)

        for spaceIkNode in self.filterGroupNodeDic['ikSpace']:
            spaceIkNodeLocal = util.fullPathName2Local(spaceIkNode)
            if spaceIkNodeLocal[1].rfind('soft') != -1:
                sourceNode = spaceIkNode
        for controlIkNode in self.filterGroupNodeDic['controlIkCon']:
            controlIkNodeLocal = util.fullPathName2Local(controlIkNode)
            if controlIkNodeLocal[1].rfind('foot') != -1 and controlIkNodeLocal[1].rfind('local') != -1:
                targetNode = controlIkNode
            elif controlIkNodeLocal[1].rfind('leg') != -1 and controlIkNodeLocal[1].rfind('Pole') != -1:
                targetUpNode = controlIkNode
        cmds.aimConstraint(targetNode, sourceNode, aim = [1,0,0], u= [0,1,0], wut='object', wuo=targetUpNode)

        for blendNode in self.filterGroupNodeDic['outputBlend']:
            blendNodeLocal = util.fullPathName2Local(blendNode)
            blendNodeLocalPrefix = blendNodeLocal[1].split('_')[0]
            blendNodeOp = util.createOpNode(self.moduleNameSpace, 'blendColors', blendNodeLocalPrefix+'_blend_op')
            cmds.connectAttr(self.filterGroupNodeDic['fk2ikCon'].keys()[0]+'.fk2ik', blendNodeOp+'.blender', f=True)
            for ikJntNode in self.filterGroupNodeDic['ikJnt']:
                ikJntNodeLocal = util.fullPathName2Local(ikJntNode)
                if  blendNodeLocalPrefix+'_ik' == ikJntNodeLocal[1]:
                    cmds.connectAttr(ikJntNode+'.rotate', blendNodeOp+'.color1', f=True)
            for fkJntNode in self.filterGroupNodeDic['fkJnt']:
                fkJntNodeLocal = util.fullPathName2Local(fkJntNode)
                if  blendNodeLocalPrefix+'_fk' == fkJntNodeLocal[1]:
                    cmds.connectAttr(fkJntNode+'.rotate', blendNodeOp+'.color2', f=True)
            cmds.connectAttr(blendNodeOp+'.output', blendNode+'.rotate', f=True)

            ikConDisplayOp = util.createOpNode(self.moduleNameSpace, 'condition', 'ik_con_display_op')
            cmds.setAttr(ikConDisplayOp+'.operation', 0)
            cmds.setAttr(ikConDisplayOp+'.secondTerm', 1)
            cmds.setAttr(ikConDisplayOp+'.colorIfTrueR', 1)
            cmds.setAttr(ikConDisplayOp+'.colorIfFalseR', 0)
            fkConDisplayOp = util.createOpNode(self.moduleNameSpace, 'condition', 'fk_con_display_op')
            cmds.setAttr(fkConDisplayOp+'.operation', 0)
            cmds.setAttr(fkConDisplayOp+'.secondTerm', 0)
            cmds.setAttr(fkConDisplayOp+'.colorIfTrueR', 1)
            cmds.setAttr(fkConDisplayOp+'.colorIfFalseR', 0)
            cmds.connectAttr(self.filterGroupNodeDic['fk2ikCon'].keys()[0]+'.controlDisplay', ikConDisplayOp+'.firstTerm', f=True)
            cmds.connectAttr(self.filterGroupNodeDic['fk2ikCon'].keys()[0]+'.controlDisplay', fkConDisplayOp+'.firstTerm', f=True)

        for blendNode in self.filterGroupNodeDic['outputBlend']:
            blendNodeLocal = util.fullPathName2Local(blendNode)
            if blendNodeLocal[1].rfind('upleg') != -1:
                cmds.connectAttr(blendNode+'.rotate', self.filterGroupNodeDic['fk2ikSpace'].keys()[0]+'.rotate', f=True)

        placementList = ['Fk', 'Ik']
        for typeStr in placementList:
            for placementNode in self.filterGroupNodeDic['control'+typeStr+'Placement'].iterkeys():
                placementNodeLocal = util.fullPathName2Local(placementNode)
                if placementNodeLocal[1].rfind('upleg') != -1 and placementNodeLocal[1].rfind('fk2ik') == -1:
                    if typeStr == placementList[0]:
                        cmds.connectAttr(fkConDisplayOp+'.outColorR', placementNode+'.visibility', f=True)
                    else:
                        cmds.connectAttr(ikConDisplayOp+'.outColorR', placementNode+'.visibility', f=True)
        
        legPoleAutoAssetPath = self.pathInfo.assetDirPath + 'poleVectorPosAutoOpAsset' + '.' + self.file_extenstion_str
        legPoleAutoOpNode = ''
        legPoleAutoOpNodeNew = ''
        fileCheck = cmds.file( legPoleAutoAssetPath, query=True, exists=True )
        if fileCheck:
            cmds.file( legPoleAutoAssetPath, i=True, mergeNamespacesOnClash=True )
            containerNodes = cmds.ls(type='container', l=True)
            if containerNodes != None:
                for containerNode in containerNodes:
                    localStr = containerNode.split(':')[-1]
                    if localStr == 'poleVectorPosAutoOp':
                        legPoleAutoOpNode = containerNode
        if cmds.objExists(legPoleAutoOpNode):
            legPoleAutoOpNodeNew = cmds.rename(legPoleAutoOpNode, legPoleAutoOpNode + '_' + self.component_val)
        
        uplegIkMotion = ''
        legPoleAuto = ''
        legPoleSideAuto = ''
        legPoleFntAuto = ''
        footIkConLocal = ''
        
        uplegIkMotionStr = ''
        legPoleAutoStr = ''
        legPoleSideAutoStr = ''
        legPoleFntAutoStr = ''
        footIkConLocalStr = ''
        
        for conPoleAutoNode in self.filterGroupNodeDic['controlPoleAuto']:
            conPoleAutoNodeLocal = util.fullPathName2Local(conPoleAutoNode)
            if conPoleAutoNodeLocal[1].rfind('Pole_Auto') != -1:
                legPoleAuto = conPoleAutoNode
                legPoleAutoStr = conPoleAutoNodeLocal[1]
                
            elif conPoleAutoNodeLocal[1].rfind('Side') != -1:
                legPoleSideAuto = conPoleAutoNode
                legPoleSideAutoStr = conPoleAutoNodeLocal[1]
                
            elif conPoleAutoNodeLocal[1].rfind('Fnt') != -1:
                legPoleFntAuto = conPoleAutoNode
                legPoleFntAutoStr = conPoleAutoNodeLocal[1]
                
        for motinoIkSpaceNode in self.filterGroupNodeDic['ikSpace']:
            motinoIkSpaceNodeLocal = util.fullPathName2Local(motinoIkSpaceNode)
            if motinoIkSpaceNodeLocal[1].rfind('upleg') != -1:
                uplegIkMotion = motinoIkSpaceNode
                uplegIkMotionStr = motinoIkSpaceNodeLocal[1]
        
        for conIkNode in self.filterGroupNodeDic['controlIkCon']:
            conIkNodeLocal = util.fullPathName2Local(conIkNode)
            if conIkNodeLocal[1] == 'foot_ik_Con_local':
                footIkConLocal = conIkNode
                footIkConLocalStr = conIkNodeLocal[1]
        
        uplegIkMotionDecompOp = util.createOpNode(self.moduleNameSpace, 'decomposeMatrix', uplegIkMotionStr+'_decomp')
        footIkConLocalDecompOp = util.createOpNode(self.moduleNameSpace, 'decomposeMatrix', footIkConLocalStr+'_decomp')
        legPoleSideAutoDecompOp = util.createOpNode(self.moduleNameSpace, 'decomposeMatrix', legPoleSideAutoStr+'_decomp')
        cmds.connectAttr(uplegIkMotion+'.worldMatrix', uplegIkMotionDecompOp +'.inputMatrix', f=True)
        cmds.connectAttr(footIkConLocal+'.worldMatrix', footIkConLocalDecompOp +'.inputMatrix', f=True)
        cmds.connectAttr(legPoleSideAuto+'.worldMatrix', legPoleSideAutoDecompOp +'.inputMatrix', f=True)
        
        cmds.connectAttr(uplegIkMotionDecompOp+'.outputTranslate', legPoleAutoOpNodeNew +'.Input_ikSpaceWorldPos', f=True)
        cmds.connectAttr(footIkConLocalDecompOp+'.outputTranslate', legPoleAutoOpNodeNew +'.Input_conSpaceWorldPos', f=True)
        cmds.connectAttr(legPoleSideAutoDecompOp+'.outputTranslate', legPoleAutoOpNodeNew +'.Input_ikSideWorldPos', f=True)
        
        legPoleSideAutoCompOp = util.createOpNode(self.moduleNameSpace, 'composeMatrix', legPoleSideAutoStr+'_comp')
        cmds.connectAttr(legPoleAutoOpNodeNew+'.Output_poleVectorWorldPos', legPoleSideAutoCompOp +'.inputTranslate', f=True)
        
        matrixOps = util.localMatrixOp(self.moduleNameSpace, legPoleSideAutoStr+'_comp')
        cmds.connectAttr(legPoleAuto+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(legPoleSideAutoCompOp +'.outputMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], legPoleFntAuto, option=2)
        
        for conIkSpaceNode in self.filterGroupNodeDic['controlIkSpace']:
            conIkSpaceNodeLocal = util.fullPathName2Local(conIkSpaceNode)
            if conIkSpaceNodeLocal[1].rfind('Pole_Pos') != -1:
                cmds.pointConstraint(legPoleFntAuto, conIkSpaceNode)
        
        legFk2IkConNode = self.filterGroupNodeDic['fk2ikCon'].keys()[0]
        if self._side == 'L':
            legFk2IkConShapeNode = cmds.listRelatives(legFk2IkConNode, shapes=True, f=True)[0]
            spanNums = cmds.getAttr(legFk2IkConShapeNode+'.spans')
            spanNums = spanNums + 1
            for i in range(0, spanNums):
                originalPos = cmds.getAttr(legFk2IkConShapeNode+".controlPoints["+ str(i)+"].zValue")
                cmds.setAttr(legFk2IkConShapeNode+".controlPoints["+ str(i)+"].zValue", originalPos * -1)