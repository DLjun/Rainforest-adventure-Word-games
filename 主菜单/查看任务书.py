import os
import sys
sys.path.append(r'..')
from 任务 import *
from 内建函数 import *
with open(os.getcwd()+"\\txt\\存档.txt") as r:exec(r.read())
def ZCD_XZ2():#主菜单-查看任务书
    wancheng=NEW("wancheng")
    renwu=[]
    if(shuxing[0]>=0):
        if "搭建临时庇护所" not in wancheng:
            renwu.append("搭建临时庇护所")
    xuhao=1
    CLS()
    print("    ========任务列表========")
    for i in renwu:
        print(str(xuhao)+"、"+i)
    print("    ========================")
    try:
        eval(str(renwu[int(input("请输入任务序号(换行退出):"))-1])+"()")
    except:
        ''
