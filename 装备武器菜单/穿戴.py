import sys
sys.path.append(r'穿戴菜单')
MK=["存档","内建函数","查看背包","查看当前人物物品","穿戴物品","卸下物品"]
for i in MK:exec("from %s import *"%i)
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
def ZWCD_XZ1():#装备&武器菜单-穿戴菜单
    
