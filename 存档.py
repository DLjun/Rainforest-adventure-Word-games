import os
#with open(os.path.dirname(os.getcwd())+"\\雨林探险\\txt\\存档.txt") as r:exec(r.read())
with open("txt\存档.txt") as r:exec(r.read())
def SAVE(exp=exp,shuxingbiao=shuxingbiao,shuxing=shuxing,BAG=BAG,changjing=changjing,BED=BED,HD=HD,BHS=BHS,wancheng=wancheng,ZBbiao=ZBbiao,WQbiao=WQbiao):
    t1=open("txt/存档.txt","w")
    t1.write(\
'''###########################
#人物属性

#经验值
exp=%s
#属性
shuxingbiao=%s
#人物属性【等级/生命/体力/耐力/速度/力量/狩猎】
shuxing=%s
#背包
BAG=%s
#人物位置
changjing=%s
###########################
#建筑属性

#床
BED=%s
#火堆天数
HD=%s
#庇护所
BHS=%s
###########################    
#任务状态
wancheng=%s
#任务-已完成
###########################
#装备武器
ZBbiao=%s
#1头部 2胸部 3腿部 4脚部 5左手戒指 
#6右手戒指 7左肩 8右肩 9腰部 10背部 11项链
WQbiao=%s
#1左手 2右手
###########################'''%(exp,shuxingbiao,shuxing,BAG,changjing,BED,HD,BHS,wancheng,ZBbiao,WQbiao))
    t1.close()

#SAVE(0,[100,50,10,10,10,0],[100,50,10,10,10,0],[],["森林"],0,0,0,[],["","","","","","","","","","",""],["",""])
