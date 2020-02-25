import maya.cmds as cmds
import maya.mel as mel
import random
# select top controller group

class treeSim():
    
    def __init__ (self):
        self.a = 0
        self.b = 0
        self.intList = [ y for y in range(300) ]
        self.sel_ = cmds.ls(sl=1)[0]
        # con List 
        self.list = cmds.ls('*_CON')
        
    def getDistance(self, pos1, pos2 ):
        self.distance = ( ( pos1[0] - pos2[0] ) **2 + ( pos1[1] - pos2[1] ) **2 + ( pos1[2] - pos2[2] ) **2 ) **0.5
        self.distance = round( self.distance, 4 )
        return self.distance
    """    
    def get_dis( pos1, pos2 ):
        
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        
        distance = math.sqrt(math.pow(x2-x1, 2)
                        + math.pow(y2-y1, 2)
                        + math.pow(z2-z1, 2))
        return distance
    """
    
    def nearestJointsList(self, base, objList ):
        self.nDisList = []
        self.disList = []
        for x in range( len( objList ) ):
            basePos = cmds.xform( base, ws=True, t=True, q=True )
            pos = cmds.xform( objList[x], ws=True, t=True, q=True )
            dis = self.getDistance( basePos, pos )
            self.disList.append( dis )
        for i in range( len( self.disList ) ):
            if len( self.disList ) != 0:
                disIndex = self.disList.index( min( self.disList ) )
                self.nDisList.append( objList[ disIndex ] )
                #print objList[ disIndex ]
                del self.disList[ disIndex ]
                del objList[ disIndex ]
                
        return self.nDisList

            
#nearestJointsList( 'locator1', cmds.ls(sl=True) )             
    def calPow(self,lp):
        jointLen = len(cmds.listRelatives(self.sel_ ,ad=1))
        if lp >= jointLen:
            self.a= 0.0
        if jointLen > lp > jointLen/10 * 9:
            self.a=0.5            
        if jointLen/10 * 9 >= lp > jointLen/10 * 8:
            self.a= 1.0          
        if jointLen/10 * 8 >= lp > jointLen/10 * 6:
            self.a= 1.5        
        if jointLen/10 * 6 >= lp > jointLen/10 * 5:
            self.a = 2.0
        if jointLen/10 * 5 >= lp > jointLen/10 * 4:
            self.a= 2.5
        if jointLen/10 * 4 >= lp > jointLen/10 * 3:
            self.a= 3.0
        if jointLen/10 * 3 >= lp > jointLen/10 * 2:
            self.a= 4.0
        if jointLen/10 * 2 >= lp > jointLen/10 * 1:
            self.a= 5.0
                                 
        return self.a     

       
    def branchSim(self):
        
        arrayList = self.nearestJointsList(self.sel_, self.list )
            
        #double zero out
        for x in arrayList :
                
            #add attribute
         
            mel.eval('addAttr -ln "swayFrequency"  -at double  -min 0.001 -dv 0.001 %s' %x)
            cmds.setAttr('%s.swayFrequency' %x, e=True, keyable= True)
            mel.eval('addAttr -ln "swaySpeed"  -at double  -min 0.001 -dv 0.001 %s' %x)
            cmds.setAttr('%s.swaySpeed' %x, e=True, keyable= True)
            mel.eval('addAttr -ln "swayTurbulence"  -at double  -min 0.001 -dv 0.001 %s' %x)
            cmds.setAttr('%s.swayTurbulence' %x, e=True, keyable= True)
            mel.eval('addAttr -ln "swayOffset"  -at double  -min -100.0 -dv 0.0 %s' %x)
            cmds.setAttr('%s.swayOffset' %x, e=True, keyable= True)
            
            ##################################################3
            
            grpName = cmds.group(em=True, w=True)
            cmds.select(x,grpName)
            mel.eval('delete`parentConstraint`')    
            cmds.parent(grpName,x.split('_CON')[0] + '_NUL')
            cmds.parent(x,grpName)
               
            sp_name = x.split('_CON')[0] + '_expression_NUL'
            cmds.rename(grpName , sp_name)
            
            random.shuffle(self.intList)
        
            pow = len(cmds.listRelatives(x,ad=1))
            self.calPow(pow)
                   
            #add Expression
            #cmds.expression(o = sp_name ,s = 'rx = (%s.swayFrequency + %s) * noise(((time + %s) / %s.swaySpeed - %s ) * %s.swayTurbulence);' %(x,self.a,self.intList[1],x,self.a,x) )
           
            random.shuffle(self.intList)          
            cmds.expression(o = sp_name , s= "if ( %s.swayFrequency == 0 ){\n\n\t\t%s.rotateX = 0;\n\n} else if ( %s.swaySpeed == 0 ){\n\n\t\t%s.rotateX = 0;\n\n} else if ( %s.swayTurbulence == 0 ){\n\t\t\n\t\t%s.rotateX = 0;\n\t\t\n} else {\n\n\t\t%s.rotateX = (%s.swayFrequency + %s) * noise(((time + %s + %s.swayOffset) / %s.swaySpeed - %s) * %s.swayTurbulence);\n\n}"
            %(x,sp_name,x,sp_name,x,sp_name,sp_name,x,self.a,self.intList[1],x,x,self.a,x))  
           
            random.shuffle(self.intList)           
            cmds.expression(o = sp_name , s= "if ( %s.swayFrequency == 0 ){\n\n\t\t%s.rotateY = 0;\n\n} else if ( %s.swaySpeed == 0 ){\n\n\t\t%s.rotateY = 0;\n\n} else if ( %s.swayTurbulence == 0 ){\n\t\t\n\t\t%s.rotateY = 0;\n\t\t\n} else {\n\n\t\t%s.rotateY = (%s.swayFrequency + %s) * noise(((time + %s + %s.swayOffset) / %s.swaySpeed - %s) * %s.swayTurbulence);\n\n}"
            %(x,sp_name,x,sp_name,x,sp_name,sp_name,x,self.a,self.intList[1],x,x,self.a,x))  
           
            random.shuffle(self.intList)
            cmds.expression(o = sp_name , s= "if ( %s.swayFrequency == 0 ){\n\n\t\t%s.rotateZ = 0;\n\n} else if ( %s.swaySpeed == 0 ){\n\n\t\t%s.rotateZ = 0;\n\n} else if ( %s.swayTurbulence == 0 ){\n\t\t\n\t\t%s.rotateZ = 0;\n\t\t\n} else {\n\n\t\t%s.rotateZ = (%s.swayFrequency + %s) * noise(((time + %s + %s.swayOffset) / %s.swaySpeed - %s) * %s.swayTurbulence);\n\n}"
            %(x,sp_name,x,sp_name,x,sp_name,sp_name,x,self.a,self.intList[1],x,x,self.a,x))  
                        
            #random.shuffle(self.intList)
            #cmds.expression(o = sp_name ,s = 'ry = (%s.swayFrequency + %s) * noise(((time + %s) / %s.swaySpeed - %s) * %s.swayTurbulence);' %(x,self.a,self.intList[1],x,self.a,x) )
            #random.shuffle(self.intList)
            
            #cmds.expression(o = sp_name ,s = 'rz = (%s.swayFrequency + %s) * noise(((time + %s) / %s.swaySpeed - %s) * %s.swayTurbulence);' %(x,self.a,self.intList[1],x,self.a,x) )
        
cName = treeSim()
cName.branchSim()

