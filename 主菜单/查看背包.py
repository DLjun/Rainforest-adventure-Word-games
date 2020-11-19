import os
import sys
sys.path.append(r'..')
from 内建函数 import *
def ZCD_XZ3():#主菜单-查看背包
    CLS()
    BAG=NEW("BAG")
    ci=0
    item=[]
    WQ=[]
    ZB=[]
    bag_list="    ==========背包==========\n"
    for i in range(0,len(BAG),2):
        QZ=BAG[i].split("_")
        if(QZ[0]=="item"):
            item.append("           %s x %s\n"%(QZ[1],BAG[i+1]))
        if(QZ[0]=="ZB"):
            ZB.append("           %s x %s\n"%(QZ[1],BAG[i+1]))
        if(QZ[0]=="WQ"):
            WQ.append("           %s x %s\n"%(QZ[1],BAG[i+1]))
    if(item!=[]):
        bag_list+="          ====材料====\n"
        for i in item:
            bag_list+=i
    if(WQ!=[]):
        bag_list+="          ====武器====\n"
        for i in WQ:
            bag_list+=i
    if(ZB!=[]):
        bag_list+="          ====装备====\n"
        for i in ZB:
            bag_list+=i
    bag_list+="    ========================"
    print(bag_list)
    STOP()
