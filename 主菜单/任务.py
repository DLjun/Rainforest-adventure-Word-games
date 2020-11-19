import sys
sys.path.append(r'..')
from 存档 import *
from 内建函数 import *
###########################
#任务
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
#with open("\txt\存档.txt") as r:exec(r.read())
def 搭建临时庇护所():
    exp=NEW("exp")
    BHS=NEW("BHS")
    shuxing=NEW("shuxing")
    shuxingbiao=NEW("shuxingbiao")
    CLS()
    print("任务要求:搭建一个庇护所")
    print(\
    '''任务需求:
           -建筑:简易庇护所 x1''')
    print(\
    '''任务奖励:
           -等级 +100exp
           -生命上限 +20
           -体力上限 +10
           -力量上限 +5''')
    STOP()
    if(BHS==1):
        print("任务已完成，任务奖励已发送！")
        STOP()
        exp+=100
        RWSX([[0,'exp','+',100],[0,'生命','+',20],[0,'体力','+',10],[0,'力量','+',5]])
##        shuxingbiao[1]+=20
##        shuxingbiao[2]+=10
##        shuxingbiao[5]+=5
        wancheng.append("搭建临时庇护所")
########################### 

