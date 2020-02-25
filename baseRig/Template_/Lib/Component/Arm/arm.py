import maya.cmds as cmds
import Template.Lib.Util.util as util
import os
import Template.Tool.ComponentManager.globalPath as globalPath

class armComponent(object):
    def __init__(self, name):
        self.name = name
        self.fitNode = None
        self.component_str = self.name
        self.component_val = 'arm'
        self.fitComponent_str = 'fit'
        self.moduleComponent_str = 'module'
        self.componentType_str = ''
        self.pathInfo = globalPath.globalPath('Arm')
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
        sideVal = 0
        if self._side == 'L':
            sideVal = 1
            for key, value in self.fitNodeInfo.iteritems():
                transZ = cmds.getAttr(value+'.translateZ')
                transZ_neg = transZ * -1
                cmds.setAttr(value+'.translateZ', transZ_neg)
                
        cmds.setAttr(fitSpaceNodeStr+'.sideInfo', sideVal)
        
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
        self._parentSocketNodes, self._childPlugNodes, self._useConnectionConNodes = self.setConnectionInfo()
        
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
        initAllNodes = {}

        motionInputPlacementNodes = {}
        motionInputPlugNodes = {}

        motionFkPlacementNodes = {}
        motionFkSpaceNodes = {}
        motionFkJnts = {}

        motionIkPlacementNodes = {}
        motionIkSpaceNodes = {}
        motionIkJnts = {}
        motionIkHandles = {}
        motionIkHandleSolvers = {}
        motionIkSoftNodes = {}
        motionIkRefNodes = {}

        motionOutputPlacementNodes = {}
        motionOutputSpaceNodes = {}
        motionOutputBlendJnts = {}
        motionOutputSocketNodes = {}
        motionOutputNodes = {}

        controlPlacementNodes = {}
        controlFkPlacementNodes = {}
        controlIkPlacementNodes = {}
        controlFkConSpaceNodes = {}
        controlIkConSpaceNodes = {}        
        
        controlFkSpaceNodes = {}
        controlIkSpaceNodes = {}
        fkConNodes = {}
        ikConNodes = {}
        refNodes = {}
        fk2ikConNodes = {}
        fk2ikSpaceNodes = {}
        controlNodes = {}

        for key in self.outputs.iterkeys():
            if self.outputs[key]['parent'] == self.modulePathDic['top']:
                if key.rfind(self.modulePathDic['init'][1:]) != -1:
                    util.getChildrenNodes(key, 'init', initNodes, 1)
                    util.getChildrenNodes(key, '', initAllNodes, 1)

                elif key.rfind(self.modulePathDic['input'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionInputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'child_plug', motionInputPlugNodes, 1)

                elif key.rfind(self.modulePathDic['fk'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionFkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'space', motionFkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'jnt', motionFkJnts, 1, objectType='joint')

                elif key.rfind(self.modulePathDic['ik'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionIkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'space', motionIkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'jnt', motionIkJnts, 1, objectType='joint')
                    util.getChildrenNodes(key, 'handle', motionIkHandles, 1)
                    util.getChildrenNodes(key, 'handle', motionIkHandleSolvers, 1, objectType='ikHandle')
                    util.getChildrenNodes(key, 'soft', motionIkSoftNodes, 1)
                    util.getChildrenNodes(key, 'ref', motionIkRefNodes, 1)

                elif key.rfind(self.modulePathDic['output'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionOutputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'space', motionOutputSpaceNodes, 1)
                    util.getChildrenNodes(key, 'blend', motionOutputBlendJnts, 1, objectType='joint')
                    util.getChildrenNodes(key, 'parent_socket', motionOutputSocketNodes, 1)
                    util.getChildrenNodes(key, '', motionOutputNodes, 1)

                elif key.rfind(self.modulePathDic['control'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', controlPlacementNodes, 1)
                    util.getChildrenNodes(key, 'fk_Con_placement', controlFkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'ik_Con_placement', controlIkPlacementNodes, 1)
                    util.getChildrenNodes(key, 'fk_Con_space', controlFkConSpaceNodes, 1)
                    util.getChildrenNodes(key, 'ik_Con_space', controlIkConSpaceNodes, 1)
                    util.getChildrenNodes(key, 'fk_space', controlFkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'ik_space', controlIkSpaceNodes, 1)
                    util.getChildrenNodes(key, 'fk_Con', fkConNodes, 1)
                    util.getChildrenNodes(key, 'ik_Con', ikConNodes, 1)
                    util.getChildrenNodes(key, 'ref', refNodes, 1)
                    util.getChildrenNodes(key, 'fk2ik_Con', fk2ikConNodes, 1)
                    util.getChildrenNodes(key, 'fk2ik_space', fk2ikSpaceNodes, 1)
                    util.getChildrenNodes(key, '', controlNodes, 1)
                else:
                    continue

        self.filterGroupNodeDic['init'] = initNodes
        self.filterGroupNodeDic['initAll'] = initAllNodes

        self.filterGroupNodeDic['inputPlacement'] = motionInputPlacementNodes
        self.filterGroupNodeDic['inputChildPlug'] = motionInputPlugNodes

        self.filterGroupNodeDic['fkPlacement'] = motionFkPlacementNodes
        self.filterGroupNodeDic['fkSpace'] = motionFkSpaceNodes
        self.filterGroupNodeDic['fkJnt'] = motionFkJnts

        self.filterGroupNodeDic['ikPlacement'] = motionIkPlacementNodes
        self.filterGroupNodeDic['ikSpace'] = motionIkSpaceNodes
        self.filterGroupNodeDic['ikJnt'] = motionIkJnts
        self.filterGroupNodeDic['ikHandle'] = motionIkHandles
        self.filterGroupNodeDic['ikHandleSolvers'] = motionIkHandleSolvers
        self.filterGroupNodeDic['ikSoft'] = motionIkSoftNodes
        self.filterGroupNodeDic['ikRef'] = motionIkRefNodes
        
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
        self.filterGroupNodeDic['controlFkConSpace'] = controlFkConSpaceNodes
        self.filterGroupNodeDic['controlIkConSpace'] = controlIkConSpaceNodes
        self.filterGroupNodeDic['controlFkCon'] = fkConNodes
        self.filterGroupNodeDic['controlIkCon'] = ikConNodes
        self.filterGroupNodeDic['controlRef'] = refNodes
        self.filterGroupNodeDic['controlNodes'] = controlNodes
        self.filterGroupNodeDic['fk2ikCon'] = fk2ikConNodes
        self.filterGroupNodeDic['fk2ikSpace'] = fk2ikSpaceNodes
        return self.filterGroupNodeDic

    def setConnectionInfo(self):
        parentSocketNodes = {}
        childPlugNodes = {}
        useConnectionConNodes = {}
        if self.filterGroupNodeDic['outputParentSocket'] != None:
            for socketNode in self.filterGroupNodeDic['outputParentSocket'].keys():
                socketLocalNode = util.fullPathName2Local(socketNode)
                parentSocketNodes[socketLocalNode[1]] = socketNode
        if self.filterGroupNodeDic['inputChildPlug'] != None:
            for plugNode in self.filterGroupNodeDic['inputChildPlug'].keys():
                plugLocalNode = util.fullPathName2Local(plugNode)
                childPlugNodes[plugLocalNode[1]] = plugNode
        if self.filterGroupNodeDic['controlIkCon'] != None:
            for plugNode in self.filterGroupNodeDic['controlIkCon'].keys():
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
        placementNodesList = [self.filterGroupNodeDic['inputPlacement'], self.filterGroupNodeDic['fkPlacement'], self.filterGroupNodeDic['ikPlacement'], self.filterGroupNodeDic['outputPlacement'], self.filterGroupNodeDic['controlPlacement']]
        for initNode, parentNode in self.filterGroupNodeDic['init'].iteritems():
            initLocalNode = util.fullPathName2Local(initNode)
            if initLocalNode[1].rfind('clavicle') != -1:
                matchStr = 'clavicle'
                for i in range(0, len(placementNodesList)):
                    if i == 0:
                        for placementNode in placementNodesList[i]:
                            placementNodeLocal = util.fullPathName2Local(placementNode)
                            if placementNodeLocal[1].rfind(matchStr) != -1:
                                util.transformChannelBinding(initNode, placementNode)
                    else:
                        for placementNode in placementNodesList[i]:
                            util.transformChannelBinding(initNode, placementNode)
        
        clavicleInit = ''
        clavicleAlign = ''
        uparmInit = ''
        poleInit = ''
        
        for initNode, parentNode in self.filterGroupNodeDic['init'].iteritems():
            initLocalNode = util.fullPathName2Local(initNode)
            if initLocalNode[1].rfind('clavicle') != -1:
                clavicleInit = initNode
                initNodeNodeNew = initLocalNode[1].replace('init', 'align')
                clavicleAlign = initLocalNode[0]+initNodeNodeNew
                cmds.connectAttr(initNode+'.translate', clavicleAlign+'.translate', f=True)
            elif initLocalNode[1].rfind('uparm') != -1:
                uparmInit = initNode
            elif initLocalNode[1].rfind('pole') != -1:
                poleInit = initNode

        uparmBaseIkSpaceNode = ''
        shldrIkHandleSpaceNode = ''
        uparmAutoIkOffsetSpaceNode = ''
        for ikSpaceNode in self.filterGroupNodeDic['ikSpace']:
            ikSpaceNodeLocal = util.fullPathName2Local(ikSpaceNode)
            if ikSpaceNodeLocal[1].rfind('parent_space') != -1:
                uparmBaseIkSpaceNode = ikSpaceNode
            elif ikSpaceNodeLocal[1].rfind('shldr_ik') != -1:
                shldrIkHandleSpaceNode = ikSpaceNode
            elif ikSpaceNodeLocal[1].rfind('auto_ik_offset') != -1:
                uparmAutoIkOffsetSpaceNode = ikSpaceNode
        
        controlUparmFkSpaceNode = ''
        controlLoarmFkSpaceNode = ''
        for fkSpaceNode in self.filterGroupNodeDic['controlFkSpace']:
            fkSpaceNodeLocal = util.fullPathName2Local(fkSpaceNode)
            if fkSpaceNodeLocal[1].rfind('uparm') != -1:
                controlUparmFkSpaceNode = fkSpaceNode
            elif fkSpaceNodeLocal[1].rfind('loarm') != -1:
                controlLoarmFkSpaceNode = fkSpaceNode
        
        initUparmAlignNode = ''
        loarmInit = ''
        loarmUp = ''
        wristInit = ''
        poleInit = ''
        for initNode in self.filterGroupNodeDic['initAll']:
            initNodeLocal = util.fullPathName2Local(initNode)
            if initNodeLocal[1] == 'uparm_align':
                initUparmAlignNode = initNode
            elif initNodeLocal[1] == 'loarm_init':
                loarmInit = initNode
            elif initNodeLocal[1] == 'loarm_up':
                loarmUp = initNode
            elif initNodeLocal[1] == 'wrist_init':
                wristInit = initNode
            elif initNodeLocal[1] == 'pole_init':
                poleInit = initNode
        
        aimVector = [1, 0, 0]
        upVector = [0, 1, 0]
        if self._side == 'L':
            aimVector = [-1, 0, 0]
            upVector = [0, -1, 0]
            
        cmds.aimConstraint(loarmInit, clavicleAlign, aim = aimVector, u= upVector, wut='object', wuo=loarmUp)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'uparm_ik_init')
        cmds.connectAttr(clavicleInit+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(uparmInit+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], uparmBaseIkSpaceNode)
        util.decompChannelBinding(matrixOps[1], shldrIkHandleSpaceNode)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'uparm_align_init')
        cmds.connectAttr(clavicleInit+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(uparmInit+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        cmds.connectAttr(matrixOps[1]+'.outputTranslate', initUparmAlignNode+'.translate')

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'uparm_fk_init')
        cmds.connectAttr(clavicleInit+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(uparmInit+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], controlUparmFkSpaceNode)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'pole_ik_init')
        cmds.connectAttr(clavicleInit+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(poleInit+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        
        claviclePoleRefNode = ''
        for controlRefNode in self.filterGroupNodeDic['controlRef']:
            controlRefNodeLocal = util.fullPathName2Local(controlRefNode)
            if controlRefNodeLocal[1] == 'clavicle_pole_ik_Con_ref':
                claviclePoleRefNode = controlRefNode
                util.decompChannelBinding(matrixOps[1], claviclePoleRefNode, option=1)
                
        for placementNode in self.filterGroupNodeDic['inputPlacement']:
            placementNodeLocal = util.fullPathName2Local(placementNode)
            if placementNodeLocal[1].rfind('pole') != -1:
                util.transformChannelBinding(poleInit, placementNode)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'uparm_jnt')
        cmds.connectAttr(clavicleInit+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(uparmInit+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        
        jntGrpList = [self.filterGroupNodeDic['fkJnt'], self.filterGroupNodeDic['ikJnt'], self.filterGroupNodeDic['outputBlend']]
        for jntGrp in jntGrpList:
            for jnt in jntGrp:
                jntLocal = util.fullPathName2Local(jnt)
                if jntLocal[1].rfind('uparm') != -1 and jntLocal[1].rfind('basis') == -1:
                    if jntLocal[1].rfind('auto') != -1:
                        cmds.connectAttr(matrixOps[1]+'.outputTranslate', jnt+'.translate')
                    else:
                        cmds.connectAttr(matrixOps[1]+'.outputTranslate', jnt+'.translate')
                        cmds.connectAttr(matrixOps[1]+'.outputRotate', jnt+'.jointOrient')
        
        
        for placementNode in self.filterGroupNodeDic['inputPlacement']:
            placementNodeLocal = util.fullPathName2Local(placementNode)
            if placementNodeLocal[1].rfind('uparm') != -1:
                util.transformChannelBinding(uparmInit, placementNode)
         
        autoShldrSelectorOp = util.createOpNode(self.moduleNameSpace, 'choice', 'auto_shldr_selector_op')
        cmds.connectAttr(uparmInit+'.worldInverseMatrix', autoShldrSelectorOp+'.input[0]')
        cmds.connectAttr(initUparmAlignNode+'.worldInverseMatrix', autoShldrSelectorOp+'.input[1]')
        cmds.connectAttr(self.modulePathDic['ik']+'.useAutoShldr', autoShldrSelectorOp+'.selector')
        
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'uparm_auto_ik_offset_space')
        cmds.connectAttr(autoShldrSelectorOp+'.output', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(uparmInit+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], uparmAutoIkOffsetSpaceNode)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'loarm_fk_space')
        cmds.connectAttr(uparmInit+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(loarmInit+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], controlLoarmFkSpaceNode)

        jntGrpList = [self.filterGroupNodeDic['fkJnt'], self.filterGroupNodeDic['ikJnt'], self.filterGroupNodeDic['outputBlend']]
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'loarm_init')
        cmds.connectAttr(uparmInit+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(loarmInit+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        for jntGrp in jntGrpList:
            for jnt in jntGrp:
                jntLocal = util.fullPathName2Local(jnt)
                if jntLocal[1].rfind('loarm') != -1:
                    cmds.connectAttr(matrixOps[1]+'.outputTranslate', jnt+'.translate')
                    cmds.connectAttr(matrixOps[1]+'.outputRotate', jnt+'.jointOrient')
        
        uparmDistanceInitOp = util.createOpNode(self.moduleNameSpace, 'distanceBetween', 'uparm_distance_init_op')
        loarmDistanceInitOp = util.createOpNode(self.moduleNameSpace, 'distanceBetween', 'loarm_distance_init_op')
        armDistanceInitOp = util.createOpNode(self.moduleNameSpace, 'plusMinusAverage', 'arm_distance_init_op')
        cmds.setAttr(armDistanceInitOp+'.operation', 1)
        cmds.connectAttr(uparmInit+'.worldMatrix', uparmDistanceInitOp+'.inMatrix1', f=True)
        cmds.connectAttr(loarmInit+'.worldMatrix', uparmDistanceInitOp+'.inMatrix2', f=True)
        cmds.connectAttr(loarmInit+'.worldMatrix', loarmDistanceInitOp+'.inMatrix1', f=True)
        cmds.connectAttr(wristInit+'.worldMatrix', loarmDistanceInitOp+'.inMatrix2', f=True)
        cmds.connectAttr(uparmDistanceInitOp+'.distance', armDistanceInitOp+'.input1D[0]')
        cmds.connectAttr(loarmDistanceInitOp+'.distance', armDistanceInitOp+'.input1D[1]')

        softIkAssetPath = self.pathInfo.assetDirPath + 'softIkOpAsset' + '.' + self.file_extenstion_str
        softIkOpNode = ''
        softIkOpNodeNew = ''
        softIkOpNodeBasis = ''
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
            softIkOpNodeBasis = cmds.duplicate(softIkOpNodeNew, n= softIkOpNode + '_' + self.component_val + '_basis')[0]

        cmds.connectAttr(armDistanceInitOp+'.output1D', softIkOpNodeNew+'.In_initLength', f=True)
        cmds.connectAttr(armDistanceInitOp+'.output1D', softIkOpNodeBasis+'.In_initLength', f=True)
        
        wristIkConRefNode = ''
        for controlRefNode in self.filterGroupNodeDic['controlRef']:
            controlRefNodeLocal = util.fullPathName2Local(controlRefNode)
            if controlRefNodeLocal[1].rfind('wrist_ik') != -1:
                wristIkConRefNode = controlRefNode
        
        wristIkConNode = ''
        for controlNode in self.filterGroupNodeDic['controlIkCon']:
            controlNodeLocal = util.fullPathName2Local(controlNode)
            if controlNodeLocal[1].rfind('wrist_ik') != -1 and controlNodeLocal[1].rfind('ref') == -1:
                wristIkConNode = controlNode
        
        uparmAutoBlendRefNode = ''
        for ikRefNode in self.filterGroupNodeDic['ikRef']:
            ikRefNodeLocal = util.fullPathName2Local(ikRefNode)
            if ikRefNodeLocal[1].rfind('auto_blend') != -1:
                uparmAutoBlendRefNode = ikRefNode
        
        uparmBasisIkspaceNode = ''
        for ikSpaceNode in self.filterGroupNodeDic['ikSpace']:
            ikSpaceNodeLocal = util.fullPathName2Local(ikSpaceNode)
            if ikSpaceNodeLocal[1].rfind('uparm_basis') != -1:
                uparmBasisIkspaceNode = ikSpaceNode
        
        cmds.connectAttr(wristIkConNode+'.softIK', softIkOpNodeNew+'.In_softWeight', f=True)
        cmds.connectAttr(wristIkConNode+'.softIK', softIkOpNodeBasis+'.In_softWeight', f=True)

        armDistanceMotionOp = util.createOpNode(self.moduleNameSpace, 'distanceBetween', 'arm_distance_motion_op')
        armDistanceBasisOp = util.createOpNode(self.moduleNameSpace, 'distanceBetween', 'arm_distance_basis_op')
        cmds.connectAttr(wristIkConRefNode+'.worldMatrix', armDistanceMotionOp+'.inMatrix1')
        cmds.connectAttr(wristIkConRefNode+'.worldMatrix', armDistanceBasisOp+'.inMatrix1')
        cmds.connectAttr(uparmAutoBlendRefNode+'.worldMatrix', armDistanceMotionOp+'.inMatrix2')
        cmds.connectAttr(uparmBasisIkspaceNode+'.worldMatrix', armDistanceBasisOp+'.inMatrix2')
        
        cmds.connectAttr(armDistanceMotionOp+'.distance', softIkOpNodeNew+'.In_motionLength', f=True)
        cmds.connectAttr(armDistanceBasisOp+'.distance', softIkOpNodeBasis+'.In_motionLength', f=True)

        uparmIkSoftnode = ''
        uparmBasisIkSoftnode = ''
        for softIkNode in self.filterGroupNodeDic['ikSoft']:
            softIkNodeLocal = util.fullPathName2Local(softIkNode)
            if softIkNodeLocal[1].rfind('uparm_ik') != -1 and softIkNodeLocal[1].rfind('space') == -1:
                uparmIkSoftnode = softIkNode
            elif softIkNodeLocal[1].rfind('uparm_basis_ik') != -1 and softIkNodeLocal[1].rfind('space') == -1:
                uparmBasisIkSoftnode = softIkNode
        
        cmds.connectAttr(softIkOpNodeNew+'.Out_softDistance', uparmIkSoftnode+'.translateX')
        
        if self._side == 'L':
            flipOp = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', 'softIKFlip')
            cmds.setAttr(flipOp+'.operation', 1)
            cmds.setAttr(flipOp+'.input2X', -1)
            cmds.connectAttr(softIkOpNodeBasis+'.Out_softDistance', flipOp+'.input1X')
            cmds.connectAttr(flipOp+'.outputX', uparmBasisIkSoftnode+'.translateX')
        else:
            cmds.connectAttr(softIkOpNodeBasis+'.Out_softDistance', uparmBasisIkSoftnode+'.translateX')
        
        for inputPlacementNode in self.filterGroupNodeDic['inputPlacement']:
            inputPlacementNodeLocal = util.fullPathName2Local(inputPlacementNode)
            if inputPlacementNodeLocal[1].rfind('wrist') != -1:
                util.transformChannelBinding(wristInit, inputPlacementNode)
        
        jntGrpList = [self.filterGroupNodeDic['fkJnt'], self.filterGroupNodeDic['ikJnt'], self.filterGroupNodeDic['outputBlend']]
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'wrist_init')
        cmds.connectAttr(loarmInit+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(wristInit+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        for jntGrp in jntGrpList:
            for jnt in jntGrp:
                jntLocal = util.fullPathName2Local(jnt)
                if jntLocal[1].rfind('wrist') != -1:
                    cmds.connectAttr(matrixOps[1]+'.outputTranslate', jnt+'.translate')
                    cmds.connectAttr(matrixOps[1]+'.outputRotate', jnt+'.jointOrient')
                    
        for controlFkSpace in self.filterGroupNodeDic['controlFkSpace']:
            controlFkSpaceLocal = util.fullPathName2Local(controlFkSpace)
            if controlFkSpaceLocal[1].rfind('wrist') != -1:
                util.decompChannelBinding(matrixOps[1], controlFkSpace)
        
        for outputSpaceNode in self.filterGroupNodeDic['outputSpace']:
            outputSpaceNodeLocal = util.fullPathName2Local(outputSpaceNode)
            if outputSpaceNodeLocal[1].rfind('wrist_orbit') != -1:
                cmds.connectAttr(matrixOps[1]+'.outputTranslate', outputSpaceNode+'.translate', f=True)
    
    def applyMotionNodeConnections(self):
        
        wristChildPlugNode = ''
        clavicleChildPlugNode = ''
        uparmChildPlugNode = ''
        poleChildPlugNode = ''
        
        for inputChildPlugNode in self.filterGroupNodeDic['inputChildPlug']:
            inputChildPlugNodeLocal = util.fullPathName2Local(inputChildPlugNode)
            if inputChildPlugNodeLocal[1].rfind('wrist') != -1:
                wristChildPlugNode = inputChildPlugNode
            elif inputChildPlugNodeLocal[1].rfind('clavicle') != -1:
                clavicleChildPlugNode = inputChildPlugNode
            elif inputChildPlugNodeLocal[1].rfind('uparm') != -1:
                uparmChildPlugNode = inputChildPlugNode
            elif inputChildPlugNodeLocal[1].rfind('pole') != -1:
                poleChildPlugNode = inputChildPlugNode


        controlarmIkPoleSpaceNode = ''
        for ikSpaceNode in self.filterGroupNodeDic['controlIkSpace']:
            ikSpaceNodeLocal = util.fullPathName2Local(ikSpaceNode)
            if ikSpaceNodeLocal[1].rfind('pole') != -1:
                controlarmIkPoleSpaceNode = ikSpaceNode
                
        ikConPlacementNode = ''
        for placementNode in self.filterGroupNodeDic['controlIkPlacement']:
            placementNodeLocal = util.fullPathName2Local(placementNode)
            if placementNodeLocal[1].rfind('ik_Con') != -1:
                ikConPlacementNode = placementNode

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'arm_pole_ik_space')
        cmds.connectAttr(ikConPlacementNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(poleChildPlugNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], controlarmIkPoleSpaceNode)
        

        spaceGroupList = [self.filterGroupNodeDic['fkSpace'], self.filterGroupNodeDic['ikSpace'], self.filterGroupNodeDic['outputSpace']]
        for spaceGroup in spaceGroupList:
            for spaceNode in spaceGroup:
                spaceNodeLocal = util.fullPathName2Local(spaceNode)
                if spaceNodeLocal[1].rfind('arm') == 0 and spaceNodeLocal[1].rfind('handle') == -1:
                    util.transformChannelBinding(clavicleChildPlugNode, spaceNode)
        
        util.transformChannelBinding(clavicleChildPlugNode, self.filterGroupNodeDic['controlFkConSpace'].keys()[0])
        util.transformChannelBinding(clavicleChildPlugNode, self.filterGroupNodeDic['controlIkConSpace'].keys()[0])
        
        wristChildPlugDecompOp = util.createOpNode(self.moduleNameSpace, 'decomposeMatrix', 'wrist_child_plug_decomp_op')
        cmds.connectAttr(wristChildPlugNode+'.worldMatrix', wristChildPlugDecompOp+'.inputMatrix', f=True)
        wristChildPlugComposeOp = util.createOpNode(self.moduleNameSpace, 'composeMatrix', 'wrist_child_plug_compose_op')
        cmds.connectAttr(wristChildPlugDecompOp+'.outputTranslate', wristChildPlugComposeOp+'.inputTranslate', f=True)
        
        for controlIkSpace in self.filterGroupNodeDic['controlIkSpace']:
            controlIkSpaceLocal = util.fullPathName2Local(controlIkSpace)
            if controlIkSpaceLocal[1].rfind('wrist') != -1:
                matrixOps = util.localMatrixOp(self.moduleNameSpace, 'wrist_child_plug')
                cmds.connectAttr(self.filterGroupNodeDic['controlIkConSpace'].keys()[0]+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
                cmds.connectAttr(wristChildPlugComposeOp+'.outputMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
                util.decompChannelBinding(matrixOps[1], controlIkSpace)
        
        armBasisIkHandleSpaceNode = ''
        armIkHandleSpaceNode = ''
        armBasisIkSpaceNode = ''
        armIkSpaceNode = ''
        for motionIkSpacenode in self.filterGroupNodeDic['ikSpace']:
            motionIkSpacenodeLocal = util.fullPathName2Local(motionIkSpacenode)
            if motionIkSpacenodeLocal[1].rfind('arm') == 0 and motionIkSpacenodeLocal[1].rfind('handle') != -1:
                if motionIkSpacenodeLocal[1].rfind('basis') != -1:
                    armBasisIkHandleSpaceNode = motionIkSpacenode
                else:
                    armIkHandleSpaceNode = motionIkSpacenode
            elif motionIkSpacenodeLocal[1].rfind('arm_basis') != -1 and motionIkSpacenodeLocal[1].rfind('handle') == -1:
                armBasisIkSpaceNode = motionIkSpacenode
            elif motionIkSpacenodeLocal[1].rfind('arm') == 0 and motionIkSpacenodeLocal[1].rfind('handle') == -1:
                if motionIkSpacenodeLocal[1].rfind('basis') == -1 and motionIkSpacenodeLocal[1].rfind('refer') == -1:
                    armIkSpaceNode = motionIkSpacenode
        
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'arm_ik_handle_space')
        cmds.connectAttr(armIkSpaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(wristChildPlugNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], armIkHandleSpaceNode)
        
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'arm_basis_ik_handle_space')
        cmds.connectAttr(armBasisIkSpaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(wristChildPlugNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], armBasisIkHandleSpaceNode)

        for motionIkSpacenode in self.filterGroupNodeDic['ikSpace']:
            motionIkSpacenodeLocal = util.fullPathName2Local(motionIkSpacenode)
            if motionIkSpacenodeLocal[1].rfind('uparm_basis') != -1 and motionIkSpacenodeLocal[1].rfind('soft') == -1:
                util.transformChannelBinding(uparmChildPlugNode, motionIkSpacenode)

        for fkConNode in self.filterGroupNodeDic['controlFkCon']:
            fkConNodeLocal = util.fullPathName2Local(fkConNode)
            if fkConNodeLocal[1].rfind('placement') == -1 and fkConNodeLocal[1].rfind('space') == -1:
                matchStr = fkConNodeLocal[1].replace('_fk_Con', '')
                for fkJnt in self.filterGroupNodeDic['fkJnt']:
                    fkJntLocal = util.fullPathName2Local(fkJnt)
                    if fkJntLocal[1].rfind(matchStr) != -1:
                        cmds.connectAttr(fkConNode+'.rotate', fkJnt+'.rotate', f=True)
        
        loarmBasisIkjntRef = ''
        uparmBasisIkjntRef = ''
        for motionIkRefNode in self.filterGroupNodeDic['ikRef']:
            motionIkRefNodeLocal = util.fullPathName2Local(motionIkRefNode)
            if motionIkRefNodeLocal[1].rfind('loarm_basis_ik') != -1:
                loarmBasisIkjntRef = motionIkRefNode
            elif motionIkRefNodeLocal[1].rfind('uparm_basis_ik') != -1:
                uparmBasisIkjntRef = motionIkRefNode
        
        elbowTargetSpaceNode = ''
        elbowTargetNode = ''
        shldrAutoIkHandleSpaceNode = ''
        for motionIkSpacenode in self.filterGroupNodeDic['ikSpace']:
            motionIkSpacenodeLocal = util.fullPathName2Local(motionIkSpacenode)
            if motionIkSpacenodeLocal[1].rfind('elbow_target') != -1:
                elbowTargetSpaceNode = motionIkSpacenode
                elbowTargetNode = elbowTargetSpaceNode + '|' + self.moduleNameSpace[1:] + ':elbow_target'
            elif motionIkSpacenodeLocal[1].rfind('shldr_auto_ik_handle') != -1:
                shldrAutoIkHandleSpaceNode = motionIkSpacenode

        elbowTargetSelectOp = util.createOpNode(self.moduleNameSpace, 'choice', 'elbow_target_select_op')
        cmds.connectAttr(self.modulePathDic['ik']+'.useAutoShldr', elbowTargetSelectOp+'.selector')
        cmds.connectAttr(uparmBasisIkjntRef+'.worldMatrix', elbowTargetSelectOp+'.input[0]')
        cmds.connectAttr(loarmBasisIkjntRef+'.worldMatrix', elbowTargetSelectOp+'.input[1]')
        
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'elbow_target')
        cmds.connectAttr(elbowTargetSpaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(elbowTargetSelectOp+'.output', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], elbowTargetNode)
        util.transformChannelBinding(elbowTargetNode, shldrAutoIkHandleSpaceNode)
        
        uparmBasisIkSpace = ''
        armReferSpace = ''
        for motionIkSpacenode in self.filterGroupNodeDic['ikSpace']:
            motionIkSpacenodeLocal = util.fullPathName2Local(motionIkSpacenode)
            if motionIkSpacenodeLocal[1].rfind('uparm_basis') != -1 and motionIkSpacenodeLocal[1].rfind('soft') == -1:
                uparmBasisIkSpace = motionIkSpacenode
            elif motionIkSpacenodeLocal[1].rfind('arm_refer') != -1:
                armReferSpace = motionIkSpacenode

        uparmAutoIkOffsetSpaceNode = ''
        for ikSpaceNode in self.filterGroupNodeDic['ikSpace']:
            ikSpaceNodeLocal = util.fullPathName2Local(ikSpaceNode)
            if ikSpaceNodeLocal[1].rfind('auto_ik_offset') != -1:
                uparmAutoIkOffsetSpaceNode = ikSpaceNode

        wristIkConNode = ''
        for controlNode in self.filterGroupNodeDic['controlIkCon']:
            controlNodeLocal = util.fullPathName2Local(controlNode)
            if controlNodeLocal[1].rfind('wrist_ik') != -1 and controlNodeLocal[1].rfind('ref') == -1:
                wristIkConNode = controlNode
                
        uparmNonAutoRef = ''
        uparmAutoRef = ''
        uparmBlendRef = ''
        for motionIkRefNode in self.filterGroupNodeDic['ikRef']:
            motionIkRefNodeLocal = util.fullPathName2Local(motionIkRefNode)
            if motionIkRefNodeLocal[1].rfind('uparm_non_auto') != -1:
                uparmNonAutoRef = motionIkRefNode
            elif motionIkRefNodeLocal[1].rfind('uparm_auto_ref') != -1:
                uparmAutoRef = motionIkRefNode
            elif motionIkRefNodeLocal[1].rfind('uparm_auto_blend') != -1:
                uparmBlendRef = motionIkRefNode

        uparmIkSoftSpacenode = ''
        uparmIkSoftnode = ''
        for softIkNode in self.filterGroupNodeDic['ikSoft']:
            softIkNodeLocal = util.fullPathName2Local(softIkNode)
            if softIkNodeLocal[1].rfind('uparm_ik') != -1 and softIkNodeLocal[1].rfind('space') != -1:
                uparmIkSoftSpacenode = softIkNode
            elif softIkNodeLocal[1].rfind('uparm_ik') != -1 and softIkNodeLocal[1].rfind('space') == -1:
                uparmIkSoftnode = softIkNode
        
        wristIkConRefNode = ''
        armPoleIkConRefNode = ''
        shldrIkConRefNode = ''
        for controlRefNode in self.filterGroupNodeDic['controlRef']:
            controlRefNodeLocal = util.fullPathName2Local(controlRefNode)
            if controlRefNodeLocal[1].rfind('wrist_ik') != -1:
                wristIkConRefNode = controlRefNode
            elif controlRefNodeLocal[1].rfind('arm_pole_ik') != -1:
                armPoleIkConRefNode = controlRefNode
            elif controlRefNodeLocal[1].rfind('shldr_ik') != -1:
                shldrIkConRefNode = controlRefNode
        
        if self._side == 'L':
            cmds.setAttr(shldrIkConRefNode+'.rotateX', -180)
            cmds.setAttr(shldrIkConRefNode+'.rotateY', -90)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'uparm_non_auto_ref')
        cmds.connectAttr(armReferSpace+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(uparmBasisIkSpace+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], uparmNonAutoRef)

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'uparm_auto_ref')
        cmds.connectAttr(armReferSpace+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(uparmAutoIkOffsetSpaceNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], uparmAutoRef)
        
        uparmAutoBlendTrans = util.createOpNode(self.moduleNameSpace, 'blendColors', 'uparm_auto_blend_trans')
        uparmAutoBlendRot = util.createOpNode(self.moduleNameSpace, 'blendColors', 'uparm_auto_blend_rot')
        
        cmds.connectAttr(uparmNonAutoRef+'.translate', uparmAutoBlendTrans+'.color2', f=True)
        cmds.connectAttr(uparmAutoRef+'.translate', uparmAutoBlendTrans+'.color1', f=True)
        cmds.connectAttr(wristIkConNode+'.autoShldr', uparmAutoBlendTrans+'.blender', f=True)

        cmds.connectAttr(uparmNonAutoRef+'.rotate', uparmAutoBlendRot+'.color2', f=True)
        cmds.connectAttr(uparmAutoRef+'.rotate', uparmAutoBlendRot+'.color1', f=True)
        cmds.connectAttr(wristIkConNode+'.autoShldr', uparmAutoBlendRot+'.blender', f=True)
        
        cmds.connectAttr(uparmAutoBlendTrans+'.output', uparmBlendRef+'.translate', f=True)
        cmds.connectAttr(uparmAutoBlendRot+'.output', uparmBlendRef+'.rotate', f=True)
        
        cmds.connectAttr(uparmBlendRef+'.translate', uparmIkSoftSpacenode+'.translate', f=True)
        cmds.aimConstraint(wristIkConRefNode, uparmIkSoftSpacenode, aim = [1,0,0], u= [0,0,1], wut='object', wuo=armPoleIkConRefNode)

        ikConSpaceNode = self.filterGroupNodeDic['controlIkConSpace'].keys()[0]
        uparmAutoBlendDecompOp = util.createOpNode(self.moduleNameSpace, 'decomposeMatrix', 'uparm_auto_blend_decomp_op')
        cmds.connectAttr(uparmBlendRef+'.worldMatrix', uparmAutoBlendDecompOp+'.inputMatrix', f=True)
        uparmAutoBlendCompOp = util.createOpNode(self.moduleNameSpace, 'composeMatrix', 'uparm_auto_blend_comp_op')
        cmds.connectAttr(uparmAutoBlendDecompOp+'.outputTranslate', uparmAutoBlendCompOp+'.inputTranslate', f=True)

        shldrIkSpaceNode = ''
        for controlIkSpaceNode in self.filterGroupNodeDic['controlIkSpace']:
            controlIkSpaceNodeLocal = util.fullPathName2Local(controlIkSpaceNode)
            if controlIkSpaceNodeLocal[1].rfind('shldr') != -1:
                shldrIkSpaceNode = controlIkSpaceNode
                
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'shldr_ik_space')
        cmds.connectAttr(ikConSpaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(uparmAutoBlendCompOp+'.outputMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], shldrIkSpaceNode)

        armIkHandleNode = ''
        shldrIkHandleNode = ''
        for ikHandleSolverNode in self.filterGroupNodeDic['ikHandleSolvers'] :
            ikHandleSolverNodeLocal = util.fullPathName2Local(ikHandleSolverNode)
            if ikHandleSolverNodeLocal[1] == 'arm_ik_handle':
                armIkHandleNode = ikHandleSolverNode
            elif ikHandleSolverNodeLocal[1] == 'shldr_ik_handle':
                shldrIkHandleNode = ikHandleSolverNode
        
        armIkHandleSpaceNode = ''
        shldrIkHandleSpaceNode = ''
        for ikHandleSpaceNode in self.filterGroupNodeDic['ikSpace']:
            ikHandleSpaceNodeLocal = util.fullPathName2Local(ikHandleSpaceNode)
            if ikHandleSpaceNodeLocal[1].rfind('arm_ik_handle') != -1:
                armIkHandleSpaceNode = ikHandleSpaceNode
            elif ikHandleSpaceNodeLocal[1].rfind('shldr_ik_handle') != -1:
                shldrIkHandleSpaceNode = ikHandleSpaceNode

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'arm_ik_handle')
        cmds.connectAttr(armIkHandleSpaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(uparmIkSoftnode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], armIkHandleNode)

        # bug: ik not working the same way as aim constrint. unexpected flipping
        #matrixOps = util.localMatrixOp(self.moduleNameSpace, 'shldr_ik_handle')
        #cmds.connectAttr(shldrIkHandleSpaceNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        #cmds.connectAttr(shldrIkConRefNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        #util.decompChannelBinding(matrixOps[1], shldrIkHandleNode)
        
        ikClavicleJntNode = ''
        for ikJnt in self.filterGroupNodeDic['ikJnt']:
            ikJntLocal = util.fullPathName2Local(ikJnt)
            if ikJntLocal[1].rfind('clavicle') != -1 and ikJntLocal[1].rfind('auto') == -1:
                ikClavicleJntNode = ikJnt

        sourceNode = ''
        for motionIkSpacenode in self.filterGroupNodeDic['ikSpace']:
            motionIkSpacenodeLocal = util.fullPathName2Local(motionIkSpacenode)
            if motionIkSpacenodeLocal[1] == 'uparm_basis_ik_soft_space':
                sourceNode = motionIkSpacenode
                
        targetNode = ''
        targetUpNode = ''
        targetClavicleUpNode = ''
        targetShldrNode = ''
        for controlRefNode in self.filterGroupNodeDic['controlRef']:
            controlRefNodeLocal = util.fullPathName2Local(controlRefNode)
            if controlRefNodeLocal[1] == 'wrist_ik_Con_ref':
                targetNode = controlRefNode
            elif controlRefNodeLocal[1] == 'arm_pole_ik_Con_ref':
                targetUpNode = controlRefNode
            elif controlRefNodeLocal[1] == 'shldr_ik_Con_ref':
                targetShldrNode = controlRefNode
            elif controlRefNodeLocal[1] == 'clavicle_pole_ik_Con_ref':
                targetClavicleUpNode = controlRefNode
                
        aimVec = [1,0,0]
        upVec = [0,0,1]
        
        if self._side == 'L':
            aimVec = [-1,0,0]
            upVec = [0,0,-1]
            
        cmds.aimConstraint(targetNode, sourceNode, aim = aimVec, u= upVec, wut='object', wuo=targetUpNode)
        cmds.aimConstraint(targetShldrNode, ikClavicleJntNode, aim = aimVec, u= upVec, wut='object', wuo= targetClavicleUpNode)
        
        uparmBasisIkSoft = ''
        armBasisIkHandleSpace = ''
        armBasisIkHandle = ''
        for ikSoftnode in self.filterGroupNodeDic['ikSoft']:
            ikSoftnodeLocal = util.fullPathName2Local(ikSoftnode)
            if ikSoftnodeLocal[1] == 'uparm_basis_ik_soft':
                uparmBasisIkSoft = ikSoftnode
        
        for ikSpaceNode in self.filterGroupNodeDic['ikSpace']:
            ikSpaceNodeLocal = util.fullPathName2Local(ikSpaceNode)
            if ikSpaceNodeLocal[1] == 'arm_basis_ik_handle_space':
                armBasisIkHandleSpace = ikSpaceNode
        
        for ikHandleSolverNode in self.filterGroupNodeDic['ikHandleSolvers']:
            ikHandleSolverNodeLocal = util.fullPathName2Local(ikHandleSolverNode)
            if ikHandleSolverNodeLocal[1] == 'arm_basis_ik_handle':
                armBasisIkHandle = ikHandleSolverNode

        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'arm_basis_ik_handle')
        cmds.connectAttr(armBasisIkHandleSpace+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(uparmBasisIkSoft+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        cmds.connectAttr(matrixOps[1]+'.outputTranslate', armBasisIkHandle+'.translate')
        
        targetControlNode = ''
        targetControlUpNode = ''
        wristOrbitAimSpaceNode = ''
        wristOrbitCon = ''
        wristOrbitConSpace = ''
        wristIkCon = ''
        wristIkPivCon = ''
        
        for controlNode in self.filterGroupNodeDic['controlNodes']:
            controlNodeLocal = util.fullPathName2Local(controlNode)
            if controlNodeLocal[1] == 'wrist_orbit_aim':
                targetControlNode = controlNode
            elif controlNodeLocal[1] == 'wrist_orbit_aim_vector':
                targetControlUpNode = controlNode
            elif controlNodeLocal[1] == 'wrist_orbit_Con':
                wristOrbitCon = controlNode
            elif controlNodeLocal[1] == 'wrist_orbit_space':
                wristOrbitConSpace = controlNode
            elif controlNodeLocal[1] == 'wrist_ik_Con':
                wristIkCon = controlNode
            elif controlNodeLocal[1] == 'wrist_ik_piv_Con':
                wristIkPivCon = controlNode
            elif controlNodeLocal[1] == 'wrist_orbit_aim_space':
                wristOrbitAimSpaceNode = controlNode
        
        wristOrbitSpaceNode = ''
        motionControlNode = self.modulePathDic['control']
        
        for outputSpaceNode in self.filterGroupNodeDic['outputSpace']:
            outputSpaceNodeLocal = util.fullPathName2Local(outputSpaceNode)
            if outputSpaceNodeLocal[1].rfind('wrist_orbit_ref') != -1:
                wristOrbitSpaceNode = outputSpaceNode
                cmds.aimConstraint(targetControlNode, outputSpaceNode, aim = [1,0,0], u= [0,1,0], wut='object', wuo=targetControlUpNode)
        
        for outputNode in self.filterGroupNodeDic['outputNode']:
            outputNodeLocal = util.fullPathName2Local(outputNode)
            if outputNodeLocal[1] == 'wrist_orbit_ref':
                cmds.connectAttr(wristOrbitCon+'.rotate', outputNode+'.rotate', f=True)
        
        armFk2IkSpaceNode = self.filterGroupNodeDic['fk2ikSpace'].keys()[0]
        
        matrixOps = util.localMatrixOp(self.moduleNameSpace, 'arm_fk2ik_space')
        cmds.connectAttr(motionControlNode+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
        cmds.connectAttr(wristOrbitSpaceNode+'.worldMatrix', matrixOps[0]+'.matrixIn[0]', f=True)
        util.decompChannelBinding(matrixOps[1], armFk2IkSpaceNode)
        util.decompChannelBinding(matrixOps[1], wristOrbitConSpace)
        
        armFk2IkConNode = self.filterGroupNodeDic['fk2ikCon'].keys()[0]
        cmds.connectAttr(wristOrbitCon+'.rotate', armFk2IkConNode+'.rotate', f=True)
        
        if self._side == 'L':
            armFk2IkConShapeNode = cmds.listRelatives(armFk2IkConNode, shapes=True, f=True)[0]
            spanNums = cmds.getAttr(armFk2IkConShapeNode+'.spans')
            spanNums = spanNums + 1
            for i in range(0, spanNums):
                originalPos = cmds.getAttr(armFk2IkConShapeNode+".controlPoints["+ str(i)+"].yValue")
                cmds.setAttr(armFk2IkConShapeNode+".controlPoints["+ str(i)+"].yValue", originalPos * -1)

        cmds.connectAttr(wristIkPivCon+'.translate', wristIkCon+'.rotatePivot', f=True)

        blendWristJntNode = ''
        ikWristJntNode = ''
        ikWristJntNodeLocal = ''
        fkWristJntNode = ''
        fkWristJntNodeLocal = ''
        
        for blendJnt in self.filterGroupNodeDic['outputBlend']:
            blendJntLocal = util.fullPathName2Local(blendJnt)
            if blendJntLocal[1].rfind('wrist') != -1:
                blendWristJntNode = blendJnt
        for ikJnt in self.filterGroupNodeDic['ikJnt']:
            ikJntLocal = util.fullPathName2Local(ikJnt)
            if ikJntLocal[1].rfind('wrist') != -1:
                ikWristJntNode = ikJnt
                ikWristJntNodeLocal = ikJntLocal[1]
        for fkJnt in self.filterGroupNodeDic['fkJnt']:
            fkJntLocal = util.fullPathName2Local(fkJnt)
            if fkJntLocal[1].rfind('wrist') != -1:
                fkWristJntNode = fkJnt
                fkWristJntNodeLocal = fkJntLocal[1]
        
        wristOrbitAimSpaceOriOp = cmds.orientConstraint(fkWristJntNode, ikWristJntNode, wristOrbitAimSpaceNode)
        wristOrbitAimSpacePosOp = cmds.pointConstraint(blendWristJntNode, wristOrbitAimSpaceNode)
        
        wristOrbitAimWeightReverseOp = util.createOpNode(self.moduleNameSpace, 'remapValue', 'wrist_orbit_aim_weight_reverse_op')
        cmds.setAttr(wristOrbitAimWeightReverseOp+'.inputMin', 0)
        cmds.setAttr(wristOrbitAimWeightReverseOp+'.inputMax', 1)
        cmds.setAttr(wristOrbitAimWeightReverseOp+'.outputMin', 1)
        cmds.setAttr(wristOrbitAimWeightReverseOp+'.outputMax', 0)
        cmds.connectAttr(armFk2IkConNode+'.fk2ik', wristOrbitAimWeightReverseOp+'.inputValue', f=True)
        cmds.connectAttr(wristOrbitAimWeightReverseOp+'.outValue', wristOrbitAimSpaceOriOp[0]+'.'+fkWristJntNodeLocal+'W0', f=True)
        cmds.connectAttr(armFk2IkConNode+'.fk2ik', wristOrbitAimSpaceOriOp[0]+'.'+ikWristJntNodeLocal+'W1', f=True)
        
        blendJntList = self.filterGroupNodeDic['outputBlend'].keys()
        blendOpList = []
        for i in range(0, len(blendJntList)):
            blendJntLocal = util.fullPathName2Local(blendJntList[i])
            blendJntOp = util.createOpNode(self.moduleNameSpace, 'blendColors', blendJntLocal[1]+'_op')
            blendOpList.append(blendJntOp)
            cmds.connectAttr(blendOpList[i]+'.output', blendJntList[i]+'.rotate' )
            if i == 0:
                cmds.connectAttr(armFk2IkConNode+'.fk2ik', blendOpList[i]+'.blender', f=True)
            else:
                cmds.connectAttr(blendOpList[i-1]+'.blender', blendOpList[i]+'.blender', f=True)
            
            filterStr = blendJntLocal[1].split('_')[0]
            
            for ikJntNode in self.filterGroupNodeDic['ikJnt']:
                ikJntNodeLocal = util.fullPathName2Local(ikJntNode)
                if ikJntNodeLocal[1].rfind(filterStr) != -1 and ikJntNodeLocal[1].rfind('basis') == -1 and ikJntNodeLocal[1].rfind('auto') == -1:
                    cmds.connectAttr(ikJntNode+'.rotate', blendOpList[i]+'.color1', f=True)
                    
            for fkJntNode in self.filterGroupNodeDic['fkJnt']:
                fkJntNodeLocal = util.fullPathName2Local(fkJntNode)
                if fkJntNodeLocal[1].rfind(filterStr) != -1:
                    cmds.connectAttr(fkJntNode+'.rotate', blendOpList[i]+'.color2', f=True)