import maya.cmds as cmds
import maya.mel as mel
import os
import site
basePath = os.path.abspath(__file__ + '/../')
site.addsitedir(basePath)
import ControllerTem as ct ;reload(ct)

class FkConMake:
    def __init__(self):
        self.dictA = {}
        self.dictL = {}
        self.conList = []
        self.selList = None
        self.hiList = None

    def dictFunc_(self,A_,DIC_,C_):
        if not A_ in DIC_ :
            DIC_[A_] = C_

        elif type(DIC_[A_]) == type(u'string'):
            DIC_[A_] = [DIC_[A_] , C_]

        elif type(DIC_[A_]) == type([]):
            DIC_[A_] = DIC_[A_] + [C_]

    def selectionFunc(self):
        
        # IF MORE THAN TWO SELECTION #     
        hiList = cmds.ls(sl = 1 , dag=True,ni=True , type = 'transform')       
        for qa in hiList:

            if cmds.listRelatives(qa,p=1):              
                
                if cmds.listRelatives(qa,f=1):
                    upperG = cmds.listRelatives(qa,f=1)[0].split('|')[1]
                    self.dictFunc_(upperG,self.dictL,qa)

            
            else:
                upperG = qa
                self.dictL[upperG] = qa
        return self.dictL
   
    def hireachyQuery(self,selList):
        # select hierachy save

        for k in selList:
            Rel_ = cmds.listRelatives(k,p=True)

            if Rel_:
                a = Rel_[0] #shape
                self.dictFunc_(a,self.dictA,k)

        return self.dictA

    def ConMake(self,shape,selList):
        self.conList= []
        set_l = ['x','y','z']
        for i in selList:

            #con make		

            FK_con = ct.chooseConShape(shape) 
            cmds.rename(FK_con , i + '_CON')
            self.conList.append(i+'_CON')
            for y in set_l:
                if cmds.objectType(i) == 'joint':
                    if not cmds.getAttr(i + '.r' + y) == 0 :
                        cmds.select(i)
                        mel.eval('makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;')

                t_jo = cmds.xform(i , q=True , t=True)
                ro_jo = cmds.xform(i , q=True , ro = True)

                for x in range(len(t_jo)):
                    high_set = set_l[x].upper()
                    if cmds.objectType(i) == 'joint':
                        r_jo = cmds.getAttr(i +'.jointOrient'+high_set)

                        cmds.setAttr(i+'_CON' +'.t' + set_l[x] , t_jo[x])
                        cmds.setAttr(i+'_CON' +'.r' + set_l[x] , r_jo)
                    else:
                        cmds.setAttr(i+'_CON' +'.t' + set_l[x] , t_jo[x])
                        cmds.setAttr(i+'_CON' +'.r' + set_l[x] , ro_jo[x])

    def scaleEdit (self,selList,scale_):

        for i in selList:
            cls_ = cmds.cluster(i)
            cmds.scale (scale_ ,scale_ ,scale_ , r=True )
            cmds.delete(i ,ch=True)

    def colorEdit (self,selList,color_):

        for x in selList:
	    s = cmds.listRelatives(x , s=1)[0]
            cmds.setAttr(s + '.overrideEnabled', 1)
            cmds.setAttr(s + '.overrideColor', color_)


    def zeroOut(self,selList): #con List
        #nulGroup

        for re_ in selList:
            nul = cmds.group(n= re_.replace('_CON','_NUL') ,em =True)
            cmds.select (re_ ,nul)
            mel.eval('delete`parentConstraint`')
            cmds.parent(re_ , nul)

    def parentFunc(self,selList):

        for jo in selList:

            if self.dictA.get(jo):
                cmds.parent(self.dictA[jo],jo) # lower , upper

                if type(self.dictA[jo]) == type(u'string'):
                    conNul = self.dictA[jo]+ '_NUL'
                    conName = jo + '_CON'
                    cmds.parent(conNul , conName)
                elif type(self.dictA[jo]) == type([]):
                    for a in self.dictA[jo]:
                        conNul = a + '_NUL'
                        conName = jo + '_CON'
                        cmds.parent(conNul , conName)
            conF = jo+ '_CON'
            cmds.parentConstraint(conF,jo, mo =True)

    def launcher(self,sca_,shape,col_):
        dictS = self.selectionFunc()

        for i in dictS:
            if type(dictS[i]) == type([]):
                b = self.hireachyQuery(dictS[i])

                for di in dictS[i]:
                    if cmds.listRelatives(di , p=True):
                        cmds.parent(di , w=True)
            # func
            if type(dictS[i]) == type(u'string'):
                fValue = [dictS[i]]
            else:
                fValue = dictS[i]
        
	    print fValue
            self.ConMake(shape,fValue)
            self.scaleEdit(self.conList,sca_)
            self.colorEdit(self.conList,col_)
            self.zeroOut(self.conList)
            self.parentFunc(fValue)

