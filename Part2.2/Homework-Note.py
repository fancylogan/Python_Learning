#######UTF-8
#------韩范西出品
#2019-8-1

import time
import re
import pickle


class Memo:
    """我是记事本"""
    def __init__(self,memo_admin,ID="",location="",thing="",date=""):
        "init"
        self.memo_admin = memo_admin
        self._ID = ID
        self.location = location
        self.date = date
        self.thing = thing
        self._db = self.memo_admin.readdb()

    @property
    def get_id(self):
        "取ID"
        return self._ID
    
    def platform(self):
        '主界面'
        self._db = self.memo_admin.readdb()
        print()
        print("_________________________________________________________________")
        print('我是一个备忘录，备忘本领强'.center(40,"="))
        if len(self._db) == 0:
            print("现在你的备忘录是空的，快写点啥啊！")
            print()
        else :
            print(f"现在共有{len(self._db)}条备忘：")
            print()
            i = 0
            [print(f'{i+1}、你要在{self._db[i][0]}的时候，在{self._db[i][1]}{self._db[i][2]}') for i in range(len(self._db))]
            print()
        print("_________________________________________________________________")
        print ("1、写点啥 2、删点啥  3、改点啥 4、查点啥 5、退出，大胆说出你的选择是：")
    
    def choice (self):
        "选择按钮"
        choice = input ("大胆说出你的选项：")
        return choice


    def typein_add (self):
        "前端添加"
        try:
            self._ID = len(self._db)+1
            self.date = input("时间：")
            self.location = input("地点：")
            self.thing = input('你都想干啥：')
            self.memo_admin.add_note (self._ID,self.date,self.location,self.thing)
        except Exception as f:
            print("老铁有毛病，你看：",f)

    def typin_del (self):
        "前端删除"
        if len(self._db) == 0:
            input ("老铁，空的没法删啊！")
        else:
            try:
                typein = int(input("告诉我你想删几号，我帮你删他："))
                self.memo_admin.del_note(typein)
                input("不客气老铁，我给你把"+str(typein)+"删了！")
            except Exception as f:
                print ("老铁有毛病，你看：",f)

    def typein_modify(self):
        "前端修改"
        if len( self._db) == 0:
            input ("老铁，空的没法改啊！")
        else:
            try:
                typein = int(input("告诉我改sei，我帮你改了他："))
                self._ID = typein -1 
                print("我的老铁正在修改第"+str(typein)+"条记录：")
                self.date = input("时间改成啥：")
                self.location = input("地点改成啥：")
                self.thing = input('你都想干啥改成啥：')
                self.memo_admin.modify_note (self._ID,self.date,self.location,self.thing)
                input("不客气老铁，我给你把"+str(typein)+"改完了，你瞅瞅！")
            except Exception as f:
                print("老铁有毛病，你看：",f)


    def typein_query(self):
        "查找前端"
        if len( self._db) == 0:
            input ("老铁，空的，臣妾查不到啊！")       
        else:
            try:
                typein = int(input("老铁想查个sei，给俺说："))
                if typein <= len(self._db):
  
                    print (f'{typein}、你要在{self._db[typein-1][0]}的时候，在{self._db[typein-1][1]}{self._db[typein-1][2]}' )
                    input("查到了老铁！")
                else:
                    typein("老铁，你输的数不在这里头啊！")
            except Exception as f:
                print("老铁有毛病，你看：",f)

    def goodbye (self):
        print()
        print("关掉备忘录吧，记忆是痛苦的根源，郑重承诺，不充钱一样记得准，再见！")



class MemoAdmin():

    def __init__(self):
        try: 
            self.dic = self.readdb()
        except :
            self.dic = []
            self.savedb()
        
    def savedb (self):
        with open ("db1.pk2","wb") as f:
            pickle.dump(self.dic,f)

    def readdb (self):
        with open ("db1.pk2","rb") as f:
            self.dic = pickle.load(f)
        return self.dic


    def add_note (self,ID,date,location,thing):
        self.dic.append([date,location,thing])
        self.savedb()

    def modify_note (self,ID,date,location,thing):
        self.dic[ID]=([date,location,thing])
        self.savedb()       

    def query_note (self):
        pass

    def del_note (self,key):
        try:
            self.dic.pop(key-1)
            self.savedb()
        except :
            print ("老铁你这输入有毛病啊！")


def main():
    memoadmin = MemoAdmin()
    memo = Memo(memoadmin)
    while True:
        memo.platform()
        choice = memo.choice()
        if choice == "1":
            memo.typein_add()
            continue
        elif choice == "2":
            memo.typin_del()
            continue
        elif choice == "3":
            memo.typein_modify()
            continue

        elif choice == "4":
            memo.typein_query()
            continue

        elif choice == "5":
            memo.goodbye()
            exit()
        else:
            input("老铁，你这输入的有毛病，再瞅瞅！")
        


    

if __name__ == "__main__":
    main()


