import os
from 存档 import *
from 内建函数 import *
from 查看背包 import *
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\建筑.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\item.txt") as r:exec(r.read())
def JZCD_XZ2():
    def JZBED():
        BED=NEW("BED")
        ci=1
        cailiao=""
        for i in JZ_床[1]:
            if(ci==2):
                cailiao+=" x"+str(i)+"\n"
                ci=1
                continue
            cailiao+="        - "+i.strip("item_")
            ci=2
        print(\
'''
=====建造床=====
名称:
    -床
功能:
    -建造床后可以睡觉
材料:
%s
建造建筑:
    -床:剩余%s天
================'''%(cailiao,str(BED)))
        BAG=NEW("BAG")
        zhizuo="(合成公式:耗材+剩余天数+制作天数)\n"
        shu=int("99999"*9)
        made=1
        for i in range(0,len(JZ_床[1]),2):
            md=0
            for a in range(0,len(BAG),2):
                if JZ_床[1][i] in BAG[a]:
                    ci=1
                    huihe=0
                    while True:
                        huihe=BAG[a+1]//(JZ_床[1][i+1]+BED+ci)
                        if(huihe<=0):
                            ci-=1
                            if(ci<1):
                                ci=1
                                made=0
                            break
                        ci+=1
                    zhizuo+="    - %s x %s/%s\n"%(JZ_床[1][i].strip("item_"),BAG[a+1],(JZ_床[1][i+1]+BED+ci))
                    md=1
            if(md==0):
                zhizuo+="         - %s x %s/%s"%(JZ_床[1][i].strip("item_"),"0",(JZ_床[1][i+1]+BED+1))
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
                for i in range(0,len(JZ_床[1]),2):
                    for a in range(0,len(BAG),2):
                        if JZ_床[1][i] in BAG[a]:
                            BAG[a+1]-=(JZ_床[1][i+1]+BED+int(md))
                            if(BAG[a+1]==0):
                                rem.append(a)
                                rem.append(a+1)
                                continue
                rem.sort()
                for i in rem[::-1]:
                    BAG.pop(int(i))
                BED=NEW("BED")
                BED+=int(md)
                print(\
'''==============================================
        制作成功
==============================================''')
                SAVE(BAG=BAG,BED=BED)
                if(input("是否查看床剩余天数?T/F:").upper()=="T"):
                    BED=NEW("BED")
                    print("床剩余天数:%s天"%BED)
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
    BED=NEW("BED")
    XZ=input(\
'''
==========床菜单===========
==== 1.作用说明        ====
==== 2.建造            ====
==== 3.升级(%s级)      ====
===========================
请输入操作序号(换行退出):'''%(str(BED+1)))
    if(XZ=="1"):
        print(\
'''
============床介绍=============
说明:建造床后可以睡觉
===============================
''')
        STOP()
    elif(XZ=="2" and BED==0):
        JZBED()
    elif(XZ=="2" and BED!=0):
        LOAD("检测到您已经有床了，已帮你自动跳转升级功能！",1,0.2)
        JZBED()
    elif(XZ=="3" and BED!=0):
        JZBED()
    elif(XZ=="3" and BED==0):
        LOAD("检测到您没有床，已帮你自动跳转建造功能！",1,0.2)
        JZBED()
    
