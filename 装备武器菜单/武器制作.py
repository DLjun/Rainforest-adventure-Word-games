import sys
sys.path.append(r'../操作菜单')
from 制作 import *
with open(os.path.dirname(os.getcwd())+"\\雨林探险\\txt\\存档.txt") as r:exec(r.read())
def ZWCD_XZ3():#装备&武器菜单-武器制作
    wuping=[]
    zhizuo_list=\
'''========制作列表========
等级:%s\n'''%(exp)
    L0=["粗制长矛 x1"]
    L1=["粗制长矛 x1"]
    xuhao=1
    for i in range(exp+1):
        zhizuo_list+="=========Level %s========\n"%str(int(i))
        for k in eval("L%s"%i):
            zhizuo_list+="%s、%s\n"%(str(xuhao),k)
            wuping.append(k)
            xuhao+=1
    print(zhizuo_list)
    item=eval("WQ_"+wuping[int(input("请输入需要制作的物品序号(换行退出):"))-1].split(" ")[0])
    zhizuo(item,TX="WQ_")
