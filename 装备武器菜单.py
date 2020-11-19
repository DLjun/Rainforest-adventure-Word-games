import os
import sys
sys.path.append(r'主菜单')
sys.path.append(r'装备武器菜单')
MK=["存档","内建函数","查看背包","装备制作","武器制作","穿戴菜单"]
for i in MK:exec("from %s import *"%i)
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
def CZCD_XZ5():#操作菜单-装备&武器
    while True:
##        try:
        eval("ZWCD_XZ"+str(input(\
'''
======装备&武器菜单======
====   1.穿戴装备    ====
====   2.装备制作    ====
====   3.武器制作    ====
=========================
请输入操作序号(换行退出):''')+"()"))
        CLS()
##        except:
##            break
##穿戴位置:
##1  头部
##2  胸部
##3  腿部
##4  脚部
##5  左手
##6  右手
##7  左肩
##8  右肩
##9  腰部
##10 背部
##11 项链
##12 左手戒指
##13 右手戒指
