# -*- coding: utf-8 -*-
from pyfbsdk import *
import os
import site

path = os.path.abspath( __file__ +'{}'.format('/../'))
#site.addsitedir(path)
lSystem = FBSystem()
lSysOnUIIdle = lSystem.OnUIIdle
ScrPath = [
            '{}'.format(path)+'/LockUpWindow.py',
            #'{}'.format(path)+'/NoDockWidget.py',
            '{}'.format(path)+'/AddShelfButton.py',
            ]
# UIIdle 이벤트의 초기화(이외에도 사용하고 있는 툴이 있었을 때의 회피용)
lSysOnUIIdle.RemoveAll()
StartUp=-1
def RunStartUp(pOjbect, pEventName):
    global StartUp
    if StartUp==-1:
        # 스타트업 스크립트를 실행
        #print "RunStartUp"
        StartUp=0
        for i in ScrPath:
            FBApplication().ExecuteScript(r"%s"%i)
    else:
        # UIIdle 이벤트를 해제
        #print "EventOff"
        lSysOnUIIdle.Remove(RunStartUp)
 
# UIIdle 이벤트에 스크립트 실행처리 추가
lSysOnUIIdle.Add(RunStartUp)
