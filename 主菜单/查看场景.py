import os
import sys
sys.path.append(r'..')
from 内建函数 import *
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
def ZCD_XZ4():#主菜单-查看场景
    with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
    CLS()
    print("当前地点:%s"%changjing[0])
    STOP()
