import os
import sys
import time
sys.path.append(r'主菜单')
MK=["存档","任务","初始化","内建函数","查看任务书","查看人物状态","查看背包","查看场景","操作菜单"]
for i in MK:exec("from %s import *"%i)
###########################
#初始化
try:
    with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
except:
    start()
###########################
#主函数
def ZCD_XZ6():
    if(input("退出游戏？T/F:").upper()=="T"):
        SAVE(exp,shuxingbiao,shuxing,BAG,changjing,BED,HD,BHS,wancheng)
        quit()
    else:CLS()
def ZCD_XZ():CLS()
while True:
##    try:
    eval("ZCD_XZ"+str(input(\
    '''
    ==========菜单==========
    ==== 1.查看人物状态 ====
    ==== 2.查看任务书   ====
    ==== 3.查看背包     ====
    ==== 4.查看场景     ====
    ==== 5.操作菜单     ====
    ==== 6.退出游戏     ====
    ========================
    请输入操作序号:'''))+"()")
    with open(os.path.dirname(os.getcwd())+"\\雨林探险\\txt\\存档.txt") as r:exec(r.read())
    SAVE(exp,shuxingbiao,shuxing,BAG,changjing,BED,HD,BHS,wancheng)
    CLS()
##    except:
##        LOAD("输入有误",1,0.2)
##        CLS()




