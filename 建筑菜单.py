import os
import sys
sys.path.append(r'建筑菜单')
sys.path.append(r'主菜单')
MK=["存档","内建函数","查看背包","庇护所","床","火堆"]
for i in MK:exec("from %s import *"%i)
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
def CZCD_XZ3():#操作菜单-建筑菜单    
    while True:
        HD=NEW("HD")
        BHS=NEW("BHS")
        BED=NEW("BED")
        try:
            eval("JZCD_XZ"+str(input(\
'''    ========建筑菜单=========
    ==== 1.庇护所(%s级)   ====
    ==== 2.床(剩余%s天)   ====
    ==== 3.火堆(剩余%s天) ====
    =========================
    请输入操作序号(换行退出):'''%(BHS,BED,HD))+"()"))
            CLS()
        except:
            break
