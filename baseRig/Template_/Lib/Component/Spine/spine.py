import maya.cmds as cmds
import Template.Lib.Util.util as util
import os
import Template.Tool.ComponentManager.globalPath as globalPath

class spineComponent(object):
    def __init__(self, name):
        self.name = name
        self.fitNode = None
        self.component_str = self.name
        self.component_val = 'spine'
        self.fitComponent_str = 'fit'
        self.moduleComponent_str = 'module'
        self.componentType_str = ''
        self.pathInfo = globalPath.globalPath('Spine')
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

        self._side = 'M'
        self._childPlugNodes = {}
        self._parentSocketNodes = {}
        self._useConnectionConNodes = {}
        self.spineLengthOp = None
        self.spineIkCurveNode = None
        
        self._params = [
            {
                'name' : 'live Connection',
                'type' : 'checkBox',
                'default' : False,
                'value': False,
                'callback': 'test'
            },
            {
                'name' : 'Spine Number',
                'type' : 'lineEdit',
                'default' : 5,
                'value': 5,
                'callback': 'test'
            }
            
        ]
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
        motionFkNodes = {}

        motionIkPlacementNodes = {}
        motionIkSpaceNodes = {}
        motionIkNodes = {}
        motionIkHandles = {}
        motionIkCurves = {}

        motionOutputPlacementNodes = {}
        motionOutputSpaceNodes = {}
        motionOutputBlendNodes = {}
        motionOutputSocketNodes = {}

        controlPlacementNodes = {}
        controlFkPlacementNodes = {}
        controlIkPlacementNodes = {}
        
        controlSpaceNodes = {}
        controlFkSpaceNodes = {}
        controlIkSpaceNodes = {}
        
        fkConNodes = {}
        ikConNodes = {}
        refNodes = {}
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
                    util.getChildrenNodes(key, 'fk_node', motionFkNodes, 1)

                elif key.rfind(self.modulePathDic['ik'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionIkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'space', motionIkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'ik_node', motionIkNodes, 1)
                    util.getChildrenNodes(key, 'handle', motionIkHandles, 1)
                    util.getChildrenNodes(key, 'curve', motionIkCurves, 1)

                elif key.rfind(self.modulePathDic['output'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionOutputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'space', motionOutputSpaceNodes, 1)
                    util.getChildrenNodes(key, 'blend', motionOutputBlendNodes, 1)
                    util.getChildrenNodes(key, 'parent_socket', motionOutputSocketNodes, 1)

                elif key.rfind(self.modulePathDic['control'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', controlPlacementNodes, 1)
                    util.getChildrenNodes(key, 'fk_control_placement', controlFkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'ik_control_placement', controlIkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'space', controlSpaceNodes, 1)
                    util.getChildrenNodes(key, 'fk_control_space', controlFkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'ik_control_space', controlIkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'fk_Con', fkConNodes, 1)
                    util.getChildrenNodes(key, 'ik_Con', ikConNodes, 1)
                    util.getChildrenNodes(key, 'ref', refNodes, 1)
                    util.getChildrenNodes(key, 'fk2ik_Con', fk2ikConNodes, 1)
                    util.getChildrenNodes(key, 'fk2ik_space', fk2ikSpaceNodes, 1)
                else:
                    continue

        self.filterGroupNodeDic['init'] = initNodes

        self.filterGroupNodeDic['inputPlacement'] = motionInputPlacementNodes
        self.filterGroupNodeDic['inputChildPlug'] = motionInputPlugNodes

        self.filterGroupNodeDic['fkPlacement'] = motionFkPlacementNodes
        self.filterGroupNodeDic['fkSpace'] = motionFkSpaceNodes
        self.filterGroupNodeDic['fkJnt'] = motionFkNodes

        self.filterGroupNodeDic['ikPlacement'] = motionIkPlacementNodes
        self.filterGroupNodeDic['ikSpace'] = motionIkSpaceNodes
        self.filterGroupNodeDic['ikJnt'] = motionIkNodes
        self.filterGroupNodeDic['ikHandle'] = motionIkHandles
        self.filterGroupNodeDic['ikCurve'] = motionIkCurves

        self.filterGroupNodeDic['outputPlacement'] = motionOutputPlacementNodes
        self.filterGroupNodeDic['outputSpace'] = motionOutputSpaceNodes
        self.filterGroupNodeDic['outputBlend'] = motionOutputBlendNodes
        self.filterGroupNodeDic['outputParentSocket'] = motionOutputSocketNodes

        self.filterGroupNodeDic['controlPlacement'] = controlPlacementNodes
        self.filterGroupNodeDic['controlFkPlacement'] = controlFkPlacementNodes
        self.filterGroupNodeDic['controlIkPlacement'] = controlIkPlacementNodes
        self.filterGroupNodeDic['controlSpace'] = controlSpaceNodes
        self.filterGroupNodeDic['controlFkSpace'] = controlFkSpaceNodes
        self.filterGroupNodeDic['controlIkSpace'] = controlIkSpaceNodes
        self.filterGroupNodeDic['controlFkCon'] = fkConNodes
        self.filterGroupNodeDic['controlIkCon'] = ikConNodes
        self.filterGroupNodeDic['controlRef'] = refNodes
        
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

        self.updateCurveRestlength()

        liveConnection = self.params[0]['value']
        if liveConnection != True:
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
    
    def updateCurveRestlength(self):
        if self.spineLengthOp != None:
            defaultCurveLength = cmds.getAttr(self.spineLengthOp+'.arcLength')
            if self.spineIkCurveNode != None:
                cmds.setAttr(self.spineIkCurveNode+'.restCurveLength', defaultCurveLength)

    def applyInitNodeConnections(self):

        initNodeFullName = cmds.ls(self.modulePathDic['init'], l=True)[0]
        placementNodesList = [self.filterGroupNodeDic['inputPlacement'], self.filterGroupNodeDic['ikPlacement'], self.filterGroupNodeDic['controlPlacement']]

        p0_init_full = ''
        p0_handle_init_full = ''
        p1_init_full = ''
        p1_handle_init_full = ''
        spine_init_full = ''
        
        for initNode, parentNode in self.filterGroupNodeDic['init'].iteritems():
            initLocalNode = util.fullPathName2Local(initNode)
            if initLocalNode[1].replace('_init', '') == 'p0':
                p0_init_full = initNode
            elif initLocalNode[1].replace('_init', '') == 'p0_handle':
                p0_handle_init_full = initNode
            elif initLocalNode[1].replace('_init', '') == 'p1':
                p1_init_full = initNode
            elif initLocalNode[1].replace('_init', '') == 'p1_handle':
                p1_handle_init_full = initNode
            else:
                spine_init_full = initNode

        for placementNodes in placementNodesList:
            for placementNode in placementNodes:
                placementLocalNode = util.fullPathName2Local(placementNode)
                if placementLocalNode[1].rfind('p0_placement') != -1:
                    matrixOps = util.localMatrixOp(self.moduleNameSpace, placementLocalNode[1])
                    cmds.connectAttr(spine_init_full+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                    cmds.connectAttr(p0_init_full+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                    util.decompChannelBinding(matrixOps[1], placementNode)
        
        p0_init_worldMOp = util.createOpNode(self.moduleNameSpace,'decomposeMatrix', 'p0_init_worldM')
        p1_init_worldMOp = util.createOpNode(self.moduleNameSpace,'decomposeMatrix', 'p1_init_worldM')
        p0_p1_distanceOp = util.createOpNode(self.moduleNameSpace,'distanceBetween', 'p0_p1_distance')
        p0_p1_distance_negOp = util.createOpNode(self.moduleNameSpace,'multiplyDivide', 'p0_p1_distance_neg')
        p0_p1_midPosOp = util.createOpNode(self.moduleNameSpace,'blendColors', 'p0_p1_midPos')
        p0_p1_midPosMOp = util.createOpNode(self.moduleNameSpace,'composeMatrix', 'p0_p1_midPosM')
        
        cmds.connectAttr(p0_init_full+'.worldMatrix', p0_init_worldMOp+'.inputMatrix', f=True)
        cmds.connectAttr(p1_init_full+'.worldMatrix', p1_init_worldMOp+'.inputMatrix', f=True)
        cmds.connectAttr(p0_init_full+'.worldMatrix', p0_p1_distanceOp+'.inMatrix1', f=True)
        cmds.connectAttr(p1_init_full+'.worldMatrix', p0_p1_distanceOp+'.inMatrix2', f=True)
        cmds.connectAttr(p0_p1_distanceOp+'.distance', p0_p1_distance_negOp+'.input1Z', f=True)
        cmds.setAttr(p0_p1_distance_negOp+'.input2Z', -2)
        cmds.connectAttr(p0_init_worldMOp+'.outputTranslate', p0_p1_midPosOp+'.color1', f=True)
        cmds.connectAttr(p1_init_worldMOp+'.outputTranslate', p0_p1_midPosOp+'.color2', f=True)
        cmds.setAttr(p0_p1_midPosOp+'.blender', 0.5)
        cmds.connectAttr(p0_p1_midPosOp+'.output', p0_p1_midPosMOp+'.inputTranslate', f=True)
        
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'p0_p1_midPosM')
        distance_sum_posOp = util.createOpNode(self.moduleNameSpace,'plusMinusAverage', 'distance_sum_pos')
        
        cmds.connectAttr(p0_p1_midPosMOp+'.outputMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        cmds.connectAttr(spine_init_full+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(matrixOps[1]+'.outputTranslate', distance_sum_posOp+'.input3D[0]', f=True)
        cmds.connectAttr(p0_p1_distance_negOp+'.output', distance_sum_posOp+'.input3D[1]', f=True)
        
        spinePolePlacementNode = ''
        spineUpvectorNode = ''
        
        for spinePoleNode in self.filterGroupNodeDic['inputPlacement']:
            spinePoleNodeLocal = util.fullPathName2Local(spinePoleNode)
            if spinePoleNodeLocal[1].rfind('pole') != -1:
                spinePolePlacementNode = spinePoleNode
        
        for spineUpvec in self.filterGroupNodeDic['controlPlacement']:
            spineUpvecLocal = util.fullPathName2Local(spineUpvec)
            if spineUpvecLocal[1].rfind('upvector') != -1:
                spineUpvectorNode = spineUpvec
        
        cmds.connectAttr(distance_sum_posOp+'.output3D', spinePolePlacementNode+'.translate', f=True)
        cmds.connectAttr(distance_sum_posOp+'.output3D', spineUpvectorNode+'.translate', f=True)
        
        util.decompChannelBinding(matrixOps[1], spinePolePlacementNode, option=3)
        util.decompChannelBinding(matrixOps[1], spineUpvectorNode, option=3)
        util.decompChannelBinding(matrixOps[1], spinePolePlacementNode, option=4)
        util.decompChannelBinding(matrixOps[1], spineUpvectorNode, option=4)
        
        spinePoleChildPlug = ''
        spineUpVectorSpace = ''
        for childPlugNode in self.filterGroupNodeDic['inputChildPlug']:
            childPlugNodeLocal = util.fullPathName2Local(childPlugNode)
            if childPlugNodeLocal[1].rfind('spine_pole') != -1:
                spinePoleChildPlug = childPlugNode
        
        for controlSpaceNode in self.filterGroupNodeDic['controlSpace']:
            controlSpaceNodeLocal = util.fullPathName2Local(controlSpaceNode)
            if controlSpaceNodeLocal[1].rfind('spine_upvector') != -1:
                spineUpVectorSpace = controlSpaceNode
        
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'spineUpVec_space')
        cmds.connectAttr(spineUpvectorNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(spinePoleChildPlug+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], spineUpVectorSpace)

        p0HandlePlacementNode = ''
        spineP0HandlePlacementNode = ''
        
        for ikPlacementNode in self.filterGroupNodeDic['ikPlacement']:
            ikPlacementNodeLocal = util.fullPathName2Local(ikPlacementNode)
            if ikPlacementNodeLocal[1].rfind('p0_handle') != -1:
                p0HandlePlacementNode = ikPlacementNode
                
        for controlPlacementNode in self.filterGroupNodeDic['controlPlacement']:
            controlPlacementNodeLocal = util.fullPathName2Local(controlPlacementNode)
            if controlPlacementNodeLocal[1].rfind('p0_handle') != -1:
                spineP0HandlePlacementNode = controlPlacementNode
        
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'spine_p0_handle')
        cmds.connectAttr(p0_init_full+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(p0_handle_init_full+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], spineP0HandlePlacementNode)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'p0_handle_placement')
        cmds.connectAttr(spine_init_full+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(p0_handle_init_full+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], p0HandlePlacementNode)

        p1PlacementArrayFilterList = ['inputPlacement', 'ikPlacement', 'controlPlacement']
        p1PlacementNodeList = []

        for p1PlacementArrayFilter in p1PlacementArrayFilterList:
            for placementNode in self.filterGroupNodeDic[p1PlacementArrayFilter]:
                placementNodeLocal = util.fullPathName2Local(placementNode)
                if placementNodeLocal[1].rfind('p1_placement') != -1:
                    p1PlacementNodeList.append(placementNode)

        for p1PlacementNode in p1PlacementNodeList:
            p1PlacementNodeLocal = util.fullPathName2Local(p1PlacementNode)
            matrixOps = util.localMatrixOp(self.moduleNameSpace, p1PlacementNodeLocal[1])
            cmds.connectAttr(spine_init_full+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
            cmds.connectAttr(p1_init_full+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
            util.decompChannelBinding(matrixOps[1], p1PlacementNode)

        for placementNode in self.filterGroupNodeDic['controlPlacement']:
            placementNodeLocal = util.fullPathName2Local(placementNode)
            if placementNodeLocal[1].rfind('p1_handle') != -1:
                matrixOps = util.localMatrixOp(self.moduleNameSpace, placementNodeLocal[1])
                cmds.connectAttr(p1_init_full+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(p1_handle_init_full+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], placementNode)

        for placementNode in self.filterGroupNodeDic['ikPlacement']:
            placementNodeLocal = util.fullPathName2Local(placementNode)
            if placementNodeLocal[1].rfind('p1_handle') != -1:
                matrixOps = util.localMatrixOp(self.moduleNameSpace, placementNodeLocal[1])
                cmds.connectAttr(spine_init_full+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(p1_handle_init_full+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], placementNode)

        spineikPlacementArrayFilterList = ['inputPlacement', 'ikPlacement', 'fkPlacement','controlPlacement','outputPlacement']
        for spineikPlacementArrayFilter in spineikPlacementArrayFilterList:
            for placementNode in self.filterGroupNodeDic[spineikPlacementArrayFilter]:
                placementNodeLocal = util.fullPathName2Local(placementNode)
                if placementNodeLocal[1].rfind('spine_ik') != -1 or placementNodeLocal[1].rfind('spine_fk') != -1 or placementNodeLocal[1].rfind('spine_output') != -1 or placementNodeLocal[1].rfind('spine_input') != -1:
                    util.transformChannelBinding(spine_init_full, placementNode)
                    
    def applyMotionNodeConnections(self):
        
        filterStrList = ['p0', 'p1']
        filterStrList2 = ['controlSpace', 'ikSpace']
        
        for childPlugNode in self.filterGroupNodeDic['inputChildPlug']:
            childPlugNodeLocal = util.fullPathName2Local(childPlugNode)
            for filterStr in filterStrList:
                if childPlugNodeLocal[1].rfind(filterStr) != -1 and childPlugNodeLocal[1].rfind('pole') == -1:
                    for controlPlacementNode in self.filterGroupNodeDic['controlPlacement']:
                        controlPlacementNodeLocal = util.fullPathName2Local(controlPlacementNode)
                        controlSpaceNodeLocal = controlPlacementNodeLocal[1].replace('placement', 'space')
                        if controlPlacementNodeLocal[1].rfind(filterStr+'_placement') != -1:
                            controlSpaceNode = controlPlacementNode + '|'+ self.moduleNameSpace + ':' + controlSpaceNodeLocal
                            matrixOps = util.localMatrixOp(self.moduleNameSpace, controlSpaceNodeLocal)
                            cmds.connectAttr(controlPlacementNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                            cmds.connectAttr(childPlugNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                            util.decompChannelBinding(matrixOps[1], controlSpaceNode)
                            
        for childPlugNode in self.filterGroupNodeDic['inputChildPlug']:
            childPlugNodeLocal = util.fullPathName2Local(childPlugNode)
            if childPlugNodeLocal[1].rfind('spine_child') != -1:
                for filterStr2 in filterStrList2:
                    for spaceNode in self.filterGroupNodeDic[filterStr2]:
                        spaceNodeLocal = util.fullPathName2Local(spaceNode)
                        if spaceNodeLocal[1].rfind('_ik_space') != -1:
                            util.transformChannelBinding(childPlugNode, spaceNode)

        curveInputs = ['','','','']
        
        for spaceNode in self.filterGroupNodeDic['ikSpace']:
            spaceNodeLocal = util.fullPathName2Local(spaceNode)
            nodeLocal = spaceNodeLocal[1].replace('_space', '')
            node = spaceNode + '|'+ self.moduleNameSpace + ':' + nodeLocal
            if nodeLocal == 'p0':
                curveInputs[0] = node
            elif nodeLocal == 'p0_handle':
                curveInputs[1] = node
            elif nodeLocal == 'p1_handle':
                curveInputs[2] = node
            elif nodeLocal == 'p1':
                curveInputs[3] = node
                
            for controlIkConNode in self.filterGroupNodeDic['controlIkCon']:
                controlIkConNodeLocal = util.fullPathName2Local(controlIkConNode)
                if controlIkConNodeLocal[1] == 'spine_' + nodeLocal + '_ik_Con':
                    matrixOps = util.localMatrixOp(self.moduleNameSpace, nodeLocal)
                    cmds.connectAttr(spaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                    cmds.connectAttr(controlIkConNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                    util.decompChannelBinding(matrixOps[1], node)

        self.spineIkCurveNode = ''
        spineIkCurveShapeNode = ''
        spineIkConCurveShapeNode = ''
        
        for ikCurveNode in self.filterGroupNodeDic['ikCurve']:
            ikCurveNodeLocal = util.fullPathName2Local(ikCurveNode)
            cmds.connectAttr(self.filterGroupNodeDic['fk2ikCon'].keys()[0]+'.debugDisplay', ikCurveNode+'.visibility', f=True)
            
            if ikCurveNodeLocal[1].rfind('con') == -1:
                self.spineIkCurveNode = ikCurveNode
                children = cmds.listRelatives(ikCurveNode, c=1, s=1, f=1)
                spineIkCurveShapeNode = children[0]
            else:
                children = cmds.listRelatives(ikCurveNode, c=1, s=1, f=1)
                spineIkConCurveShapeNode = children[0]
                
        for i in range(0, len(curveInputs)):
            curveInputLocal = util.fullPathName2Local(curveInputs[i])
            matrixOps = util.localMatrixOp(self.moduleNameSpace, curveInputLocal[1]+'_input')
            cmds.connectAttr(self.spineIkCurveNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
            cmds.connectAttr(curveInputs[i]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
            cmds.connectAttr(matrixOps[1]+'.outputTranslate', spineIkCurveShapeNode+'.controlPoints['+str(i) + ']')
            cmds.connectAttr(matrixOps[1]+'.outputTranslate', spineIkConCurveShapeNode+'.controlPoints['+str(i) + ']')

        self.spineLengthOp = util.createOpNode(self.moduleNameSpace, 'curveInfo', 'spine_length')
        
        lengthPreserveCondOp = util.createOpNode(self.moduleNameSpace, 'condition', 'length_preserve_condition')
        cmds.setAttr(lengthPreserveCondOp+'.operation', 3)
        cmds.setAttr(lengthPreserveCondOp+'.colorIfTrueR', 1)
        cmds.setAttr(lengthPreserveCondOp+'.colorIfFalseR', 0)
        
        lengthPreserveWeightOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', 'length_preserve_weight')
        cmds.setAttr(lengthPreserveWeightOp+'.operation', 1)
        
        lengthPreserveBlendOp = util.createOpNode(self.moduleNameSpace, 'blendTwoAttr', 'length_preserve_blend')
        lengthRatioOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', 'length_ratio')
        cmds.setAttr(lengthRatioOp+'.operation', 2)
        
        cmds.connectAttr(spineIkCurveShapeNode+'.worldSpace', self.spineLengthOp+'.inputCurve', f=True)
        
        cmds.connectAttr(self.spineLengthOp+'.arcLength', lengthPreserveCondOp+'.firstTerm', f=True)
        cmds.connectAttr(self.spineIkCurveNode+'.restCurveLength', lengthPreserveCondOp+'.secondTerm', f=True)

        #defaultCurveLength = cmds.getAttr(self.spineLengthOp+'.arcLength')
        #print "Curve initial Length:", defaultCurveLength
        #cmds.setAttr(self.spineIkCurveNode+'.restCurveLength', defaultCurveLength)
        #currentCurveLength = cmds.getAttr(self.spineIkCurveNode+'.restCurveLength')
        #print "Curve current Length:", currentCurveLength
        
        self.updateCurveRestlength()

        cmds.connectAttr(self.spineIkCurveNode+'.preserveLength', lengthPreserveWeightOp+'.input1X', f=True)
        cmds.connectAttr(lengthPreserveCondOp+'.outColorR', lengthPreserveWeightOp+'.input2X', f=True)
        
        cmds.connectAttr(lengthPreserveWeightOp+'.outputX', lengthPreserveBlendOp+'.attributesBlender', f=True)
        cmds.connectAttr(self.spineLengthOp+'.arcLength', lengthPreserveBlendOp+'.input[0]', f=True)
        cmds.connectAttr(self.spineIkCurveNode+'.restCurveLength', lengthPreserveBlendOp+'.input[1]', f=True)
        
        cmds.connectAttr(lengthPreserveBlendOp+'.output', lengthRatioOp+'.input1X', f=True)

        spineNumOption = self._params[1]['value']
        print "spine sample number:", spineNumOption
        cmds.setAttr(lengthRatioOp+'.input2X', spineNumOption)

        spineIkSampleSpaceNode = ''
        for ikSpaceNode in self.filterGroupNodeDic['ikSpace']:
            ikSpaceNodeLocal = util.fullPathName2Local(ikSpaceNode)
            if ikSpaceNodeLocal[1].rfind('sample') != -1:
                spineIkSampleSpaceNode = ikSpaceNode

        nodeList = []
        nodeTwistList = []
        nodeRefList = []
        endNode = ''
        for i in range(0, spineNumOption+1):
            spineRatioOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', 'spine_0'+str(i)+'_ratio')
            cmds.setAttr(spineRatioOp+'.operation', 1)
            cmds.setAttr(spineRatioOp+'.input1X', i)
            cmds.connectAttr(lengthRatioOp+'.outputX', spineRatioOp+'.input2X', f=True)
            length2ParamOp = util.createOpNode(self.moduleNameSpace, 'curveLength2ParamU', 'spine_0'+str(i)+'_length2Param')
            cmds.connectAttr(spineRatioOp+'.outputX', length2ParamOp+'.inputLength', f=True)
            cmds.connectAttr(spineIkCurveShapeNode+'.worldSpace', length2ParamOp+'.inputCurve', f=True)
            
            pointOnCurveOp = util.createOpNode(self.moduleNameSpace, 'pointOnCurveInfo', 'spine_0'+str(i)+'_pointOnCurve')
            cmds.connectAttr(length2ParamOp+'.outputParamU', pointOnCurveOp+'.parameter', f=True)
            cmds.connectAttr(spineIkCurveShapeNode+'.worldSpace', pointOnCurveOp+'.inputCurve', f=True)
            
            composeMatOp = util.createOpNode(self.moduleNameSpace, 'composeMatrix', 'spine_0'+str(i)+'_composeM')
            cmds.connectAttr(pointOnCurveOp+'.position', composeMatOp+'.inputTranslate', f=True)
            
            matrixOps = util.localMatrixOp(self.moduleNameSpace, 'spine_0'+str(i))
            cmds.connectAttr(spineIkSampleSpaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
            cmds.connectAttr(composeMatOp+'.outputMatrix', matrixOps[0]+'.matrixIn[0]', f=True)

            nodes = cmds.spaceLocator(n='spine_node_0'+str(i))
            shapeNodes = cmds.listRelatives(nodes[0], s=True)
            cmds.delete(shapeNodes)
            refNodes = cmds.spaceLocator(n='spine_node_0'+str(i)+'_ref')
            shapeNodes = cmds.listRelatives(refNodes[0], s=True)
            cmds.delete(shapeNodes)
            twistNodes = cmds.spaceLocator(n='spine_twist_0'+str(i))
            shapeNodes = cmds.listRelatives(twistNodes[0], s=True)
            cmds.delete(shapeNodes)
            
            nodeFull = cmds.ls(nodes[0], l=True)[0]
            refNodeFull = cmds.ls(refNodes[0], l=True)[0]
            twistNodeFull = cmds.ls(twistNodes[0], l=True)[0]
            
            node = cmds.parent(nodeFull, spineIkSampleSpaceNode)[0]
            twistNode = cmds.parent(twistNodeFull, node)[0]
            refNode = cmds.parent(refNodeFull, node)[0]
            util.decompChannelBinding(matrixOps[1], node, option=2)
            util.decompChannelBinding(matrixOps[1], node, option=4)
            nodeList.append(node)
            nodeTwistList.append(twistNode)
            nodeRefList.append(refNode)
            
            if i == spineNumOption:
                end_nodes = cmds.spaceLocator(n='spine_node_0'+str(i)+'_end')
                shapeNodes = cmds.listRelatives(end_nodes[0], s=True)
                cmds.delete(shapeNodes)
                end_nodeFull = cmds.ls(end_nodes[0], l=True)[0]
                end_node = cmds.parent(end_nodeFull, spineIkSampleSpaceNode)[0]
                util.decompChannelBinding(matrixOps[1], end_node)
                endNode = end_node
        
        upVectorRefNod = self.filterGroupNodeDic['controlRef'].keys()[0]
        for i in range(0, len(nodeList)):
            aimVector = [0,1,0]
            aimVectorReverse = [0,-1,0]
            upVecttor = [0,0,-1]
            if i < len(nodeList)-2:
                cmds.aimConstraint(nodeList[i+1], nodeList[i], aim=aimVector, u=upVecttor, wut='object', wuo=upVectorRefNod)
            elif i == len(nodeList)-2:
                cmds.aimConstraint(endNode, nodeList[i], aim=aimVector, u=upVecttor, wut='object', wuo=upVectorRefNod)
            elif i == len(nodeList)-1:
                cmds.aimConstraint(nodeList[i-1], nodeList[i], aim=aimVectorReverse, u=upVecttor, wut='object', wuo=upVectorRefNod)

        spineTwistSpace = ''
        spineStartTwistSpace = ''
        spineEndTwistSpace = ''
        fk2ikSpace = ''
        for controlSpaceNode in self.filterGroupNodeDic['controlSpace']:
            controlSpaceNodeLocal = util.fullPathName2Local(controlSpaceNode)
            if controlSpaceNodeLocal[1].rfind('spine_twist') != -1:
                spineTwistSpace = controlSpaceNode
            elif controlSpaceNodeLocal[1].rfind('start_twist') != -1:
                spineStartTwistSpace = controlSpaceNode
            elif controlSpaceNodeLocal[1].rfind('end_twist') != -1:
                spineEndTwistSpace = controlSpaceNode
            elif controlSpaceNodeLocal[1].rfind('fk2ik') != -1:
                fk2ikSpace = controlSpaceNode

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'spine_start_twsit')
        cmds.connectAttr(spineTwistSpace+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(nodeRefList[0]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], spineStartTwistSpace)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'spine_end_twsit')
        cmds.connectAttr(spineTwistSpace+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(nodeRefList[-1]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], spineEndTwistSpace)
        
        cmds.pointConstraint([spineStartTwistSpace, spineEndTwistSpace], fk2ikSpace)

        twistConList = ['','']
        conList = ['','']
        for ikConNode in self.filterGroupNodeDic['controlIkCon']:
            ikConNodeLocal = util.fullPathName2Local(ikConNode)
            if ikConNodeLocal[1].rfind('start_twist') != -1:
                twistConList[0] = ikConNode
            elif ikConNodeLocal[1].rfind('end_twist') != -1:
                twistConList[1] = ikConNode
            elif ikConNodeLocal[1].rfind('start_ik_Con') != -1:
                conList[0] = ikConNode
            elif ikConNodeLocal[1].rfind('end_ik_Con') != -1:
                conList[1] = ikConNode

        filterStrList = ['p0', 'p1']
        for childPlugNode in self.filterGroupNodeDic['inputChildPlug']:
            childPlugNodeLocal = util.fullPathName2Local(childPlugNode)
            if childPlugNodeLocal[1].rfind(filterStrList[0]) != -1:
                mainConNode = conList[0]
                inputChildNode = childPlugNode
                twistConNode = twistConList[0]
                twistConSumYOp = util.createOpNode(self.moduleNameSpace, 'addDoubleLinear', 'twist_control_sum_0'+str(i))
                cmds.connectAttr(mainConNode+'.rotateY', twistConSumYOp+'.input1', f=True)
                cmds.connectAttr(inputChildNode+'.rotateY', twistConSumYOp+'.input2', f=True)
                cmds.connectAttr(twistConSumYOp+'.output', twistConNode+'.rotateY', f=True)
            elif childPlugNodeLocal[1].rfind(filterStrList[1]) != -1:
                mainConNode = conList[1]
                inputChildNode = childPlugNode
                twistConNode = twistConList[1]
                twistConSumYOp = util.createOpNode(self.moduleNameSpace, 'addDoubleLinear', 'twist_control_sum_0'+str(i))
                cmds.connectAttr(mainConNode+'.rotateY', twistConSumYOp+'.input1', f=True)
                cmds.connectAttr(inputChildNode+'.rotateY', twistConSumYOp+'.input2', f=True)
                cmds.connectAttr(twistConSumYOp+'.output', twistConNode+'.rotateY', f=True)
                
        twistRatioList = []
        twistRatioListRevese = []
        for i in range(0, len(nodeList)):
            twistRatioOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', 'twistRatio_0'+str(i))
            cmds.setAttr(twistRatioOp+'.operation', 2)
            cmds.setAttr(twistRatioOp+'.input1X', i)
            cmds.setAttr(twistRatioOp+'.input2X', len(nodeList)-1)
            twistRatioList.append(twistRatioOp)
        twistRatioListRevese = twistRatioList[::-1]

        startInterpApplyOpList = []
        endInterpApplyOpList = []
        for i in range(0, len(twistConList)):
            prefix = ''
            if i == 0:
                prefix = 'startTwist0'
            else:
                prefix = 'endTwist0'
            for j in range(0, len(nodeList)):
                interpApplyOp = util.createOpNode(self.moduleNameSpace, 'multDoubleLinear', prefix+str(j)+'_apply')
                cmds.addAttr(twistConList[i], ln= prefix+str(j), attributeType='float')
                cmds.connectAttr(twistConList[i]+'.rotateY', interpApplyOp+'.input1')
                cmds.connectAttr(interpApplyOp+'.output', twistConList[i]+'.'+prefix+str(j))
                if i == 0:
                    startInterpApplyOpList.append(interpApplyOp)
                else:
                    endInterpApplyOpList.append(interpApplyOp)

        for i in range(0, len(nodeList)):
            cmds.connectAttr(twistRatioList[i]+'.outputX', endInterpApplyOpList[i]+'.input2', f=True)
        for i in range(0, len(nodeList)):
            cmds.connectAttr(twistRatioListRevese[i]+'.outputX', startInterpApplyOpList[i]+'.input2', f=True)
        
        for i in range(0, len(nodeList)):
            twistSumOp = util.createOpNode(self.moduleNameSpace, 'addDoubleLinear', 'twist_sum_0'+str(i))
            for j in range(0, len(twistConList)):
                if j == 0:
                    cmds.connectAttr(twistConList[j]+'.startTwist0'+str(i), twistSumOp+'.input1', f=True)
                else:
                    cmds.connectAttr(twistConList[j]+'.endTwist0'+str(i), twistSumOp+'.input2', f=True)
            cmds.connectAttr(twistSumOp+'.output', nodeTwistList[i]+'.rotateY', f=True)

        spineIkNodeSpaceNode = ''
        for ikSpaceNode in self.filterGroupNodeDic['ikSpace']:
            ikSpaceNodeLocal = util.fullPathName2Local(ikSpaceNode)
            if ikSpaceNodeLocal[1].rfind('node') != -1:
                spineIkNodeSpaceNode = ikSpaceNode

        spineIkNodeList = []
        spineIkNode = ''
        for i in range(0, spineNumOption+1):
            if i == 0:
                spineIkNodes = cmds.spaceLocator(n='spine_ik_node_0'+str(i))
                shapeNodes = cmds.listRelatives(spineIkNodes[0], s=True)
                cmds.delete(shapeNodes)
                spineIkNodeFull = cmds.ls(spineIkNodes[0], l=True)[0]
                spineIkNode = cmds.parent(spineIkNodeFull, spineIkNodeSpaceNode)[0]
            else:
                spineIkNodes = cmds.spaceLocator(n='spine_ik_node_0'+str(i))
                shapeNodes = cmds.listRelatives(spineIkNodes[0], s=True)
                cmds.delete(shapeNodes)                
                spineIkNodeFull = cmds.ls(spineIkNodes[0], l=True)[0]
                childNode = cmds.parent(spineIkNodeFull, spineIkNode)[0]
                spineIkNode = childNode
            spineIkNodeList.append(spineIkNode)
            
        for i in range(0, len(spineIkNodeList)):
            spineIkNodeLocal = spineIkNodeList[i].split(':')[-1]
            matrixOps = util.localMatrixOp(self.moduleNameSpace, spineIkNodeLocal)
            parentSpaceNode = ''
            if i == 0:
                parentSpaceNode = spineIkNodeSpaceNode
            else:
                parentSpaceNode = nodeTwistList[i-1]
            cmds.connectAttr(parentSpaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
            cmds.connectAttr(nodeTwistList[i]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
            util.decompChannelBinding(matrixOps[1], spineIkNodeList[i])

        spineControlFkSpaceNode = ''
        for controlFkSpaceNode in self.filterGroupNodeDic['controlFkSpace']:
            controlFkSpaceNodeLocal = util.fullPathName2Local(controlFkSpaceNode)
            if controlFkSpaceNodeLocal[1].rfind('spine_fk') != -1:
                spineControlFkSpaceNode = controlFkSpaceNode

                
        util.fileLoad('icons', self.templateDir, self.component_val, self.moduleNameSpace, self.file_extenstion_str)
        fkConPath = self.moduleNameSpace+':fk_Con'
        visualNodePath = self.moduleNameSpace+':visualNode'
        fkConTemplate = cmds.ls(fkConPath[1:], l=True)[0]
        visualNodeTemplate = cmds.ls(visualNodePath[1:], l=True)[0]

        spineConFkSpaceNodeList = []
        spineConFkSpaceNode = ''
        for i in range(0, spineNumOption+1):
            if i == 0:
                spineConFkSpaceNodes = cmds.spaceLocator(n='spine_0'+str(i)+'_fk_space')
                shapeNodes = cmds.listRelatives(spineConFkSpaceNodes[0], s=True)
                cmds.delete(shapeNodes)
                spineConFkSpaceNodeFull = cmds.ls(spineConFkSpaceNodes[0], l=True)[0]
                spineConFkSpaceNode = cmds.parent(spineConFkSpaceNodeFull, spineControlFkSpaceNode)[0]
                
                matrixOps = util.localMatrixOp(self.moduleNameSpace, 'spine_0'+str(i)+'_fk_space')
                cmds.connectAttr(spineControlFkSpaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(nodeTwistList[i]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], spineConFkSpaceNode)
                
                fkConTemplateDup = cmds.duplicate(fkConTemplate, st=True, n='spine_0'+str(i)+'_fk_Con')[0]
                childNode = cmds.parent(fkConTemplateDup, spineConFkSpaceNode, r=True)[0]
                spineConFkSpaceNode = childNode
            else:
                spineConFkSpaceNodes = cmds.spaceLocator(n='spine_0'+str(i)+'_fk_space')
                shapeNodes = cmds.listRelatives(spineConFkSpaceNodes[0], s=True)
                cmds.delete(shapeNodes)
                spineConFkSpaceNodeFull = cmds.ls(spineConFkSpaceNodes[0], l=True)[0]
                parentSpaceNode = spineConFkSpaceNode
                spineConFkSpaceNode = cmds.parent(spineConFkSpaceNodeFull, parentSpaceNode)[0]

                matrixOps = util.localMatrixOp(self.moduleNameSpace, 'spine_0'+str(i)+'_fk_space')
                cmds.connectAttr(nodeTwistList[i-1]+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(nodeTwistList[i]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], spineConFkSpaceNode)
                
                fkConTemplateDup = cmds.duplicate(fkConTemplate, st=True, n='spine_0'+str(i)+'_fk_Con')[0]
                childNode = cmds.parent(fkConTemplateDup, spineConFkSpaceNode, r=True)[0]
                spineConFkSpaceNode = childNode
            spineConFkSpaceNodeList.append(spineConFkSpaceNode)

        spineFkNodeSpaceNode = ''
        for fkSpaceNode in self.filterGroupNodeDic['fkSpace']:
            fkSpaceNodeLocal = util.fullPathName2Local(fkSpaceNode)
            if fkSpaceNodeLocal[1].rfind('node') != -1:
                spineFkNodeSpaceNode = fkSpaceNode

        spineFkNodeList = []
        spineFkNode = ''
        for i in range(0, spineNumOption+1):
            if i == 0:
                spineFkNodes = cmds.spaceLocator(n='spine_fk_node_0'+str(i))
                shapeNodes = cmds.listRelatives(spineFkNodes[0], s=True)
                cmds.delete(shapeNodes)
                spineFkNodeFull = cmds.ls(spineFkNodes[0], l=True)[0]
                spineFkNode = cmds.parent(spineFkNodeFull, spineFkNodeSpaceNode)[0]

                matrixOps = util.localMatrixOp(self.moduleNameSpace, 'spine_fk_node_0'+str(i))
                cmds.connectAttr(spineFkNodeSpaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(spineConFkSpaceNodeList[i]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], spineFkNode)
                
            else:
                spineFkNodes = cmds.spaceLocator(n='spine_fk_node_0'+str(i))
                shapeNodes = cmds.listRelatives(spineFkNodes[0], s=True)
                cmds.delete(shapeNodes)
                spineFkNodeFull = cmds.ls(spineFkNodes[0], l=True)[0]
                childNode = cmds.parent(spineFkNodeFull, spineFkNode)[0]
                
                matrixOps = util.localMatrixOp(self.moduleNameSpace, 'spine_fk_node_0'+str(i))
                cmds.connectAttr(spineFkNodeList[i-1]+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(spineConFkSpaceNodeList[i]+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], childNode)
                
                spineFkNode = childNode
            spineFkNodeList.append(spineFkNode)

        spineOutputSpaceNode = ''
        for outputSpaceNode in self.filterGroupNodeDic['outputSpace']:
            outputSpaceNodeLocal = util.fullPathName2Local(outputSpaceNode)
            if outputSpaceNodeLocal[1].rfind('output') != -1:
                spineOutputSpaceNode = outputSpaceNode
        
        spineOutputNodeList = []
        spineBlendNode = ''
        for i in range(0, spineNumOption+1):
            if i == 0:
                spineBlendNodes = cmds.spaceLocator(n='spine_blend_node_0'+str(i))
                spineParentSocketNodes = cmds.spaceLocator(n='spine_0'+str(i)+'_parent_socket')
                cmds.select(clear=True)
                spineJntNode = cmds.joint(n='spine_0'+str(i)+'_jnt')
                cmds.setAttr(spineJntNode+'.radius', 0.5)
                shapeNodes = cmds.listRelatives(spineBlendNodes[0], s=True)
                cmds.delete(shapeNodes)
                shapeNodes = cmds.listRelatives(spineParentSocketNodes[0], s=True)
                cmds.delete(shapeNodes)
                spineBlendNodeFull = cmds.ls(spineBlendNodes[0], l=True)[0]
                spineParentSocketNodeFull = cmds.ls(spineParentSocketNodes[0], l=True)[0]
                spineJntNodeFull = cmds.ls(spineJntNode, l=True)[0]
                spineBlendNode = cmds.parent(spineBlendNodeFull, spineOutputSpaceNode)[0]
                visualNodeTemplateDup = cmds.duplicate(visualNodeTemplate, st=True, n='spine_visual_node_0'+str(i))[0]
                cmds.parent(visualNodeTemplateDup, spineBlendNode, r=True)[0]
                cmds.parent(spineParentSocketNodeFull, spineBlendNode)[0]
                cmds.parent(spineJntNodeFull, spineBlendNode)[0]
            else:
                spineBlendNodes = cmds.spaceLocator(n='spine_blend_node_0'+str(i))
                spineParentSocketNodes = cmds.spaceLocator(n='spine_0'+str(i)+'_parent_socket')
                cmds.select(clear=True)
                spineJntNode = cmds.joint(n='spine_0'+str(i)+'_jnt')
                cmds.setAttr(spineJntNode+'.radius', 0.5)
                shapeNodes = cmds.listRelatives(spineBlendNodes[0], s=True)
                cmds.delete(shapeNodes)
                shapeNodes = cmds.listRelatives(spineParentSocketNodes[0], s=True)
                cmds.delete(shapeNodes)
                spineBlendNodeFull = cmds.ls(spineBlendNodes[0], l=True)[0]
                spineParentSocketNodeFull = cmds.ls(spineParentSocketNodes[0], l=True)[0]
                spineJntNodeFull = cmds.ls(spineJntNode, l=True)[0]
                childNode = cmds.parent(spineBlendNodeFull, spineBlendNode)[0]
                visualNodeTemplateDup = cmds.duplicate(visualNodeTemplate, st=True, n='spine_visual_node_0'+str(i))[0]
                cmds.parent(visualNodeTemplateDup, childNode, r=True)[0]
                cmds.parent(spineParentSocketNodeFull, childNode)[0]
                cmds.parent(spineJntNodeFull, childNode)[0]
                spineBlendNode = childNode
            spineOutputNodeList.append(spineBlendNode)
 
        for i in range(0, len(spineOutputNodeList)):
            transBlendOp = util.createOpNode(self.moduleNameSpace, 'blendColors', 'blend_trans_0'+str(i))
            cmds.setAttr(transBlendOp+'.blender', 0)
            rotBlendOp = util.createOpNode(self.moduleNameSpace, 'blendColors', 'blend_rot_0'+str(i))
            cmds.setAttr(rotBlendOp+'.blender', 0)
            cmds.connectAttr(spineIkNodeList[i]+'.translate', transBlendOp+'.color1')
            cmds.connectAttr(spineFkNodeList[i]+'.translate', transBlendOp+'.color2')
            cmds.connectAttr(spineIkNodeList[i]+'.rotate', rotBlendOp+'.color1')
            cmds.connectAttr(spineFkNodeList[i]+'.rotate', rotBlendOp+'.color2')
            cmds.connectAttr(transBlendOp+'.output', spineOutputNodeList[i]+'.translate')
            cmds.connectAttr(rotBlendOp+'.output', spineOutputNodeList[i]+'.rotate')
            
        cmds.delete(fkConTemplate)
        cmds.delete(visualNodeTemplate)
        
        # since the nodes on motion have been generated dynamic, the variable dictionary needs to updated
        self.updateVariables()

