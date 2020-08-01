#!/usr/bin/python
# -*- coding: UTF-8 -*-

#code by AllAloneForYou(qq695023921)
#enjoy this
#截至编码日 2020-08-01 04：35 很多角色没上场过 无法具体观察实际机制 本人对数据的准确性不做任何担保
#总之 梭哈就对了 赢了会所嫩模 输了下海干活儿嘛 看开点


import random

i=0



            

        
###########################################################################                
def player1skill0(ch):
    if(ch==0):
        pass
    elif (ch==1):#30%概率令对方跳过下回合
        if(random.randint(0,100)<30):
            print(player1.name+'成功发动'+player1.skill0name,end='  ')
            player2.jumpround=1        
    elif (ch==2):#25%概率连续4次12伤害的攻击（会计算护甲）
        if(random.randint(0,100)<25):
            print(player1.name+'成功发动'+player1.skill0name,end='  ')
            for i in range(0,4):#连续4次
                if(random.randint(0,100)<player1.hit*100):#命中计算
                    player2.hp-=12-player2.defence      
    elif (ch==3):#对手为5，7，8，10时 攻击翻倍
        if(iplayer2==5 or iplayer2==7 or iplayer2==8 or iplayer2==10):
            print(player1.name+'成功发动'+player1.skill0name,end='  ')
            player1.attack*=2
    elif (ch==4):#35%概率 该次伤害降低3点 但对手永久降低攻击4点
        if(random.randint(0,100)<35):
            print(player1.name+'成功发动'+player1.skill0name,end='  ')
            if(random.randint(0,100)<player1.hit*100):
                player2.hp-=player1.attack-3
                player2.attack-=4
    elif (ch==5):#30%概率回复25生命
        if(random.randint(0,100)<30):
            print(player1.name+'成功发动'+player1.skill0name,end='  ')
            player1.hp+=25
    elif (ch==6):#若对手是0 输出提升25% 否则有25%概率输出提升25%
        if(iplayer2==0):
            print(player1.name+'成功发动'+player1.skill0name,end='  ')
            player1.attack*=1.25
        else:
            if(random.randint(0,100)<25):
                print(player1.name+'成功发动'+player1.skill0name,end='  ')
                player1.attack*=1.25
    elif (ch==7):#进行一次攻击判定后 对手永久降防5点
        #if(random.randint(0,100)<player1.hit*100):
            #player2.hp-=player1.attack-player2.defence
        if(random.randint(0,100)<30):
            print(player1.name+'成功发动'+player1.skill0name,end='  ')
            player2.defence-=5
    elif (ch==8):#自身生命恢复至20点
        if(player1.cold==9999):
            print(player1.name+'成功发动'+player1.skill0name,end='  ')
            player1.hp=20
            player1.cold=1
    elif (ch==9):#单数回合时伤害提升10但防御下降5 双数回合时随机恢复0-15生命 伤害降低10 防御提升5
        if(round%2==1):
            print(player1.name+'成功发动'+player1.skill0name,end='  ')
            player1.attack+=10
            player1.defence-=5
        else:
            print(player1.name+'成功发动'+player1.skill1name,end='  ')
            player1.hp+=random.randint(0,15)
            player1.attack-=10
            player1.defence+=5
    elif (ch==10):#自身伤害提升3点
        print(player1.name+'成功发动'+player1.skill0name,end='  ')
        player1.attack+=3
    elif (ch==11):#自身获得元素穿透
        print(player1.name+'成功发动'+player1.skill0name,end='  ')
        player1.elemental=1

def player2skill0(ch):
    if(ch==0):
        pass
    elif (ch==1):
        if(random.randint(0,100)<30):
            print(player2.name+'成功发动'+player2.skill0name,end='  ')
            player1.jumpround=1
    elif (ch==2):
        if(random.randint(0,100)<25):
            print(player2.name+'成功发动'+player2.skill0name,end='  ')
            for i in range(0,4):#连续4次
                if(random.randint(0,100)<player2.hit*100):#命中计算
                    player1.hp-=12-player1.defence
    elif (ch==3):
        if(iplayer1==5 or iplayer1==7 or iplayer1==8 or iplayer1==10):
            print(player2.name+'成功发动'+player2.skill0name,end='  ')
            player2.attack*=2
    elif (ch==4):
        if(random.randint(0,100)<35):
            print(player2.name+'成功发动'+player2.skill0name,end='  ')
            if(random.randint(0,100)<player2.hit*100):
                player1.hp-=player2.attack-3
                player1.attack-=4
    elif (ch==5):
        if(random.randint(0,100)<30):
            print(player2.name+'成功发动'+player2.skill0name,end='  ')
            player2.hp+=25
    elif (ch==6):
        if(iplayer1==0):
            print(player2.name+'成功发动'+player2.skill0name,end='  ')
            player2.attack*=1.25
        else:
            if(random.randint(0,100)<25):
                print(player2.name+'成功发动'+player2.skill0name,end='  ')
                player2.attack*=1.25
    elif (ch==7):
        #if(random.randint(0,100)<player2.hit*100):
            #player1.hp-=player2.attack-player1.defence
        if(random.randint(0,100)<30):
            print(player2.name+'成功发动'+player2.skill0name,end='  ')
            player1.defence-=5
    elif (ch==8):
        if(player2.cold==9999):
            print(player2.name+'成功发动'+player2.skill0name,end='  ')
            player2.hp=20
            player2.cold=1
    elif (ch==9):
        if(round%2==1):
            print(player2.name+'成功发动'+player2.skill0name,end='  ')
            player2.attack+=10
            player2.defence-=5
        else:
            print(player2.name+'成功发动'+player2.skill1name,end='  ')
            player2.hp+=random.randint(0,15)
            player2.attack-=10
            player2.defence+=5
    elif (ch==10):
        print(player2.name+'成功发动'+player2.skill0name,end='  ')
        player2.attack+=3
    elif (ch==11):
        print(player2.name+'成功发动'+player2.skill0name,end='  ')
        player2.elemental=1
def player1skill1(ch):
    if(ch==0):
        if(random.randint(0,100)<player1.hit*100):
            player2.hp-=(player2.defence+player1.attack)
            #print("is"+str((player2.defence+player1.attack)))
            if(random.randint(0,100)<35):
                player1.jumpround=1
            
    elif (ch==1):
        for i in range(0,5):
            if(random.randint(0,100)<player1.hit*100):
                player2.hp-=3
    elif (ch==2):
        if(random.randint(0,100)<player2.hit*100):
            player2.hp-=random.randint(0,100)
    elif (ch==3):
        player1.attack*=2
        player1.hit*=0.65
        print(player1.name+"使用普攻")
        if(random.randint(0,100)<player1.hit*100):
            player2.hp-=player1.attack-(1-player1.elemental)*player2.defence
                        #丽塔         #芽衣
            if(iplayer1==4 or iplayer1==1):
                player1skill0(iplayer1)
            print(player2.name+"剩余血量"+str(player2.hp))
        else:
            print("但是被闪避了")
    elif (ch==4):
        player2.hp+=4
        player2.banskill=1
        player2.attack*=0.6
    elif (ch==5):
        if(random.randint(0,100)<player1.hit*100):
            player2.hp-=25
    elif (ch==6):
        for i in range(0,7):
            if(random.randint(0,100)<player1.hit*100):
                player2.hp-=16-player2.defence
    elif (ch==7):
        for i in range(0,5):
            if(random.randint(0,100)<player1.hit*100):
                player2.hp-=16-player2.defence
    elif (ch==8):
        if(random.randint(0,100)<50):
            player2.hp-=233-player2.defence
        else:
            player2.hp-=50-player2.defence
        player1.cold=9998
    elif (ch==9):
        pass
    elif (ch==10):
        player2.hp-=30-player2.defence
    elif (ch==11):
        player2.hp-=18
        player2.hit*=0.75
def player2skill1(ch):
    if(ch==0):
        if(random.randint(0,100)<player2.hit*100):
            player1.hp-=(player1.defence+player2.attack)
            if(random.randint(0,100)<35):
                player2.jumpround=1
    elif (ch==1):
        for i in range(0,5):
            if(random.randint(0,100)<player2.hit*100):
                player1.hp-=3
    elif (ch==2):
        if(random.randint(0,100)<player2.hit*100):
            player1.hp-=random.randint(0,100)
    elif (ch==3):
        player2.attack*=2
        player2.hit*=0.65
        print(player2.name+"使用普攻")
        if(random.randint(0,100)<player2.hit*100):
            player1.hp-=player2.attack-(1-player2.elemental)*player1.defence
                        #丽塔         #芽衣
            if(iplayer2==4 or iplayer2==1):
                player2skill0(iplayer2)
            print(player1.name+"剩余血量"+str(player1.hp))
        else:
            print("但是被闪避了")
    elif (ch==4):
        player1.hp+=4
        player1.banskill=1
        player1.attack*=0.6
    elif (ch==5):
        if(random.randint(0,100)<player2.hit*100):
            player1.hp-=25
    elif (ch==6):
        for i in range(0,7):
            if(random.randint(0,100)<player2.hit*100):
                player1.hp-=16-player1.defence
    elif (ch==7):
        for i in range(0,5):
            if(random.randint(0,100)<player2.hit*100):
                player1.hp-=16-player1.defence
    elif (ch==8):
        if(random.randint(0,100)<50):
            player1.hp-=233-player1.defence
        else:
            player1.hp-=50-player1.defence
        player2.cold=9998
    elif (ch==9):
        pass
    elif (ch==10):
        player1.hp-=30-player1.defence
    elif (ch==11):
        player1.hp-=18
        player1.hit*=0.75

def player1_attack_player2():
    #攻击前
                #呆鹅          #希儿         #樱莲
    if(iplayer1==10 or iplayer1==9 or iplayer1==5):
        player1skill0(iplayer1)

    #攻击中
    if(player1.jumpround==0):#未被控制
        if(player1.banskill==0):#未被封技能
            if(round%player1.cold==0):#大招可释放
                if(iplayer2==10 and random.randint(0,100)<16):#呆鹅打断大招判定
                    print(player1.name+"发动技能"+player1.skill1name,end=' ')
                    print(player2.name+"发动技能"+player2.skill1name,end=' ')
                    player2skill1(iplayer2)
                    print(player1.name+"剩余血量"+str(player1.hp))
                else:
                    print(player1.name+"发动技能"+player1.skill1name,end='  ')
                    player1skill1(iplayer1)
                    print(player2.name+"剩余血量"+str(player2.hp))
            else:
                print(player1.name+"使用普攻",end='  ')
                if(random.randint(0,100)<player1.hit*100):
                    player2.hp-=player1.attack-(1-player1.elemental)*player2.defence
                               #德莉莎         #丽塔         #芽衣
                    if(iplayer1==7 or iplayer1==4 or iplayer1==1):
                        player1skill0(iplayer1)
                    print(player2.name+"剩余血量"+str(player2.hp))
                else:
                    print("但是被闪避了")
        else:
            player1.banskill-=0.5
            if(random.randint(0,100)<player1.hit*100):
                player2.hp-=player1.attack-(1-player1.elemental)*player2.defence

    else:
        player1.jumpround=0
        print(player1.name+"跳过了回合")

    #攻击后
                     #板鸭
    if(iplayer1==2 ):
        player1skill0(iplayer1)   
    #承伤复活判定
    if(iplayer2==8 and player2.hp<=0):
        player2skill0(iplayer2)

def player2_attack_player1():
    #攻击前
                #呆鹅          #希儿           #樱莲
    if(iplayer2==10 or iplayer2==9 or iplayer2==5):
        player2skill0(iplayer2)

    #攻击中
    if(player2.jumpround==0):#未被控制
        if(player2.banskill==0):#未被封技能
            if(iplayer2!=9 or iplayer2!=8 or iplayer2 !=10):
                if(round%player2.cold==0):
                    if(iplayer1==10 and random.randint(0,100)<16):
                        print(player2.name+"发动技能"+player2.skill1name,end=' ')
                        print(player1.name+"发动技能"+player1.skill1name,end=' ')
                        player1skill1(iplayer1)
                        print(player2.name+"剩余血量"+str(player2.hp))
                    else:
                        print(player2.name+"发动技能"+player2.skill1name,end='  ')
                        player2skill1(iplayer2)
                        print(player1.name+"剩余血量"+str(player1.hp))
                else:
                    print(player2.name+"使用普攻",end='  ')
                    if(random.randint(0,100)<player2.hit*100):
                        player1.hp-=player2.attack-(1-player2.elemental)*player1.defence
                                  #德莉莎       #丽塔         #芽衣
                        if(iplayer2==7 or iplayer2==4 or iplayer2==1):
                            player2skill0(iplayer2)
                        print(player1.name+"剩余血量"+str(player1.hp))
                    else:
                        print("但是被闪避了")
        else:
            player2.banskill-=0.5
            if(random.randint(0,100)<player2.hit*100):
                player1.hp-=player2.attack-(1-player2.elemental)*player1.defence

    else:
        player2.jumpround=0
        print(player2.name+"恢复行动了")

    #攻击后
                 #板鸭
    if(iplayer2==2 ):
        player2skill0(iplayer2)   
    #承伤复活判定
    if(iplayer1==8 and player1.hp<=0):
        player1skill0(iplayer1)



chlist=('琪亚娜','芽衣','板鸭','姬子','丽塔','樱莲','渡鸦','德莉莎','阿琳','希儿','呆鹅','符华')



print("请选择对阵角色")
for index in chlist:
    print(i,end=' ')
    i+=1
    print(index)

iplayer1=int(input())
print(chlist[iplayer1])
iplayer2=int(input())
print(chlist[iplayer2])

print("输入对战次数")
times=int(input())

player1win=0
player2win=0
for i in range(1,times+1):
    print('\r\n第'+str(i)+'次模拟')
    class kiana:
        name='琪亚娜'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=24   
        defence=11
        speed=23
        hit=1
        elemental=0
        cold=2
        skill1name='吃我一矛'
        skill1debuffname='音浪太强'

    class mei:
        name='芽衣'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=22
        defence=12
        speed=30
        hit=1
        elemental=0
        cold=2
        skill0name='崩坏世界的歌姬'
        skill1name='雷电家的龙女仆'

    class banya:
        name='板鸭'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=21
        defence=10
        speed=20
        hit=1
        elemental=0
        cold=3
        skill0name='天使重构'
        skill1name='摩托bike'
    
    class jizi:
        name='姬子'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=23
        defence=9
        speed=12
        hit=1
        elemental=0
        cold=2
        skill0name='真爱不死'
        skill1name='干杯朋友'
    #4
    class lita:
        name='丽塔'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=26
        defence=11
        speed=17
        hit=1
        elemental=0
        cold=4
        skill0name='女仆的温柔清理'
        skill1name='完美心意'
                



        #5
    class yinglian:
        name='樱莲'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=20
        defence=9
        speed=18
        hit=1
        elemental=0
        cold=2
        skill0name='八重樱的饭团'
        skill1name='卡莲的饭团'



        #6
    class duya:
        name='渡鸦'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=23
        defence=14
        speed=14
        hit=1
        elemental=0
        cold=3
        skill0name='不是针对你'
        skill1name='别墅小岛'



        #7
    class delisha:
        name='德莉莎'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=19
        defence=12
        speed=22
        hit=1
        elemental=0
        cold=3
        skill0name='血犹大第一可爱'
        skill1name='在线踢人'
    


        #8
    class alin:
        name='阿琳姐妹'
        resurrectFlag=0
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=18
        defence=10
        speed=10
        hit=1
        elemental=0
        cold=9999
        skill0name='生命之水'
        skill1name='变成星星吧'

        #9
    class seele:
        name='希儿'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=23
        defence=13
        speed=26
        hit=1
        elemental=0
        cold=9999
        skill0name='我换我自己'
        skill1name='拜托了另一个我'

        #10
    class daie:
        name='呆鹅'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=19
        defence=10
        speed=15
        hit=1
        elemental=0
        cold=9999
        skill0name='摸鱼的快乐'
        skill1name='反弹无效'
    

        #11
    class hua:
        name='符华'
        banskill=0
        jumpround=0
        win=0
        hp=100
        attack=17
        defence=15
        speed=16
        hit=1
        elemental=1
        cold=3
        skill0name='凭神化剑'
        skill1name='形之笔墨'

    playerlist=(kiana,mei,banya,jizi,lita,yinglian,duya,delisha,alin,seele,daie,hua)

    player1=playerlist[iplayer1]
    #print(kiana.hp)
    #print(player1.hp)
    player2=playerlist[iplayer2]
    #print(player2.hp)
    print(player1.name+" 对阵 "+player2.name+" !" )
#    player1.hp=100
#    player2.hp=100

    print("round0")
    if(iplayer1==3 or iplayer1==11 or iplayer1==6 ):
        player1skill0(iplayer1)
    if(iplayer2==3 or iplayer2==11 or iplayer2==6 ):
        player2skill0(iplayer2)
    print()  
    round=1  
    while(player1.hp>0 and player2.hp>0):
        #开战前
        

        if(player1.speed>player2.speed):
            print("round"+str(round))
            #print("round"+str(round)+".1")

            player1_attack_player2()

            if(player2.hp>0):
                
                #print("round"+str(round)+".2")

                player2_attack_player1()
                
                if(player1.hp>0):
                    round+=1
                else:
                    print("game is over,winner is"+player2.name)
                    player2win+=1
                    break

            else:
                print("game is over,winner is"+player1.name)
                player1win+=1
                break
        else:
            print("round"+str(round))
            #print("round"+str(round)+".1")

            player2_attack_player1()

            if(player1.hp>0):
                
                #print("round"+str(round)+".2")

                player1_attack_player2()

                if(player2.hp>0):
                    
                    round+=1
                else:
                    print("game is over,winner is"+player1.name)
                    player1win+=1
                    break
            else:
                print("game is over,winner is"+player2.name)
                player2win+=1
                break
print("\r\n\r\ncode by AllAloneForYou(qq695023921)\r\nenjoy this\r\n截至编码日 2020-08-01 04：35 很多角色没上场过 无法具体观察实际机制 本人对数据的准确性不做任何担保\r\n总之 梭哈就对了 赢了会所嫩模 输了下海干活儿嘛 看开点")
print("times="+str(times)+","+player1.name+"的胜率为"+str((player1win/times)*100)+"%,胜场数为"+str(player1win))
print("times="+str(times)+","+player2.name+"的胜率为"+str((player2win/times)*100)+"%,胜场数为"+str(player2win))

print("回车关闭窗口")

input()



