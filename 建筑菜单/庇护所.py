import os
from 存档 import *
from 内建函数 import *
from 查看背包 import *
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\建筑.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\item.txt") as r:exec(r.read())
def JZCD_XZ1():
    def JZBHS():
        BHS=NEW("BHS")
        BHS+=1
        ci=1
        cailiao=""
        for i in JZ_庇护所[1]:
            if(ci==2):
                cailiao+=" x"+str(i*BHS)+"\n"
                ci=1
                continue
            cailiao+="        - "+i.strip("item_")
            ci+=1
        print(\
'''
=====建造庇护所=====
名称:
    -%s级庇护所
功能:
    -火堆减少%s消耗、床减少%s消耗
前置:
    -床天数   %s/%s
    -火堆天数 %s/%s
材料:
%s
建造建筑:
    -庇护所:%s级庇护所'''%(str(BHS),str(BHS*10)+"%",str(BHS*10)+"%",BED,JZ_庇护所[2]*(BHS*2),HD,JZ_庇护所[3]*(BHS*2),cailiao,str(BHS)))
        BAG=NEW("BAG")
        zhizuo=""
        made=1
        if(BED<JZ_庇护所[2]*(BHS*2) or HD<JZ_庇护所[3]*(BHS*2)):
            made=0
        for i in range(0,len(JZ_庇护所[1]),2):
            md=0
            for a in range(0,len(BAG),2):
                if JZ_庇护所[1][i] in BAG[a]:
                    ci=BAG[a+1]//JZ_庇护所[1][i+1]
                    zhizuo+="         - %s x %s/%s\n"%(JZ_庇护所[1][i].strip("item_"),BAG[a+1],JZ_庇护所[1][i+1]*BHS)
                    md=1
                    if(ci==0):
                        made=0
                        continue
            if(md==0):
                zhizuo+="         - %s x %s/%s"%(JZ_庇护所[1][i].strip("item_"),"0",JZ_庇护所[1][i+1]*BHS)
                made=0
        if(len(zhizuo)>1):
            print(\
'''合成材料:
%s
===================='''%(zhizuo))
        if(made==1):
            md=input(\
    '''==============================================
        材料齐全，是否开始制作?(T/F):''')
            if(md.upper()=="T"):
                rem=[]
                for i in range(0,len(JZ_庇护所[1]),2):
                    for a in range(0,len(BAG),2):
                        if JZ_庇护所[1][i] in BAG[a]:
                            BAG[a+1]-=JZ_庇护所[1][i+1]*BHS
                            if(BAG[a+1]==0):
                                rem.append(a)
                                rem.append(a+1)
                                continue
                rem.sort()
                for i in rem[::-1]:
                    BAG.pop(int(i))
                BHS=NEW("BHS")
                BHS+=1
                print(\
'''==============================================
        制作成功
==============================================''')
                SAVE(BAG=BAG,BHS=BHS)
                if(input("是否查看庇护所等级?T/F:").upper()=="T"):
                    print("庇护所等级:%s级"%BHS)
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
    BHS=NEW("BHS")
    XZ=input(\
'''
========庇护所菜单=========
==== 1.作用说明        ====
==== 2.建造            ====
==== 3.升级(%s级)      ====
===========================
请输入操作序号(换行退出):'''%(str(BHS+1)))
    if(XZ=="1"):
        print(\
'''
============庇护所介绍=============
说明:避难所可以减少消耗
一级:火堆减少10%消耗、床减少10%消耗
二级:火堆减少20%消耗、床减少20%消耗
三级:火堆减少30%消耗、床减少30%消耗
===================================
''')
        STOP()
    elif(XZ=="2" and BHS==0):
        JZBHS()
    elif(XZ=="2" and BHS!=0):
        LOAD("检测到您已经有庇护所了，已帮你自动跳转升级功能！",1,0.2)
        JZBHS()
    elif(XZ=="3" and BHS!=0):
        JZBHS()
    elif(XZ=="3" and BHS==0):
        LOAD("检测到您没有庇护所，已帮你自动跳转建造功能！",1,0.2)
        JZBHS()
    
