from 制作 import *
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
def CZCD_XZ1():#操作菜单-制作物品
    wuping=[]
    zhizuo_list=\
'''========制作列表========
等级:%s\n'''%(exp)
    L0=["简易草绳 x1"]
    L1=["普通草绳 x1"]
    xuhao=1
    for i in range(exp+1):
        zhizuo_list+="=========Level %s========\n"%str(int(i))
        for k in eval("L%s"%i):
            zhizuo_list+="%s、%s\n"%(str(xuhao),k)
            wuping.append(k)
            xuhao+=1
    print(zhizuo_list)
    item=eval("item_"+wuping[int(input("请输入需要制作的物品序号(换行退出):"))-1].split(" ")[0])
    zhizuo(item)
    
