#————我要写个聊天机器人
#作者：Logan
#PS：不充钱也可以聊得来 

import pickle


storage = {
     "你好":"哦，你好",
     "你是谁":"老公，我是你的小三呀",
     "操你妈":"赛脸了吧，骂谁呢？"
}

def savedict(dict):
     with open ("chat.pkl","wb") as f:
          f.write(pickle.dumps(dict))


          

class BotFace():
     def __init__(self,BI):
          self.bot_name = "你的小三"
          self.AI = BI
     def chat (self):
          usr_say = input("你：")
          return usr_say
     def welcome (self):
          return "风里雨里，你的小三陪你！你好，我是你的小三！"
     def goodbye (self):
          return "不充钱一样聊得来，小三和你说再见！"

     def replay (self):
          print (f'{self.bot_name}: {self.AI.think(self.chat())}')




class BotBrain():
     def __init__(self):
          self.dict = self.readdict()
     
     def readdict(self):
          with open("chat.pkl","rb") as f:
               return pickle.loads(f.read())

     def think(self,thinkwhat):
          if thinkwhat in self.dict:
               return self.dict[thinkwhat]
          else:
               return "哦"
     


def main():
     savedict(storage)
     AI=BotBrain()
     bot = BotFace(BI=BotBrain())
     bot.welcome()
     loop = True
     while loop:
         #bot.chat()
          bot.replay()
     bot.goodbye()

if __name__ == "__main__":
   main() 

