import maya.cmds as cmds
import Template.Lib.Util.util as util
import os
import Template.Tool.ComponentManager.globalPath as globalPath

class handComponent(object):
    def __init__(self, name):
        self.name = name
        self.fitNode = None
        self.component_str = self.name
        self.component_val = 'hand'
        self.fitComponent_str = 'fit'
        self.moduleComponent_str = 'module'
        self.componentType_str = ''
        self.pathInfo = globalPath.globalPath('Hand')
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
        self._parentSocketNodes, self._childPlugNodes, self._useConnectionConNodes = self.setConnectionInfo()

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
        motionInputPlacementNodes = {}
        motionOutputPlacementNodes = {}
        motionOutputSocketNodes = {}
        motionInputPlugNodes = {}
        motionOutputPlugNodes = {}
        motionOutputNodes = {}
        controlPlacementNodes = {}
        
        controlPlugNodes = {}
        fkConNodes = {}
        
        for key in self.outputs.iterkeys():
            if self.outputs[key]['parent'] == self.modulePathDic['top']:
                if key.rfind(self.modulePathDic['init'][1:]) != -1:
                    util.getChildrenNodes(key, 'init', initNodes, 1)
                elif key.rfind(self.modulePathDic['input'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionInputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'child_plug', motionInputPlugNodes, 1)
                elif key.rfind(self.modulePathDic['output'][1:]) != -1:
                    util.getChildrenNodes(key, 'placement', motionOutputPlacementNodes, 1)
                    util.getChildrenNodes(key, 'parent_socket', motionOutputSocketNodes, 1)
                    util.getChildrenNodes(key, 'child_plug', motionOutputPlugNodes, 1)
                    util.getChildrenNodes(key, 'node', motionOutputNodes, 1)
                elif key.rfind(self.modulePathDic['control'][1:]) != -1:     
                    util.getChildrenNodes(key, 'placement', controlPlacementNodes, 1)
                    util.getChildrenNodes(key, 'child_plug', controlPlugNodes, 1)
                    util.getChildrenNodes(key, 'fk_Con', fkConNodes, 1)
                else:
                    continue

        self.filterGroupNodeDic['init'] = initNodes
        self.filterGroupNodeDic['inputPlacement'] = motionInputPlacementNodes
        self.filterGroupNodeDic['inputChildPlug'] = motionInputPlugNodes
        
        self.filterGroupNodeDic['outputPlacement'] = motionOutputPlacementNodes
        self.filterGroupNodeDic['outputParentSocket'] = motionOutputSocketNodes
        self.filterGroupNodeDic['outputChildPlug'] = motionOutputPlugNodes
        self.filterGroupNodeDic['outputNode'] = motionOutputNodes

        self.filterGroupNodeDic['controlPlacement'] = controlPlacementNodes
        self.filterGroupNodeDic['controlChildPlug'] = controlPlugNodes
        self.filterGroupNodeDic['controlFkCon'] = fkConNodes
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
            sourceLocal = util.fullPathName2Local(sourceNode)
            matchNodes = {}
            util.getChildrenNodes(self.modulePathDic['init'], sourceLocal[1], matchNodes, 1)
            sourceNode = matchNodes.keys()[0]
            util.transformChannelBinding(sourceNode, key)
            
        for key in self.filterGroupNodeDic['controlPlacement'].keys():
            sourceNode = key.replace("motion_control","init").replace("control_placement", "init")
            sourceLocal = util.fullPathName2Local(sourceNode)
            matchNodes = {}
            util.getChildrenNodes(self.modulePathDic['init'], sourceLocal[1], matchNodes, 1)
            sourceNode = matchNodes.keys()[0]
            util.transformChannelBinding(sourceNode, key)
    
    def applyMotionNodeConnections(self):
        for key in self.filterGroupNodeDic['outputChildPlug'].keys():
            sourceNode = key.replace("motion_output","motion_input").replace("output", "input")
            util.transformChannelBinding(sourceNode, key)
        
        for key in self.filterGroupNodeDic['controlChildPlug'].keys():
            sourceNode = key.replace("motion_control","motion_input").replace("control", "input")
            util.transformChannelBinding(sourceNode, key)
        
        for key in self.filterGroupNodeDic['controlFkCon'].keys():
            keyLocal = util.fullPathName2Local(key)
            if keyLocal[1].rfind('space') == -1:
                outputNodes = {}
                nodeStrLocal = keyLocal[1].replace("fk_Con", "node")
                util.getChildrenNodes(self.modulePathDic['output'], nodeStrLocal, outputNodes, 1)
                for node in outputNodes:
                    if node.split('|')[-1].rfind('space') != -1 or node.split('|')[-1].rfind('socket') != -1:
                        continue
                    else:
                        if keyLocal[1].rfind('hand_roll') != -1:
                            util.transformChannelBinding(key, node, 3)
                        else:
                            util.transformChannelBinding(key, node)
        
        
        hand_piv_con_op = util.createOpNode(self.moduleNameSpace, 'plusMinusAverage', 'hand_piv_con_add_op')
                
        for key in self.filterGroupNodeDic['controlPlacement']:
            keyLocal = util.fullPathName2Local(key)
            if keyLocal[1].rfind('piv') != -1:
                cmds.connectAttr(key+'.translate', hand_piv_con_op+'.input3D[0]', f=True)
        for key in self.filterGroupNodeDic['controlFkCon']:
            keyLocal = util.fullPathName2Local(key)
            if keyLocal[1].rfind('piv') != -1 and keyLocal[1].rfind('space') == -1:
                cmds.connectAttr(key+'.translate', hand_piv_con_op+'.input3D[1]', f=True)
        rollFkConNode = ''
        for key in self.filterGroupNodeDic['controlFkCon']:
            keyLocal = util.fullPathName2Local(key)
            if keyLocal[1].rfind('roll') != -1 and keyLocal[1].rfind('space') == -1:
                rollFkConNode = key
                cmds.connectAttr(hand_piv_con_op+'.output3D', key+'.rotatePivot', f=True)
        
        hand_piv_node_op = util.createOpNode(self.moduleNameSpace, 'plusMinusAverage', 'hand_piv_node_add_op')
                
        for key in self.filterGroupNodeDic['outputPlacement']:
            keyLocal = util.fullPathName2Local(key)
            if keyLocal[1].rfind('piv') != -1:
                cmds.connectAttr(key+'.translate', hand_piv_node_op+'.input3D[0]', f=True)
        for key in self.filterGroupNodeDic['outputNode']:
            keyLocal = util.fullPathName2Local(key)
            if keyLocal[1].rfind('piv') != -1:
                cmds.connectAttr(key+'.translate', hand_piv_node_op+'.input3D[1]', f=True)
        for key in self.filterGroupNodeDic['outputNode']:
            keyLocal = util.fullPathName2Local(key)
            if keyLocal[1].rfind('roll') != -1 and keyLocal[1].rfind('space') == -1 and keyLocal[1].rfind('socket') == -1:
                cmds.connectAttr(hand_piv_node_op+'.output3D', key+'.rotatePivot', f=True)
            elif keyLocal[1].rfind('roll') != -1 and keyLocal[1].rfind('space') != -1:
                cmds.connectAttr(rollFkConNode+'.translate', key+'.translate', f=True)