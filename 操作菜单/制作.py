import os
from 存档 import *
from 内建函数 import *
from 查看背包 import *
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\建筑.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\item.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\装备.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\武器.txt") as r:exec(r.read())
TX="item_"
def zhizuo(item,TX=TX):
    ci=1
    cailiao=""
    for i in item[2]:
        if(ci==2):
            cailiao+=" x"+str(i)+"\n"
            ci=1
            continue
        cailiao+="        - "+i.strip("item_").strip("ZB_").strip("WQ_")
        ci=2
    CLS()
    if(len(item)>7):
        shuliang=item[8]
    else:
        shuliang=item[3]
    print(\
'''
==============================================

    名称:
         - %s
    简介:
         - %s
    材料:
%s
    合成物品:
         - %s x %s'''%(item[0],item[1],cailiao,item[0],shuliang))
    BAG=NEW("BAG")
    zhizuo=""
    shu=int("99999"*9)
    made=1
    for i in range(0,len(item[2]),2):
        md=0
        for a in range(0,len(BAG),2):
            if item[2][i] in BAG[a]:
                ci=BAG[a+1]//item[2][i+1]
                zhizuo+="         - %s x %s/%s\n"%(item[2][i].strip("item_"),BAG[a+1],item[2][i+1])
                md=1
                if(ci==0):
                    made=0
                    continue
                if(shu>ci):
                    shu=ci
                    break
        if(md==0):
            zhizuo+="         - %s x %s/%s"%(item[2][i].strip("item_"),"0",item[2][i+1])
            made=0
    if(len(zhizuo)>1):
        print(\
'''    合成材料:
%s
    '''%(zhizuo))
    if(made==1):
        md=input(\
'''==============================================
    现在最多可以制作%s个,请输入制作数量:'''%(str(shu)))
        if(int(md)<=shu and int(md)!=0):
            rem=[]
            for i in range(0,len(item[2]),2):
                for a in range(0,len(BAG),2):
                    if item[2][i] in BAG[a]:
                        BAG[a+1]-=item[2][i+1]*int(md)
                        if(BAG[a+1]==0):
                            rem.append(a)
                            rem.append(a+1)
                            continue
            rem.sort()
            for i in rem[::-1]:
                BAG.pop(int(i))
            BAG.append(TX+item[0])
            BAG.append(int(md))
            print(\
'''==============================================
    制作成功
==============================================''')
            SAVE(BAG=BAG)
            if(input("是否查看背包?T/F:").upper()=="T"):
                ZCD_XZ3()
        else:
            print(\
'''==============================================
    制作取消
==============================================''')
            STOP()
    if(made==0):
        print(\
'''==============================================
    你暂时无法制作本物品
==============================================''')
        STOP()
