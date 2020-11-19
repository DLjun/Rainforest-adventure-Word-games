import sys
sys.path.append(r'穿戴菜单')
MK=["存档","内建函数","查看背包","查看当前人物物品","穿戴物品","卸下物品"]
for i in MK:exec("from %s import *"%i)
def ZWCD_XZ1():#装备&武器菜单-穿戴菜单
    def CDCD_XZ():CLS()
    def CDCD_XZ1():
        print("作用:增加人物使用或穿戴武器装备时的武器装备属性")
        STOP()
    while True:
##        try:
        eval("CDCD_XZ"+str(input(\
    '''
    =======穿戴菜单=======
    === 1.说明         ===
    === 2.穿戴物品     ===
    === 3.卸下物品     ===
    === 4.查看当前着装 ===
    ======================
    请输入操作序号:'''))+"()")
##        except:
##            CLS()
##            break
