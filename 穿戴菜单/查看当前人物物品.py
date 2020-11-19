import os
from 存档 import *
from 内建函数 import *
from 查看背包 import *
with open(os.getcwd()+"\\txt\\装备.txt") as r:exec(r.read())
with open(os.getcwd()+"\\txt\\武器.txt") as r:exec(r.read())
def CDCD_XZ4():
    BAG=NEW("BAG")
    ZBbiao=NEW("ZBbiao")
    WQbiao=NEW("WQbiao")
    DZB1={'0':'头部','1':'胸部','2':'腿部','3':'脚部','4':'左手戒指','5':'右手戒指','6':'左肩','7':'右肩','8':'腰部','9':'背部','10':'项链'}
    DZB2={'0':'左手','1':'右手'}
    xianyou=""
    ci=0
    if(WQbiao!=['', '']):
        xianyou+="===========武器===========\n"
        for i in WQbiao:
            if(i!=""):
                xianyou+=("%s:%s\n"%(DZB2[str(WQbiao.index(i))],i))
                ci=1
    if(ZBbiao!=['', '', '', '', '', '', '', '', '', '', '']):
        xianyou+="===========装备===========\n"
        ci=0
        for i in ZBbiao:
            if(i!=""):
                xianyou+=("%s:%s\n"%(DZB1[str(ZBbiao.index(i))],i))
                ci=1
    if(ci==0):
        xianyou+="=========查询结果=========\n"
        xianyou+="你目前没有任何装备和武器!\n"
    xianyou+="==========================\n"
    print(xianyou)
    STOP()
