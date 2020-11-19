import os
import time
from 存档 import *
###########################
#内建函数
def CLS():#清屏
    os.system("cls")
def STOP():#暂停
    input("点击换行继续...")
T=1
def LOAD(load,ci,t1,T=0):#自定义加载
    for i in range(ci):
        for i in range(3):
            print(load+"."*(int(i)+1))
            time.sleep(t1)
            if(T==1):
                CLS()
def NEW(new):#获取存档新值
    glb={}
    with open(os.path.dirname(os.getcwd())+"\\雨林探险\\txt\\存档.txt") as r:
        exec(r.read(),locals(),glb)
    return glb[new]
T=1
def RWSX(CR,T=0):#人物属性修改
    #0表是上限，1表是属性
    #[[表,参数,操作,值],[表,参数,操作,值]]
    #CZ=[[1,"生命","+",10],[1,"体力","+",10]]
    exp=NEW("exp")
    shuxing=NEW("shuxing")
    shuxingbiao=NEW("shuxingbiao")
    DZB={"0":"shuxingbiao[%s]","1":"shuxing[%s]","生命":0,"体力":1,"耐力":2,"速度":3,"力量":4,"狩猎":5,"性别":6}
    for CZ in CR:
        #等级:exp=exp[操作]([传入值]*100)
        if(CZ[1]=="等级"):
            CZ[1]=="exp"
            CZ[3]*=100
        if(CZ[1]=="exp"):
            CZ[1]=="exp"
            glb={}
            exec("exp=%s%s%s"%(CZ[1],CZ[2],CZ[3]),locals(),glb)
            if(exp<0):
                return "None"
            
            exec("exp=%s"%(exp))
        glb={}
        if(CZ[1]!="exp"):
            exec("jisuan=%s%s%s"%(eval(DZB[str(CZ[0])]%(DZB[CZ[1]])),CZ[2],CZ[3]),locals(),glb)
            if(glb["jisuan"]<0):
                return "None"
            exec("%s=%s"%(DZB[str(CZ[0])]%(DZB[CZ[1]]),glb["jisuan"]))
    fanhui=[exp,shuxingbiao,shuxing]
    if(T==1):
        SAVE(exp=exp,shuxingbiao=shuxingbiao,shuxing=shuxing)
    return fanhui
##RWSX([[,'','',]])
###########################
##人物属性【生命/体力/耐力/速度/力量/狩猎/性别】    
##shuxingbiao=[100, 50, 10, 10, 10, 0]
##shuxing=[100, 50, 10, 10, 10, 0]
