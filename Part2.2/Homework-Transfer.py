#===单位换算=====
#UTF-8
#韩范西出品

"""
根据输入内容判断单位类型
完成温度转换 华氏度与摄氏度
完成长度转换   cm inch
完成货币转换：美元与人民币

    7月30日
        1美元=6.8889人民币
        1人民币=0.1452美元

科普知识：
   
    1、 1华氏度=1摄氏度*1.8+32
        1摄氏度=（1华氏度-32）/1.8

    2、 1 inch=2.54cm
        1 foot(英尺)= 0.305meters(米)

"""
import re

class Transfer():
    ''' 我是一个类，叫transfer，用来转换东西的 '''
    def __init__(self):
        pass

   
    def start(self):
        '''开始菜单'''
        print ('这是一个单位换算器'.center(30,'='))
        print ('输入你要换算的东西，数值加上单位，目前只支持如下三条：')
        print ("1、华氏度与摄氏度的转换")
        print ("2、英制长度与国际单位长度转换")
        print ("3、美元与人民币转换")
        print ("4、退出")


    def input(self,choice,content):
        "输入值"
        pass



class TransTemp:
    """我是负责温度转换的类"""


    def judge (self,typein):
        "找单位，看是C还是F"
        if re.match ("\d+f|\d+F|\d+c|\d+C",typein,re.X):
            C = re.search("c",typein,re.I)  #不区分大小写找C
            F = re.search("f",typein,re.I)  #不区分大小写找F
            if C :   
                temp = re.split(C.group(0),typein)
                temp = float(temp[0].replace(" ",""))
                return f'{temp}摄氏度 = {self.temptrans_c(temp)}华氏度'
            elif F :
                temp = re.split(F.group(0),typein)
                temp = float(temp[0].replace(" ",""))
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

    



def main():
    a = TransTemp()
    b = input("typein:")
    print (a.judge(b))

if __name__ == "__main__":
    main()



'''





loop = True
while loop :


    choice = input('大胆说出你的选择：')
    choice=int(choice.strip(""))
    if choice ==1:  #摄氏度转换器
        print()
        print('恭喜你选择了\"华氏度与摄氏度的转换\"，请输入要转换的数值与单位，例如：10C或10F')
        temp = input('大胆输入你的值：')
        if temp.endswith("C") or temp.endswith("c"):
            tempF = float(temp[:-1])*1.8+32
            print(f'{temp[:-1]}摄氏度 == {tempF}华氏度')
            conti = input("是否继续：y 或 n：")
            if conti == 'y':
                continue
            else :
                loop = False
                print()
                print("谢谢使用，郑重承诺：不充钱一样算的准！")
        elif temp.endswith("F") or temp.endswith("f"):
            tempC = (float(temp[:-1])-32) / 1.8
            print(f'{temp[:-1]}华氏度 == {tempC}摄氏度')      
            conti = input("是否继续：y 或 n：")
            if conti == 'y':
                continue
            else :
                loop = False
                print()
                print("谢谢使用，郑重承诺：不充钱一样算的准！")
        else:
            print("输啥玩意呢，我不认识")


    elif choice ==2:     #inch 和cm
        print()
        print('恭喜你选择了\"英制长度与国际单位长度转换\"，请输入要转换的数值与单位，目前支持单位：in ft cm m')
        temp = input('大胆输入你的值：')
        if temp.endswith("in"):
            inch = float(temp[:-2])
            cm = inch*2.54
            m = cm /100
            print(f"{round(inch,3)}英寸 == {round(cm,3)}厘米 == {round(m,3)}米")
            conti = input("是否继续：y 或 n：")
            if conti == 'y':
                continue
            else :
                loop = False
                print()
                print("谢谢使用，郑重承诺：不充钱一样算的准！")
        if temp.endswith('ft'):
            ft = float(temp[:-2])
            m = 0.305*ft 
            cm = 100*m
            print(f"{round(ft,3)}英尺 == {round(cm,3)}厘米 == {round(m,3)}米")
            conti = input("是否继续：y 或 n：")
            if conti == 'y':
                continue
            else :
                loop = False
                print()
                print("谢谢使用，郑重承诺：不充钱一样算的准！")
        if temp.endswith('m'):
            if temp.endswith("cm"):
                cm = float(temp[:-2])
                m = cm / 100
                inch = cm/2.54
                ft = inch / 12
                print(f"{round(cm,3)}厘米 == {round(inch,3)}英寸 == {round(ft,3)}英尺")
                conti = input("是否继续：y 或 n：")
                if conti == 'y':
                    continue
                else :
                    loop = False
                    print()
                    print("谢谢使用，郑重承诺：不充钱一样算的准！")
            elif temp.endswith("m"):
                m = float(temp[:-1])
                cm = 100*m
                inch = cm/2.54
                ft = inch / 12
                print(f"{round(m,3)}米 == {round(inch,3)}英寸 == {round(ft,3)}英尺")   
                conti = input("是否继续：y 或 n：")
                if conti == 'y':
                    continue
                else :
                    loop = False
                    print()
                    print("谢谢使用，郑重承诺：不充钱一样算的准！")

    elif choice ==3:
        print()
        print('恭喜你选择了\"美元与人民币转换\"功能，请输入你要换算你的钱，如10USD or 10RMB')
        temp = input('大胆输入你的钱：')
        if temp.endswith('usd') or temp.endswith("USD"):
            money = float(temp[:-3]) /6.8889
            print(f'{temp} == {round(money,3)}RMB')
            conti = input("是否继续：y 或 n：")
            if conti == 'y':
                continue
            else :
                loop = False
                print()
                print("谢谢使用，郑重承诺：不充钱一样算的准！")
        if temp.endswith('rmb') or temp.endswith("RMB"):
            money = float(temp[:-3]) * 6.8889
            print(f'{temp} == {round(money,3)}USD')
            conti = input("是否继续：y 或 n：")
            if conti == 'y':
                continue
            else :
                loop = False
                print()
                print("谢谢使用，郑重承诺：不充钱一样算的准！")
    
    elif choice == 4:
        loop = False
        print()
        print("谢谢使用，郑重承诺：不充钱一样算的准！")
    else:
        print("爸爸不认识")


'''









