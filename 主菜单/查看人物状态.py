import os
import sys
sys.path.append(r'..')
from 内建函数 import *
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
def ZCD_XZ1():#主菜单-查看人物状态
    exp=NEW("exp")
    shuxing=NEW("shuxing")
    shuxingbiao=NEW("shuxingbiao")
    CLS()
    print(\
    '''
    属性表【现有-上限】
    等级:{}
    生命:{}/{}
    体力:{}/{}
    耐力:{}/{}
    速度:{}/{}
    力量:{}/{}
    狩猎:{}/{}
    '''.format(exp//100,shuxing[0],shuxingbiao[0],shuxing[1],shuxingbiao[1],shuxing[2],shuxingbiao[2],shuxing[3],shuxingbiao[3],shuxing[4],shuxingbiao[4],shuxing[5],shuxingbiao[5]))
    STOP()
