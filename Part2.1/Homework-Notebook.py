#######UTF-8
#------韩范西出品
#2019-8-1

import time
loop = True
note = {}
while loop:
    print()
    print("_________________________________________________________________")
    print('我是一个备忘录，备忘本领强'.center(40,"="))

    if len(note) == 0:
        print("现在你的备忘录是空的，快写点啥啊！")
        print()
    else :
        print(f"现在共有{len(note)}条备忘：")
        print()
        [print(f'{key}、你要在{value[0]}的时候，在{value[1]}{value[2]}') for key, value in note.items()]
        print()
    print("_________________________________________________________________")
    choice = input("1、写点啥 2、删点啥  3、智能识别 4、退出，大胆说出你的选择是：")
    if choice == '1' :
        date = input("时间：")
        locaiton = input("地点：")
        thing = input('你都想干啥：')
        key = str(len(note)+1)
        note[key]=[date,locaiton,thing]
        # [print(a,b) for a,b in note.items()]
        # print(len(note))
        continue

    if choice == "2":
        if len(note)==0:
            print("没东西咋删除啊(3s后返回)")
            time.sleep(3)
            continue
        else:
            delnum = input('你想删除几？   输入：')
            del note[delnum]
            print("删除成功，3s后返回")
            time.sleep(3)
            continue
    if choice == "3":
        print("恭喜你选择了人工智能模式，告诉我你想在几点在哪干些啥，如：晚上10：00在家学Python")
        todo= str(input("说吧，你都啥安排："))
        if todo.find(":") != -1:   #用冒号定位时间，判断英文冒号
            date = todo[todo.find(":")-2:todo.find(":")+3]
            point = todo.find(":")+3
        elif todo.find("：") != -1:           #判断中文冒号
            date = todo[todo.find("：")-2:todo.find("：")+3]
            point = todo.find("：")+3
        if todo.find("在") != -1:
            locaiton = todo[todo.find("在")+1:]     #
        
        if todo.find("在") == -1:
            locaiton = todo[point:]
        
        thing = ""
        key = str(len(note)+1)
        note[key]=[date,locaiton,thing]
        # [print(a,b) for a,b in note.items()]
        # print(len(note))
        continue
    if choice == '4':
        loop = False


#note = {'1':['10:30','赵兄托我办点事']}   




print()
print("关掉备忘录吧，记忆是痛苦的根源，郑重承诺，不充钱一样记得准，再见！")


