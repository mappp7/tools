
import os
import json
import maya.api.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
from Qt import QtGui, QtCore, QtWidgets, load_ui

from Qt.QtGui import *
from Qt.QtCore import *
from Qt.QtWidgets import *
from functools import partial

basePath = os.path.abspath(__file__ + '/../')

import numpy as np
from scipy.optimize import lsq_linear
from scipy.cluster.vq import vq, kmeans, whiten

import time
import math
#import module.samplingSim as sS ; reload(sS)

uiFile = os.path.join(basePath, 'DTSCtool.ui')

class MtscTool(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MtscTool, self).__init__(parent)
        
        self.ui = load_ui(uiFile)
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # value
        self.status=0
        self.mode = 0
        self.min_ = int(cmds.playbackOptions(q=1 , min=1))
        self.max_ = int(cmds.playbackOptions(q=1 , max=1))
        self.ui.simulationRange_min_LED.setText(str(self.min_))
        self.ui.simulationRange_max_LED.setText(str(self.max_))
        
        self.skincluster = None
        self.numBones = 5
        self.boneList = list()
        self.mesh = None
        self.rest_pose = None
        self.poses = None
        self.W = None
        self.bone_transforms = None

        self.setWindowTitle('MTSC_tool')
        self.createConnections()

    def createConnections(self):
        self.ui.mode_CBX.currentIndexChanged.connect(self.modeSelection)
        self.ui.boneList_BTN.clicked.connect(self.InsertBoneList)       
        self.ui.mesh_BTN.clicked.connect(self.InsertMesh)
        self.ui.pose_BTN.clicked.connect(self.InsertPose)
        #self.ui.maxInfluence_SPB
        #self.ui.initIteration_SPB
        
        #self.connect(self.ui.poses_LWG, SIGNAL('itemClicked(QListWidgetItem)') , self.clickPoses)
        self.ui.posesInsert_BTN.clicked.connect(self.addPoses)
        #self.connect(self.ui.posesInsert_BTN, SIGNAL('clicked()') , partial(self.addPoses , self.ui.poses_LWG))
        
        self.ui.posesClear_BTN.clicked.connect(self.clearPoses)
        #self.connect(self.ui.posesClear_BTN, SIGNAL('clicked()') , partial(self.clearPoses , self.ui.poses_LWG))
        self.ui.both_BTN.clicked.connect(self.updateBothFunc)
        
        #MTSC(poses, rest_pose, num_bones, sparseness=4, max_iterations=5 , iterations = 3 , mayaMesh = None , jointList = None)

    def isclose(self,x, y, rtol=1.e-5, atol=1.e-8):
        return abs(x-y) <= atol + rtol * abs(y)

    def euler_angles_from_rotation_matrix(self,R):
        '''
        From a paper by Gregory G. Slabaugh (undated),
        "Computing Euler angles from a rotation matrix
        '''
        phi = 0.0
        if self.isclose(R[2,0],-1.0):
            theta = math.pi/2.0
            psi = math.atan2(R[0,1],R[0,2])
        elif self.isclose(R[2,0],1.0):
            theta = -math.pi/2.0
            psi = math.atan2(-R[0,1],-R[0,2])
        else:
            theta = -math.asin(R[2,0])
            cos_theta = math.cos(theta)
            psi = math.atan2(R[2,1]/cos_theta, R[2,2]/cos_theta)
            phi = math.atan2(R[1,0]/cos_theta, R[0,0]/cos_theta)
        return psi*57.2958, theta*57.2958, phi*57.2958


    def manual_codebook(self ,mayaMesh ,jointList):
        sel = om.MSelectionList()
        sel.add(mayaMesh)
        dPath = sel.getDagPath(0)
        mMesh = om.MFnMesh(dPath)
        num = mMesh.numVertices
        #fine skinCluster
        skincluster = mel.eval('findRelatedSkinCluster("%s")'%mayaMesh)
        # array codeBook
        arrayL = []
        correct_JList = []

        for i in range(num) :
            spct = cmds.skinPercent(skincluster , mayaMesh + '.vtx[' + str(i) + ']' , q=1 , value =1 )
            # please do not paint skinweight
            for x in range(len(spct)):
                if spct[x] >= 0.6:
                    arrayL.append(x)

        codeBook = np.array(arrayL)
        #correct joint Index

        for y in range(len(jointList)):
            b = cmds.connectionInfo(skincluster+'.matrix[' + str(y) + ']' , sfd = 1)
            j = b.split('.')[0]
            correct_JList.append(j)
        print codeBook , correct_JList
        return codeBook , correct_JList

    def kabsch(self,P, Q):
    
        if (P.size == 0 or Q.size == 0):
            raise ValueError("Empty matrices sent to kabsch")
        centroid_P = np.mean(P, axis=0) # mean(axis=0) is rows average return array[0.2 , 0.5, 0.4]
        centroid_Q = np.mean(Q, axis=0)
        P_centered = P - centroid_P                       # Center both matrices on centroid
        Q_centered = Q - centroid_Q
        H = P_centered.T.dot(Q_centered)                  # covariance matrix
        U, S, V = np.linalg.svd(H)                        # SVD
        R = U.dot(V).T                                    # calculate optimal rotation
        if np.linalg.det(R) < 0:                          # correct rotation matrix for
            V[2,:] *= -1                                  #  right-hand coordinate system
            R = U.dot(V).T

        t = centroid_Q - R.dot(centroid_P)                # translation vector

        return np.vstack((R, t))


    def initialize(self , poses, rest_pose, num_bones, iterations, mayaMesh=None, jointList=None):
        bones=[]
        num_verts = rest_pose.shape[0] # shape mean array scale
        num_poses = poses.shape[0]

        bone_transforms = np.empty((num_bones, num_poses, 4, 3))   # [(R, T) for for each pose] for each bone
                                                            # 3rd dim has 3 rows for R and 1 row for T

        # Use k-means to assign bones to vertices
        whitened = whiten(rest_pose)
        codebook, _ = kmeans(whitened, num_bones)
        rest_pose_corrected = np.empty((num_bones, num_verts, 3))  # Rest pose - mean of vertices attached to each bone

        # confirm mode
        if mayaMesh:
            #rigid Skin
            vert_assignments , bones = self.manual_codebook(mayaMesh , jointList)
            boneArray = []
            for i in bones :
                boneArray.append(cmds.xform(i , q=1 , t=1 ,ws=1))

            rest_bones_t = np.array(boneArray)
            #rest_bones_t = np.empty((num_bones , 3))

            for bone in range(num_bones):
                #rest_bones_t[bone] = np.mean(rest_pose[vert_assignments == bone] , axis = 0)
                rest_bones_t[bone] = np.array(boneArray[bone])
                rest_pose_corrected[bone] = rest_pose - rest_bones_t[bone]

                for pose in range(num_poses):

                    bone_transforms[bone, pose] = self.kabsch(rest_pose_corrected[bone, vert_assignments == bone], poses[pose, vert_assignments == bone])

        else:
            # Compute initial random bone transformations

            vert_assignments, _ = vq(whitened, codebook) # Bone assignment for each vertex (|num_verts| x 1)
            rest_bones_t = np.empty((num_bones , 3))                    # Translations for bones at rest pose

            for bone in range(num_bones):
                rest_bones_t[bone] = np.mean(rest_pose[vert_assignments == bone] , axis = 0)
                rest_pose_corrected[bone] = rest_pose - rest_bones_t[bone]

                for pose in range(num_poses):

                    bone_transforms[bone, pose] = self.kabsch(rest_pose_corrected[bone, vert_assignments == bone], poses[pose, vert_assignments == bone])

        for it in range(iterations):
            
            # Re-assign bones to vertices using smallest reconstruction error from all poses
            constructed = np.empty((num_bones, num_poses, num_verts, 3)) # |num_bones| x |num_poses| x |num_verts| x 3
            for bone in range(num_bones):
                Rp = bone_transforms[bone,:,:3,:].dot((rest_pose - rest_bones_t[bone]).T).transpose((0, 2, 1)) # |num_poses| x |num_verts| x 3
                # R * p + T
                constructed[bone] = Rp + bone_transforms[bone, :, np.newaxis, 3, :]
            errs = np.linalg.norm(constructed - poses, axis=(1, 3))
            vert_assignments = np.argmin(errs, axis=0)
            

            # For each bone, for each pose, compute new transform using kabsch
            for bone in range(num_bones):
                if mayaMesh:
                    #rest_bones_t[bone] = np.mean(rest_pose[vert_assignments == bone] , axis= 0)
                    rest_bones_t[bone] = np.array(boneArray[bone])
                else:
                    rest_bones_t[bone] = np.mean(rest_pose[vert_assignments == bone] , axis= 0)

                rest_pose_corrected[bone] = rest_pose - rest_bones_t[bone]

                for pose in range(num_poses):
                    P = rest_pose_corrected[bone, vert_assignments == bone]
                    Q = poses[pose, vert_assignments == bone]
                    print P,Q
                    if (P.size == 0 or Q.size == 0):
                        print 'Skip Iteration'
                    else:

                        bone_transforms[bone, pose] = self.kabsch(P, Q)

        # jointList is correct Index Joint

        return bone_transforms, rest_bones_t , bones
    
    def update_weight_map(self,bone_transforms, rest_bones_t, poses, rest_pose, sparseness):
    
        num_verts = rest_pose.shape[0]
        num_poses = poses.shape[0]
        num_bones = bone_transforms.shape[0]

        W = np.empty((num_verts, num_bones))
        
        for v in range(num_verts):
            # For every vertex, solve a least squares problem
            Rp = np.empty((num_bones, num_poses, 3))
            for bone in range(num_bones):
                Rp[bone] = bone_transforms[bone,:,:3,:].dot(rest_pose[v] - rest_bones_t[bone]) # |num_bones| x |num_poses| x 3
            # R * p + T
            Rp_T = Rp + bone_transforms[:, :, 3, :] # |num_bones| x |num_poses| x 3
            A = Rp_T.transpose((1, 2, 0)).reshape((3 * num_poses, num_bones)) # 3 * |num_poses| x |num_bones|
            b = poses[:, v, :].reshape(3 * num_poses) # 3 * |num_poses| x 1

            # Bounds ensure non-negativity constraint and kind of affinity constraint
            w = lsq_linear(A, b, bounds=(0, 1), method='bvls').x  # |num_bones| x 1
            w /= np.sum(w) # Ensure that w sums to 1 (affinity constraint)

            # Remove |B| - |K| bone weights with the least "effect"
            effect = np.linalg.norm((A * w).reshape(num_poses, 3, num_bones), axis=1) # |num_poses| x |num_bones|
            effect = np.sum(effect, axis=0) # |num_bones| x 1
            num_discarded = max(num_bones - sparseness, 0)
            effective = np.argpartition(effect, num_discarded)[num_discarded:] # |sparseness| x 1

            # Run least squares again, but only use the most effective bones
            A_reduced = A[:, effective] # 3 * |num_poses| x |sparseness|
            w_reduced = lsq_linear(A_reduced, b, bounds=(0, 1), method='bvls').x # |sparseness| x 1
            w_reduced /= np.sum(w_reduced) # Ensure that w sums to 1 (affinity constraint)

            w_sparse = np.zeros(num_bones)
            w_sparse[effective] = w_reduced
            w_sparse /= np.sum(w_sparse) # Ensure that w_sparse sums to 1 (affinity constraint)

            W[v] = w_sparse

        return W

    def update_bone_transforms(self,W, bone_transforms, rest_bones_t, poses, rest_pose):
    
        num_bones = W.shape[1]
        num_poses = poses.shape[0]
        num_verts = W.shape[0]

        for pose in range(num_poses):
            for bone in range(num_bones):
                # Represents the points in rest pose without this rest bone's translation
                p_corrected = rest_pose - rest_bones_t[bone] # |num_verts| x 3

                # Calculate q_i for all vertices by equation (6)
                constructed = np.empty((num_bones, num_verts, 3)) # |num_bones| x |num_verts| x 3
                for bone2 in range(num_bones):
                    # can't use p_corrected before because we want to correct for every bone2 distinctly
                    Rp = bone_transforms[bone2,pose,:3,:].dot((rest_pose - rest_bones_t[bone2]).T).T # |num_verts| x 3
                    # R * p + T
                    constructed[bone2] = Rp + bone_transforms[bone2, pose, 3, :]
                # w * (R * p + T)
                constructed = constructed.transpose((1, 0, 2)) * W[:, :, np.newaxis] # |num_verts| x |num_bones| x 3
                constructed = np.delete(constructed, bone, axis=1) # |num_verts| x |num_bones-1| x 3
                q = poses[pose] - np.sum(constructed, axis=1) # |num_verts| x 3

                # Calculate p_star, q_star, p_bar, and q_bar for all verts by equation (8)
                p_star = np.sum(np.square(W[:, bone, np.newaxis]) * p_corrected, axis=0) # |num_verts| x 3 => 3 x 1
                p_star /= np.sum(np.square(W[:, bone])) # 3 x 1

                q_star = np.sum(W[:, bone, np.newaxis] * q, axis=0) # |num_verts| x 3 => 3 x 1
                q_star /= np.sum(np.square(W[:, bone])) # 3 x 1
                p_bar = p_corrected - p_star # |num_verts| x 3
                q_bar = q - W[:, bone, np.newaxis] * q_star # |num_verts| x 3

                # Perform SVD by equation (9)
                P = (p_bar * W[:, bone, np.newaxis]).T # 3 x |num_verts|
                Q = q_bar.T # 3 x |num_verts|

                U, S, V = np.linalg.svd(np.matmul(P, Q.T))

                # Calculate rotation R and translation t by equation (10)
                R = U.dot(V).T # 3 x 3

                t = q_star - R.dot(p_star) # 3 x 1

                bone_transforms[bone, pose, :3, :] = R
                bone_transforms[bone, pose, 3, :] = t


        return bone_transforms

    def MTSC(self , poses, rest_pose, num_bones, iterations = 5 , max_iterations = 5 ,sparseness=4 ,mayaMesh = None , jointList = None):
        start_time = time.time()
        if not mayaMesh and jointList:
            bone_transforms, rest_bones_t ,finalBone = self.initialize(poses, rest_pose, num_bones , iterations , mayaMesh , jointList)
        else:
            bone_transforms, rest_bones_t ,finalBone = self.initialize(poses, rest_pose, num_bones , iterations)

        for _ in range(max_iterations):
            self.W = self.update_weight_map(bone_transforms, rest_bones_t, poses, rest_pose, sparseness)
            bone_transforms = self.update_bone_transforms(self.W, bone_transforms, rest_bones_t, poses, rest_pose)
            #print("Reconstruction error:", self.reconstruction_err(poses, rest_pose, bone_transforms, rest_bones_t, self.W))

        end_time = time.time()
        
        # final bone is correct index joint
        return self.W, bone_transforms, rest_bones_t ,finalBone

    def reconstruction_err(self,poses, rest_pose, bone_transforms, rest_bones_t, W):

        num_bones = bone_transforms.shape[0]
        num_verts = W.shape[0]
        num_poses = poses.shape[0]
        # Points in rest pose without rest bone translations
        p_corrected = rest_pose[np.newaxis, :, :] - rest_bones_t[:, np.newaxis, :] # |num_bones| x |num_verts| x 3
        constructions = np.empty((num_bones, num_poses, num_verts, 3)) # |num_bones| x |num_poses| x |num_verts| x 3
        for bone in range(num_bones):
            # When you are a vectorizing GOD
            constructions[bone] = np.einsum('ijk,lk->ilj', bone_transforms[bone, :, :3, :], p_corrected[bone]) # |num_poses| x |num_verts| x 3
        constructions += bone_transforms[:, :, np.newaxis, 3, :] # |num_bones| x |num_poses| x |num_verts| x 3
        constructions *= (W.T)[:, np.newaxis, :, np.newaxis] # |num_bones| x |num_poses| x |num_verts| x 3
        errors = poses - np.sum(constructions, axis=0) # |num_poses| x |num_verts| x 3
        return np.mean(np.linalg.norm(errors, axis=2))   
    
    def modeSelection(self):
        modeIndex = self.ui.mode_CBX.currentIndex()
        self.mode = modeIndex
        if modeIndex == 0 : 
            #vq mode
            #enable
            self.ui.boneNum_SPB.setEnabled(1)
            #disable
            self.ui.boneList_LED.setEnabled(0)
            self.ui.boneList_BTN.setEnabled(0)
            
                       
        else:
            #vw mode
            #enable
            self.ui.boneList_LED.setEnabled(1)
            self.ui.boneList_BTN.setEnabled(1)
            
            #disable
            self.ui.boneNum_SPB.setEnabled(0)

    def InsertBoneList(self):
        sel = cmds.ls(sl=1)
        if sel:            
            self.ui.boneList_LED.setText(str(sel))
            self.boneList = sel
        else:
            print 'please select Joints'
            self.ui.boneList_LED.clear()
            self.boneList = None

        return self.boneList
        

    def InsertMesh(self):
        sel = cmds.ls(sl=1)
        if len(sel) == 1 :
            sel = sel[0]
            self.ui.mesh_LED.setText(sel)
            self.mesh = sel
            selectionLs = om.MGlobal.getActiveSelectionList()
            self.rest_pose = np.array(om.MFnMesh(selectionLs.getDagPath(0)).getPoints(om.MSpace.kWorld))[:, :3]
            
            
            #find skinCluster
            skincluster = mel.eval('findRelatedSkinCluster("%s")'%self.mesh)
            if skincluster:
                self.skincluster = skincluster
            
        else:
            print 'please select one head rest pose mesh' 
            self.ui.mesh_LED.clear()
            self.mesh = None

        print self.rest_pose ,self.mesh , self.skincluster
        return self.rest_pose ,self.mesh , self.skincluster
        
    
    def InsertPose(self):
        sel = cmds.ls(sl=1)
        if len(sel) == 1 :
            sel = sel[0]
            self.ui.pose_LED.setText(sel)
        else:
            print 'please select one pose Mesh(simulation)'
            self.ui.pose_LED.clear()
        
    def addPoses(self):
        items = list()
        for i in xrange(self.ui.poses_LWG.count()):
            items.append(self.ui.poses_LWG.item(i))

        if self.ui.pose_LED and self.ui.simulationRange_min_LED and self.ui.simulationRange_max_LED: 
            #simulation sampling pose 
            
            self.status = 0
            self.min_ = int(self.ui.simulationRange_min_LED.text())
            self.max_ = int(self.ui.simulationRange_max_LED.text())
            pose = self.ui.pose_LED.text()
            
            simPoses = list()
            for i in range(self.min_ , self.max_+1):
                cmds.currentTime(i)
                cmds.select(pose)
                sel = om.MGlobal.getActiveSelectionList()
                simPoses.append(om.MFnMesh(sel.getDagPath(0)).getPoints(om.MSpace.kWorld))
            self.poses = np.array(simPoses)[:,:,:3]
            print self.poses
            source = '{pose} : {min} ~ {max}'.format(pose = pose , min = self.min_ , max = self.max_)
            
            if not source in items : 
                self.ui.poses_LWG.addItems([source])

        else:
            self.status = 1
            posesMesh = list()
            if items:
                posesMesh += items
            posesMesh += cmds.ls(sl=1)
            self.ui.poses_LWG.clear()
            for na in posesMesh:
                if not na in items:
                    self.ui.poses_LWG.addItems([na])
            selectionLs = om.MGlobal.getActiveSelectionList()
            num_poses = selectionLs.length()
            self.poses = np.array([om.MFnMesh(selectionLs.getDagPath(i)).getPoints(om.MSpace.kWorld) for i in range(num_poses)])[:, :, :3]
        
        return self.status

    def clearPoses(self):
        self.poses = None
        self.ui.poses_LWG.clear()
        
    def updateBothFunc(self ):
        self.ui.inprogress_PGB.reset()
        
        iterations = self.ui.initIteration_SPB.value()
        sparseness = self.ui.maxInfluence_SPB.value()
        maxIterations = self.ui.updateIteration_SPB.value()
        
        if self.mode == 1:
            num_bones = len(self.boneList)
            self.W, self.bone_transforms, rest_bones_t ,finalBone = self.MTSC(self.poses, self.rest_pose ,num_bones ,iterations , maxIterations , sparseness ,self.mesh ,self.boneList)
        else:
            num_bones = self.ui.boneNum_SPB.value()
            self.W, self.bone_transforms, rest_bones_t ,finalBone = self.MTSC(self.poses, self.rest_pose , num_bones ,iterations ,maxIterations ,sparseness)
     
        if not finalBone:
            for x in rest_bones_t:
                    cmds.select(cl=1)
                    j = cmds.joint()
                    cmds.xform(j , t = x)
                    finalBone.append(j)
            for y in finalBone:
                cmds.select(y , add=1)                 
            cmds.skinCluster(finalBone , self.mesh , tsb = 1)    

            self.skincluster = mel.eval('findRelatedSkinCluster("%s")'%self.mesh)

        tvdict = {}
        preX = None
        for x in range(len(self.W)):
            listClear = []
            for i,na in enumerate(finalBone):
                tp = (na,self.W[x][i])
                listClear.append(tp)
            preX = x
            tvdict[preX] = listClear

        for x in range(len(self.W)): 
            cmds.skinPercent(self.skincluster , '{name}.vtx[{num}]'.format(name = self.mesh , num = x) , transformValue = tvdict[x] )
        
        if self.status == 0:
            for pn in range(self.min_ , self.max_ + 1):
                cmds.currentTime(pn)
                for i,na in enumerate(finalBone):
                    rotation = self.euler_angles_from_rotation_matrix(self.bone_transforms[i][pn][:3,:])
                    trans = self.bone_transforms[i][pn][3,:]
                    cmds.xform(na , t = trans , ro = rotation)
                
                cmds.select(finalBone)
                cmds.setKeyframe()
        
            


def OPEN():
    global Window
    try:
        Window.close()
        Window.deleteLater()
    except:
        pass

    Window = MtscTool()

    Window.ui.show()