#UTF-8
#韩范西出品


#  ♣     ♥       ♠     ♦
# 1-13  14-26  27-39  40-52

import random
caohua = '♣'
hongtao = '♥'
heitao = '♠'
fangpian = "♦"

def JQK(i):
    if i >10:
        i = 10
    else:
        i = int(i)
    return(i)

def poker():
    poke = []
    for j in range(1,53):
        poke.append(j)
    return(poke)

def fapai(a): #从哪个列表发牌
    num = len(a)
    c =  random.randint(1,num)
    d = a[c-1]
    a.pop(c-1)
    d = int (d)
    return(d)
    
def fanshi(x):
    if x == 1:
        return("A")
    if x <= 10:
        return(x)
    if x ==11:
        return('J')
    if x == 12:
        return("Q")
    if x ==13:
        return("K")

def suijifapai(b,i):# a=1 b=当前循环次数  i=随机取值fapai
    for j in range(1,b+1):
        #choice = input(" 发牌按1，退出发牌按2:  ")
        # choice = "1"
        #if choice=="1":
        #i = 
        i = int(i)
        if 1<=i<=13:
            print(caohua,fanshi(i))
            pai = JQK(i)
            return(pai)
            break
        if 14<=i<=26:
            print(hongtao,fanshi(i-13))
            pai = JQK(i-13)
            return(pai)
            break
        if 27<=i<=39:
            print(heitao,fanshi(i-26))
            pai = JQK(i-26)
            return(pai)
            break
        if 40<=i<=52:
            print(fangpian,fanshi(i-39))
            pai = JQK(i-39)
            return(pai)
            break
        j = j+1

j=1
x = 1
loop = True
cwin = 0
uwin = 0
print("欢迎光临21点游戏商城：不充钱一样赢")
print()
pukepai = poker()   #准备好52张扑克
while loop:
    
    if len(pukepai)<6:
        print("没牌了，重新开始吧")
        break
    if x == 1 :
        judge = input("开始吗？ y or n:  ")             
    if x > 1 :
        judge = input("继续吗？ y or n:  ")
    if judge == "n":
        print("郑重承诺：不花钱一样玩得赢，欢迎再来！")
        break
    if judge == "y":
        x= x +1
        print("-".center(40,"-"))
        print("你拿到的牌是：")     #给自己发牌
        first = suijifapai (len(pukepai),fapai(pukepai))
        second = suijifapai (len(pukepai),fapai(pukepai))
        judge2 =  input("当前牌型点数："+str(first+second)+" 还要一张吗？： y or n  :") #"你当前的点数是"+str(first+second)+"，
        if judge2 == "n":
            userFinial = first + second
            print("你的牌型得分是：",userFinial)
        if judge2 == "y":
            print("你的第三张牌是：",end="")
            third = suijifapai (len(pukepai),fapai(pukepai))
            userFinial = first+second+third
            print("你的牌型得分是：",userFinial)

        print()
        print("对手的牌型是：")
        first2 = suijifapai (len(pukepai),fapai(pukepai))
        second2 = suijifapai (len(pukepai),fapai(pukepai))
        if first2+second2 <16:
            third2 = suijifapai (len(pukepai),fapai(pukepai))
            compFinial = first2 + second2 + third2
        if first2+second2 >= 16:
            compFinial = first2 + second2
        print("对手得分：",compFinial)
        print()
        print("比赛结果".center(40,"-"))
        UW = abs(userFinial-21)
        CW = abs(compFinial-21)
        if CW < UW:
            print("电脑得分更接近21，电脑胜利！")
            cwin= cwin+1
        if CW > UW:
            print("恭喜你比电脑牛逼，你的得分更接近21，你赢了！")
            uwin = uwin +1
        
        print(f"当前比分-------电脑{cwin}：玩家{uwin}--------")
        print("当前剩余纸牌数：",len(pukepai))
        print()





    # a = input("Continue? :")
    # if a == "n":
    #     loop = False
    if len(pukepai)==0:
        print("没牌了兄弟")
        break
    # suijifapai (len(pukepai),fapai(pukepai))
    # print (len(pukepai))






    



