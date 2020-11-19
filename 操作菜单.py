import os
import sys
sys.path.append(r'操作菜单')
sys.path.append(r'主菜单')
MK=["存档","内建函数","查看背包","制作","制作物品","睡觉","探险菜单","建筑菜单","探险菜单","装备武器菜单"]
for i in MK:exec("from %s import *"%i)
with open(os.path.dirname(os.getcwd())+"\\雨林探险\\txt\\存档.txt") as r:exec(r.read())
def ZCD_XZ5():#主菜单-操作人物
    LOAD("正在进入制作菜单",1,0.2)
    CLS()
    while True: 
##        try:
        CLS()
        with open(os.path.dirname(os.getcwd())+"\\雨林探险\\txt\\存档.txt") as r:exec(r.read())
        SAVE(exp,shuxingbiao,shuxing,BAG,changjing,BED,HD,BHS,wancheng)
        eval("CZCD_XZ"+str(input(\
'''
========操作菜单========
==== 1.制作物品     ====
==== 2.睡觉         ====
==== 3.建筑菜单     ====
==== 4.探险菜单     ====
==== 5.装备&武器    ====
========================
请输入操作序号(换行退出):''')+"()"))
        CLS()
##        except:
##            LOAD("正在返回主菜单",1,0.3)
##            break
