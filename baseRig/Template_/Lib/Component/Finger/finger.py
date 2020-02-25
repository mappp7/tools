import maya.cmds as cmds
import Template.Lib.Util.util as util
import os
import Template.Tool.ComponentManager.globalPath as globalPath

class fingerComponent(object):
    def __init__(self, name):
        self.name = name
        self.fitNode = None
        self.component_str = self.name
        self.component_val = 'finger'
        self.fitComponent_str = 'fit'
        self.moduleComponent_str = 'module'
        self.componentType_str = ''
        self.pathInfo = globalPath.globalPath('Finger')
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
        self.snapOps = []
        self.setCurrentNamespace(self.currentNamespace)

        self._side = 'R'
        #self._part = 'index'
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
        self._params = [
            {
                'name' : 'live Connection',
                'type' : 'checkBox',
                'default' : False,
                'value': False,
                'callback': 'test'
            },
            {
                'name' : 'Is Thumb',
                'type' : 'checkBox',
                'default' : False,
                'value': False,
                'callback': 'test'
            },
            {
                'name' : 'Meta Curl Weight',
                'type' : 'lineEdit',
                'default' : 0.2,
                'value': 0.2,
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

    #@property
    #def part(self):
        #return self._part

    #@side.setter
    #def part(self, value):
        #self._part = value

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value

    def prepNamespace(self):
        self.componentType_str = self.setComponentType('fit')
        #self.fitNamespace = util.prepNamespace(self._side, self.component_str, self.fitComponent_str, part_str=self._part)
        self.fitNamespace = util.prepNamespace(self._side, self.component_str, self.fitComponent_str)
        self.moduleNameSpace = self.fitNamespace.replace(self.fitComponent_str, self.moduleComponent_str)

    def reloadFit(self):
        util.fileLoad(self.componentType_str, self.templateDir, self.component_val, self.fitNamespace, self.file_extenstion_str)
        self.fitNodeInfo = self.getFitNodeInfo(self.fitNamespace, self.component_val)
        self.setCurrentNamespace(self.fitNamespace)

    def reloadModule(self):
        self.componentType_str = self.setComponentType(self.moduleComponent_str)
        if self._params[1]['value']:
            self.componentType_str = 'template_thumb'
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
        #self.modulePathDic['top'] = ':' + self._side + ':' + self.component_str + ':' + self._part + ':' + self.moduleComponent_str + ':' + self.component_val + '_system'
        #self.modulePathDic['init'] = ':' + self._side + ':' + self.component_str + ':' + self._part + ':'+ self.moduleComponent_str + ':init'
        #self.modulePathDic['control'] = ':' + self._side + ':' + self.component_str + ':' + self._part + ':'+ self.moduleComponent_str + ':motion_control'
        #self.modulePathDic['input'] = ':' + self._side + ':' + self.component_str + ':' + self._part + ':'+ self.moduleComponent_str + ':motion_input'
        #self.modulePathDic['output'] = ':' + self._side + ':' + self.component_str + ':' + self._part + ':'+ self.moduleComponent_str + ':motion_output'
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
        motionInputPlacementNodes = {}
        motionOutputPlacementNodes = {}
        motionOutputSocketNodes = {}
        motionOutputPlugNodes = {}
        motionOutputNodes = {}
        controlPlacementNodes = {}
        
        controlPlugNodes = {}
        fkConSpaceNodes = {}
        addFkSpaceNodes = {}
        
        for key in self.outputs.iterkeys():
            if self.outputs[key]['parent'] == self.modulePathDic['top']:
                if key.rfind(self.modulePathDic['init'][1:]) != -1:
                    util.getChildrenNodes(key, 'init', initNodes, 1)
                elif key.rfind(self.modulePathDic['input'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionInputPlacementNodes, 1)
                elif key.rfind(self.modulePathDic['output'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionOutputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'parent_socket', motionOutputSocketNodes, 1)
                    util.getChildrenNodes(key, 'child_plug', motionOutputPlugNodes, 1)
                    util.getChildrenNodes(key, 'node', motionOutputNodes, 1)
                elif key.rfind(self.modulePathDic['control'][1:]) != -1:     
                    util.getChildrenNodes(key, 'placement', controlPlacementNodes, 1)
                    util.getChildrenNodes(key, 'child_plug', controlPlugNodes, 1)
                    util.getChildrenNodes(key, 'fk_Con_space', fkConSpaceNodes, 1)
                    util.getChildrenNodes(key, 'add_fk_Con_space', addFkSpaceNodes, 1)
                else:
                    continue

        self.filterGroupNodeDic['init'] = initNodes
        self.filterGroupNodeDic['inputPlacement'] = motionInputPlacementNodes
        
        self.filterGroupNodeDic['outputPlacement'] = motionOutputPlacementNodes
        self.filterGroupNodeDic['outputParentSocket'] = motionOutputSocketNodes
        self.filterGroupNodeDic['outputChildPlug'] = motionOutputPlugNodes
        self.filterGroupNodeDic['outputNode'] = motionOutputNodes

        self.filterGroupNodeDic['controlPlacement'] = controlPlacementNodes
        self.filterGroupNodeDic['controlChildPlug'] = controlPlugNodes
        self.filterGroupNodeDic['controlFkConSpace'] = fkConSpaceNodes
        self.filterGroupNodeDic['controlAddFkConSpace'] = addFkSpaceNodes
        return self.filterGroupNodeDic

    def setConnectionInfo(self):
        parentSocketNodes = {}
        childPlugNodes = {}
        if self.filterGroupNodeDic['outputParentSocket'] != None:
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
        initNodeFullName = cmds.ls(self.modulePathDic['init'], l=True)[0]
        for match in self.fitNodeInfo.iterkeys():
            for node, parentInfo in self.filterGroupNodeDic['init'].iteritems():
                nodeLocal = util.fullPathName2Local(node)
                if nodeLocal[1] == match + '_init':
                    parentInit = parentInfo['parent']
                    matrixOps = util.localMatrixOp(self.moduleNameSpace, match + '_init')
                    snapOps += matrixOps
                    cmds.connectAttr(parentInit+'.worldInverseMatrix', matrixOps[0]+'.matrixIn[1]', f=True)
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
        
        for key in self.filterGroupNodeDic['inputPlacement'].keys():
            sourceNode = key.replace("motion_input","init").replace("input_placement", "init")
            util.transformChannelBinding(sourceNode, key)
        
        for key in self.filterGroupNodeDic['outputPlacement'].keys():
            sourceNode = key.replace("motion_output","init").replace("output_placement", "init")
            util.transformChannelBinding(sourceNode, key)
        
        for key in self.filterGroupNodeDic['controlPlacement'].keys():
            sourceNode = key.replace("motion_control","init").replace("control_placement", "init")
            util.transformChannelBinding(sourceNode, key)
    
    def applyMotionNodeConnections(self):

        for key in self.filterGroupNodeDic['outputChildPlug'].keys():
            sourceNode = key.replace("motion_output","motion_input").replace("output", "input")
            util.transformChannelBinding(sourceNode, key)
        
        for key in self.filterGroupNodeDic['controlChildPlug'].keys():
            sourceNode = key.replace("motion_control","motion_input").replace("control", "input")
            util.transformChannelBinding(sourceNode, key)

        addFkConNode = cmds.listRelatives(self.filterGroupNodeDic['controlAddFkConSpace'].keys()[0], c=1, s=0, f=1, typ='transform')[0]

        for key in self.filterGroupNodeDic['controlFkConSpace'].keys():
            localKey = util.fullPathName2Local(key)
            baseName = localKey[1]
            part = baseName.split('_')[0]
            for initNode in self.filterGroupNodeDic['init']:
                localName = util.fullPathName2Local(initNode)
                if localName[1].rfind(part) != -1:
                    addOpNode = util.createOpNode(self.moduleNameSpace, 'plusMinusAverage', 'add_fk_op_'+part)
                    if part != 'meta':
                        cmds.connectAttr(initNode+'.rotate', addOpNode+'.input3D[0]', f=True)
                    cmds.connectAttr(addFkConNode+'.curl', addOpNode+'.input3D[1]', f=True)
                    
                    if part == "meta":
                        multOpNode = util.createOpNode(self.moduleNameSpace, 'multiplyDivide', 'add_fk_mult_op_'+part)
                        cmds.setAttr(multOpNode+'.operation', 1)
                        cmds.setAttr(multOpNode+'.input2X', self._params[2]['value'])
                        cmds.setAttr(multOpNode+'.input2Y', self._params[2]['value'])
                        cmds.setAttr(multOpNode+'.input2Z', self._params[2]['value'])
                        cmds.connectAttr(addOpNode+'.output3D', multOpNode+'.input1', f=True)
                        cmds.connectAttr(multOpNode+'.output', key+'.rotate', f=True)
                    else:
                        util.transformChannelBinding(initNode, key, 2)
                        util.transformChannelBinding(initNode, key, 4) 
                        cmds.connectAttr(addOpNode+'.output3D', key+'.rotate', f=True)
        
        fkConNodes = []
        for key in self.filterGroupNodeDic['controlFkConSpace'].keys():
            child = cmds.listRelatives(key, c=1, s=0, f=1, typ='transform')[0]
            fkConNodes.append(child)
        
        for fkConNode in fkConNodes:
            localKey = util.fullPathName2Local(fkConNode)
            baseName = localKey[1]
            if baseName == 'fk_Con':
                for node in self.filterGroupNodeDic['outputNode']:
                    localNode = util.fullPathName2Local(node)
                    baseName2 = localNode[1]
                    part = baseName2.split('_')[0]
                    part2 = baseName2.split('_')[-1]
                    if part == 'meta' and part2 != 'space': 
                        util.transformChannelBinding(fkConNode, node)
            else:
                for node in self.filterGroupNodeDic['outputNode']:
                    localNode = util.fullPathName2Local(node)
                    baseName2 = localNode[1]
                    part = baseName2.split('_')[0]
                    localFkCon = util.fullPathName2Local(fkConNode)
                    if part in localFkCon[1]:
                        if baseName2.rfind('space') != -1:
                            continue
                        matrixOp = util.localMatrixOp(self.moduleNameSpace, part)
                        spaceNode = self.filterGroupNodeDic['outputNode'][node]['parent']
                        cmds.connectAttr(fkConNode+'.worldMatrix', matrixOp[0]+'.matrixIn[0]', f=True)
                        cmds.connectAttr(spaceNode+'.worldInverseMatrix', matrixOp[0]+'.matrixIn[1]', f=True)
                        cmds.connectAttr(matrixOp[1]+'.outputTranslate', node+'.translate', f=True)
                        cmds.connectAttr(matrixOp[1]+'.outputRotate', node+'.rotate', f=True)
                        cmds.connectAttr(matrixOp[1]+'.outputScale', node+'.scale', f=True)
                        cmds.connectAttr(matrixOp[1]+'.outputShear', node+'.shear', f=True)