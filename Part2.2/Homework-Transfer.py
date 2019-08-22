#===单位换算=====
#UTF-8
#韩范西出品

"""
根据输入内容判断单位类型
完成温度转换 华氏度与摄氏度
完成长度转换   cm inch
完成货币转换：美元与人民币

    8月22日
        1美元=7.0839人民币
        1人民币=0.1412美元

科普知识：
   
    1、 1华氏度=1摄氏度*1.8+32
        1摄氏度=（1华氏度-32）/1.8

    2、 1 inch=2.54cm
        1 foot(英尺)= 0.305meters(米)

"""
import re

class Transfer():
    ''' 我是一个类，叫transfer，用来转换东西的 '''
    def __init__(self,temprature,unit,money):
        self.unit = unit
        self.temprature = temprature
        self.money = money

   
    def init(self):
        '''开始菜单'''
        print ('这是一个单位换算器'.center(30,'='))
        print ('输入你要换算的东西，数值加上单位，目前只支持如下三条：')
        print ("1、华氏度与摄氏度的转换")
        print ("2、英制长度与国际单位长度转换")
        print ("3、美元与人民币转换")
        print ("4、退出")

    def goodbye(self):
        "再见结束语"
        print("不充钱一样转换的准！欢迎再次使用!")
        
       


    def inputnumber(self):
        "输入选项"
        print("-".center(40,"-"))
        inputnumber = input("大胆输入你的值：")
        return inputnumber

    def start(self):
        "主程序"
        choice = input("大胆输入你的选项吧：")
        
        if choice == "1":
            self.temprature.welcome()
            print(self.temprature.judge(self.inputnumber()))
        elif choice == "2":
            self.unit.welcome()
            print(self.unit.judge(self.inputnumber()))
        elif choice == "3":
            self.money.welcome()
            print(self.money.judge(self.inputnumber()))
        elif choice == "4":
            self.goodbye()
            exit()
        else:
            print("我只认识“1、2、3、4”")
            
            



class TransTemp:
    """我是负责温度转换的类"""
    def welcome(self):
        return "恭喜你选择温度转换功能！转换贼准！"

    def judge (self,typein):
        "找单位，看是C还是F"
        if re.match ("\d+f$|\d+c$",typein.strip(" "),re.I):  
            C = re.search("c",typein,re.I)  #不区分大小写找C
            F = re.search("f",typein,re.I)  #不区分大小写找F
            if C :   
                temp = re.split(C.group(0),typein)
                temp = float(temp[0])
                return f'{temp}摄氏度 = {self.temptrans_c(temp)}华氏度'
            elif F :
                temp = re.split(F.group(0),typein)
                temp = float(temp[0])
                return f'{temp}华氏度 = {self.temptrans_f(temp)}摄氏度'
        else:
            return "写的啥玩意啊，看不懂！"


    def temptrans_c(self,tempC):
        "C转换F"
        tempF = tempC*1.8+32
        return(round(tempF,3))
    
    def temptrans_f(self,tempF):
        "F转换C"
        tempC = (tempF - 32) / 1.8
        return (round(tempC,3))

    

class Length:
    '''我是负责长度的'''

    def welcome(self):
        return "恭喜你选择长度转换功能，转换贼准！"

    def judge(self,typein):
        if re.match ("\d+cm$|\d+inch$|\d+m$|\d+foot$",typein.replace(" ",""),re.I):
            cm = re.search("cm",typein,re.I)  #不区分大小写找cm
            m = re.search("m",typein,re.I)  #不区分大小写找m
            foot = re.search("foot",typein,re.I)  #不区分大小写找foot
            inch = re.search("inch",typein,re.I)  #不区分大小写找inch
            
            if cm :
                length = re.split(cm.group(0),typein)
                length = float(length[0])
                return f'{length}厘米 = {round(length/100,3)}米 = {round(self.cm_to_inch(length),3)}英寸 = {round(self.inch_to_foot(self.cm_to_inch(length)),3)}英尺'
            if m :
                length = re.split(m.group(0),typein)
                length = float(length[0])
                return f'{length}厘 = {length * 100}厘米 = {round(self.foot_to_inch(self.m_to_foot(length)),3)}英寸 = {round(self.m_to_foot(length),3)}英尺'
            if foot :
                length = re.split(foot.group(0),typein)
                length = float(length[0])
                return f'{length}英尺 = {round(self.foot_to_inch(length),3)}英寸 = {round(self.foot_to_m(length),3)}米 = {round(self.foot_to_m(length)*100,3)}厘米'
            if inch :
                length = re.split(inch.group(0),typein)
                length = float(length[0])
                return f'{length}英寸 = {round(self.inch_to_foot(length),3)}英尺 = {round(self.inch_to_cm(length)/100,3)}米 = {round(self.inch_to_cm(length),3)}厘米'
        else:
            return "写的啥玩意啊，看不懂！"
    
    def cm_to_inch(self,length):
        inch = length / 2.54
        return inch

    def inch_to_cm(self,length):
        cm = length * 2.54
        return cm

    def m_to_foot(self,length):
        foot = length / 0.305
        return foot
        
    def foot_to_m(self,length):
        m = 0.305 * length  
        return m     

    def foot_to_inch(self,length):
        inch = length * 12
        return inch
        
    def inch_to_foot(self,length):
        foot = length / 12
        return foot


class Money:
    """我是转换钱用的"""
    def welcome(self):
        return "恭喜你选择美金人民币转换功能！转换贼准！"

    def judge(self,typein):
        "判断输入是不是美金"
        if re.match ("\d+\$$|\d+美金$|\d+美刀$|\d+USD$|\d+RMB$|\d+刀$|\d+人民币$|\d+￥$",typein.replace(" ",""),re.I):
            USD = re.search("\$|美金|美刀|usd",typein.replace(" ",""),re.I)
            RMB = re.search("\￥|rmb|人民币|毛爷爷",typein.replace(" ",""),re.I)
            if USD :
                rmb = re.split(USD.group(0),typein)
                rmb = float(rmb[0])
                return f'{rmb}美金现在能值个{self.usd_to_rmb(rmb)}人民币'
            if RMB :
                usd = re.split(RMB.group(0),typein)
                usd = float(usd[0])
                return f'{usd}人民币现在能值个{self.rmb_to_usd(usd)}美金'

        else:
            return "我也不认识我转换啥呀"

    def rmb_to_usd(self,money):
        usd = money * 0.1412
        return usd
    
    def usd_to_rmb (self,money):
        rmb = money * 7.0389
        return rmb




def main():
    temp = TransTemp()
    length = Length()
    money = Money()
    mainapp = Transfer(temp,length,money)

    while True:
        mainapp.init()
        mainapp.start()





if __name__ == "__main__":
    main()










