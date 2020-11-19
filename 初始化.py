import os
from 存档 import *
from 内建函数 import *
###########################
#初始化
def start():
    SAVE(0,[100,50,10,10,10,0],[100,50,10,10,10,0],[],"森林",0,0,0,[],["","","","","","","","","","",""],["",""])
    with open(os.path.dirname(os.getcwd())+"\\雨林探险\\txt\\存档.txt") as r:exec(r.read())
    print("====================")
    print("      雨林探险      ")
    print("====================")
    STOP()
    mnt=input("请选择初始性别(1.男/2.女):")
    while True:
        if(mnt=="1"):
            shuxingbiao.append(1)
            break
        elif(mnt=="2"):
            shuxingbiao.append(0)
            break
        shuxingbiao=shuxing
    STOP()
    CLS()
    T1=list("你独自进入了森林，为接下来的探险做好了准备。\n你的手上有着一本早已策划好的任务书。\n你将在这个丛林中生活下去。")
    k=""
    for i in T1:
        CLS()
        k+=i
        print(k)
        time.sleep(0.1)
    SAVE(exp,shuxingbiao,shuxing,BAG,changjing,BED,HD,BHS,wancheng)
    STOP()
    CLS()
###########################    
