import os
from 存档 import *
from 内建函数 import *
from 查看背包 import *
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\建筑.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\item.txt") as r:exec(r.read())
def JZCD_XZ3():
    def JZHD():
        HD=NEW("HD")
        ci=1
        cailiao=""
        for i in JZ_火堆[1]:
            if(ci==2):
                cailiao+=" x"+str(i)+"\n"
                ci=1
                continue
            cailiao+="        - "+i.strip("item_")
            ci=2
        print(\
'''
====建造火堆====
名称:
    -火堆
功能:
    -有火堆才可以使用床
材料:
%s
建造建筑:
    -火堆:剩余%s天
================'''%(cailiao,str(HD)))
        BAG=NEW("BAG")
        zhizuo="(合成公式:耗材+剩余天数+制作天数)\n"
        shu=int("99999"*9)
        made=1
        for i in range(0,len(JZ_火堆[1]),2):
            md=0
            for a in range(0,len(BAG),2):
                if JZ_火堆[1][i] in BAG[a]:
                    ci=1
                    huihe=0
                    while True:
                        huihe=BAG[a+1]//(JZ_火堆[1][i+1]+HD+ci)
                        if(huihe<=0):
                            ci-=1
                            if(ci<1):
                                ci=1
                                made=0
                            break
                        ci+=1
                    zhizuo+="    - %s x %s/%s\n"%(JZ_火堆[1][i].strip("item_"),BAG[a+1],(JZ_火堆[1][i+1]+HD+ci))
                    md=1
            if(md==0):
                zhizuo+="         - %s x %s/%s"%(JZ_火堆[1][i].strip("item_"),"0",(JZ_火堆[1][i+1]+HD+1))
                made=0
        if(len(zhizuo)>1):
            print(\
'''合成材料:
%s'''%(zhizuo))
        if(made==1):
            md=input(\
    '''==============================================
        现在最多可以制作%s个，请输入制作数量:'''%ci)
            if(int(md)<=ci and int(md)!=0):
                rem=[]
                for i in range(0,len(JZ_火堆[1]),2):
                    for a in range(0,len(BAG),2):
                        if JZ_火堆[1][i] in BAG[a]:
                            BAG[a+1]-=(JZ_火堆[1][i+1]+HD+int(md))
                            if(BAG[a+1]==0):
                                rem.append(a)
                                rem.append(a+1)
                                continue
                rem.sort()
                for i in rem[::-1]:
                    BAG.pop(int(i))
                HD=NEW("HD")
                HD+=int(md)
                print(\
'''==============================================
        制作成功
==============================================''')
                SAVE(BAG=BAG,HD=HD)
                if(input("是否查看火堆剩余天数?T/F:").upper()=="T"):
                    HD=NEW("HD")
                    print("火堆剩余天数:%s天"%HD)
                    STOP()
            else:
                print(\
'''==============================================
        制作取消
==============================================''')
                STOP()
        if(made==0):
            print(\
'''==============================================
        你暂时无法制作本建筑
==============================================''')
            STOP()
    HD=NEW("HD")
    XZ=input(\
'''
=========火堆菜单==========
==== 1.作用说明        ====
==== 2.建造            ====
==== 3.升级(%s级)      ====
===========================
请输入操作序号(换行退出):'''%(str(HD+1)))
    if(XZ=="1"):
        print(\
'''
===========火堆介绍============
说明:有火堆才可以使用床
===============================
''')
        STOP()
    elif(XZ=="2" and HD==0):
        JZHD()
    elif(XZ=="2" and HD!=0):
        LOAD("检测到您已经有火堆了，已帮你自动跳转升级功能！",1,0.2)
        JZHD()
    elif(XZ=="3" and HD!=0):
        JZHD()
    elif(XZ=="3" and HD==0):
        LOAD("检测到您没有火堆，已帮你自动跳转建造功能！",1,0.2)
        JZHD()
    
